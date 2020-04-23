#!/usr/bin/env python
import argparse
import os
import pathlib
import subprocess
import sys

import yaml
from jinja2 import Template

ENABLED_APPS = ["nvim", "zsh", "tmux", "rofi", "xcolors", "nvim-status"]

SEPARATORS = {
    "rounded": ["", ""],
    "right_slant": ["", ""],
    "left_slant": ["", ""],
    "fade": ["", ""],
    "tabbed": ["", ""],
    "diamond": ["", ""],
    "trapezoid": ["", ""],
}


class Renderer:
    def __init__(self):
        self.home_dir = os.path.expanduser("~")
        package_dir = pathlib.Path(__file__).parent.parent.resolve()
        app_dir = os.path.join(package_dir, "templates/applications")
        self.output_dir = os.path.join(self.home_dir, ".thematic")
        self.theme_dir = os.path.join(package_dir, "templates/themes")
        self.app_files = [
            os.path.join(app_dir, f)
            for f in os.listdir(app_dir)
            if os.path.isfile(os.path.join(app_dir, f))
        ]
        self.themes = [
            f.split(".")[0]
            for f in os.listdir(self.theme_dir)
            if os.path.isfile(os.path.join(self.theme_dir, f))
        ]

    def print_themes(self):
        for f in self.themes:
            print(f)

    def render_themed_files(
        self, theme, dry_run=True, separators=SEPARATORS["rounded"]
    ):
        theme_data = self.get_theme_data(theme)
        for app_file in self.app_files:
            app_data = self.load_yaml(app_file)
            app_data["separators"] = separators
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

    def get_theme_data(self, theme):
        theme_file = os.path.join(self.theme_dir, theme + ".yaml")
        return self.load_yaml(theme_file)

    def check_origin_file(self, output_file, origin_file):
        with open(os.path.join(self.home_dir, origin_file), "r") as f:
            contents = f.read()
            if contents.find(output_file) < 0:
                print(
                    f"Please source {output_file} in {origin_file} for theme to take effect!"
                )

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

    @staticmethod
    def load_yaml(theme_file):
        with open(theme_file, "r") as f:
            try:
                return yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(f"Theme failed to load")
                print(e)


class Shell:
    def __init__(self):
        self.platform = sys.platform

    def load_theme(self, theme):
        if self.platform == "darwin":
            self.change_iterm_profile(theme)
            self.load_alfred_theme(theme)
        if self.platform == "linux":
            self.reload_xresources()
        self.reload_tmux()

    def change_iterm_profile(self, theme):
        template = "\e]1337;SetProfile={}\007"
        if os.getenv("TMUX") or os.getenv("TERM").find("tmux") >= 0:
            template = f"\ePtmux;\e{template}\e\\"
        command = "echo -n " + "'" + template.format(theme) + "'"
        self.call_with_shell(command)

    def reload_tmux(self):
        command = "tmux source-file ~/.tmux.conf"
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


def parse_arguments(themes):
    parser = argparse.ArgumentParser(description="Switch to a theme")
    g = parser.add_mutually_exclusive_group()
    g.add_argument("--list-themes", action="store_true")
    g.add_argument(
        "theme", type=str, nargs="?", metavar="THEME", choices=themes, help="theme name"
    )
    g.add_argument(
        "separator",
        type=str,
        nargs="?",
        metavar="SEPARATOR",
        choices=SEPARATORS.keys(),
        help="status bar separator type",
    )
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main():
    renderer = Renderer()
    shell = Shell()
    args = parse_arguments(renderer.themes)

    if args.list_themes:
        renderer.print_themes()
        return

    renderer.render_themed_files(args.theme, dry_run=args.dry_run)
    if not args.dry_run:
        shell.load_theme(args.theme)


if __name__ == "__main__":
    main()
