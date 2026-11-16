"""
MCZombieNautilusVariants is the catalogue of the game's zombie nautilus
variants: an enumeration with one member for every zombie nautilus variant of
the data file that ships with mcdex, each the same zombie nautilus variant in
every version, with the id each version knows it by: what /summon takes for a
zombie nautilus of that variant.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import MCThing, ZombieNautilusVariantId


class MCZombieNautilusVariants(MCThing, strictCase=False):
  """
  The catalogue of the game's zombie nautilus variants, each a member. A member
  is named by its unique name in PascalCase, and found by that name in any case
  or by the unique name itself:

    warm = MCZombieNautilusVariants.Warm
    warm is MCZombieNautilusVariants['warm']  # True
    warm[Version.V1_21_11]
    # ZombieNautilusVariantId('warm',
    #   'minecraft:zombie_nautilus{variant:"minecraft:warm"}')
    len(MCZombieNautilusVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'zombie_nautilus_variants.json' beside this
  module. mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'zombie_nautilus_variants.json'
  __data_key__ = 'zombie_nautilus_variants'
  __id_class__ = ZombieNautilusVariantId
  __kind__ = 'zombie nautilus variant'

  #  Members, one for every thing of 'zombie_nautilus_variants.json'
  Temperate = Kee[str]('temperate')
  Warm = Kee[str]('warm')
