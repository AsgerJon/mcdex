"""
The 'mcdex.block_entities' package provides the block entities of the game: the
'MCBlockEntities' catalogue, an enumeration of every block entity of the data
file 'block_entities.json' that ships with the package.

- MCBlockEntities
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_block_entities import MCBlockEntities

__all__ = (
  'MCBlockEntities',
)
