# Thematic 🧞

Set your entire environment to a consistent theme.

## What is it?

Thematic is an opinionated Python CLI application that instantly
themes multiple commonly-used apps.

Thematic is invoked with `theme <theme_name>`.

This command generates multiple theme-specific mini config files
at `~/.thematic` which can be sourced in any or all of the
applications Thematic supports.

## Supported applications

* iTerm2
* neovim (with separate statusline theme)
* tmux (with separate statusline theme)
* rofi
* xresources

## Themes

### Dracula
### Monokai
### Solarized (light & dark variants)
### Spacemacs
### OneDark

## How do I use it?
```sh
pip install thematic
```
```sh
theme sonokai
```

## Gotchas

Getting all of your applications playing nicely with Thematic
requires some initial envionrment setup.

1. For Alfred 4 theme changing to work properly, you must have an
  existing Alfred 4 theme configured that has the same name as a
  Thematic theme

2. For iTerm2 theme changing to work properly, you must have an
  existing iTerm2 profile with the same name as a Thematic theme

3. Neovim themeing requires the following colorschemes be installed:
  1. [solarized8](https://github.com/lifepillar/vim-solarized8)
  2. [space-vim-theme](https://github.com/liuchengxu/space-vim-theme)
  3. [vim-monokai-tasty](https://github.com/patstockwell/vim-monokai-tasty)
  4. [dracula](https://github.com/dracula/vim)

## Adding a Theme

_Coming soon..._

## Adding and Application

_Coming soon..._


