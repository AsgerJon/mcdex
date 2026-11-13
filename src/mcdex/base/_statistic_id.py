"""
StatisticId pairs a statistic's unique name with the id a version of the game
needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class StatisticId(GameId):
  """
  The id of a statistic in one version: its 'uniqueName', the same in every
  version, and its 'minecraftId', the name the game keeps the count under,
  which '/scoreboard' objectives count in that version.

  Implementation
  --------------

  All of it is 'GameId's: a 'StatisticId' is equal only to a 'StatisticId'.
  """
