"""
MCBiomes is the catalogue of the game's biomes: an enumeration with one
member for every biome of the data file that ships with mcdex, each the
same biome in every version, with the id each version knows it by:
the biome's number to 1.8.9, its name from 1.9.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import BiomeId, MCThing


class MCBiomes(MCThing, strictCase=False):
  """
  The catalogue of the game's biomes, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    plains = MCBiomes.Plains
    plains is MCBiomes['plains']  # True
    plains[Version.V1_8_9]  # BiomeId('plains', '1')
    len(MCBiomes)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'biomes.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'biomes.json'
  __data_key__ = 'biomes'
  __id_class__ = BiomeId
  __kind__ = 'biome'

  #  Members, one for every thing of 'biomes.json'
  Badlands = Kee[str]('badlands')
  BadlandsPlateau = Kee[str]('badlands_plateau')
  BambooJungle = Kee[str]('bamboo_jungle')
  BambooJungleHills = Kee[str]('bamboo_jungle_hills')
  BasaltDeltas = Kee[str]('basalt_deltas')
  Beach = Kee[str]('beach')
  BirchForest = Kee[str]('birch_forest')
  BirchForestHills = Kee[str]('birch_forest_hills')
  CherryGrove = Kee[str]('cherry_grove')
  ColdOcean = Kee[str]('cold_ocean')
  CrimsonForest = Kee[str]('crimson_forest')
  DappledForest = Kee[str]('dappled_forest')
  DarkForest = Kee[str]('dark_forest')
  DarkForestHills = Kee[str]('dark_forest_hills')
  DeepColdOcean = Kee[str]('deep_cold_ocean')
  DeepDark = Kee[str]('deep_dark')
  DeepFrozenOcean = Kee[str]('deep_frozen_ocean')
  DeepLukewarmOcean = Kee[str]('deep_lukewarm_ocean')
  DeepOcean = Kee[str]('deep_ocean')
  DeepWarmOcean = Kee[str]('deep_warm_ocean')
  Desert = Kee[str]('desert')
  DesertHills = Kee[str]('desert_hills')
  DesertLakes = Kee[str]('desert_lakes')
  DripstoneCaves = Kee[str]('dripstone_caves')
  EndBarrens = Kee[str]('end_barrens')
  EndHighlands = Kee[str]('end_highlands')
  EndMidlands = Kee[str]('end_midlands')
  ErodedBadlands = Kee[str]('eroded_badlands')
  FlowerForest = Kee[str]('flower_forest')
  Forest = Kee[str]('forest')
  FrozenOcean = Kee[str]('frozen_ocean')
  FrozenPeaks = Kee[str]('frozen_peaks')
  FrozenRiver = Kee[str]('frozen_river')
  GiantSpruceTaigaHills = Kee[str]('giant_spruce_taiga_hills')
  GiantTreeTaigaHills = Kee[str]('giant_tree_taiga_hills')
  Grove = Kee[str]('grove')
  IceSpikes = Kee[str]('ice_spikes')
  JaggedPeaks = Kee[str]('jagged_peaks')
  Jungle = Kee[str]('jungle')
  JungleHills = Kee[str]('jungle_hills')
  LukewarmOcean = Kee[str]('lukewarm_ocean')
  LushCaves = Kee[str]('lush_caves')
  MangroveSwamp = Kee[str]('mangrove_swamp')
  Meadow = Kee[str]('meadow')
  ModifiedBadlandsPlateau = Kee[str]('modified_badlands_plateau')
  ModifiedGravellyMountains = Kee[str]('modified_gravelly_mountains')
  ModifiedJungle = Kee[str]('modified_jungle')
  ModifiedJungleEdge = Kee[str]('modified_jungle_edge')
  ModifiedWoodedBadlandsPlateau = Kee[str]('modified_wooded_badlands_plateau')
  MountainEdge = Kee[str]('mountain_edge')
  MushroomFieldShore = Kee[str]('mushroom_field_shore')
  MushroomFields = Kee[str]('mushroom_fields')
  NetherWastes = Kee[str]('nether_wastes')
  Ocean = Kee[str]('ocean')
  OldGrowthBirchForest = Kee[str]('old_growth_birch_forest')
  OldGrowthPineTaiga = Kee[str]('old_growth_pine_taiga')
  OldGrowthSpruceTaiga = Kee[str]('old_growth_spruce_taiga')
  PaleGarden = Kee[str]('pale_garden')
  Plains = Kee[str]('plains')
  River = Kee[str]('river')
  Savanna = Kee[str]('savanna')
  SavannaPlateau = Kee[str]('savanna_plateau')
  ShatteredSavannaPlateau = Kee[str]('shattered_savanna_plateau')
  SmallEndIslands = Kee[str]('small_end_islands')
  SnowyBeach = Kee[str]('snowy_beach')
  SnowyMountains = Kee[str]('snowy_mountains')
  SnowyPlains = Kee[str]('snowy_plains')
  SnowySlopes = Kee[str]('snowy_slopes')
  SnowyTaiga = Kee[str]('snowy_taiga')
  SnowyTaigaHills = Kee[str]('snowy_taiga_hills')
  SnowyTaigaMountains = Kee[str]('snowy_taiga_mountains')
  SoulSandValley = Kee[str]('soul_sand_valley')
  SparseJungle = Kee[str]('sparse_jungle')
  StonyPeaks = Kee[str]('stony_peaks')
  StonyShore = Kee[str]('stony_shore')
  SulfurCaves = Kee[str]('sulfur_caves')
  SunflowerPlains = Kee[str]('sunflower_plains')
  Swamp = Kee[str]('swamp')
  SwampHills = Kee[str]('swamp_hills')
  Taiga = Kee[str]('taiga')
  TaigaHills = Kee[str]('taiga_hills')
  TaigaMountains = Kee[str]('taiga_mountains')
  TallBirchHills = Kee[str]('tall_birch_hills')
  TheEnd = Kee[str]('the_end')
  TheVoid = Kee[str]('the_void')
  WarmOcean = Kee[str]('warm_ocean')
  WarpedForest = Kee[str]('warped_forest')
  WindsweptForest = Kee[str]('windswept_forest')
  WindsweptGravellyHills = Kee[str]('windswept_gravelly_hills')
  WindsweptHills = Kee[str]('windswept_hills')
  WindsweptSavanna = Kee[str]('windswept_savanna')
  WoodedBadlands = Kee[str]('wooded_badlands')
  WoodedHills = Kee[str]('wooded_hills')
