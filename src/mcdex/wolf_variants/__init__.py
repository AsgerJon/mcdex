"""
The 'mcdex.wolf_variants' package provides the wolf variants of the game: the
'MCWolfVariants' catalogue, an enumeration of every wolf variant of the data
file 'wolf_variants.json' that ships with the package.

- MCWolfVariants
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_wolf_variants import MCWolfVariants

__all__ = (
  'MCWolfVariants',
)
