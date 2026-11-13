"""
MCCatSoundVariants is the catalogue of the game's cat sound variants: an
enumeration with one member for every cat sound variant of the data file that
ships with mcdex, each the same cat sound variant in every version, with the id
each version knows it by: what /summon takes for a cat of that sound variant.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import CatSoundVariantId, MCThing


class MCCatSoundVariants(MCThing):
  """
  The catalogue of the game's cat sound variants, each a member, found by its
  name in capitals, in any case, or by its unique name:

    royal = MCCatSoundVariants.ROYAL
    royal is MCCatSoundVariants['royal']  # True
    royal['26.1']
    # CatSoundVariantId('royal',
    #   'minecraft:cat{sound_variant:"minecraft:royal"}')
    len(MCCatSoundVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'cat_sound_variants.json' beside this
  module. mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'cat_sound_variants.json'
  __data_key__ = 'cat_sound_variants'
  __id_class__ = CatSoundVariantId
  __kind__ = 'cat sound variant'

  #  Members, one for every name of 'cat_sound_variants.json'
  CLASSIC = Kee[str]('classic')
  ROYAL = Kee[str]('royal')
