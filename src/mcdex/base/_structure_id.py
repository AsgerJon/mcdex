"""
StructureId pairs a structure's unique name with the id a version of the game
needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class StructureId(GameId):
  """
  The id of a structure in one version: its 'uniqueName', the same in
  every version, and its 'minecraftId', what /locate takes in that version.

  Implementation
  --------------

  All of it is 'GameId's: a 'StructureId' is equal only to a 'StructureId'.
  """
