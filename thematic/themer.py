import asyncio
import os

import aiofiles
from jinja2 import Template
import typer

from thematic.apps.alacritty import Alacritty
from thematic.apps.alfred import Alfred
from thematic.apps.awesome import Awesomewm
from thematic.apps.base import App
from thematic.apps.galaxyline import Galaxyline
from thematic.apps.rofi import Rofi
from thematic.apps.tmux import Tmux
from thematic.apps.neovim import Neovim
from thematic.apps.xcolors import Xcolors
from thematic.apps.zsh import Zsh
from thematic.constants import OPERATING_SYSTEM, SEPARATORS
from thematic.themes.onedark import Onedark
from thematic.themes.gruvbox_dark import GruvboxDark


THEMES = {theme.name: theme for theme in (Onedark, GruvboxDark)}


class Themer:
    def __init__(self):
        apps = (
            Alfred,
            Awesomewm,
            Neovim,
            Galaxyline,
            Tmux,
            Rofi,
            Zsh,
            Xcolors,
            Alacritty,
        )
        self.apps = [app() for app in apps if OPERATING_SYSTEM in app.supported_oses]
        self.output_dir = os.path.join(os.path.expanduser("~"), ".thematic")
        self.themes = THEMES.keys()

    async def set_bars(self, separator_type: str):
        self._maybe_create_output_directory()

        async def safe_render(app: App):
            if not (app.bar_template and app.bar_file):
                return
            await self._render_file(
                app.bar_template,
                {"separators": SEPARATORS[separator_type]},
                os.path.join(self.output_dir, app.bar_file),
            )

        await asyncio.gather(
            *[safe_render(app) for app in self.apps],
            *[app.reload() for app in self.apps],
        )

    async def set_theme(self, theme: str):
        self._maybe_create_output_directory()

        async def safe_render(app: App):
            if not (app.theme_template and app.theme_file):
                return
            await self._render_file(
                app.theme_template,
                THEMES[theme].asdict(),
                os.path.join(self.output_dir, app.theme_file),
            )

        await asyncio.gather(
            *[safe_render(app) for app in self.apps],
            *[app.set_theme(THEMES[theme]) for app in self.apps],
            *[app.reload() for app in self.apps],
        )

    async def set_font(self, font: str) -> None:
        await asyncio.gather(*[app.set_font(font) for app in self.apps])

    def _maybe_create_output_directory(self) -> None:
        if not os.path.isdir(self.output_dir):
            typer.echo(
                f"Output directory not found: creating directory at {self.output_dir}"
            )
            try:
                os.mkdir(self.output_dir)
            except OSError:
                typer.echo("Error creating output directory")
                raise

    @staticmethod
    async def _render_file(
        app_template: str, theme_data: dict, output_path: str
    ) -> None:
        temp = Template(app_template)
        rendered = temp.render(**theme_data)
        async with aiofiles.open(output_path, "w+") as output:
            await output.write(rendered)
