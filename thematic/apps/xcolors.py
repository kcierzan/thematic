import os

from thematic import util
from thematic.apps import base


class Xcolors(base.App):
    supported_oses = {"linux", "darwin"}
    config_file = ".Xresources"
    theme_file = "thematic-xcolors"
    theme_template = """
*.foreground: {{foreground}}
*.background: {{dark_bg}}
*.color0: {{dark_bg}}
*.color1: {{xcolors_01}}
*.color2: {{xcolors_02}}
*.color3: {{xcolors_03}}
*.color4: {{xcolors_04}}
*.color5: {{xcolors_05}}
*.color6: {{xcolors_06}}
*.color7: {{xcolors_07}}
*.color8: {{xcolors_08}}
*.color9: {{xcolors_09}}
*.color10: {{xcolors_10}}
*.color11: {{xcolors_11}}
*.color12: {{xcolors_12}}
*.color13: {{xcolors_13}}
*.color14: {{xcolors_14}}
*.color15: {{xcolors_15}}
*.color257: {{foreground}}
*.color256: {{dark_bg}}
Sxiv.foreground: {{foreground}}
Sxiv.background: {{dark_bg}}
    """

    @staticmethod
    async def set_theme(theme: str) -> None:
        pass

    @staticmethod
    async def set_font(font: str) -> None:
        pass

    @staticmethod
    async def reload() -> None:
        await util.call_with_shell(
            "xrdb merge " + os.path.expanduser("~") + "/.Xresources 2>/dev/null"
        )
