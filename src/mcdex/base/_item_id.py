"""
ItemId pairs an item's unique name with the id a version of the game
needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class ItemId(GameId):
  """
  A user of mcdex names an item once, by its unique name, as
  'pink_wool', and each version of the game needs its own id for it.
  'ItemId' holds the two: 'uniqueName', the same in every version, and
  'minecraftId', all that one version needs to identify the item, as
  one string in the notation of its era:

    ItemId('pink_wool', '35:6')                 # before 1.7.2
    ItemId('pink_wool', 'minecraft:wool:6')     # 1.7.2 to 1.12.2
    ItemId('pink_wool', 'minecraft:pink_wool')  # since 1.13

  Before 1.7.2 the game had only numbers, the id and the meta value;
  then names, with the meta where it told items apart; and since 1.13
  the name alone. A meta that is only damage, as the elytra's was, is no
  part of the id. A registry name has no ':' in its path, so a trailing
  ':6' is always the meta. An item the game told apart by NBT carries it
  after the name, as the /give command takes it: a creeper spawn egg of
  1.12.2 is 'minecraft:spawn_egg{EntityTag:{id:"minecraft:creeper"}}'.

  Implementation
  --------------

  All of it is 'GameId's: an 'ItemId' is equal only to an 'ItemId'.
  """
