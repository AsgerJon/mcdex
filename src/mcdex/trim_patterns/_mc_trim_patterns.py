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


class MCTrimPatterns(MCThing):
  """
  The catalogue of the game's trim patterns, each a member, found by its name
  in capitals, in any case, or by its unique name:

    coast = MCTrimPatterns.COAST
    coast is MCTrimPatterns['coast']  # True
    coast['1.20']  # TrimPatternId('coast', 'minecraft:coast')
    len(MCTrimPatterns)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'trim_patterns.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'trim_patterns.json'
  __data_key__ = 'trim_patterns'
  __id_class__ = TrimPatternId
  __kind__ = 'trim pattern'

  #  Members, one for every name of 'trim_patterns.json'
  BOLT = Kee[str]('bolt')
  COAST = Kee[str]('coast')
  DUNE = Kee[str]('dune')
  EYE = Kee[str]('eye')
  FLOW = Kee[str]('flow')
  HOST = Kee[str]('host')
  RAISER = Kee[str]('raiser')
  RIB = Kee[str]('rib')
  SENTRY = Kee[str]('sentry')
  SHAPER = Kee[str]('shaper')
  SILENCE = Kee[str]('silence')
  SNOUT = Kee[str]('snout')
  SPIRE = Kee[str]('spire')
  TIDE = Kee[str]('tide')
  VEX = Kee[str]('vex')
  WARD = Kee[str]('ward')
  WAYFINDER = Kee[str]('wayfinder')
  WILD = Kee[str]('wild')
