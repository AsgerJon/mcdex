"""
BannerPatternId pairs a banner pattern's unique name with the id a version of
the game needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class BannerPatternId(GameId):
  """
  The id of a banner pattern in one version: its 'uniqueName', the same in
  every version, and its 'minecraftId', what a banner's pattern takes in that
  version.

  A command takes it only inside a banner's data, whose shape changed over
  the versions: see the README's 'Ids that go inside an item'.

  Implementation
  --------------

  All of it is 'GameId's: a 'BannerPatternId' is equal only to a
  'BannerPatternId'.
  """
