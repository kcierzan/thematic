import os
import pathlib

ENABLED_APPS = ["nvim", "zsh", "tmux", "rofi", "xcolors", "nvim", "galaxyline"]
ENABLED_BARS = ["nvim", "tmux", "galaxyline"]
NVIM_SOCKET = "NVIM_LISTEN_ADDRESS"
ALACRITTY_CONFIG = ".config/alacritty/alacritty.yml"
PACKAGE_DIR = pathlib.Path(__file__).parent.parent.resolve()
THEME_DIR = os.path.join(PACKAGE_DIR, "templates/themes")
APP_DIR = os.path.join(PACKAGE_DIR, "templates/applications")
BAR_DIR = os.path.join(PACKAGE_DIR, "templates/bars")
DATA_DIR = os.path.join(PACKAGE_DIR, "templates/data")
