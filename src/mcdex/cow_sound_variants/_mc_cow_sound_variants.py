"""
MCCowSoundVariants is the catalogue of the game's cow sound variants: an
enumeration with one member for every cow sound variant of the data file that
ships with mcdex, each the same cow sound variant in every version, with the id
each version knows it by: what /summon takes for a cow of that sound variant.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import CowSoundVariantId, MCThing


class MCCowSoundVariants(MCThing):
  """
  The catalogue of the game's cow sound variants, each a member, found by its
  name in capitals, in any case, or by its unique name:

    moody = MCCowSoundVariants.MOODY
    moody is MCCowSoundVariants['moody']  # True
    moody['26.1']
    # CowSoundVariantId('moody',
    #   'minecraft:cow{sound_variant:"minecraft:moody"}')
    len(MCCowSoundVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'cow_sound_variants.json' beside this
  module. mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'cow_sound_variants.json'
  __data_key__ = 'cow_sound_variants'
  __id_class__ = CowSoundVariantId
  __kind__ = 'cow sound variant'

  #  Members, one for every name of 'cow_sound_variants.json'
  CLASSIC = Kee[str]('classic')
  MOODY = Kee[str]('moody')
