"""
MCPigVariants is the catalogue of the game's pig variants: an enumeration with
one member for every pig variant of the data file that ships with mcdex, each
the same pig variant in every version, with the id each version knows it by:
what /summon takes for a pig of that variant.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import MCThing, PigVariantId


class MCPigVariants(MCThing):
  """
  The catalogue of the game's pig variants, each a member, found by its name in
  capitals, in any case, or by its unique name:

    temperate = MCPigVariants.TEMPERATE
    temperate is MCPigVariants['temperate']  # True
    temperate['1.12.2']  # PigVariantId('temperate', 'minecraft:pig')
    len(MCPigVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'pig_variants.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'pig_variants.json'
  __data_key__ = 'pig_variants'
  __id_class__ = PigVariantId
  __kind__ = 'pig variant'

  #  Members, one for every name of 'pig_variants.json'
  COLD = Kee[str]('cold')
  TEMPERATE = Kee[str]('temperate')
  WARM = Kee[str]('warm')
