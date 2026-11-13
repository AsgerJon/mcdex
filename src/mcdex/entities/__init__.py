"""
The 'mcdex.entities' package provides the entities of the game: the
'MCEntities' catalogue, an enumeration of every entity of the data file
'entities.json' that ships with the package.

- MCEntities
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_entities import MCEntities

__all__ = (
  'MCEntities',
)
