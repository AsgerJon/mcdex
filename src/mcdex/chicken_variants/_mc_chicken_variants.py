"""
MCChickenVariants is the catalogue of the game's chicken variants: an
enumeration with one member for every chicken variant of the data file that
ships with mcdex, each the same chicken variant in every version, with the id
each version knows it by: what /summon takes for a chicken of that variant.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import ChickenVariantId, MCThing


class MCChickenVariants(MCThing):
  """
  The catalogue of the game's chicken variants, each a member, found by its
  name in capitals, in any case, or by its unique name:

    cold = MCChickenVariants.COLD
    cold is MCChickenVariants['cold']  # True
    cold[Version.V1_21_5]
    # ChickenVariantId('cold', 'minecraft:chicken{variant:"minecraft:cold"}')
    len(MCChickenVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'chicken_variants.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'chicken_variants.json'
  __data_key__ = 'chicken_variants'
  __id_class__ = ChickenVariantId
  __kind__ = 'chicken variant'

  #  Members, one for every name of 'chicken_variants.json'
  COLD = Kee[str]('cold')
  TEMPERATE = Kee[str]('temperate')
  WARM = Kee[str]('warm')
