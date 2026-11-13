"""
BiomeId pairs a biome's unique name with the id a version of the game
needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class BiomeId(GameId):
  """
  The id of a biome in one version: its 'uniqueName', the same in every
  version, and its 'minecraftId', the biome's number to 1.8.9, its name from
  1.9 in that version.

  Implementation
  --------------

  All of it is 'GameId's: a 'BiomeId' is equal only to a 'BiomeId'.
  """
