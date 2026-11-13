"""
The 'mcdex.items' package provides the items of the game: the
'MCItems' catalogue, an enumeration of every item of the data file
'items.json' that ships with the package.

- MCItems
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_items import MCItems

__all__ = (
  'MCItems',
)
