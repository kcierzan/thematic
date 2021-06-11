from thematic.themes import base


class GruvboxDark(base.Theme):
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
        xcolors_09=red,
        xcolors_10=green,
        xcolors_11=yellow,
        xcolors_12=blue,
        xcolors_13=orange,
        xcolors_14=cyan,
        xcolors_15=white_bright,
    )


