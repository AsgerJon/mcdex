"""
EntityId pairs an entity's unique name with the id a version of the game
needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class EntityId(GameId):
  """
  A user of mcdex names an entity once, by its unique name, as
  'wither_skeleton', and each version of the game needs its own id for
  it: what '/summon' takes. 'EntityId' holds the two: 'uniqueName', the
  same in every version, and 'minecraftId', all that one version needs
  to identify the entity, as one string in the notation of its era:

    EntityId('creeper', 'Creeper')                    # 1.7.2 to 1.10.2
    EntityId('creeper', 'minecraft:creeper')          # since 1.11

  Where an old version told entities apart by their data, the id carries
  that data after the name, as /summon takes it: the wither skeleton of
  1.10.2 is a skeleton of type 1, 'Skeleton{SkeletonType:1}', and a
  spruce boat before 1.21.2 'minecraft:boat{Type:"spruce"}'.

  An 'EntityId' is never an 'ItemId', even where the two have the same
  text: the pig and its spawn egg are different things.

  Implementation
  --------------

  All of it is 'GameId's: an 'EntityId' is equal only to an 'EntityId'.
  """
