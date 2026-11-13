"""
BlockEntityId pairs a block entity's unique name with the id a version of the
game needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class BlockEntityId(GameId):
  """
  The id of a block entity in one version: its 'uniqueName', the same in every
  version, and its 'minecraftId', the name it is saved under, the 'id' in its
  data in that version.

  Implementation
  --------------

  All of it is 'GameId's: a 'BlockEntityId' is equal only to a 'BlockEntityId'.
  """
