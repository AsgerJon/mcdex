"""
VillagerProfessionId pairs a villager profession's unique name with the id a
version of the game needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class VillagerProfessionId(GameId):
  """
  The id of a villager profession in one version: its 'uniqueName', the same in
  every version, and its 'minecraftId', what /summon takes for a villager of
  that profession in that version: the villager with its data, from 1.14 its
  'VillagerData', before it its profession and career numbers.

  Implementation
  --------------

  All of it is 'GameId's: a 'VillagerProfessionId' is equal only to a
  'VillagerProfessionId'.
  """
