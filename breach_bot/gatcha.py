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


@dataclass
class Agent:
    name: str
    role: str


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

AGENTS = [
    Agent(name="Brimstone", role="Controller"),
    Agent(name="Viper", role="Controller"),
    Agent(name="Omen", role="Controller"),
    Agent(name="Killjoy", role="Sentinel"),
    Agent(name="Cypher", role="Sentinel"),
    Agent(name="Sova", role="Initiator"),
    Agent(name="Sage", role="Sentinel"),
    Agent(name="Phoenix", role="Duelist"),
    Agent(name="Jett", role="Duelist"),
    Agent(name="Reyna", role="Duelist"),
    Agent(name="Raze", role="Duelist"),
    Agent(name="Breach", role="Initiator"),
    Agent(name="Skye", role="Initiator"),
    Agent(name="Yoru", role="Duelist"),
    Agent(name="Astra", role="Controller"),
    Agent(name="KAYO", role="Initiator"),
    Agent(name="Chamber", role="Sentinel"),
    Agent(name="Neon", role="Duelist"),
    Agent(name="Fade", role="Initiator"),
    Agent(name="Harbor", role="Controller"),
    Agent(name="Gekko", role="Initiator"),
]


def generate_map_text(map: Map):
    return f'Selected map is **"{map.name}"**'


def generate_agent_text(map: Map):
    return f'Selected agent is **"{map.name}"**'


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


async def gatcha_agent(message: discord.Message):

    logger.info(f"agent gatcha called by {message.author}")

    await message.add_reaction("😎")

    args = message.content.split(" ")[1:]

    if "--initiator" in args:
        candidates = [a for a in AGENTS if a.role == "Initiator"]
    elif "--duelist" in args:
        candidates = [a for a in AGENTS if a.role == "Duelist"]
    elif "--controller" in args:
        candidates = [a for a in AGENTS if a.role == "Controller"]
    elif "--sentinel" in args:
        candidates = [a for a in AGENTS if a.role == "Sentinel"]
    else:
        candidates = AGENTS

    choosen = random.choice(candidates)
    await message.channel.send(generate_agent_text(choosen))
