import os

from thematic import util
from thematic.apps import base


class Xcolors(base.App):
    supported_oses = {"linux"}

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



