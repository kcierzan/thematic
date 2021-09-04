import os

import aiofiles
import yaml

from thematic import util
from thematic.themes import base as base_theme
from thematic.apps import base
from thematic.constants import ALACRITTY_CONFIG, FONTS


class App(base.App):
    supported_oses = {"darwin", "linux"}

    @staticmethod
    async def reload() -> None:
        ...

    @staticmethod
    async def set_font(font: str) -> None:
        config_path = os.path.join(os.path.expanduser("~"), ALACRITTY_CONFIG)
        current_config = await util.load_yaml(config_path)
        new_font = {
            "font": {
                "bold": {
                    "family": FONTS[font]["family"],
                },
                "normal": {
                    "family": FONTS[font]["family"],
                    "style": FONTS[font]["style"],
                },
                "italic": {
                    "family": FONTS[font]["family"],
                },
            }
        }
        x_offset = FONTS[font].get("x_offset")
        if x_offset:
            new_font["font"]["offset"] = {"x": x_offset}
        current_config.update(new_font)
        async with aiofiles.open(config_path, "w") as f:
            await f.write(yaml.dump(current_config, default_flow_style=False))

    @staticmethod
    async def set_theme(theme: base_theme.Theme) -> None:
        config_path = os.path.join(os.path.expanduser("~"), ALACRITTY_CONFIG)
        current = await util.load_yaml(config_path)
        new_colors = {
            "colors": {
                "primary": {
                    "foreground":theme.xcolors.foreground,
                    "background":theme.xcolors.background,
                },
                "normal": {
                    "black":theme.xcolors.xcolors_00,
                    "red":theme.xcolors.xcolors_01,
                    "green":theme.xcolors.xcolors_02,
                    "yellow":theme.xcolors.xcolors_03,
                    "blue":theme.xcolors.xcolors_04,
                    "magenta":theme.xcolors.xcolors_05,
                    "cyan":theme.xcolors.xcolors_06,
                    "white":theme.xcolors.xcolors_07,
                },
                "bright": {
                    "black":theme.xcolors.xcolors_08,
                    "red":theme.xcolors.xcolors_09,
                    "green":theme.xcolors.xcolors_10,
                    "yellow":theme.xcolors.xcolors_11,
                    "blue":theme.xcolors.xcolors_12,
                    "magenta":theme.xcolors.xcolors_13,
                    "cyan":theme.xcolors.xcolors_14,
                    "white":theme.xcolors.xcolors_15,
                },
                "cursor": {
                    "cursor":theme.cursor,
                    "text":theme.cursor_text,
                }
            }
        }
        current.update(new_colors)
        async with aiofiles.open(config_path, "w") as f:
            await f.write(yaml.dump(current, default_flow_style=False))
