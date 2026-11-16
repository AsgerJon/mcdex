"""
MCTrimPatterns is the catalogue of the game's trim patterns: an enumeration
with one member for every trim pattern of the data file that ships with mcdex,
each the same trim pattern in every version, with the id each version knows it
by: what an armor trim's pattern takes.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import MCThing, TrimPatternId


class MCTrimPatterns(MCThing, strictCase=False):
  """
  The catalogue of the game's trim patterns, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    coast = MCTrimPatterns.Coast
    coast is MCTrimPatterns['coast']  # True
    coast[Version.V1_20]  # TrimPatternId('coast', 'minecraft:coast')
    len(MCTrimPatterns)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'trim_patterns.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'trim_patterns.json'
  __data_key__ = 'trim_patterns'
  __id_class__ = TrimPatternId
  __kind__ = 'trim pattern'

  #  Members, one for every thing of 'trim_patterns.json'
  Bolt = Kee[str]('bolt')
  Coast = Kee[str]('coast')
  Dune = Kee[str]('dune')
  Eye = Kee[str]('eye')
  Flow = Kee[str]('flow')
  Host = Kee[str]('host')
  Raiser = Kee[str]('raiser')
  Rib = Kee[str]('rib')
  Sentry = Kee[str]('sentry')
  Shaper = Kee[str]('shaper')
  Silence = Kee[str]('silence')
  Snout = Kee[str]('snout')
  Spire = Kee[str]('spire')
  Tide = Kee[str]('tide')
  Vex = Kee[str]('vex')
  Ward = Kee[str]('ward')
  Wayfinder = Kee[str]('wayfinder')
  Wild = Kee[str]('wild')
