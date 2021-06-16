from thematic.themes import base


class Indo(base.Theme):
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

    xcolors = base.Xcolors(
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
    autosuggestions = "238"
    tmux_mode_fg = red

