"""
The 'mcdex.particles' package provides the particles of the game: the
'MCParticles' catalogue, an enumeration of every particle of the data file
'particles.json' that ships with the package.

- MCParticles
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_particles import MCParticles

__all__ = (
  'MCParticles',
)
