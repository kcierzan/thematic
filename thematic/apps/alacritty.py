import os

import aiofiles
import yaml

from thematic import util
from thematic.apps import base
from thematic.constants import ALACRITTY_CONFIG, FONTS


class Alacritty(base.App):
    supported_oses = {"linux", "darwin"}

    @staticmethod
    async def reload() -> None:
        pass

    @staticmethod
    async def set_font(font: str) -> None:
        config_path = os.path.join(os.path.expanduser("~"), ALACRITTY_CONFIG)
        current = await util.load_yaml(config_path)
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
        current.update(new_font)
        async with aiofiles.open(config_path, "w") as f:
            await f.write(yaml.dump(current, default_flow_style=False))

    @staticmethod
    async def set_theme(theme: str) -> None:
        config_path = os.path.join(os.path.expanduser("~"), ALACRITTY_CONFIG)
        current = await util.load_yaml(config_path)
        theme_data = await util.get_theme_data(theme)
        c = theme_data["iterm_colors"]
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
        async with aiofiles.open(config_path, "w") as f:
            await f.write(yaml.dump(current, default_flow_style=False))



