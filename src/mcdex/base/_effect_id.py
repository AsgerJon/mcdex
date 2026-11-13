"""
EffectId pairs an effect's unique name with the id a version of the game
needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class EffectId(GameId):
  """
  The id of an effect in one version: its 'uniqueName', the same in
  every version, and its 'minecraftId', what '/effect' takes in that version.

  Implementation
  --------------

  All of it is 'GameId's: an 'EffectId' is equal only to an 'EffectId'.
  """
