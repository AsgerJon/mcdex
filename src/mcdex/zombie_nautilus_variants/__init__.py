"""
The 'mcdex.zombie_nautilus_variants' package provides the zombie nautilus
variants of the game: the 'MCZombieNautilusVariants' catalogue, an enumeration
of every zombie nautilus variant of the data file
'zombie_nautilus_variants.json' that ships with the package.

- MCZombieNautilusVariants
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_zombie_nautilus_variants import MCZombieNautilusVariants

__all__ = (
  'MCZombieNautilusVariants',
)
