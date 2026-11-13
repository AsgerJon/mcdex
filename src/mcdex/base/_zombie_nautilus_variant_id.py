"""
ZombieNautilusVariantId pairs a zombie nautilus variant's unique name with the
id a version of the game needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class ZombieNautilusVariantId(GameId):
  """
  The id of a zombie nautilus variant in one version: its 'uniqueName', the
  same in every version, and its 'minecraftId', what /summon takes for a zombie
  nautilus of that variant in that version.

  Implementation
  --------------

  All of it is 'GameId's: a 'ZombieNautilusVariantId' is equal only to a
  'ZombieNautilusVariantId'.
  """
