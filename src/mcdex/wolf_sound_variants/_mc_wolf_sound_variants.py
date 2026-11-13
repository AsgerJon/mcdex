"""
MCWolfSoundVariants is the catalogue of the game's wolf sound variants: an
enumeration with one member for every wolf sound variant of the data file that
ships with mcdex, each the same wolf sound variant in every version, with the
id each version knows it by: what /summon takes for a wolf of that sound
variant.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import MCThing, WolfSoundVariantId


class MCWolfSoundVariants(MCThing):
  """
  The catalogue of the game's wolf sound variants, each a member, found by its
  name in capitals, in any case, or by its unique name:

    puglin = MCWolfSoundVariants.PUGLIN
    puglin is MCWolfSoundVariants['puglin']  # True
    puglin['1.21.5']
    # WolfSoundVariantId('puglin',
    #   'minecraft:wolf{sound_variant:"minecraft:puglin"}')
    len(MCWolfSoundVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'wolf_sound_variants.json' beside this
  module. mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'wolf_sound_variants.json'
  __data_key__ = 'wolf_sound_variants'
  __id_class__ = WolfSoundVariantId
  __kind__ = 'wolf sound variant'

  #  Members, one for every name of 'wolf_sound_variants.json'
  ANGRY = Kee[str]('angry')
  BIG = Kee[str]('big')
  CLASSIC = Kee[str]('classic')
  CUTE = Kee[str]('cute')
  GRUMPY = Kee[str]('grumpy')
  PUGLIN = Kee[str]('puglin')
  SAD = Kee[str]('sad')
