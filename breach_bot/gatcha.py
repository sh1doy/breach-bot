"""
Gatcha feature
"""

from dataclasses import dataclass
import logging
import random
import sys
import discord

logger = logging.getLogger(__name__)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.INFO)
logger.setLevel(logging.INFO)
logger.addHandler(sh)


@dataclass
class Map:
    name: str
    is_regular: bool


MAPS = [
    Map(name="Bind", is_regular=True),
    Map(name="Haven", is_regular=True),
    Map(name="Split", is_regular=True),
    Map(name="Ascent", is_regular=True),
    Map(name="Fracture", is_regular=True),
    Map(name="Pearl", is_regular=True),
    Map(name="Lotus", is_regular=True),
    Map(name="Icebox", is_regular=False),
    Map(name="Breeze", is_regular=False),
]


def generate_map_text(map: Map):
    return f'Selected map is **"{map.name}"**'


async def gatcha_map(message: discord.Message):

    logger.info(f"map gatcha called by {message.author}")

    await message.add_reaction("😎")

    args = message.content.split(" ")[1:]

    if "--regular" in args:
        candidates = [m for m in MAPS if m.is_regular]
    else:
        candidates = MAPS

    choosen = random.choice(candidates)
    await message.channel.send(generate_map_text(choosen))
