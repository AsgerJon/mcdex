"""
CowSoundVariantId pairs a cow sound variant's unique name with the id a version
of the game needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class CowSoundVariantId(GameId):
  """
  The id of a cow sound variant in one version: its 'uniqueName', the same in
  every version, and its 'minecraftId', what /summon takes for a cow of that
  sound variant in that version.

  Implementation
  --------------

  All of it is 'GameId's: a 'CowSoundVariantId' is equal only to a
  'CowSoundVariantId'.
  """
