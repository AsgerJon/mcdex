"""
The 'mcdex.attributes' package provides the attributes of the game: the
'MCAttributes' catalogue, an enumeration of every attribute of the data file
'attributes.json' that ships with the package.

- MCAttributes
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_attributes import MCAttributes

__all__ = (
  'MCAttributes',
)
