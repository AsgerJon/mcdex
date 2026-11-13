"""
The 'mcdex.advancements' package provides the advancements of the game: the
'MCAdvancements' catalogue, an enumeration of every advancement of the data
file 'advancements.json' that ships with the package.

- MCAdvancements
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_advancements import MCAdvancements

__all__ = (
  'MCAdvancements',
)
