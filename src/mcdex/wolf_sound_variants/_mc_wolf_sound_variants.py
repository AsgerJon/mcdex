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


class MCWolfSoundVariants(MCThing, strictCase=False):
  """
  The catalogue of the game's wolf sound variants, each a member. A member is
  named by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    puglin = MCWolfSoundVariants.Puglin
    puglin is MCWolfSoundVariants['puglin']  # True
    puglin[Version.V1_21_5]
    # WolfSoundVariantId('puglin',
    #   'minecraft:wolf{sound_variant:"minecraft:puglin"}')
    len(MCWolfSoundVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'wolf_sound_variants.json' beside this
  module. mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'wolf_sound_variants.json'
  __data_key__ = 'wolf_sound_variants'
  __id_class__ = WolfSoundVariantId
  __kind__ = 'wolf sound variant'

  #  Members, one for every thing of 'wolf_sound_variants.json'
  Angry = Kee[str]('angry')
  Big = Kee[str]('big')
  Classic = Kee[str]('classic')
  Cute = Kee[str]('cute')
  Grumpy = Kee[str]('grumpy')
  Puglin = Kee[str]('puglin')
  Sad = Kee[str]('sad')
