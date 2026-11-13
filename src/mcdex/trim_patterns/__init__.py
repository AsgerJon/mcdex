"""
The 'mcdex.trim_patterns' package provides the trim patterns of the game: the
'MCTrimPatterns' catalogue, an enumeration of every trim pattern of the data
file 'trim_patterns.json' that ships with the package.

- MCTrimPatterns
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_trim_patterns import MCTrimPatterns

__all__ = (
  'MCTrimPatterns',
)
