"""
VillagerTypeId pairs a villager type's unique name with the id a version of the
game needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class VillagerTypeId(GameId):
  """
  The id of a villager type in one version: its 'uniqueName', the same in every
  version, and its 'minecraftId', what /summon takes for a villager of that
  type, its home biome's look, in that version: the villager with its
  'VillagerData' from 1.14, the villager itself before, when every villager
  was of the plains type.

  Implementation
  --------------

  All of it is 'GameId's: a 'VillagerTypeId' is equal only to a
  'VillagerTypeId'.
  """
