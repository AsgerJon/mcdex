"""
DimensionId pairs a dimension's unique name with the id a version of the game
needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class DimensionId(GameId):
  """
  The id of a dimension in one version: its 'uniqueName', the same in
  every version, and its 'minecraftId', what /execute in takes in that version.

  Implementation
  --------------

  All of it is 'GameId's: a 'DimensionId' is equal only to a 'DimensionId'.
  """
