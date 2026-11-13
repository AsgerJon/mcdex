"""
The 'mcdex.game_rules' package provides the game rules of the game: the
'MCGameRules' catalogue, an enumeration of every game rule of the data file
'game_rules.json' that ships with the package.

- MCGameRules
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_game_rules import MCGameRules

__all__ = (
  'MCGameRules',
)
