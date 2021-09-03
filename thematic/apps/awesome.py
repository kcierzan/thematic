from thematic.apps import base
from thematic.themes import base as base_theme
from thematic.util import call_with_shell


class App(base.App):
    supported_oses = {"linux"}

    @staticmethod
    async def set_theme(_: base_theme.Theme) -> None:
        ...

    @staticmethod
    async def set_font(font: str) -> None:
        ...

    @staticmethod
    async def reload():
        command = "echo 'awesome.restart()' | awesome-client 2>/dev/null"
        await call_with_shell(command)
