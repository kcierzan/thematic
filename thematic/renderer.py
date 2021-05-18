import os
import sys
from typing import Tuple, List

from jinja2 import Template
import yaml
import typer

from thematic import util
from thematic.constants import (
    ENABLED_APPS,
    ENABLED_BARS,
    ALACRITTY_CONFIG,
    THEME_DIR,
    APP_DIR,
    BAR_DIR,
)


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
            bar_data = util.load_yaml(bar_file)
            if bar_data["name"] in ENABLED_BARS:
                output_file = os.path.join(self.output_dir, bar_data["output_file"])
                if sys.platform in bar_data["os_types"]:
                    self.render_file(
                        bar_data["template"],
                        {"separators": util.load_separators()[separator_type]},
                        output_file,
                    )
                    self.maybe_source_generated_file(bar_data)

    def render_themed_files(self, theme, dry_run):
        self.maybe_create_output_directory()
        theme_data = util.get_theme_data(theme)
        for app_file in self.app_files:
            app_data = util.load_yaml(app_file)
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
        current = util.load_yaml(config_path)
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
