#!/usr/bin/env python3
import asyncio

import typer

from thematic.constants import FONTS, SEPARATORS
from thematic.themer import Themer

app = typer.Typer()
themer = Themer()


@app.command()
def colors(theme: str, dry_run: bool = False, iterm: bool = False) -> None:
    if theme == "":
        return
    if theme not in themer.themes:
        typer.echo(f"Colorscheme '{theme}' not found. Enter one of the following:")
        for theme in themer.themes:
            typer.echo(theme)
        return
    typer.echo(f"Setting colorscheme to {theme}...")
    if not dry_run:
        asyncio.run(themer.set_theme(theme, iterm))
        typer.echo("Colorscheme loaded.")


@app.command()
def bars(separator_style: str) -> None:
    if separator_style == "":
        return
    if separator_style not in SEPARATORS.keys():
        typer.echo(f"Bar '{separator_style}' not found. Enter one of the following:")
        for bar in SEPARATORS.keys():
            typer.echo(bar)
        return
    typer.echo(f"Setting bars to {separator_style}...")
    asyncio.run(themer.set_bars(separator_style))
    typer.echo("Bars updated.")


@app.command()
def font(font: str) -> None:
    if font == "":
        return
    if font not in FONTS:
        typer.echo(f"Font '{font}' not found. Enter one of the following:")
        for f in FONTS.keys():
            typer.echo(f)
        return
    typer.echo(f"Setting font to {font}...")
    asyncio.run(themer.set_font(font))
    typer.echo("Font updated.")


@app.command()
def list(option: str) -> None:
    if option == "fonts":
        for font in FONTS.keys():
            typer.echo(font)
    elif option == "colors":
        for theme in themer.themes:
            typer.echo(theme)
    elif option == "bars":
        for separator in SEPARATORS.keys():
            typer.echo(separator)
    else:
        typer.echo(f"Invalid option: '{option}'. Enter 'fonts', 'themes', or 'bars'.")


def main():
    app()


if __name__ == "__main__":
    main()
