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


class MCCatVariants(MCThing):
  """
  The catalogue of the game's cat variants, each a member, found by its name in
  capitals, in any case, or by its unique name:

    black = MCCatVariants.BLACK
    black is MCCatVariants['black']  # True
    black[Version.V1_12_2]
    # CatVariantId('black', 'minecraft:ocelot{CatType:1}')
    len(MCCatVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'cat_variants.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'cat_variants.json'
  __data_key__ = 'cat_variants'
  __id_class__ = CatVariantId
  __kind__ = 'cat variant'

  #  Members, one for every name of 'cat_variants.json'
  ALL_BLACK = Kee[str]('all_black')
  BLACK = Kee[str]('black')
  BRITISH_SHORTHAIR = Kee[str]('british_shorthair')
  CALICO = Kee[str]('calico')
  JELLIE = Kee[str]('jellie')
  PERSIAN = Kee[str]('persian')
  RAGDOLL = Kee[str]('ragdoll')
  RED = Kee[str]('red')
  SIAMESE = Kee[str]('siamese')
  TABBY = Kee[str]('tabby')
  WHITE = Kee[str]('white')
