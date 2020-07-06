#!/usr/bin/env python3
import argparse
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

SEPARATORS = {
    "rounded": ("", "", "", "", "", ""),
    "slant_1": ("█", "", "", "", "", "█"),
    "slant_2": ("", "", "", "", "", ""),
    "fade": ("", "", "", "", "", ""),
    "tabbed": ("", "", "", "", "", ""),
    "diamond": ("█", "", "", "", "", "█"),
    "trapezoid": ("█", "█", "█", "█", "█", "█"),
}

PACKAGE_DIR = pathlib.Path(__file__).parent.parent.resolve()
THEME_DIR = os.path.join(PACKAGE_DIR, "templates/themes")
APP_DIR = os.path.join(PACKAGE_DIR, "templates/applications")
BAR_DIR = os.path.join(PACKAGE_DIR, "templates/bars")

app = typer.Typer()


def load_yaml(theme_file):
    with open(theme_file, "r") as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as e:
            print("Theme failed to load")
            print(e)


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
                    self.check_origin_file(
                        bar_data["output_file"], bar_data["origin_file"]
                    )

    def render_themed_files(self, theme, dry_run):
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
                        self.check_origin_file(
                            app_data["output_file"], app_data["origin_file"]
                        )

    def check_origin_file(self, output_file, origin_file):
        with open(os.path.join(self.home_dir, origin_file), "r") as f:
            contents = f.read()
            if contents.find(output_file) < 0:
                print(
                    f"Please source {output_file} in {origin_file} for theme to take effect!"
                )

    def print_themes(self):
        for f in self.themes:
            print(f)

    @staticmethod
    def render_file(app_template, theme_data, output_path):
        temp = Template(app_template)
        rendered = temp.render(**theme_data)
        with open(output_path, "w") as output:
            output.write(rendered)

    @staticmethod
    def log_output(app_template, theme_data, output_file):
        temp = Template(app_template)
        print(
            f"*********************** Rendering to '{output_file}' ***********************"
        )
        print(temp.render(**theme_data))


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

    async def change_iterm_colors(self, connection, theme):
        app = await iterm2.async_get_app(connection)
        session = app.current_window.current_tab.current_session
        iterm_colors_hex = get_theme_data(theme).get("iterm_colors")
        if session is not None:
            profile = await session.async_get_profile()
            for color_name, hex in iterm_colors_hex.items():
                color = iterm2.Color(*hex_to_rgb(hex))
                await getattr(profile, f"async_set_{color_name}_color")(color)

    # FIXME: Does not work...iterm python API is still in beta...
    def get_iterm_cookie(self):
        command = ["osascript", "-e", 'tell application "iTerm2" to request cookie']
        output = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE)
        output, _ = output.communicate()
        os.environ["ITERM2_COOKIE"] = output.decode()

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
    typer.echo(f"Setting theme to {theme}...")
    renderer = Renderer()
    shell = Shell()
    renderer.render_themed_files(theme, dry_run=dry_run)
    shell.load_theme(theme)
    typer.echo("Theme loaded.")


@app.command()
def bars(separator_style: str):
    typer.echo(f"Setting bars to {separator_style}...")
    renderer = Renderer()
    shell = Shell()
    renderer.set_bars(separator_style)
    shell.reload_tmux()
    shell.reload_neovim()
    typer.echo("Bars updated.")

def main():
    app()

if __name__ == "__main__":
    main()
