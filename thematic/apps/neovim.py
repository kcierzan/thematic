import os

import typer

from thematic import util
from thematic.apps import base
from thematic.constants import NVIM_SOCKET


class Neovim(base.App):
    supported_oses = {"darwin", "linux"}
    config_file = ".config/nvim/init.vim"
    theme_file = "theme.vim"
    theme_injection_config = {
        "command": "source",
        "with_quotes": False,
        "source_at_index": -2,
    }
    theme_template = """
{{vim_color_config}}
colorscheme {{vim_colorscheme}}
    
{{vim_overrides}}
    """

    @staticmethod
    async def set_theme(theme: str) -> None:
        pass

    @staticmethod
    async def set_font(font: str) -> None:
        pass

    @staticmethod
    async def reload() -> None:
        if not os.environ.get(NVIM_SOCKET):
            typer.echo(f"${NVIM_SOCKET} env var not set! Neovim will not be reloaded.")
            return

        nvim_socket = os.environ.get(NVIM_SOCKET)

        if nvim_socket and os.path.exists(nvim_socket):
            command = "nvr --nostart --remote-send ':so ~/.config/nvim/init.vim<CR>'"
            await util.call_with_shell(command)
