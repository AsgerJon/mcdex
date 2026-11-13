"""
AttributeId pairs an attribute's unique name with the id a version of the game
needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class AttributeId(GameId):
  """
  The id of an attribute in one version: its 'uniqueName', the same in every
  version, and its 'minecraftId', the name an entity's data gives it, and from
  1.16 what '/attribute' takes in that version.

  Implementation
  --------------

  All of it is 'GameId's: an 'AttributeId' is equal only to an 'AttributeId'.
  """
