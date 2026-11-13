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


class MCZombieNautilusVariants(MCThing):
  """
  The catalogue of the game's zombie nautilus variants, each a member, found by
  its name in capitals, in any case, or by its unique name:

    warm = MCZombieNautilusVariants.WARM
    warm is MCZombieNautilusVariants['warm']  # True
    warm[Version.V1_21_11]
    # ZombieNautilusVariantId('warm',
    #   'minecraft:zombie_nautilus{variant:"minecraft:warm"}')
    len(MCZombieNautilusVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'zombie_nautilus_variants.json' beside this
  module. mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'zombie_nautilus_variants.json'
  __data_key__ = 'zombie_nautilus_variants'
  __id_class__ = ZombieNautilusVariantId
  __kind__ = 'zombie nautilus variant'

  #  Members, one for every name of 'zombie_nautilus_variants.json'
  TEMPERATE = Kee[str]('temperate')
  WARM = Kee[str]('warm')
