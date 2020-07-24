#!/usr/bin/env python3

import argparse
import json
import os
import pathlib
import subprocess
import sys

import iterm2
from jinja2 import Template
import typer
import yaml

ENABLED_APPS = ["nvim", "zsh", "tmux", "rofi", "xcolors", "nvim"]
BARS = ["nvim", "tmux"]
NVIM_SOCKET = "NVIM_LISTEN_ADDRESS"

PACKAGE_DIR = pathlib.Path(__file__).parent.parent.resolve()
THEME_DIR = os.path.join(PACKAGE_DIR, "templates/themes")
APP_DIR = os.path.join(PACKAGE_DIR, "templates/applications")
BAR_DIR = os.path.join(PACKAGE_DIR, "templates/bars")
DATA_DIR = os.path.join(PACKAGE_DIR, "templates/data")

with open(f"{DATA_DIR}/separators.json") as f:
    SEPARATORS = json.load(f)

with open(f"{DATA_DIR}/fonts.json") as f:
    FONTS = json.load(f)

app = typer.Typer()


def load_yaml(theme_file):
    with open(theme_file, "r") as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as e:
            typer.echo("Theme failed to load")
            typer.echo(e)


def get_theme_data(theme):
    theme_file = os.path.join(THEME_DIR, theme + ".yaml")
    return load_yaml(theme_file)


def hex_to_rgb(hex):
    hex = hex.lstrip("#")
    hlen = len(hex)
    return tuple(int(hex[i : i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))


class Renderer:
    def __init__(self):
        self.home_dir = os.path.expanduser("~")
        self.output_dir = os.path.join(self.home_dir, ".thematic")
        self.app_files = [
            os.path.join(APP_DIR, f)
            for f in os.listdir(APP_DIR)
            if os.path.isfile(os.path.join(APP_DIR, f))
        ]
        self.bar_files = [
            os.path.join(BAR_DIR, f)
            for f in os.listdir(BAR_DIR)
            if os.path.isfile(os.path.join(BAR_DIR, f))
        ]
        self.themes = [
            f.split(".")[0]
            for f in os.listdir(THEME_DIR)
            if os.path.isfile(os.path.join(THEME_DIR, f))
        ]

    def set_bars(self, separator_type: str):
        for bar_file in self.bar_files:
            bar_data = load_yaml(bar_file)
            if bar_data["name"] in BARS:
                output_file = os.path.join(self.output_dir, bar_data["output_file"])
                if sys.platform in bar_data["os_types"]:
                    self.render_file(
                        bar_data["template"],
                        {"separators": SEPARATORS[separator_type]},
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
                else:
                    if sys.platform in app_data["os_types"]:
                        self.render_file(app_data["template"], theme_data, output_file)
                        self.maybe_source_generated_file(app_data)

    def maybe_create_output_directory(self):
        output_dir = f"{self.home_dir}/.thematic"
        if not os.path.isdir(output_dir):
            typer.echo(
                f"Output directory not found: creating directory at {output_dir}"
            )
            try:
                os.mkdir(output_dir)
            except Exception as e:
                typer.echo("Error creating output directory: {}".format(e))

    def maybe_source_generated_file(self, app_data):
        with open(os.path.join(self.home_dir, app_data["origin_file"]), "r+") as f:
            lines = f.readlines()
            sourced = False
            for line in lines:
                if line.find(app_data["output_file"]) > 0:
                    sourced = True
                    break

            if not sourced:
                f.seek(0)
                output_file = f"{self.output_dir}/{app_data['output_file']}"
                line = "{} {}".format(app_data["source"]["command"], output_file)
                if app_data["source"]["with_quotes"]:
                    line = '{} "{}"'.format(app_data["source"]["command"], output_file)
                line += "\n"
                typer.echo(
                    f"Editing {app_data['origin_file']} to source {output_file}!"
                )
                if (app_data["source"]["source_at_index"]) == -1:
                    lines.write(line)

                lines.insert(app_data["source"]["source_at_index"], line)
                f.writelines(lines)

    @staticmethod
    def render_file(app_template, theme_data, output_path):
        temp = Template(app_template)
        rendered = temp.render(**theme_data)
        with open(output_path, "w") as output:
            output.write(rendered)

    @staticmethod
    def log_output(app_template, theme_data, output_file):
        temp = Template(app_template)
        typer.echo(
            f"*********************** Rendering to '{output_file}' ***********************"
        )
        typer.echo(temp.render(**theme_data))


class Shell:
    def __init__(self):
        self.platform = sys.platform

    def load_theme(self, theme):
        if self.platform == "darwin":

            async def wrapped(connection):
                await self.change_iterm_colors(connection, theme)

            iterm2.run_until_complete(wrapped)
            self.load_alfred_theme(theme)
        if self.platform == "linux":
            self.reload_xresources()
        self.reload_tmux()
        self.reload_neovim()

    async def get_iterm_profile(self, connection):
        app = await iterm2.async_get_app(connection)
        session = app.current_window.current_tab.current_session
        if session is not None:
            profile = await session.async_get_profile()
            return profile

    async def change_iterm_colors(self, connection, theme):
        profile = await self.get_iterm_profile(connection)
        iterm_colors_hex = get_theme_data(theme).get("iterm_colors")
        for color_name, hex in iterm_colors_hex.items():
            color = iterm2.Color(*hex_to_rgb(hex))
            await getattr(profile, f"async_set_{color_name}_color")(color)

    async def change_iterm_font(self, connection, font):
        profile = await self.get_iterm_profile(connection)
        await profile.async_set_normal_font(f"{FONTS[font]['name']} 15")
        await profile.async_set_horizontal_spacing(FONTS[font]["horizontal_spacing"])

    def reload_tmux(self):
        command = "tmux source-file ~/.tmux.conf"
        self.call_with_shell(command)

    def reload_neovim(self):
        if not os.environ.get(NVIM_SOCKET):
            typer.echo(f"${NVIM_SOCKET} env var not set! Neovim will not be reloaded.")
            return

        if os.path.exists(os.environ.get(NVIM_SOCKET)):
            command = "nvr --nostart --remote-send ':so ~/.config/nvim/init.vim<CR>'"
            self.call_with_shell(command)

    def load_alfred_theme(self, theme):
        command = [
            "osascript",
            "-e",
            f'tell application "Alfred 4" to set theme "{theme}"',
        ]
        subprocess.Popen(command)

    def call_with_shell(self, command):
        subprocess.call([os.getenv("SHELL"), "-i", "-c", command])

    @staticmethod
    def restart_awesome():
        raise NotImplementedError()

    @staticmethod
    def reload_xresources():
        call_with_shell("xrdb merge " + os.expanduser("~") + "/.xresources")


class NotImplementedError(Exception):
    pass


@app.command()
def set(theme: str, dry_run: bool = False):
    renderer = Renderer()
    if theme not in renderer.themes:
        typer.echo(f"Theme '{theme}' not found. Enter one of the following:")
        for theme in renderer.themes:
            typer.echo(theme)
        return
    typer.echo(f"Setting theme to {theme}...")
    shell = Shell()
    renderer.render_themed_files(theme, dry_run=dry_run)
    shell.load_theme(theme)
    typer.echo("Theme loaded.")


@app.command()
def bars(separator_style: str):
    if separator_style not in SEPARATORS.keys():
        typer.echo(f"Bar '{separator_style}' not found. Enter one of the following:")
        for bar in SEPARATORS.keys():
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
def font(font: str):
    if font not in FONTS.keys():
        typer.echo(f"Font '{font}' not found. Enter one of the following:")
        for font in FONTS.keys():
            typer.echo(font)
        return
    typer.echo(f"Setting font to {font}...")
    shell = Shell()

    async def wrapped(connection):
        await shell.change_iterm_font(connection, font)

    iterm2.run_until_complete(wrapped)
    typer.echo("Font updated.")


@app.command()
def list(option: str):
    if option == "fonts":
        for font in FONTS.keys():
            typer.echo(font)
    elif option == "themes":
        renderer = Renderer()
        for theme in renderer.themes:
            typer.echo(theme)
    elif option == "bars":
        for separator in SEPARATORS.keys():
            typer.echo(separator)
    else:
        typer.echo(f"Invalid option: '{option}'. Enter 'fonts', 'themes', or 'bars'.")


def main():
    app()


if __name__ == "__main__":
    main()
