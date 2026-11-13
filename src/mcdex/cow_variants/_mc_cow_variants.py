"""
MCCowVariants is the catalogue of the game's cow variants: an enumeration with
one member for every cow variant of the data file that ships with mcdex, each
the same cow variant in every version, with the id each version knows it by:
what /summon takes for a cow of that variant.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import CowVariantId, MCThing


class MCCowVariants(MCThing):
  """
  The catalogue of the game's cow variants, each a member, found by its name in
  capitals, in any case, or by its unique name:

    warm = MCCowVariants.WARM
    warm is MCCowVariants['warm']  # True
    warm[Version.V1_21_5]
    # CowVariantId('warm', 'minecraft:cow{variant:"minecraft:warm"}')
    len(MCCowVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'cow_variants.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'cow_variants.json'
  __data_key__ = 'cow_variants'
  __id_class__ = CowVariantId
  __kind__ = 'cow variant'

  #  Members, one for every name of 'cow_variants.json'
  COLD = Kee[str]('cold')
  TEMPERATE = Kee[str]('temperate')
  WARM = Kee[str]('warm')
