"""
The 'mcdex.statistics' package provides the statistics of the game: the
'MCStatistics' catalogue, an enumeration of every statistic of the data file
'statistics.json' that ships with the package.

- MCStatistics
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_statistics import MCStatistics

__all__ = (
  'MCStatistics',
)
