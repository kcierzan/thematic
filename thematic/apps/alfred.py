from thematic import util
from thematic.apps import base
from thematic.themes import base as base_theme


class Alfred(base.App):
    supported_oses = {"darwin"}

    @staticmethod
    async def set_font(font: str) -> None:
        pass

    @staticmethod
    async def reload() -> None:
        pass

    @staticmethod
    async def set_theme(theme: base_theme.Theme) -> None:
        command = (
            f'osascript -e tell application "Alfred 4" to set theme "{theme.name}"'
        )
        await util.call_with_shell(command)

