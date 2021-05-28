from thematic import util
from thematic.apps import base


class Tmux(base.App):
    supported_oses = {"linux", "darwin"}
    config_file = ".tmux.conf"
    theme_file = "theme.conf"
    bar_file = "bars.conf"
    theme_injection_config = {
        "command": "source-file",
        "with_quotes": False,
        "source_at_index": -3
    }
    bar_injection_config = {
        "command": "source-file",
        "with_quotes": False,
        "source_at_index": -4
    }
    theme_template = """
  set -g status-position bottom
  set -g status-justify "left"
  set -g status-style "bg={{light_bg}}"
  set -g window-style "bg={{light_bg}}"
  set -g mode-style "bg={{lightest_bg}} fg={{tmux_mode_fg}}"

  # --------- LEFT HAND SEGMENTS ------------------
  # clear status-left
  set -g status-left ""

  # start far left hand segment
  set -ga status-left "#[fg={{lightest_bg}} bg={{light_bg}}]$FAR_LEFT_SEPARATOR"

  # tmux logo
  set -ga status-left "#[fg=colour03 bg={{lightest_bg}}]﬿ "

  # session name
  set -ga status-left "#[fg=colour05 bg={{lighter_bg}}] #S"

  # end right hand segment
  set -ga status-left "#[fg={{lighter_bg}} bg={{light_bg}}]$LH_RIGHT_SEPARATOR "

  set -g status-left-length 100

  # --------- RIGHT HAND SEGMENTS -----------------
  # clear status-right
  set -g status-right ""

  # start right hand segment
   set -ga status-right "#[fg={{lighter_bg}}]$RH_LEFT_SEPARATOR"

  # 12 hour time with AM/PM
   set -ga status-right "#[fg={{xcolors_03}} bg={{lighter_bg}}]%I:%M %p"

  # end right hand segment
   set -ga status-right "#[fg={{lighter_bg}} bg={{light_bg}}]$RH_RIGHT_SEPARATOR "

  # start right hand segment
  set -ga status-right "#[fg={{lighter_bg}} bg={{light_bg}}]$RH_LEFT_SEPARATOR"

  # Short date
  set -ga status-right "#[fg={{xcolors_02}} bg={{lighter_bg}}]%b %d"

  # end right hand segment
  set -ga status-right "#[fg={{lighter_bg}} bg={{light_bg}}]$RH_RIGHT_SEPARATOR "

  # add battery status
  set -ga status-right "#{battery_status_fg}#{battery_percentage} "

  # set right segments to bold
  set -g status-right-style "bold"
  set -g status-right-length 100

  # --------- INACTIVE WINDOWS ------------

  # clear inactive window
  set -g window-status-format ""

  # clear background
  set -ga window-status-format "#[bg=colour00]"

  # begin segment
  set -ga window-status-format "#[fg={{lighter_bg}} bg={{light_bg}}]$LH_LEFT_SEPARATOR"

  # current path
  set -ga window-status-format "#[fg=colour242 bg={{lighter_bg}}]#{b:pane_current_path}"

  # end segment
  set -ga window-status-format "#[fg={{lighter_bg}} bg={{light_bg}}]$LH_RIGHT_SEPARATOR "

  # --------- CURRENT WINDOW ----------------
  # clear curent window
  set -g window-status-current-format ""

  # clear background
  set -ga window-status-current-format "#[bg=colour00]"

  # begin segment
  set -ga window-status-current-format "#[fg={{lighter_bg}} bg={{light_bg}}]$LH_LEFT_SEPARATOR"

  # zoomed status
  set -ga window-status-current-format "#[fg={{xcolors_04}} bg={{lighter_bg}}]#{?window_zoomed_flag,[ﯫ] ,}"

  # explicit name, current path, or zsh
  set -ga window-status-current-format "#{?#{==:#{window_name},zsh},#{b:pane_current_path},#W}"

  # end segment
  set -ga window-status-current-format "#[fg={{lighter_bg}} bg={{light_bg}}]$LH_RIGHT_SEPARATOR "

  # ----------------- MISC --------------------
  set -g window-status-separator ""

  set -g pane-active-border-style "fg={{dark_bg}} bg={{dark_bg}}"
  set -g pane-border-style "fg={{dark_bg}} bg={{dark_bg}}"

  set -g window-active-style "bg={{dark_bg}}"
  set -g window-status-activity-style "fg={{xcolors_03}}"
    """

    bar_template = """
  FAR_LEFT_SEPARATOR="{{separators[0]}}"
  LH_LEFT_SEPARATOR="{{separators[1]}}"
  LH_RIGHT_SEPARATOR="{{separators[2]}}"
  RH_LEFT_SEPARATOR="{{separators[3]}}"
  RH_RIGHT_SEPARATOR="{{separators[4]}}"
  FAR_RIGHT_SEPARATOR="{{separators[5]}}"
    """

    @staticmethod
    async def reload() -> None:
        command = "tmux source-file ~/.tmux.conf"
        await util.call_with_shell(command)

    @staticmethod
    async def set_theme(theme: str) -> None:
        pass

    @staticmethod
    async def set_font(font: str) -> None:
        pass
