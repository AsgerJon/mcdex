"""
MCStructures is the catalogue of the game's structures: an enumeration with one
member for every structure of the data file that ships with mcdex, each the
same structure in every version, with the id each version knows it by:
what /locate takes.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import MCThing, StructureId


class MCStructures(MCThing):
  """
  The catalogue of the game's structures, each a member, found by its name in
  capitals, in any case, or by its unique name:

    villagePlains = MCStructures.VILLAGE_PLAINS
    villagePlains is MCStructures['village_plains']  # True
    villagePlains[Version.V1_12_2]
    # StructureId('village_plains', 'Village{Children:[{Type:0b}]}')
    len(MCStructures)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'structures.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'structures.json'
  __data_key__ = 'structures'
  __id_class__ = StructureId
  __kind__ = 'structure'

  #  Members, one for every name of 'structures.json'
  ABANDONED_CAMP_BAMBOO_JUNGLE = Kee[str]('abandoned_camp_bamboo_jungle')
  ABANDONED_CAMP_BIRCH_FOREST = Kee[str]('abandoned_camp_birch_forest')
  ABANDONED_CAMP_CHERRY_GROVE = Kee[str]('abandoned_camp_cherry_grove')
  ABANDONED_CAMP_DAPPLED_FOREST = Kee[str]('abandoned_camp_dappled_forest')
  ABANDONED_CAMP_FLOWER_FOREST = Kee[str]('abandoned_camp_flower_forest')
  ABANDONED_CAMP_FOREST = Kee[str]('abandoned_camp_forest')
  ABANDONED_CAMP_MEADOW = Kee[str]('abandoned_camp_meadow')
  ABANDONED_CAMP_OLD_GROWTH_BIRCH_FOREST = Kee[str](
    'abandoned_camp_old_growth_birch_forest')
  ABANDONED_CAMP_OLD_GROWTH_PINE_TAIGA = Kee[str](
    'abandoned_camp_old_growth_pine_taiga')
  ABANDONED_CAMP_OLD_GROWTH_SPRUCE_TAIGA = Kee[str](
    'abandoned_camp_old_growth_spruce_taiga')
  ABANDONED_CAMP_PALE_GARDEN = Kee[str]('abandoned_camp_pale_garden')
  ABANDONED_CAMP_SAVANNA = Kee[str]('abandoned_camp_savanna')
  ABANDONED_CAMP_SNOWY_TAIGA = Kee[str]('abandoned_camp_snowy_taiga')
  ABANDONED_CAMP_SPARSE_JUNGLE = Kee[str]('abandoned_camp_sparse_jungle')
  ABANDONED_CAMP_SWAMP = Kee[str]('abandoned_camp_swamp')
  ABANDONED_CAMP_TAIGA = Kee[str]('abandoned_camp_taiga')
  ABANDONED_CAMP_WINDSWEPT_FOREST = Kee[str]('abandoned_camp_windswept_forest')
  ABANDONED_CAMP_WOODED_BADLANDS = Kee[str]('abandoned_camp_wooded_badlands')
  ANCIENT_CITY = Kee[str]('ancient_city')
  BASTION_REMNANT = Kee[str]('bastion_remnant')
  BURIED_TREASURE = Kee[str]('buried_treasure')
  DESERT_PYRAMID = Kee[str]('desert_pyramid')
  END_CITY = Kee[str]('end_city')
  FORTRESS = Kee[str]('fortress')
  IGLOO = Kee[str]('igloo')
  JUNGLE_PYRAMID = Kee[str]('jungle_pyramid')
  MANSION = Kee[str]('mansion')
  MINESHAFT = Kee[str]('mineshaft')
  MINESHAFT_MESA = Kee[str]('mineshaft_mesa')
  MONUMENT = Kee[str]('monument')
  NETHER_FOSSIL = Kee[str]('nether_fossil')
  OCEAN_RUIN_COLD = Kee[str]('ocean_ruin_cold')
  OCEAN_RUIN_WARM = Kee[str]('ocean_ruin_warm')
  PILLAGER_OUTPOST = Kee[str]('pillager_outpost')
  RUINED_PORTAL = Kee[str]('ruined_portal')
  RUINED_PORTAL_DESERT = Kee[str]('ruined_portal_desert')
  RUINED_PORTAL_JUNGLE = Kee[str]('ruined_portal_jungle')
  RUINED_PORTAL_MOUNTAIN = Kee[str]('ruined_portal_mountain')
  RUINED_PORTAL_NETHER = Kee[str]('ruined_portal_nether')
  RUINED_PORTAL_OCEAN = Kee[str]('ruined_portal_ocean')
  RUINED_PORTAL_SWAMP = Kee[str]('ruined_portal_swamp')
  SHIPWRECK = Kee[str]('shipwreck')
  SHIPWRECK_BEACHED = Kee[str]('shipwreck_beached')
  STRONGHOLD = Kee[str]('stronghold')
  SWAMP_HUT = Kee[str]('swamp_hut')
  TRAIL_RUINS = Kee[str]('trail_ruins')
  TRIAL_CHAMBERS = Kee[str]('trial_chambers')
  VILLAGE_DESERT = Kee[str]('village_desert')
  VILLAGE_PLAINS = Kee[str]('village_plains')
  VILLAGE_SAVANNA = Kee[str]('village_savanna')
  VILLAGE_SNOWY = Kee[str]('village_snowy')
  VILLAGE_TAIGA = Kee[str]('village_taiga')
