from thematic import util
from thematic.apps import base


class Alfred(base.App):
    supported_oses = {"darwin"}

    @staticmethod
    async def set_font(font: str) -> None:
        pass

    @staticmethod
    async def reload() -> None:
        pass

    @staticmethod
    async def set_theme(theme) -> None:
        command = f'osascript -e tell application "Alfred 4" to set theme "{theme}"'
        await util.call_with_shell(command)


