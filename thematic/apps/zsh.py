from thematic.themes import base as base_theme
from thematic.apps import base


class App(base.App):
    supported_oses = {"linux", "darwin"}
    config_file = ".zshenv"
    theme_file = "theme.zsh"
    theme_template = """
export ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg={{autosuggestions}}'
    """

    @staticmethod
    async def set_theme(theme: base_theme.Theme) -> None:
        pass

    @staticmethod
    async def set_font(font: str) -> None:
        pass

    @staticmethod
    async def reload() -> None:
        pass
