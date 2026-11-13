"""
The 'mcdex.painting_variants' package provides the painting variants of the
game: the 'MCPaintingVariants' catalogue, an enumeration of every painting
variant of the data file 'painting_variants.json' that ships with the package.

- MCPaintingVariants
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_painting_variants import MCPaintingVariants

__all__ = (
  'MCPaintingVariants',
)
