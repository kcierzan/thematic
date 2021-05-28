import abc


class App(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    async def set_theme(theme: str) -> None:
        ...

    @staticmethod
    @abc.abstractmethod
    async def set_font(font: str) -> None:
        ...

    @staticmethod
    @abc.abstractmethod
    async def reload() -> None:
        ...

    @staticmethod
    @abc.abstractmethod
    async def render_files(self):