"""
The 'mcdex.dimensions' package provides the dimensions of the game: the
'MCDimensions' catalogue, an enumeration of every dimension of the data file
'dimensions.json' that ships with the package.

- MCDimensions
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_dimensions import MCDimensions

__all__ = (
  'MCDimensions',
)
