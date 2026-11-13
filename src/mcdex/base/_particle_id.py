"""
ParticleId pairs a particle's unique name with the id a version of the game
needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class ParticleId(GameId):
  """
  The id of a particle in one version: its 'uniqueName', the same in
  every version, and its 'minecraftId', what '/particle' takes in that version.

  Implementation
  --------------

  All of it is 'GameId's: a 'ParticleId' is equal only to a 'ParticleId'.
  """
