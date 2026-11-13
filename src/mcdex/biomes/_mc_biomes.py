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


class MCBiomes(MCThing):
  """
  The catalogue of the game's biomes, each a member, found by its name in
  capitals, in any case, or by its unique name:

    plains = MCBiomes.PLAINS
    plains is MCBiomes['plains']  # True
    plains['1.8.9']  # BiomeId('plains', '1')
    len(MCBiomes)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'biomes.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'biomes.json'
  __data_key__ = 'biomes'
  __id_class__ = BiomeId
  __kind__ = 'biome'

  #  Members, one for every name of 'biomes.json'
  BADLANDS = Kee[str]('badlands')
  BADLANDS_PLATEAU = Kee[str]('badlands_plateau')
  BAMBOO_JUNGLE = Kee[str]('bamboo_jungle')
  BAMBOO_JUNGLE_HILLS = Kee[str]('bamboo_jungle_hills')
  BASALT_DELTAS = Kee[str]('basalt_deltas')
  BEACH = Kee[str]('beach')
  BIRCH_FOREST = Kee[str]('birch_forest')
  BIRCH_FOREST_HILLS = Kee[str]('birch_forest_hills')
  CHERRY_GROVE = Kee[str]('cherry_grove')
  COLD_OCEAN = Kee[str]('cold_ocean')
  CRIMSON_FOREST = Kee[str]('crimson_forest')
  DAPPLED_FOREST = Kee[str]('dappled_forest')
  DARK_FOREST = Kee[str]('dark_forest')
  DARK_FOREST_HILLS = Kee[str]('dark_forest_hills')
  DEEP_COLD_OCEAN = Kee[str]('deep_cold_ocean')
  DEEP_DARK = Kee[str]('deep_dark')
  DEEP_FROZEN_OCEAN = Kee[str]('deep_frozen_ocean')
  DEEP_LUKEWARM_OCEAN = Kee[str]('deep_lukewarm_ocean')
  DEEP_OCEAN = Kee[str]('deep_ocean')
  DEEP_WARM_OCEAN = Kee[str]('deep_warm_ocean')
  DESERT = Kee[str]('desert')
  DESERT_HILLS = Kee[str]('desert_hills')
  DESERT_LAKES = Kee[str]('desert_lakes')
  DRIPSTONE_CAVES = Kee[str]('dripstone_caves')
  END_BARRENS = Kee[str]('end_barrens')
  END_HIGHLANDS = Kee[str]('end_highlands')
  END_MIDLANDS = Kee[str]('end_midlands')
  ERODED_BADLANDS = Kee[str]('eroded_badlands')
  FLOWER_FOREST = Kee[str]('flower_forest')
  FOREST = Kee[str]('forest')
  FROZEN_OCEAN = Kee[str]('frozen_ocean')
  FROZEN_PEAKS = Kee[str]('frozen_peaks')
  FROZEN_RIVER = Kee[str]('frozen_river')
  GIANT_SPRUCE_TAIGA_HILLS = Kee[str]('giant_spruce_taiga_hills')
  GIANT_TREE_TAIGA_HILLS = Kee[str]('giant_tree_taiga_hills')
  GROVE = Kee[str]('grove')
  ICE_SPIKES = Kee[str]('ice_spikes')
  JAGGED_PEAKS = Kee[str]('jagged_peaks')
  JUNGLE = Kee[str]('jungle')
  JUNGLE_HILLS = Kee[str]('jungle_hills')
  LUKEWARM_OCEAN = Kee[str]('lukewarm_ocean')
  LUSH_CAVES = Kee[str]('lush_caves')
  MANGROVE_SWAMP = Kee[str]('mangrove_swamp')
  MEADOW = Kee[str]('meadow')
  MODIFIED_BADLANDS_PLATEAU = Kee[str]('modified_badlands_plateau')
  MODIFIED_GRAVELLY_MOUNTAINS = Kee[str]('modified_gravelly_mountains')
  MODIFIED_JUNGLE = Kee[str]('modified_jungle')
  MODIFIED_JUNGLE_EDGE = Kee[str]('modified_jungle_edge')
  MODIFIED_WOODED_BADLANDS_PLATEAU = Kee[str](
    'modified_wooded_badlands_plateau')
  MOUNTAIN_EDGE = Kee[str]('mountain_edge')
  MUSHROOM_FIELD_SHORE = Kee[str]('mushroom_field_shore')
  MUSHROOM_FIELDS = Kee[str]('mushroom_fields')
  NETHER_WASTES = Kee[str]('nether_wastes')
  OCEAN = Kee[str]('ocean')
  OLD_GROWTH_BIRCH_FOREST = Kee[str]('old_growth_birch_forest')
  OLD_GROWTH_PINE_TAIGA = Kee[str]('old_growth_pine_taiga')
  OLD_GROWTH_SPRUCE_TAIGA = Kee[str]('old_growth_spruce_taiga')
  PALE_GARDEN = Kee[str]('pale_garden')
  PLAINS = Kee[str]('plains')
  RIVER = Kee[str]('river')
  SAVANNA = Kee[str]('savanna')
  SAVANNA_PLATEAU = Kee[str]('savanna_plateau')
  SHATTERED_SAVANNA_PLATEAU = Kee[str]('shattered_savanna_plateau')
  SMALL_END_ISLANDS = Kee[str]('small_end_islands')
  SNOWY_BEACH = Kee[str]('snowy_beach')
  SNOWY_MOUNTAINS = Kee[str]('snowy_mountains')
  SNOWY_PLAINS = Kee[str]('snowy_plains')
  SNOWY_SLOPES = Kee[str]('snowy_slopes')
  SNOWY_TAIGA = Kee[str]('snowy_taiga')
  SNOWY_TAIGA_HILLS = Kee[str]('snowy_taiga_hills')
  SNOWY_TAIGA_MOUNTAINS = Kee[str]('snowy_taiga_mountains')
  SOUL_SAND_VALLEY = Kee[str]('soul_sand_valley')
  SPARSE_JUNGLE = Kee[str]('sparse_jungle')
  STONY_PEAKS = Kee[str]('stony_peaks')
  STONY_SHORE = Kee[str]('stony_shore')
  SULFUR_CAVES = Kee[str]('sulfur_caves')
  SUNFLOWER_PLAINS = Kee[str]('sunflower_plains')
  SWAMP = Kee[str]('swamp')
  SWAMP_HILLS = Kee[str]('swamp_hills')
  TAIGA = Kee[str]('taiga')
  TAIGA_HILLS = Kee[str]('taiga_hills')
  TAIGA_MOUNTAINS = Kee[str]('taiga_mountains')
  TALL_BIRCH_HILLS = Kee[str]('tall_birch_hills')
  THE_END = Kee[str]('the_end')
  THE_VOID = Kee[str]('the_void')
  WARM_OCEAN = Kee[str]('warm_ocean')
  WARPED_FOREST = Kee[str]('warped_forest')
  WINDSWEPT_FOREST = Kee[str]('windswept_forest')
  WINDSWEPT_GRAVELLY_HILLS = Kee[str]('windswept_gravelly_hills')
  WINDSWEPT_HILLS = Kee[str]('windswept_hills')
  WINDSWEPT_SAVANNA = Kee[str]('windswept_savanna')
  WOODED_BADLANDS = Kee[str]('wooded_badlands')
  WOODED_HILLS = Kee[str]('wooded_hills')
