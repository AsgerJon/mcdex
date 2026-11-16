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


class MCStructures(MCThing, strictCase=False):
  """
  The catalogue of the game's structures, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    villagePlains = MCStructures.VillagePlains
    villagePlains is MCStructures['village_plains']  # True
    villagePlains[Version.V1_12_2]
    # StructureId('village_plains', 'Village{Children:[{Type:0b}]}')
    len(MCStructures)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'structures.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'structures.json'
  __data_key__ = 'structures'
  __id_class__ = StructureId
  __kind__ = 'structure'

  #  Members, one for every thing of 'structures.json'
  AbandonedCampBambooJungle = Kee[str]('abandoned_camp_bamboo_jungle')
  AbandonedCampBirchForest = Kee[str]('abandoned_camp_birch_forest')
  AbandonedCampCherryGrove = Kee[str]('abandoned_camp_cherry_grove')
  AbandonedCampDappledForest = Kee[str]('abandoned_camp_dappled_forest')
  AbandonedCampFlowerForest = Kee[str]('abandoned_camp_flower_forest')
  AbandonedCampForest = Kee[str]('abandoned_camp_forest')
  AbandonedCampMeadow = Kee[str]('abandoned_camp_meadow')
  AbandonedCampOldGrowthBirchForest = Kee[str](
    'abandoned_camp_old_growth_birch_forest')
  AbandonedCampOldGrowthPineTaiga = Kee[str](
    'abandoned_camp_old_growth_pine_taiga')
  AbandonedCampOldGrowthSpruceTaiga = Kee[str](
    'abandoned_camp_old_growth_spruce_taiga')
  AbandonedCampPaleGarden = Kee[str]('abandoned_camp_pale_garden')
  AbandonedCampSavanna = Kee[str]('abandoned_camp_savanna')
  AbandonedCampSnowyTaiga = Kee[str]('abandoned_camp_snowy_taiga')
  AbandonedCampSparseJungle = Kee[str]('abandoned_camp_sparse_jungle')
  AbandonedCampSwamp = Kee[str]('abandoned_camp_swamp')
  AbandonedCampTaiga = Kee[str]('abandoned_camp_taiga')
  AbandonedCampWindsweptForest = Kee[str]('abandoned_camp_windswept_forest')
  AbandonedCampWoodedBadlands = Kee[str]('abandoned_camp_wooded_badlands')
  AncientCity = Kee[str]('ancient_city')
  BastionRemnant = Kee[str]('bastion_remnant')
  BuriedTreasure = Kee[str]('buried_treasure')
  DesertPyramid = Kee[str]('desert_pyramid')
  EndCity = Kee[str]('end_city')
  Fortress = Kee[str]('fortress')
  Igloo = Kee[str]('igloo')
  JunglePyramid = Kee[str]('jungle_pyramid')
  Mansion = Kee[str]('mansion')
  Mineshaft = Kee[str]('mineshaft')
  MineshaftMesa = Kee[str]('mineshaft_mesa')
  Monument = Kee[str]('monument')
  NetherFossil = Kee[str]('nether_fossil')
  OceanRuinCold = Kee[str]('ocean_ruin_cold')
  OceanRuinWarm = Kee[str]('ocean_ruin_warm')
  PillagerOutpost = Kee[str]('pillager_outpost')
  RuinedPortal = Kee[str]('ruined_portal')
  RuinedPortalDesert = Kee[str]('ruined_portal_desert')
  RuinedPortalJungle = Kee[str]('ruined_portal_jungle')
  RuinedPortalMountain = Kee[str]('ruined_portal_mountain')
  RuinedPortalNether = Kee[str]('ruined_portal_nether')
  RuinedPortalOcean = Kee[str]('ruined_portal_ocean')
  RuinedPortalSwamp = Kee[str]('ruined_portal_swamp')
  Shipwreck = Kee[str]('shipwreck')
  ShipwreckBeached = Kee[str]('shipwreck_beached')
  Stronghold = Kee[str]('stronghold')
  SwampHut = Kee[str]('swamp_hut')
  TrailRuins = Kee[str]('trail_ruins')
  TrialChambers = Kee[str]('trial_chambers')
  VillageDesert = Kee[str]('village_desert')
  VillagePlains = Kee[str]('village_plains')
  VillageSavanna = Kee[str]('village_savanna')
  VillageSnowy = Kee[str]('village_snowy')
  VillageTaiga = Kee[str]('village_taiga')
