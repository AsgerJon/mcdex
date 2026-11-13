"""
The 'mcdex.sounds' package provides the sounds of the game: the
'MCSounds' catalogue, an enumeration of every sound of the data file
'sounds.json' that ships with the package.

- MCSounds
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_sounds import MCSounds

__all__ = (
  'MCSounds',
)
