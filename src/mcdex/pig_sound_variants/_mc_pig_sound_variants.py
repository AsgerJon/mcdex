"""
MCPigSoundVariants is the catalogue of the game's pig sound variants: an
enumeration with one member for every pig sound variant of the data file that
ships with mcdex, each the same pig sound variant in every version, with the id
each version knows it by: what /summon takes for a pig of that sound variant.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import MCThing, PigSoundVariantId


class MCPigSoundVariants(MCThing, strictCase=False):
  """
  The catalogue of the game's pig sound variants, each a member. A member is
  named by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    mini = MCPigSoundVariants.Mini
    mini is MCPigSoundVariants['mini']  # True
    mini[Version.V26_1]
    # PigSoundVariantId('mini',
    #   'minecraft:pig{sound_variant:"minecraft:mini"}')
    len(MCPigSoundVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'pig_sound_variants.json' beside this
  module. mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'pig_sound_variants.json'
  __data_key__ = 'pig_sound_variants'
  __id_class__ = PigSoundVariantId
  __kind__ = 'pig sound variant'

  #  Members, one for every thing of 'pig_sound_variants.json'
  Big = Kee[str]('big')
  Classic = Kee[str]('classic')
  Mini = Kee[str]('mini')
