from thematic.themes import base


class Onedark(base.Theme):
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

    xcolors = base.Xcolors(
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

