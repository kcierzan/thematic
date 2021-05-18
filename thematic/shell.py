import os
import sys
import subprocess

try:
    import iterm2
except:
    ...
import typer
import yaml

from thematic import util
from thematic.constants import (
    ALACRITTY_CONFIG,
    NVIM_SOCKET
)


class Shell:
    def __init__(self):
        self.platform = sys.platform

    def load_theme(self, theme: str, iterm: bool) -> None:
        if self.platform == "darwin":
            self.load_alfred_theme(theme)
            if iterm:
                self.load_iterm_theme(theme)
        if self.platform == "linux":
            self.reload_xresources()
            self.restart_awesome()
        self.reload_tmux()
        self.reload_neovim()

    async def get_iterm_profile(self, connection):
        app = await iterm2.async_get_app(connection)
        session = app.current_window.current_tab.current_session
        if session is not None:
            profile = await session.async_get_profile()
            return profile

    def load_iterm_theme(self, theme: str) -> None:
        async def wrapped(connection):
            await self.set_iterm_colors(connection, theme)

        try:
            iterm2.run_until_complete(wrapped)
        except:
            ...

    async def set_iterm_colors(self, connection, theme: str) -> None:
        profile = await self.get_iterm_profile(connection)
        try:
            iterm_colors_hex = util.get_theme_data(theme)["iterm_colors"]
        except KeyError:
            typer.echo("iTerm2 color data not defined in colorscheme")
            raise
        for color_name, hex in iterm_colors_hex.items():
            color = iterm2.Color(*util.hex_to_rgb(hex))
            await getattr(profile, f"async_set_{color_name}_color")(color)

    async def set_iterm_font(self, connection, font: str) -> None:
        profile = await self.get_iterm_profile(connection)
        fonts = util.load_fonts()
        await profile.async_set_normal_font(f"{fonts[font]['name']} 15")
        await profile.async_set_horizontal_spacing(fonts[font]["horizontal_spacing"])

    def set_alacritty_font(self, font: str) -> None:
        config_path = os.path.join(os.path.expanduser("~"), ALACRITTY_CONFIG)
        current = util.load_yaml(config_path)
        fonts = util.load_fonts()
        new_font = {
            "font": {
                "bold": {
                    "family": fonts[font]["family"],
                },
                "normal": {
                    "family": fonts[font]["family"],
                    "style": fonts[font]["style"],
                },
                "italic": {
                    "family": fonts[font]["family"],
                },
            }
        }
        x_offset = fonts[font].get("x_offset")
        if x_offset:
            new_font["font"]["offset"] = {"x": x_offset}
        current.update(new_font)
        with open(config_path, "w") as f:
            yaml.dump(current, f, default_flow_style=False)

    def reload_tmux(self) -> None:
        command = "tmux source-file ~/.tmux.conf"
        self.call_with_shell(command)

    def reload_neovim(self) -> None:
        if not os.environ.get(NVIM_SOCKET):
            typer.echo(f"${NVIM_SOCKET} env var not set! Neovim will not be reloaded.")
            return

        nvim_socket = os.environ.get(NVIM_SOCKET)

        if nvim_socket and os.path.exists(nvim_socket):
            command = "nvr --nostart --remote-send ':so ~/.config/nvim/init.vim<CR>'"
            self.call_with_shell(command)

    def load_alfred_theme(self, theme) -> None:
        command = [
            "osascript",
            "-e",
            f'tell application "Alfred 4" to set theme "{theme}"',
        ]
        subprocess.Popen(command)

    def call_with_shell(self, command) -> None:
        subprocess.run(command, shell=True)

    def restart_awesome(self):
        command = "echo 'awesome.restart()' | awesome-client 2>/dev/null"
        self.call_with_shell(command)

    def reload_xresources(self) -> None:
        self.call_with_shell(
            "xrdb merge " + os.path.expanduser("~") + "/.Xresources 2>/dev/null"
        )


