import asyncio
import os

import aiofiles
import typer
from jinja2 import Template

from thematic import util
from thematic.apps.alacritty import Alacritty
from thematic.apps.alfred import Alfred
from thematic.apps.awesome import Awesomewm
from thematic.apps.galaxyline import Galaxyline
from thematic.apps.neovim import Neovim
from thematic.apps.rofi import Rofi
from thematic.apps.tmux import Tmux
from thematic.apps.xcolors import Xcolors
from thematic.apps.zsh import Zsh
from thematic.constants import (
    THEME_DIR,
    OPERATING_SYSTEM,
    SEPARATORS,
)


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
        self.home_dir = os.path.expanduser("~")
        self.output_dir = os.path.join(self.home_dir, ".thematic")
        self.themes = [
            f.split(".")[0]
            for f in os.listdir(THEME_DIR)
            if os.path.isfile(os.path.join(THEME_DIR, f))
        ]

    async def set_bars(self, separator_type: str):
        self.maybe_create_output_directory()

        async def safe_render(app):
            try:
                await self.render_file(
                    app.bar_template,
                    {"separators": SEPARATORS[separator_type]},
                    os.path.join(self.output_dir, app.bar_file),
                )
            except AttributeError:
                ...

        await asyncio.gather(
            *[safe_render(app) for app in self.apps],
            *[app.reload() for app in self.apps],
        )

    async def set_theme(self, theme, dry_run):
        self.maybe_create_output_directory()
        theme_data = await util.get_theme_data(theme)

        async def safe_render(app):
            try:
                await self.render_file(
                    app.theme_template,
                    theme_data,
                    os.path.join(self.output_dir, app.theme_file),
                )
            except AttributeError:
                ...

        await asyncio.gather(
            *[safe_render(app) for app in self.apps],
            *[app.set_theme(theme) for app in self.apps],
            *[app.reload() for app in self.apps],
        )

    async def set_font(self, font):
        await asyncio.gather(*[app.set_font(font) for app in self.apps])

    def maybe_create_output_directory(self):
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
    async def render_file(app_template, theme_data, output_path) -> None:
        temp = Template(app_template)
        rendered = temp.render(**theme_data)
        async with aiofiles.open(output_path, "w+") as output:
            await output.write(rendered)
