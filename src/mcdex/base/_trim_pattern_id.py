"""
TrimPatternId pairs a trim pattern's unique name with the id a version of the
game needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class TrimPatternId(GameId):
  """
  The id of a trim pattern in one version: its 'uniqueName', the same in every
  version, and its 'minecraftId', what an armor trim's pattern takes in that
  version.

  A command takes it only inside an armor piece's data, whose shape changed
  over the versions: see the README's 'Ids that go inside an item'.

  Implementation
  --------------

  All of it is 'GameId's: a 'TrimPatternId' is equal only to a 'TrimPatternId'.
  """
