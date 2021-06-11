from thematic.themes import base as base_theme
from thematic.apps import base


class Galaxyline(base.App):
    @staticmethod
    async def reload() -> None:
        pass

    @staticmethod
    async def set_theme(theme: base_theme.Theme) -> None:
        pass

    @staticmethod
    async def set_font(font: str) -> None:
        pass

    # TODO: how do we reload the theme?
    supported_oses = {"linux", "darwin"}
    config_file = ".config/nvim/lua/statusline.lua"
    theme_file = "galaxyline-colors.lua"
    bar_file = "galaxyline-separators.lua"
    theme_template = """
  local theme = {}

  theme.bg = "{{bg_bright}}"
  theme.line_bg = "{{bg_brighter}}"
  theme.fg = "{{foreground}}}"
  theme.green = "{{xcolors_02}}"
  theme.yellow = "{{xcolors_03}}"
  theme.cyan = "{{xcolors_06}}"
  theme.blue = "{{xcolors_04}}"
  theme.orange = "{{xcolors_09}}"
  theme.magenta = "{{xcolors_05}}"
  theme.red = "{{xcolors_01}}"

  return theme
    """
    bar_template = """
  local bars = {}

  bars.ls_left_separator = "{{separators[1]}}"
  bars.ls_right_separator = "{{separators[2]}}"

  return bars
    """
