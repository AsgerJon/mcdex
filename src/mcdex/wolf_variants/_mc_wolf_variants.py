"""
MCWolfVariants is the catalogue of the game's wolf variants: an enumeration
with one member for every wolf variant of the data file that ships with mcdex,
each the same wolf variant in every version, with the id each version knows it
by: what /summon takes for a wolf of that variant.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import MCThing, WolfVariantId


class MCWolfVariants(MCThing):
  """
  The catalogue of the game's wolf variants, each a member, found by its name
  in capitals, in any case, or by its unique name:

    ashen = MCWolfVariants.ASHEN
    ashen is MCWolfVariants['ashen']  # True
    ashen[Version.V1_20_5]
    # WolfVariantId('ashen', 'minecraft:wolf{variant:"minecraft:ashen"}')
    len(MCWolfVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'wolf_variants.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'wolf_variants.json'
  __data_key__ = 'wolf_variants'
  __id_class__ = WolfVariantId
  __kind__ = 'wolf variant'

  #  Members, one for every name of 'wolf_variants.json'
  ASHEN = Kee[str]('ashen')
  BLACK = Kee[str]('black')
  CHESTNUT = Kee[str]('chestnut')
  PALE = Kee[str]('pale')
  RUSTY = Kee[str]('rusty')
  SNOWY = Kee[str]('snowy')
  SPOTTED = Kee[str]('spotted')
  STRIPED = Kee[str]('striped')
  WOODS = Kee[str]('woods')
