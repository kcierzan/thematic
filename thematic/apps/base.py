import abc

from thematic.themes import base

class App(abc.ABC):
    theme_template = None
    theme_file = None
    bar_template = None
    bar_file = None

    @staticmethod
    @abc.abstractmethod
    async def set_theme(theme: base.Theme) -> None:
        ...

    @staticmethod
    @abc.abstractmethod
    async def set_font(font: str) -> None:
        ...

    @staticmethod
    @abc.abstractmethod
    async def reload() -> None:
        ...
