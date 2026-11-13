"""
BlockId pairs a block's unique name with the id a version of the game
needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class BlockId(GameId):
  """
  A user of mcdex names a block once, by its unique name, as
  'pink_wool', and each version of the game needs its own id for it:
  what '/setblock' takes. 'BlockId' holds the two: 'uniqueName', the same
  in every version, and 'minecraftId', all that one version needs to
  identify the block, as one string in the notation of its era:

    BlockId('pink_wool', 'minecraft:wool:6')       # 1.7.2 to 1.12.2
    BlockId('pink_wool', 'minecraft:pink_wool')    # since 1.13

  Before 1.13 a block was a name and a meta, the meta part of the id
  only where it told blocks apart: 'minecraft:oak_stairs' is any oak
  stairs, but 'minecraft:wool:6' is the pink wool. Where an old version
  told blocks apart by their block entity, the id carries that data
  after the name: the creeper head of 1.12.2 is a skull of type 4,
  'minecraft:skull:1{SkullType:4b}'. The water cauldron of 1.13 to
  1.16.5 was a cauldron with water in it, 'minecraft:cauldron[level=1]'.

  Implementation
  --------------

  All of it is 'GameId's: a 'BlockId' is equal only to a 'BlockId'.
  """
