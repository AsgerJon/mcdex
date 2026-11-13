"""
The 'mcdex.villager_types' package provides the villager types of the game: the
'MCVillagerTypes' catalogue, an enumeration of every villager type of the data
file 'villager_types.json' that ships with the package.

- MCVillagerTypes
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_villager_types import MCVillagerTypes

__all__ = (
  'MCVillagerTypes',
)
