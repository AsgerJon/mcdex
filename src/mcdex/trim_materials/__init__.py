"""
The 'mcdex.trim_materials' package provides the trim materials of the game: the
'MCTrimMaterials' catalogue, an enumeration of every trim material of the data
file 'trim_materials.json' that ships with the package.

- MCTrimMaterials
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_trim_materials import MCTrimMaterials

__all__ = (
  'MCTrimMaterials',
)
