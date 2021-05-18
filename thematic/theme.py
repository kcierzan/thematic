#!/usr/bin/env python3
import json
import os
import pathlib
import subprocess
import sys
from typing import Tuple, List

try:
    import iterm2
except:
    ...

try:
    from yaml import CLoader as Loader
except:
    from yaml import Loader

from jinja2 import Template
import typer
import yaml


ENABLED_APPS = ["nvim", "zsh", "tmux", "rofi", "xcolors", "nvim", "galaxyline"]
ENABLED_BARS = ["nvim", "tmux", "galaxyline"]
NVIM_SOCKET = "NVIM_LISTEN_ADDRESS"
ALACRITTY_CONFIG = ".config/alacritty/alacritty.yml"
PACKAGE_DIR = pathlib.Path(__file__).parent.parent.resolve()
THEME_DIR = os.path.join(PACKAGE_DIR, "templates/themes")
APP_DIR = os.path.join(PACKAGE_DIR, "templates/applications")
BAR_DIR = os.path.join(PACKAGE_DIR, "templates/bars")
DATA_DIR = os.path.join(PACKAGE_DIR, "templates/data")

app = typer.Typer()


def load_yaml(theme_file):
    with open(theme_file, "r") as f:
        try:
            return yaml.load(f, Loader=Loader)
        except yaml.YAMLError:
            typer.echo("Theme failed to load")
            raise


def get_theme_data(theme):
    theme_file = os.path.join(THEME_DIR, theme + ".yaml")
    return load_yaml(theme_file)


def load_separators():
    with open(f"{DATA_DIR}/separators.json") as f:
        return json.load(f)


def load_fonts():
    with open(f"{DATA_DIR}/fonts.json") as f:
        return json.load(f)


def hex_to_rgb(hex):
    hex = hex.lstrip("#")
    hlen = len(hex)
    return tuple(int(hex[i : i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))


class Renderer:
    def __init__(self):
        self.home_dir = os.path.expanduser("~")
        self.output_dir = os.path.join(self.home_dir, ".thematic")
        self.app_files, self.bar_files = self.get_files(APP_DIR, BAR_DIR)
        self.themes = [
            f.split(".")[0]
            for f in os.listdir(THEME_DIR)
            if os.path.isfile(os.path.join(THEME_DIR, f))
        ]

    def set_bars(self, separator_type: str):
        for bar_file in self.bar_files:
            bar_data = load_yaml(bar_file)
            if bar_data["name"] in ENABLED_BARS:
                output_file = os.path.join(self.output_dir, bar_data["output_file"])
                if sys.platform in bar_data["os_types"]:
                    self.render_file(
                        bar_data["template"],
                        {"separators": load_separators()[separator_type]},
                        output_file,
                    )
                    self.maybe_source_generated_file(bar_data)

    def render_themed_files(self, theme, dry_run):
        self.maybe_create_output_directory()
        theme_data = get_theme_data(theme)
        for app_file in self.app_files:
            app_data = load_yaml(app_file)
            if app_data["name"] in ENABLED_APPS:
                output_file = os.path.join(self.output_dir, app_data["output_file"])
                if dry_run:
                    self.log_output(app_data["template"], theme_data, output_file)
                    continue
                if sys.platform in app_data["os_types"]:
                    self.render_file(app_data["template"], theme_data, output_file)
                    self.maybe_source_generated_file(app_data)
        if not dry_run:
            self.theme_alacritty(theme_data)

    def theme_alacritty(self, theme):
        config_path = os.path.join(os.path.expanduser("~"), ALACRITTY_CONFIG)
        current = load_yaml(config_path)
        c = theme["iterm_colors"]
        new_colors = {
            "colors": {
                "primary": {
                    "foreground": c["foreground"],
                    "background": c["background"],
                },
                "normal": {
                    "black": c["ansi_0"],
                    "red": c["ansi_1"],
                    "green": c["ansi_2"],
                    "yellow": c["ansi_3"],
                    "blue": c["ansi_4"],
                    "magenta": c["ansi_5"],
                    "cyan": c["ansi_6"],
                    "white": c["ansi_7"],
                },
                "bright": {
                    "black": c["ansi_8"],
                    "red": c["ansi_9"],
                    "green": c["ansi_10"],
                    "yellow": c["ansi_11"],
                    "blue": c["ansi_12"],
                    "magenta": c["ansi_13"],
                    "cyan": c["ansi_14"],
                    "white": c["ansi_15"],
                },
            }
        }
        current.update(new_colors)
        with open(config_path, "w") as f:
            yaml.dump(current, f, default_flow_style=False)

    def maybe_create_output_directory(self):
        output_dir = f"{self.home_dir}/.thematic"
        if not os.path.isdir(output_dir):
            typer.echo(
                f"Output directory not found: creating directory at {output_dir}"
            )
            try:
                os.mkdir(output_dir)
            except:
                typer.echo("Error creating output directory")
                raise

    def maybe_source_generated_file(self, app_data) -> None:
        """Inserts lines in 'origin' files that source the generated theme files"""
        with open(os.path.join(self.home_dir, app_data["origin_file"]), "r+") as f:
            lines = f.readlines()
            sourced = False
            for line in lines:
                if line.find(app_data["output_file"]) > 0:
                    sourced = True
                    break
            if not sourced and not app_data["source"].get("skip"):
                self.insert_lines_in_file(f, lines, app_data)

    def insert_lines_in_file(self, target_file, lines, app_data) -> None:
        target_file.seek(0)
        output_file = f"{self.output_dir}/{app_data['output_file']}"
        line = "{} {}".format(app_data["source"]["command"], output_file)
        if app_data["source"]["with_quotes"]:
            line = '{} "{}"'.format(app_data["source"]["command"], output_file)
        line += "\n"
        typer.echo(f"Editing {app_data['origin_file']} to source {output_file}!")
        if (app_data["source"]["source_at_index"]) == -1:
            lines.write(line)

        lines.insert(app_data["source"]["source_at_index"], line)
        target_file.writelines(lines)

    @staticmethod
    def render_file(app_template, theme_data, output_path) -> None:
        temp = Template(app_template)
        rendered = temp.render(**theme_data)
        with open(output_path, "w+") as output:
            output.write(rendered)

    @staticmethod
    def log_output(app_template, theme_data, output_file) -> None:
        temp = Template(app_template)
        typer.echo(
            f"*********************** Rendering to '{output_file}' ***********************"
        )
        typer.echo(temp.render(**theme_data))

    @staticmethod
    def get_files(*directories) -> Tuple[List[str], ...]:
        def get_files_for_dir(directory) -> List[str]:
            return [
                os.path.join(directory, f)
                for f in os.listdir(directory)
                if os.path.isfile(os.path.join(directory, f))
            ]

        return tuple(get_files_for_dir(directory) for directory in directories)


class Shell:
    def __init__(self):
        self.platform = sys.platform

    def load_theme(self, theme: str, iterm: bool) -> None:
        if self.platform == "darwin":
            self.load_alfred_theme(theme)
            if iterm:
                self.load_iterm_theme(theme)
        if self.platform == "linux":
            self.reload_xresources()
            self.restart_awesome()
        self.reload_tmux()
        self.reload_neovim()

    async def get_iterm_profile(self, connection):
        app = await iterm2.async_get_app(connection)
        session = app.current_window.current_tab.current_session
        if session is not None:
            profile = await session.async_get_profile()
            return profile

    def load_iterm_theme(self, theme: str) -> None:
        async def wrapped(connection):
            await self.set_iterm_colors(connection, theme)

        try:
            iterm2.run_until_complete(wrapped)
        except:
            ...

    async def set_iterm_colors(self, connection, theme: str) -> None:
        profile = await self.get_iterm_profile(connection)
        try:
            iterm_colors_hex = get_theme_data(theme)["iterm_colors"]
        except KeyError:
            typer.echo("iTerm2 color data not defined in colorscheme")
            raise
        for color_name, hex in iterm_colors_hex.items():
            color = iterm2.Color(*hex_to_rgb(hex))
            await getattr(profile, f"async_set_{color_name}_color")(color)

    async def set_iterm_font(self, connection, font: str) -> None:
        profile = await self.get_iterm_profile(connection)
        fonts = load_fonts()
        await profile.async_set_normal_font(f"{fonts[font]['name']} 15")
        await profile.async_set_horizontal_spacing(fonts[font]["horizontal_spacing"])

    def set_alacritty_font(self, font: str) -> None:
        config_path = os.path.join(os.path.expanduser("~"), ALACRITTY_CONFIG)
        current = load_yaml(config_path)
        fonts = load_fonts()
        new_font = {
            "font": {
                "bold": {
                    "family": fonts[font]["family"],
                },
                "normal": {
                    "family": fonts[font]["family"],
                    "style": fonts[font]["style"],
                },
                "italic": {
                    "family": fonts[font]["family"],
                },
            }
        }
        x_offset = fonts[font].get("x_offset")
        if x_offset:
            new_font["font"]["offset"] = {"x": x_offset}
        current.update(new_font)
        with open(config_path, "w") as f:
            yaml.dump(current, f, default_flow_style=False)

    def reload_tmux(self) -> None:
        command = "tmux source-file ~/.tmux.conf"
        self.call_with_shell(command)

    def reload_neovim(self) -> None:
        if not os.environ.get(NVIM_SOCKET):
            typer.echo(f"${NVIM_SOCKET} env var not set! Neovim will not be reloaded.")
            return

        nvim_socket = os.environ.get(NVIM_SOCKET)

        if nvim_socket and os.path.exists(nvim_socket):
            command = "nvr --nostart --remote-send ':so ~/.config/nvim/init.vim<CR>'"
            self.call_with_shell(command)

    def load_alfred_theme(self, theme) -> None:
        command = [
            "osascript",
            "-e",
            f'tell application "Alfred 4" to set theme "{theme}"',
        ]
        subprocess.Popen(command)

    def call_with_shell(self, command) -> None:
        subprocess.run(command, shell=True)

    def restart_awesome(self):
        command = "echo 'awesome.restart()' | awesome-client 2>/dev/null"
        self.call_with_shell(command)

    def reload_xresources(self) -> None:
        self.call_with_shell(
            "xrdb merge " + os.path.expanduser("~") + "/.Xresources 2>/dev/null"
        )


class NotImplementedError(Exception):
    pass


@app.command()
def colors(theme: str, dry_run: bool = False, iterm: bool = False) -> None:
    renderer = Renderer()
    if theme not in renderer.themes:
        typer.echo(f"Colorscheme '{theme}' not found. Enter one of the following:")
        for theme in renderer.themes:
            typer.echo(theme)
        return
    typer.echo(f"Setting colorscheme to {theme}...")
    shell = Shell()
    renderer.render_themed_files(theme, dry_run=dry_run)
    if not dry_run:
        shell.load_theme(theme, iterm)
        typer.echo("Colorscheme loaded.")


@app.command()
def bars(separator_style: str) -> None:
    separators = load_separators()
    if separator_style not in separators.keys():
        typer.echo(f"Bar '{separator_style}' not found. Enter one of the following:")
        for bar in separators.keys():
            typer.echo(bar)
        return
    typer.echo(f"Setting bars to {separator_style}...")
    renderer = Renderer()
    shell = Shell()
    renderer.set_bars(separator_style)
    shell.reload_tmux()
    shell.reload_neovim()
    typer.echo("Bars updated.")


@app.command()
def font(font: str, iterm: bool = False) -> None:
    shell = Shell()
    typer.echo(f"Setting font to {font}...")
    try:
        if iterm:

            async def wrapped(connection):
                await shell.set_iterm_font(connection, font)

            iterm2.run_until_complete(wrapped)
        else:
            shell.set_alacritty_font(font)
    except KeyError:
        typer.echo(f"Font '{font}' not found. Enter one of the following:")
        fonts = load_fonts()
        for font in fonts.keys():
            typer.echo(font)
        return
    typer.echo("Font updated.")


@app.command()
def list(option: str) -> None:
    if option == "fonts":
        for font in load_fonts().keys():
            typer.echo(font)
    elif option == "colors":
        renderer = Renderer()
        for theme in renderer.themes:
            typer.echo(theme)
    elif option == "bars":
        for separator in load_separators().keys():
            typer.echo(separator)
    else:
        typer.echo(f"Invalid option: '{option}'. Enter 'fonts', 'themes', or 'bars'.")


def main():
    app()


if __name__ == "__main__":
    main()
