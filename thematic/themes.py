from dataclasses import dataclass


@dataclass
class Xcolors:
    foreground: str
    background: str
    xcolors_00: str
    xcolors_01: str
    xcolors_02: str
    xcolors_03: str
    xcolors_04: str
    xcolors_05: str
    xcolors_06: str
    xcolors_07: str
    xcolors_08: str
    xcolors_09: str
    xcolors_10: str
    xcolors_11: str
    xcolors_12: str
    xcolors_13: str
    xcolors_14: str
    xcolors_15: str

class Theme:
    name = ""
    autosuggestions = ""
    bat_theme = ""
    tmux_mode_fg = ""
    bg_bright = ""
    bg_brighter = ""
    bg_brightest = ""
    xcolors = Xcolors(
        foreground="",
        background="",
        xcolors_00="",
        xcolors_01="",
        xcolors_02="",
        xcolors_03="",
        xcolors_04="",
        xcolors_05="",
        xcolors_06="",
        xcolors_07="",
        xcolors_08="",
        xcolors_09="",
        xcolors_10="",
        xcolors_11="",
        xcolors_12="",
        xcolors_13="",
        xcolors_14="",
        xcolors_15=""
    )

    @classmethod
    def asdict(cls) -> dict:
        return {
            "name": cls.name,
            "autosuggestions": cls.autosuggestions,
            "bat_theme": cls.bat_theme,
            "tmux_mode_fg": cls.tmux_mode_fg,
            "bg_bright": cls.bg_bright,
            "bg_brighter": cls.bg_brighter,
            "bg_brightest": cls.bg_brightest,
            **vars(cls.xcolors)
        }


class Onedark(Theme):
    name = "onedark"
    foreground = "#B2BED1"
    background = "#282C34"
    bg_bright = "#2C323D"
    bg_brighter = "#393f4a"
    bg_brightest = "#505868"

    black = "#393f4a"
    red = "#ff6c6b"
    green = "#98C379"
    yellow = "#ecbe7b"
    blue = "#51afef"
    purple = "#c678dd"
    cyan = "#46d9ff"
    cyan_bright = "#4db5bd"
    white = "#b9bfc9"
    black_bright = "#6f7683"
    red_bright = "#c9665b"
    green_bright = "#62ac65"
    yellow_bright = "#d9a97c"
    blue_bright = "#71bdf2"
    purple_bright = "#a9a1e1"
    white_bright = "#afb0b5"

    bat_theme = "TwoDark"
    autosuggestions = "238"
    tmux_mode_fg = blue

    xcolors = Xcolors(
        foreground=foreground,
        background=background,
        xcolors_00=black,
        xcolors_01=red,
        xcolors_02=green,
        xcolors_03=yellow,
        xcolors_04=blue,
        xcolors_05=purple,
        xcolors_06=cyan,
        xcolors_07=white,
        xcolors_08=black_bright,
        xcolors_09=red_bright,
        xcolors_10=green_bright,
        xcolors_11=yellow_bright,
        xcolors_12=blue_bright,
        xcolors_13=purple_bright,
        xcolors_14=cyan_bright,
        xcolors_15=white_bright
    )


class Indo(Theme):
    name = "indo"

    background = "#2a2c3a"
    foreground = "#eeeeee"
    bg_bright = "#2C323D"
    bg_brighter = "#393f4a"
    bg_brightest = "#505868"
    black = "#2f343f"
    red = "#fd6b85"
    green = "#b2e07d"
    yellow = "#fed270"
    blue = "#67d4f2"
    orange = "#ff8167"
    cyan = "#63e0be"
    purple = "#b1a6ee"
    light_purple = "#4f4f5b"

    xcolors = Xcolors(
        background=background,
        foreground=foreground,
        xcolors_00=black,
        xcolors_01=red,
        xcolors_02=green,
        xcolors_03=yellow,
        xcolors_04=blue,
        xcolors_05=purple,
        xcolors_06=orange,
        xcolors_07=foreground,
        xcolors_08=light_purple,
        xcolors_09=red,
        xcolors_10=green,
        xcolors_11=yellow,
        xcolors_12=blue,
        xcolors_13=orange,
        xcolors_14=cyan,
        xcolors_15=light_purple,
    )
    # TODO
    bat_theme = "TwoDark"
    autosuggestions = "238"
    tmux_mode_fg = red


class GruvboxDark(Theme):
    name = "gruvbox-dark"

    foreground = '#ddc7a1'
    background = '#282828'
    bg_bright = "#32302f"
    bg_brighter = "#3c3836"
    bg_brightest = "#45403d"
    red = '#ea6962'
    cyan = '#89b482'
    blue = '#7daea3'
    yellow = '#d8a657'
    orange = '#e78a4e'
    green = '#a9b665'
    black = '#46413e'
    black_bright = '#5b534d'
    purple = '#d3869b'
    white = '#d4be98'
    white_bright = '#a89984'

    autosuggestions = "238"
    bat_theme = "gruvbox-dark"
    tmux_mode_fg = orange

    xcolors = Xcolors(
        foreground=foreground,
        background=background,
        xcolors_00=black,
        xcolors_01=red,
        xcolors_02=green,
        xcolors_03=yellow,
        xcolors_04=blue,
        xcolors_05=purple,
        xcolors_06=cyan,
        xcolors_07=white,
        xcolors_08=black_bright,
        xcolors_09=red,
        xcolors_10=green,
        xcolors_11=yellow,
        xcolors_12=blue,
        xcolors_13=orange,
        xcolors_14=cyan,
        xcolors_15=white_bright,
    )


class Dracula(Theme):
    name = "dracula"

    foreground = '#f9f9f4'
    background = '#272936'
    bg_bright = '#313446'
    bg_brighter = '#474b64'
    bg_brightest = '#555a78'
    red = '#ff6d67'
    red_bright = '#473536'
    cyan = '#99ecfd'
    purple = '#c9a8fa'
    blue = '#7ad5f1'
    yellow = '#f3f89d'
    orange = '#ef9062'
    green = '#59f68d'
    black = '#2e3140'
    black_bright = '#1A181A'
    pink = '#ff92d0'
    white = '#c7c7c7'
    white_bright = '#feffff'

    bat_theme = "Dracula"
    autosuggestions = "238"
    tmux_mode_fg = green

    xcolors = Xcolors(
        foreground=foreground,
        background=background,
        xcolors_00=black,
        xcolors_01=red,
        xcolors_02=green,
        xcolors_03=yellow,
        xcolors_04=purple,
        xcolors_05=pink,
        xcolors_06=cyan,
        xcolors_07=white,
        xcolors_08=black_bright,
        xcolors_09=red_bright,
        xcolors_10=green,
        xcolors_11=yellow,
        xcolors_12=blue,
        xcolors_13=orange,
        xcolors_14=cyan,
        xcolors_15=white_bright,
    )


class SolarizedDark(Theme):
    name = "solarized-dark"

    foreground = '#839496'
    background = '#002b36'
    bg_bright = '#003240'
    bg_brighter = '#004255'
    bg_brightest = '#00495f'
    black = '#073642'
    black_bright = '#1A181A'
    blue = '#268bd2'
    grey1 = '#839496'
    cyan = '#2aa198'
    grey2 = '#93a1a1'
    green = '#859900'
    grey3 = '#586e75'
    pink = '#d33682'
    purple = '#6c71c4'
    yellow = '#b58900'
    orange = '#cb4b16'
    red = '#dc322f'
    white = '#eee8d5'
    white_bright = '#fdf6e3'

    bat_theme = "Solarized (dark)"
    autosuggestions = "238"
    tmux_mode_fg = purple

    xcolors = Xcolors(
        foreground=foreground,
        background=background,
        xcolors_00=black,
        xcolors_01=red,
        xcolors_02=green,
        xcolors_03=yellow,
        xcolors_04=blue,
        xcolors_05=pink,
        xcolors_06=cyan,
        xcolors_07=white,
        xcolors_08=black_bright,
        xcolors_09=red,
        xcolors_10=green,
        xcolors_11=yellow,
        xcolors_12=purple,
        xcolors_13=orange,
        xcolors_14=cyan,
        xcolors_15=white_bright,
    )


class SonokaiShusia(Theme):
    name = "sonokai-shusia"

    foreground = '#E3E1E4'
    background = '#2D2A2E'
    bg_bright = '#343136'
    bg_brighter = '#3B383E'
    bg_brightest = '#423F46'
    red_bright = '#473536'
    cyan = '#7AD5F1'
    blue = '#72CCE8'
    blue_bright = '#7AD5F1'
    orange = '#EF9062'
    yellow = '#E5C463'
    green = '#9ECD6F'
    black = '#1A181A'
    purple = '#AB9DF2'
    red = '#FF6D7E'
    green_bright = '#A5E179'
    white = '#828A9A'

    autosuggestions = "238"
    bat_theme = "Monokai Extended Origin"
    tmux_mode_fg = orange

    xcolors = Xcolors(
        foreground=foreground,
        background=background,
        xcolors_00=black,
        xcolors_01=red,
        xcolors_02=green,
        xcolors_03=yellow,
        xcolors_04=blue,
        xcolors_05=purple,
        xcolors_06=cyan,
        xcolors_07=white,
        xcolors_08=black,
        xcolors_09=red_bright,
        xcolors_10=green,
        xcolors_11=yellow,
        xcolors_12=blue_bright,
        xcolors_13=orange,
        xcolors_14=cyan,
        xcolors_15=white,
    )

THEMES = {theme.name: theme for theme in (Onedark, GruvboxDark, Indo, SolarizedDark, SonokaiShusia)}
