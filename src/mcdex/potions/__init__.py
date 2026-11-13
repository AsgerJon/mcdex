"""
The 'mcdex.potions' package provides the potions of the game: the 'MCPotions'
catalogue, an enumeration of every potion of the data file 'potions.json' that
ships with the package; and the 'ModifiedPotion', a long or a strong potion,
which the catalogue gives for a base potion with a modifier.

- MCPotions
- ModifiedPotion
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._modified_potion import ModifiedPotion
from ._mc_potions import MCPotions

__all__ = (
  'MCPotions',
  'ModifiedPotion',
)
