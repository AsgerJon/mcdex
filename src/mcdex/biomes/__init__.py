"""
The 'mcdex.biomes' package provides the biomes of the game: the
'MCBiomes' catalogue, an enumeration of every biome of the data file
'biomes.json' that ships with the package.

- MCBiomes
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_biomes import MCBiomes

__all__ = (
  'MCBiomes',
)
