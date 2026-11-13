"""
The 'mcdex.damage_types' package provides the damage types of the game: the
'MCDamageTypes' catalogue, an enumeration of every damage type of the data file
'damage_types.json' that ships with the package.

- MCDamageTypes
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_damage_types import MCDamageTypes

__all__ = (
  'MCDamageTypes',
)
