"""
AdvancementId pairs an advancement's unique name with the id a version of the
game needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class AdvancementId(GameId):
  """
  The id of an advancement in one version: its 'uniqueName', the same in every
  version, and its 'minecraftId', what /advancement takes in that version.

  Implementation
  --------------

  All of it is 'GameId's: an 'AdvancementId' is equal only to an
  'AdvancementId'.
  """
