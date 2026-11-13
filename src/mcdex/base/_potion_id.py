"""
PotionId pairs a potion's unique name with the id a version of the game
needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class PotionId(GameId):
  """
  The id of a potion in one version: its 'uniqueName', the same in every
  version, and its 'minecraftId', the potion an item is made with: from 1.9 its
  name, before it the potion item's damage value in that version.

  A command takes it only inside a potion item's data, whose shape changed over
  the versions: see the README's 'Ids that go inside an item'.

  Implementation
  --------------

  All of it is 'GameId's: a 'PotionId' is equal only to a 'PotionId'.
  """
