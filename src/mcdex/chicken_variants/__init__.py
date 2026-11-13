"""
The 'mcdex.chicken_variants' package provides the chicken variants of the game:
the 'MCChickenVariants' catalogue, an enumeration of every chicken variant of
the data file 'chicken_variants.json' that ships with the package.

- MCChickenVariants
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_chicken_variants import MCChickenVariants

__all__ = (
  'MCChickenVariants',
)
