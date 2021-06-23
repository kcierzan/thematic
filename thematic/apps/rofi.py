from thematic.apps import base
from thematic.themes import base as base_theme


class Rofi(base.App):
    @staticmethod
    async def set_theme(_: base_theme.Theme) -> None:
        ...

    @staticmethod
    async def set_font(_: str) -> None:
        ...

    @staticmethod
    async def reload() -> None:
        ...

    supported_oses = {"linux"}
    config_file = ".config/rofi/config"
    theme_file = "thematic-rofi.rasi"
    template = """
  {
  	background: {{background}};
  	white07-transparent: {{foreground}}20;
  	base03: {{bg_brightest}};
  	white07: {{foreground}};
  	base08: {{xcolors_09}};
  	base09: {{xcolors_01}};
  	base0A: {{xcolors_03}};
  	base0B: {{xcolors_02}};
  	base0C: {{xcolors_06}};
  	blue04: {{xcolors_04}};
  	base0E: {{xcolors_05}};
  	base0F: {{xcolors_01}};

  	spacing: 0;
  	background-color: transparent;

  	font: "JetBrains Mono 22";
  }

  window {
  	transparency: "real";
  	fullscreen: true;
  	background-color: #282C34C0; /*background + C0 (75% opacity)*/
  }

  mainbox {
  	children: [inputbar, message, mode-switcher, listview];
  	spacing: 30px;
  	margin: 25%;
  	padding: 30px 0;
  	border-color: @blue04;
  }

  mode-switcher {
  	enabled: false;
  }

  inputbar {
  	children: [prompt, textbox-prompt-colon, entry, case-indicator];
  }

  prompt {
  	enabled: false;
  }

  textbox-prompt-colon {
  	expand: false;
  	str: "❯";
  	margin: -3px 1ch 0 0;
  	text-color: @blue04;
  	font: "SF Mono 38";
  }

  entry {
  	text-color: @white07;
  	font: "SF Mono 38";
  }

  case-indicator {
  	text-color: @base0F;
  }


  button, textbox {
  	background-color: @base03;
  	text-color: @white07;
  	padding: 5px;
  }

  button selected {
  	background-color: transparent;
  }

  listview {
  	scrollbar: false;
  	margin: 0 0 0 30px;
  }

  element {
  	padding: 5px;
  	highlight: bold underline;
  }

  element normal {
  	background-color: transparent;
  }

  element selected {
  	text-color: @blue04;
  	background-color: @white07-transparent;
  }


  element normal selected {
  	text-color: @blue04;
  }

  element normal normal, element alternate normal {
  	text-color: @white07;
  }

  element normal urgent, element selected urgent, element alternate urgent {
  	text-color: @base0F;
  }

  element normal active, element selected active, element alternate active {
  	text-color: @base0B;
  }
    """
