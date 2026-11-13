"""
The 'mcdex.effects' package provides the effects of the game: the
'MCEffects' catalogue, an enumeration of every effect of the data file
'effects.json' that ships with the package.

- MCEffects
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_effects import MCEffects

__all__ = (
  'MCEffects',
)
