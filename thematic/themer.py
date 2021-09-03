import asyncio
from functools import cached_property
import importlib
from importlib import resources
import os
from typing import List
from types import ModuleType

import aiofiles
from jinja2 import Template
import typer

from thematic.apps.base import App
from thematic.constants import OPERATING_SYSTEM, SEPARATORS


class Themer:
    def __init__(self):
        self.output_dir = os.path.join(os.path.expanduser("~"), ".thematic")

    @staticmethod
    def _is_theme_module(filename: str) -> bool:
        return filename.endswith(".py") and not filename.startswith("_") and filename != "base.py"
    
    @cached_property
    def themes(self) -> List[str]:
        themes = filter(self._is_theme_module, resources.contents("thematic.themes"))
        return [theme[:-3] for theme in themes]

    @cached_property
    def apps(self) -> List[App]:
        apps = filter(self._is_theme_module, resources.contents("thematic.apps"))
        # don't include the ".py" when importing
        modules = [importlib.import_module(f"thematic.apps.{app[:-3]}").App for app in apps]
        return [app for app in modules if OPERATING_SYSTEM in app.supported_oses]

    def _import_theme(self, theme) -> ModuleType:
        return importlib.import_module(f"thematic.themes.{theme}")

    def _import_app(self, app: str) -> ModuleType:
        return importlib.import_module(f"thematic.apps.{app}")
        
    async def set_bars(self, separator_type: str) -> None:
        self._maybe_create_output_directory()

        async def safe_render(app: App) -> None:
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

    async def set_theme(self, theme: str) -> None:
        self._maybe_create_output_directory()
        theme_module = self._import_theme(theme)

        async def safe_render(app: App):
            if not (app.theme_template and app.theme_file):
                return
            await self._render_file(
                app.theme_template,
                theme_module.Theme.asdict(),
                os.path.join(self.output_dir, app.theme_file),
            )

        await asyncio.gather(
            *[safe_render(app) for app in self.apps],
            *[app.set_theme(theme_module.Theme) for app in self.apps],
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
