from thematic.themes import base


class Theme(base.Theme):
    foreground = "#E3E1E4"
    background = "#2D2A2E"
    bg_bright = "#343136"
    bg_brighter = "#3B383E"
    bg_brightest = "#423F46"
    red_bright = "#473536"
    cyan = "#7AD5F1"
    blue = "#72CCE8"
    blue_bright = "#7AD5F1"
    orange = "#EF9062"
    yellow = "#E5C463"
    green = "#9ECD6F"
    black = "#1A181A"
    purple = "#AB9DF2"
    red = "#FF6D7E"
    green_bright = "#A5E179"
    white = "#828A9A"

    autosuggestions = "238"
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
        xcolors_08=black,
        xcolors_09=red_bright,
        xcolors_10=green,
        xcolors_11=yellow,
        xcolors_12=blue_bright,
        xcolors_13=orange,
        xcolors_14=cyan,
        xcolors_15=white,
    )

    nvim_plugins = base.NeovimPluginTheme(
        NvimTreeFolderName={"fg": foreground},
        NvimTreeOpenedFolderName={"fg": foreground}
    )
