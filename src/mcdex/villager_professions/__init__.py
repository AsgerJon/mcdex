"""
The 'mcdex.villager_professions' package provides the villager professions of
the game: the 'MCVillagerProfessions' catalogue, an enumeration of every
villager profession of the data file 'villager_professions.json' that ships
with the package.

- MCVillagerProfessions
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_villager_professions import MCVillagerProfessions

__all__ = (
  'MCVillagerProfessions',
)
