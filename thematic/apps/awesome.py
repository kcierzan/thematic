from thematic.apps import base
from thematic.util import call_with_shell


class Awesomewm(base.App):
    supported_oses = {"linux"}

    @staticmethod
    async def set_theme(theme: str) -> None:
        pass

    @staticmethod
    async def set_font(font: str) -> None:
        pass

    @staticmethod
    async def reload():
        command = "echo 'awesome.restart()' | awesome-client 2>/dev/null"
        await call_with_shell(command)
