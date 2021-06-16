from thematic.themes import base


class Dracula(base.Theme):
    name = "dracula"

    foreground = "#f9f9f4"
    background = "#272936"
    bg_bright = "#313446"
    bg_brighter = "#474b64"
    bg_brightest = "#555a78"
    red = "#ff6d67"
    red_bright = "#473536"
    cyan = "#99ecfd"
    purple = "#c9a8fa"
    blue = "#7ad5f1"
    yellow = "#f3f89d"
    orange = "#ef9062"
    green = "#59f68d"
    black = "#2e3140"
    black_bright = "#1A181A"
    pink = "#ff92d0"
    white = "#c7c7c7"
    white_bright = "#feffff"

    autosuggestions = "238"
    tmux_mode_fg = green

    xcolors = base.Xcolors(
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

