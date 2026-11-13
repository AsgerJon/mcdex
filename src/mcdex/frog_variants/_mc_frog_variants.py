"""
MCFrogVariants is the catalogue of the game's frog variants: an enumeration
with one member for every frog variant of the data file that ships with mcdex,
each the same frog variant in every version, with the id each version knows it
by: what /summon takes for a frog of that variant.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import FrogVariantId, MCThing


class MCFrogVariants(MCThing):
  """
  The catalogue of the game's frog variants, each a member, found by its name
  in capitals, in any case, or by its unique name:

    warm = MCFrogVariants.WARM
    warm is MCFrogVariants['warm']  # True
    warm['1.19']
    # FrogVariantId('warm', 'minecraft:frog{variant:"minecraft:warm"}')
    len(MCFrogVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'frog_variants.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'frog_variants.json'
  __data_key__ = 'frog_variants'
  __id_class__ = FrogVariantId
  __kind__ = 'frog variant'

  #  Members, one for every name of 'frog_variants.json'
  COLD = Kee[str]('cold')
  TEMPERATE = Kee[str]('temperate')
  WARM = Kee[str]('warm')
