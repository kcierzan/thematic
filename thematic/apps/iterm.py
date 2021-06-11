try:
    import iterm2
except:
    ...
import typer

from thematic import util
from thematic.apps import base
from thematic.themes import base as base_theme
from thematic.constants import FONTS


class Iterm(base.App):
    supported_oses = {"darwin"}

    @staticmethod
    async def reload() -> None:
        pass

    @staticmethod
    async def get_iterm_profile(connection):
        app = await iterm2.async_get_app(connection)
        session = app.current_window.current_tab.current_session
        if session is not None:
            profile = await session.async_get_profile()
            return profile

    async def set_theme(self, theme: base_theme.Theme) -> None:
        connection = iterm2.Connection()
        await self.set_iterm_colors(connection, theme)

    async def set_font(self, font) -> None:
        connection = iterm2.Connection()
        await self.set_iterm_font(connection, font)

    async def set_iterm_colors(self, connection, theme: base_theme.Theme) -> None:
        ...
        # profile = await self.get_iterm_profile(connection)
        # try:
        #     data = theme.asdict()
        #     iterm_colors_hex = data["iterm_colors"]
        # except KeyError:
        #     typer.echo("iTerm2 color data not defined in colorscheme")
        #     raise
        # for color_name, hex in iterm_colors_hex.items():
        #     color = iterm2.Color(*util.hex_to_rgb(hex))
        #     await getattr(profile, f"async_set_{color_name}_color")(color)

    async def set_iterm_font(self, connection, font: str) -> None:
        profile = await self.get_iterm_profile(connection)
        await profile.async_set_normal_font(f"{FONTS[font]['name']} 15")
        await profile.async_set_horizontal_spacing(FONTS[font]["horizontal_spacing"])
