"""
The 'mcdex.enchantments' package provides the enchantments of the game: the
'MCEnchantments' catalogue, an enumeration of every enchantment of the data
file 'enchantments.json' that ships with the package.

- MCEnchantments
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_enchantments import MCEnchantments

__all__ = (
  'MCEnchantments',
)
