from thematic.themes import base


class SolarizedDark(base.Theme):
    name = "solarized-dark"

    foreground = "#839496"
    background = "#002b36"
    bg_bright = "#003240"
    bg_brighter = "#004255"
    bg_brightest = "#00495f"
    black = "#073642"
    black_bright = "#1A181A"
    blue = "#268bd2"
    grey1 = "#839496"
    cyan = "#2aa198"
    grey2 = "#93a1a1"
    green = "#859900"
    grey3 = "#586e75"
    pink = "#d33682"
    purple = "#6c71c4"
    yellow = "#b58900"
    orange = "#cb4b16"
    red = "#dc322f"
    white = "#eee8d5"
    white_bright = "#fdf6e3"

    autosuggestions = "238"
    tmux_mode_fg = purple

    xcolors = base.Xcolors(
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

