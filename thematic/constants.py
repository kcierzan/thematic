import os
import pathlib
import sys

OPERATING_SYSTEM = sys.platform
ENABLED_APPS = ["nvim", "zsh", "tmux", "rofi", "xcolors", "nvim", "galaxyline"]
ENABLED_BARS = ["nvim", "tmux", "galaxyline"]
NVIM_SOCKET = "NVIM_LISTEN_ADDRESS"
ALACRITTY_CONFIG = ".config/alacritty/alacritty.yml"
PACKAGE_DIR = pathlib.Path(__file__).parent.parent.resolve()
APP_DIR = os.path.join(PACKAGE_DIR, "templates/applications")
BAR_DIR = os.path.join(PACKAGE_DIR, "templates/bars")
DATA_DIR = os.path.join(PACKAGE_DIR, "templates/data")

SEPARATORS = {
    "rounded": ["", "", "", "", "", ""],
    "slant_1": ["█", "", "", "", "", "█"],
    "slant_2": ["", "", "", "", "", ""],
    "fade": ["", "", "", "", "", ""],
    "tabbed": ["█", "", "", "", "", "█"],
    "diamond": ["█", "", "", "", "", "█"],
    "trapezoid": ["█", "█", "█", "█", "█", "█"],
    "none": ["█", "█", "█", "█", "█", "█"]
}

FONTS = {
    "jetbrains": {
        "name": "JetBrainsMonoNerdFontCompleteM-Regular",
        "horizontal_spacing": 1,
        "family": "JetBrainsMono Nerd Font Mono",
        "style": "Medium"
    },
    "cascadia": {
        "name": "CaskaydiaCoveNerdFontCompleteM-",
        "horizontal_spacing": 1,
        "family": "CaskaydiaCove Nerd Font Mono",
        "style": "Book"
    },
    "hack": {
        "name": "HackNerdFontCompleteM-Regular",
        "horizontal_spacing": 1,
        "family": "Hack Nerd Font Mono",
        "style": "Regular"
    },
    "iosevka": {
        "name": "IosevkaNerdFontCompleteM-Term",
        "horizontal_spacing": 1,
        "family": "Iosevka Nerd Font Mono",
        "style": "Medium"
    },
    "mononoki": {
        "name": "mononokiNerdFontCompleteM-Regular",
        "horizontal_spacing": 1,
        "family": "mononoki Nerd Font Mono",
        "style": "Regular"
    },
    "fira": {
        "name": "FiraCodeNerdFontCompleteM-Retina",
        "horizontal_spacing": 1,
        "family": "FiraCode Nerd Font Mono",
        "style": "Retina"
    },
    "inconsolata": {
        "name": "InconsolataLGCNerdFontCompleteM-",
        "horizontal_spacing": 1,
        "family": "InconsolataLGC Nerd Font Mono",
        "style": "Medium"
    },
    "monoid": {
        "name": "MonoidNerdFontCompleteM-Retina",
        "horizontal_spacing": 1,
        "family": "Monoid Nerd Font Mono",
        "style": "Retina"
    },
    "victor": {
        "name": "VictorMonoNerdFontCompleteM-Medium",
        "horizontal_spacing": 1.1,
        "family": "VictorMono Nerd Font Mono",
        "style": "Medium"
    },
    "imw": {
        "name": "iMWritingMonoSNerdFontCompleteM-Regular",
        "horizontal_spacing": 0.7,
        "x_offset": -7,
        "family": "iMWritingMonoS Nerd Font Mono",
        "style": "Regular"
    },
    "blex": {
        "name": "BlexMonoNerdFontCompleteM-Medium",
        "horizontal_spacing": 1,
        "family": "BlexMono Nerd Font Mono",
        "style": "Medium"
    },
    "sauce": {
        "name": "SauceCodeProNerdFontCompleteM-Medium",
        "horizontal_spacing": 1,
        "family": "SauceCodePro Nerd Font Mono",
        "style": "Medium"
    },
    "roboto": {
        "name": "RobotoMonoNerdFontCompleteM-Regular",
        "horizontal_spacing": 0.85,
        "x_offset": -2,
        "family": "RobotoMono Nerd Font Mono",
        "style": "Medium"
    }
}

