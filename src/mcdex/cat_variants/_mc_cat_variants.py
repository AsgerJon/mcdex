"""
MCCatVariants is the catalogue of the game's cat variants: an enumeration with
one member for every cat variant of the data file that ships with mcdex, each
the same cat variant in every version, with the id each version knows it by:
what /summon takes for a cat of that variant.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import CatVariantId, MCThing


class MCCatVariants(MCThing, strictCase=False):
  """
  The catalogue of the game's cat variants, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    black = MCCatVariants.Black
    black is MCCatVariants['black']  # True
    black[Version.V1_12_2]
    # CatVariantId('black', 'minecraft:ocelot{CatType:1}')
    len(MCCatVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'cat_variants.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'cat_variants.json'
  __data_key__ = 'cat_variants'
  __id_class__ = CatVariantId
  __kind__ = 'cat variant'

  #  Members, one for every thing of 'cat_variants.json'
  AllBlack = Kee[str]('all_black')
  Black = Kee[str]('black')
  BritishShorthair = Kee[str]('british_shorthair')
  Calico = Kee[str]('calico')
  Jellie = Kee[str]('jellie')
  Persian = Kee[str]('persian')
  Ragdoll = Kee[str]('ragdoll')
  Red = Kee[str]('red')
  Siamese = Kee[str]('siamese')
  Tabby = Kee[str]('tabby')
  White = Kee[str]('white')
