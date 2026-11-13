"""
MCVillagerTypes is the catalogue of the game's villager types: an enumeration
with one member for every villager type of the data file that ships with mcdex,
each the same villager type in every version, with the id each version knows it
by: what /summon takes for a villager of that type.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import MCThing, VillagerTypeId


class MCVillagerTypes(MCThing):
  """
  The catalogue of the game's villager types, each a member, found by its name
  in capitals, in any case, or by its unique name:

    desert = MCVillagerTypes.DESERT
    desert is MCVillagerTypes['desert']  # True
    desert['1.14']
    # VillagerTypeId('desert',
    #   'minecraft:villager{VillagerData:{type:"minecraft:desert"}}')
    len(MCVillagerTypes)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'villager_types.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'villager_types.json'
  __data_key__ = 'villager_types'
  __id_class__ = VillagerTypeId
  __kind__ = 'villager type'

  #  Members, one for every name of 'villager_types.json'
  DESERT = Kee[str]('desert')
  JUNGLE = Kee[str]('jungle')
  PLAINS = Kee[str]('plains')
  SAVANNA = Kee[str]('savanna')
  SNOW = Kee[str]('snow')
  SWAMP = Kee[str]('swamp')
  TAIGA = Kee[str]('taiga')
