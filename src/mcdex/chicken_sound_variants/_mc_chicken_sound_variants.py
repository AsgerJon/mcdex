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


class MCChickenSoundVariants(MCThing, strictCase=False):
  """
  The catalogue of the game's chicken sound variants, each a member. A member
  is named by its unique name in PascalCase, and found by that name in any case
  or by the unique name itself:

    picky = MCChickenSoundVariants.Picky
    picky is MCChickenSoundVariants['picky']  # True
    picky[Version.V26_1]
    # ChickenSoundVariantId('picky',
    #   'minecraft:chicken{sound_variant:"minecraft:picky"}')
    len(MCChickenSoundVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'chicken_sound_variants.json' beside this
  module. mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'chicken_sound_variants.json'
  __data_key__ = 'chicken_sound_variants'
  __id_class__ = ChickenSoundVariantId
  __kind__ = 'chicken sound variant'

  #  Members, one for every thing of 'chicken_sound_variants.json'
  Classic = Kee[str]('classic')
  Picky = Kee[str]('picky')
