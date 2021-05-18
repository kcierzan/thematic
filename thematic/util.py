import os
import json

try:
    from yaml import CLoader as Loader
except:
    from yaml import Loader

import yaml
import typer

from thematic.constants import (
    THEME_DIR,
    DATA_DIR
)

def load_yaml(theme_file):
    with open(theme_file, "r") as f:
        try:
            return yaml.load(f, Loader=Loader)
        except yaml.YAMLError:
            typer.echo("Theme failed to load")
            raise


def get_theme_data(theme):
    theme_file = os.path.join(THEME_DIR, theme + ".yaml")
    return load_yaml(theme_file)


def load_separators():
    with open(f"{DATA_DIR}/separators.json") as f:
        return json.load(f)


def load_fonts():
    with open(f"{DATA_DIR}/fonts.json") as f:
        return json.load(f)


def hex_to_rgb(hex):
    hex = hex.lstrip("#")
    hlen = len(hex)
    return tuple(int(hex[i : i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))


