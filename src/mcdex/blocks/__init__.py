"""
The 'mcdex.blocks' package provides the blocks of the game: the
'MCBlocks' catalogue, an enumeration of every block of the data file
'blocks.json' that ships with the package.

- MCBlocks
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_blocks import MCBlocks

__all__ = (
  'MCBlocks',
)
