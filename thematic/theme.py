#!/usr/bin/env python3
try:
    import iterm2
except:
    ...

import typer

from thematic import util
from thematic.shell import Shell
from thematic.renderer import Renderer


app = typer.Typer()

class NotImplementedError(Exception):
    pass


@app.command()
def colors(theme: str, dry_run: bool = False, iterm: bool = False) -> None:
    renderer = Renderer()
    if theme not in renderer.themes:
        typer.echo(f"Colorscheme '{theme}' not found. Enter one of the following:")
        for theme in renderer.themes:
            typer.echo(theme)
        return
    typer.echo(f"Setting colorscheme to {theme}...")
    shell = Shell()
    renderer.render_themed_files(theme, dry_run=dry_run)
    if not dry_run:
        shell.load_theme(theme, iterm)
        typer.echo("Colorscheme loaded.")


@app.command()
def bars(separator_style: str) -> None:
    separators = util.load_separators()
    if separator_style not in separators.keys():
        typer.echo(f"Bar '{separator_style}' not found. Enter one of the following:")
        for bar in separators.keys():
            typer.echo(bar)
        return
    typer.echo(f"Setting bars to {separator_style}...")
    renderer = Renderer()
    shell = Shell()
    renderer.set_bars(separator_style)
    shell.reload_tmux()
    shell.reload_neovim()
    typer.echo("Bars updated.")


@app.command()
def font(font: str, iterm: bool = False) -> None:
    shell = Shell()
    typer.echo(f"Setting font to {font}...")
    try:
        if iterm:

            async def wrapped(connection):
                await shell.set_iterm_font(connection, font)

            iterm2.run_until_complete(wrapped)
        else:
            shell.set_alacritty_font(font)
    except KeyError:
        typer.echo(f"Font '{font}' not found. Enter one of the following:")
        fonts = util.load_fonts()
        for font in fonts.keys():
            typer.echo(font)
        return
    typer.echo("Font updated.")


@app.command()
def list(option: str) -> None:
    if option == "fonts":
        for font in util.load_fonts().keys():
            typer.echo(font)
    elif option == "colors":
        renderer = Renderer()
        for theme in renderer.themes:
            typer.echo(theme)
    elif option == "bars":
        for separator in util.load_separators().keys():
            typer.echo(separator)
    else:
        typer.echo(f"Invalid option: '{option}'. Enter 'fonts', 'themes', or 'bars'.")


def main():
    app()


if __name__ == "__main__":
    main()
