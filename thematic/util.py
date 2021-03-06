import asyncio

import aiofiles
import typer
import yaml

try:
    from yaml import CLoader as Loader
except:
    from yaml import Loader




async def load_yaml(theme_file):
    async with aiofiles.open(theme_file, "r") as f:
        try:
            contents = await f.read()
            return yaml.load(contents, Loader=Loader)
        except yaml.YAMLError:
            typer.echo("Theme failed to load")
            raise


def hex_to_rgb(hex):
    hex = hex.lstrip("#")
    hlen = len(hex)
    return tuple(int(hex[i : i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))


async def call_with_shell(command) -> None:
    proc = await asyncio.create_subprocess_shell(
        command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    await proc.communicate()
