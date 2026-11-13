"""
The 'mcdex.banner_patterns' package provides the banner patterns of the game:
the 'MCBannerPatterns' catalogue, an enumeration of every banner pattern of the
data file 'banner_patterns.json' that ships with the package.

- MCBannerPatterns
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_banner_patterns import MCBannerPatterns

__all__ = (
  'MCBannerPatterns',
)
