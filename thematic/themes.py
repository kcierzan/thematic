from dataclasses import dataclass


@dataclass
class Colors:
    foreground: str
    background: str
    black: str  # black
    red: str  # red
    green: str  # green
    yellow: str  # yellow
    blue: str  # blue
    purple: str  # magenta
    cyan: str  # cyan
    white: str  # white
    black_bright: str  # black
    red_bright: str  # bright red
    green_bright: str  # bright green
    yellow_bright: str  # bright yellow
    blue_bright: str  # bright blue
    purple_bright: str  # bright magenta
    cyan_bright: str  # bright cyan
    white_bright: str  # bright white


class Onedark:
    name = "onedark"
    colors = Colors(
        foreground="#B2BED1",
        background="#282C34",
        black="#393f4a",
        red="#ff6c6b",
        green="#98C379",
        yellow="#ecbe7b",
        blue="#51afef",
        purple="#c678dd",
        cyan="#46d9ff",
        white="#b9bfc9",
        black_bright="#6f7683",
        red_bright="#c9665b",
        green_bright="#62ac65",
        yellow_bright="#d9a97c",
        blue_bright="#71bdf2",
        purple_bright="#a9a1e1",
        cyan_bright="#4db5bd",
        white_bright="#afb0b5",
    )

    bat_theme = "TwoDark"
    autosuggestions = "238"
    foreground = colors.foreground
    background = colors.background
    bg_bright = "#2C323D"
    bg_brighter = "#393f4a"
    bg_brightest = "#505868"
    xcolors_01 = colors.red
    xcolors_02 = colors.green
    xcolors_03 = colors.yellow
    xcolors_04 = colors.blue
    xcolors_05 = colors.purple
    xcolors_06 = colors.cyan
    xcolors_07 = colors.white
    xcolors_08 = colors.black_bright
    xcolors_09 = colors.red_bright
    xcolors_10 = colors.green_bright
    xcolors_11 = colors.yellow_bright
    xcolors_12 = colors.blue_bright
    xcolors_13 = colors.purple_bright
    xcolors_14 = colors.cyan_bright
    xcolors_15 = colors.white_bright
    tmux_mode_fg = colors.yellow


class Indo:
    name = "indo"
    colors = Colors(
        background="#2a2c3a",
        foreground="#eeeeee",
        black="#2f343f",
        red="#fd6b85",
        green="#b2e07d",
        yellow="#fed270",
        blue="#67d4f2",
        purple="#ff8167",
        cyan="#63e0be",
        white="#b1a6ee",
        black_bright="#4f4f5b",
        red_bright="#fd6b85",
        green_bright="#b2e07d",
        yellow_bright="#fed270",
        blue_bright="#67d4f2",
        purple_bright="#ff8167",
        cyan_bright="#63e0be",
        white_bright="#b1a6ee",
    )
    bat_theme = "TwoDark"
    autosuggestions = "238"
    foreground = colors.foreground
    background = colors.background
    bg_bright = "#2C323D"
    bg_brighter = "#393f4a"
    bg_brightest = "#505868"
    xcolors_01 = colors.red
    xcolors_02 = colors.green
    xcolors_03 = colors.yellow
    xcolors_04 = colors.blue
    xcolors_05 = colors.purple
    xcolors_06 = colors.cyan
    xcolors_07 = colors.white
    xcolors_08 = colors.black_bright
    xcolors_09 = colors.red_bright
    xcolors_10 = colors.green_bright
    xcolors_11 = colors.yellow_bright
    xcolors_12 = colors.blue_bright
    xcolors_13 = colors.purple_bright
    xcolors_14 = colors.cyan_bright
    xcolors_15 = colors.white_bright
    tmux_mode_fg = colors.yellow
