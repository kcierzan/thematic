from thematic.apps import base


class Zsh(base.App):
    supported_oses = {"linux", "darwin"}
    config_file = ".zshenv"
    theme_file = "theme.zsh"
    theme_injection_config = {
        "command": "source",
        "with_quotes": True,
        "source_at_index": -2
    }
    template = """
    export BAT_THEME='{{bat_theme}}'
    export ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg={{autosuggestions}}'
    """

    @staticmethod
    async def set_theme(theme: str) -> None:
        pass

    @staticmethod
    async def set_font(font: str) -> None:
        pass

    @staticmethod
    async def reload() -> None:
        pass
