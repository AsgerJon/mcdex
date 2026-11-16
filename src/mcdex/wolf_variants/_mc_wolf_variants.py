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


class MCWolfVariants(MCThing, strictCase=False):
  """
  The catalogue of the game's wolf variants, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    ashen = MCWolfVariants.Ashen
    ashen is MCWolfVariants['ashen']  # True
    ashen[Version.V1_20_5]
    # WolfVariantId('ashen', 'minecraft:wolf{variant:"minecraft:ashen"}')
    len(MCWolfVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'wolf_variants.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'wolf_variants.json'
  __data_key__ = 'wolf_variants'
  __id_class__ = WolfVariantId
  __kind__ = 'wolf variant'

  #  Members, one for every thing of 'wolf_variants.json'
  Ashen = Kee[str]('ashen')
  Black = Kee[str]('black')
  Chestnut = Kee[str]('chestnut')
  Pale = Kee[str]('pale')
  Rusty = Kee[str]('rusty')
  Snowy = Kee[str]('snowy')
  Spotted = Kee[str]('spotted')
  Striped = Kee[str]('striped')
  Woods = Kee[str]('woods')
