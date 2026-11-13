"""
MCChickenSoundVariants is the catalogue of the game's chicken sound variants:
an enumeration with one member for every chicken sound variant of the data file
that ships with mcdex, each the same chicken sound variant in every version,
with the id each version knows it by: what /summon takes for a chicken of that
sound variant.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import ChickenSoundVariantId, MCThing


class MCChickenSoundVariants(MCThing):
  """
  The catalogue of the game's chicken sound variants, each a member, found by
  its name in capitals, in any case, or by its unique name:

    picky = MCChickenSoundVariants.PICKY
    picky is MCChickenSoundVariants['picky']  # True
    picky['26.1']
    # ChickenSoundVariantId('picky',
    #   'minecraft:chicken{sound_variant:"minecraft:picky"}')
    len(MCChickenSoundVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'chicken_sound_variants.json' beside this
  module. mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'chicken_sound_variants.json'
  __data_key__ = 'chicken_sound_variants'
  __id_class__ = ChickenSoundVariantId
  __kind__ = 'chicken sound variant'

  #  Members, one for every name of 'chicken_sound_variants.json'
  CLASSIC = Kee[str]('classic')
  PICKY = Kee[str]('picky')
