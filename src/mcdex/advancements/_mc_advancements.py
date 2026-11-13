"""
MCAdvancements is the catalogue of the game's advancements: an enumeration with
one member for every advancement of the data file that ships with mcdex, each
the same advancement in every version, with the id each version knows it by:
what /advancement takes.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import AdvancementId, MCThing


class MCAdvancements(MCThing):
  """
  The catalogue of the game's advancements, each a member, found by its name in
  capitals, in any case, or by its unique name:

    stoneAge = MCAdvancements.STONE_AGE
    stoneAge is MCAdvancements['stone_age']  # True
    stoneAge[Version.V1_12]
    # AdvancementId('stone_age', 'minecraft:story/mine_stone')
    len(MCAdvancements)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'advancements.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'advancements.json'
  __data_key__ = 'advancements'
  __id_class__ = AdvancementId
  __kind__ = 'advancement'

  #  Members, one for every name of 'advancements.json'
  A_BALANCED_DIET = Kee[str]('a_balanced_diet')
  A_COMPLETE_CATALOGUE = Kee[str]('a_complete_catalogue')
  A_FURIOUS_COCKTAIL = Kee[str]('a_furious_cocktail')
  A_SEEDY_PLACE = Kee[str]('a_seedy_place')
  A_TERRIBLE_FORTRESS = Kee[str]('a_terrible_fortress')
  A_THROWAWAY_JOKE = Kee[str]('a_throwaway_joke')
  ACACIA_BOAT_RECIPE = Kee[str]('acacia_boat_recipe')
  ACACIA_BUTTON_RECIPE = Kee[str]('acacia_button_recipe')
  ACACIA_CHEST_BOAT_RECIPE = Kee[str]('acacia_chest_boat_recipe')
  ACACIA_DOOR_RECIPE = Kee[str]('acacia_door_recipe')
  ACACIA_FENCE_GATE_RECIPE = Kee[str]('acacia_fence_gate_recipe')
  ACACIA_FENCE_RECIPE = Kee[str]('acacia_fence_recipe')
  ACACIA_HANGING_SIGN_RECIPE = Kee[str]('acacia_hanging_sign_recipe')
  ACACIA_PLANKS_RECIPE = Kee[str]('acacia_planks_recipe')
  ACACIA_PRESSURE_PLATE_RECIPE = Kee[str]('acacia_pressure_plate_recipe')
  ACACIA_SHELF_RECIPE = Kee[str]('acacia_shelf_recipe')
  ACACIA_SIGN_RECIPE = Kee[str]('acacia_sign_recipe')
  ACACIA_SLAB_RECIPE = Kee[str]('acacia_slab_recipe')
  ACACIA_STAIRS_RECIPE = Kee[str]('acacia_stairs_recipe')
  ACACIA_TRAPDOOR_RECIPE = Kee[str]('acacia_trapdoor_recipe')
  ACACIA_WOOD_RECIPE = Kee[str]('acacia_wood_recipe')
  ACQUIRE_HARDWARE = Kee[str]('acquire_hardware')
  ACTIVATOR_RAIL_RECIPE = Kee[str]('activator_rail_recipe')
  ADVENTURE_ROOT = Kee[str]('adventure_root')
  ADVENTURING_TIME = Kee[str]('adventuring_time')
  AMETHYST_BLOCK_RECIPE = Kee[str]('amethyst_block_recipe')
  ANDESITE_RECIPE = Kee[str]('andesite_recipe')
  ANDESITE_SLAB_FROM_ANDESITE_STONECUTTING_RECIPE = Kee[str](
    'andesite_slab_from_andesite_stonecutting_recipe')
  ANDESITE_SLAB_RECIPE = Kee[str]('andesite_slab_recipe')
  ANDESITE_STAIRS_FROM_ANDESITE_STONECUTTING_RECIPE = Kee[str](
    'andesite_stairs_from_andesite_stonecutting_recipe')
  ANDESITE_STAIRS_RECIPE = Kee[str]('andesite_stairs_recipe')
  ANDESITE_WALL_FROM_ANDESITE_STONECUTTING_RECIPE = Kee[str](
    'andesite_wall_from_andesite_stonecutting_recipe')
  ANDESITE_WALL_RECIPE = Kee[str]('andesite_wall_recipe')
  ANVIL_RECIPE = Kee[str]('anvil_recipe')
  ARBALISTIC = Kee[str]('arbalistic')
  ARMOR_STAND_RECIPE = Kee[str]('armor_stand_recipe')
  ARROW_RECIPE = Kee[str]('arrow_recipe')
  BAKED_POTATO_FROM_CAMPFIRE_COOKING_RECIPE = Kee[str](
    'baked_potato_from_campfire_cooking_recipe')
  BAKED_POTATO_FROM_SMOKING_RECIPE = Kee[str](
    'baked_potato_from_smoking_recipe')
  BAKED_POTATO_RECIPE = Kee[str]('baked_potato_recipe')
  BAMBOO_BLOCK_RECIPE = Kee[str]('bamboo_block_recipe')
  BAMBOO_BUTTON_RECIPE = Kee[str]('bamboo_button_recipe')
  BAMBOO_CHEST_RAFT_RECIPE = Kee[str]('bamboo_chest_raft_recipe')
  BAMBOO_DOOR_RECIPE = Kee[str]('bamboo_door_recipe')
  BAMBOO_FENCE_GATE_RECIPE = Kee[str]('bamboo_fence_gate_recipe')
  BAMBOO_FENCE_RECIPE = Kee[str]('bamboo_fence_recipe')
  BAMBOO_HANGING_SIGN_RECIPE = Kee[str]('bamboo_hanging_sign_recipe')
  BAMBOO_MOSAIC_RECIPE = Kee[str]('bamboo_mosaic_recipe')
  BAMBOO_MOSAIC_SLAB_RECIPE = Kee[str]('bamboo_mosaic_slab_recipe')
  BAMBOO_MOSAIC_STAIRS_RECIPE = Kee[str]('bamboo_mosaic_stairs_recipe')
  BAMBOO_PLANKS_RECIPE = Kee[str]('bamboo_planks_recipe')
  BAMBOO_PRESSURE_PLATE_RECIPE = Kee[str]('bamboo_pressure_plate_recipe')
  BAMBOO_RAFT_RECIPE = Kee[str]('bamboo_raft_recipe')
  BAMBOO_SHELF_RECIPE = Kee[str]('bamboo_shelf_recipe')
  BAMBOO_SIGN_RECIPE = Kee[str]('bamboo_sign_recipe')
  BAMBOO_SLAB_RECIPE = Kee[str]('bamboo_slab_recipe')
  BAMBOO_STAIRS_RECIPE = Kee[str]('bamboo_stairs_recipe')
  BAMBOO_TRAPDOOR_RECIPE = Kee[str]('bamboo_trapdoor_recipe')
  BARREL_RECIPE = Kee[str]('barrel_recipe')
  BEACON_RECIPE = Kee[str]('beacon_recipe')
  BEACONATOR = Kee[str]('beaconator')
  BEE_OUR_GUEST = Kee[str]('bee_our_guest')
  BEEHIVE_RECIPE = Kee[str]('beehive_recipe')
  BEETROOT_SOUP_RECIPE = Kee[str]('beetroot_soup_recipe')
  BEST_FRIENDS_FOREVER = Kee[str]('best_friends_forever')
  BIRCH_BOAT_RECIPE = Kee[str]('birch_boat_recipe')
  BIRCH_BUTTON_RECIPE = Kee[str]('birch_button_recipe')
  BIRCH_CHEST_BOAT_RECIPE = Kee[str]('birch_chest_boat_recipe')
  BIRCH_DOOR_RECIPE = Kee[str]('birch_door_recipe')
  BIRCH_FENCE_GATE_RECIPE = Kee[str]('birch_fence_gate_recipe')
  BIRCH_FENCE_RECIPE = Kee[str]('birch_fence_recipe')
  BIRCH_HANGING_SIGN_RECIPE = Kee[str]('birch_hanging_sign_recipe')
  BIRCH_PLANKS_RECIPE = Kee[str]('birch_planks_recipe')
  BIRCH_PRESSURE_PLATE_RECIPE = Kee[str]('birch_pressure_plate_recipe')
  BIRCH_SHELF_RECIPE = Kee[str]('birch_shelf_recipe')
  BIRCH_SIGN_RECIPE = Kee[str]('birch_sign_recipe')
  BIRCH_SLAB_RECIPE = Kee[str]('birch_slab_recipe')
  BIRCH_STAIRS_RECIPE = Kee[str]('birch_stairs_recipe')
  BIRCH_TRAPDOOR_RECIPE = Kee[str]('birch_trapdoor_recipe')
  BIRCH_WOOD_RECIPE = Kee[str]('birch_wood_recipe')
  BIRTHDAY_SONG = Kee[str]('birthday_song')
  BLACK_BANNER_RECIPE = Kee[str]('black_banner_recipe')
  BLACK_BED_FROM_WHITE_BED_RECIPE = Kee[str]('black_bed_from_white_bed_recipe')
  BLACK_BED_RECIPE = Kee[str]('black_bed_recipe')
  BLACK_BUNDLE_RECIPE = Kee[str]('black_bundle_recipe')
  BLACK_CANDLE_RECIPE = Kee[str]('black_candle_recipe')
  BLACK_CARPET_FROM_WHITE_CARPET_RECIPE = Kee[str](
    'black_carpet_from_white_carpet_recipe')
  BLACK_CARPET_RECIPE = Kee[str]('black_carpet_recipe')
  BLACK_CONCRETE_POWDER_RECIPE = Kee[str]('black_concrete_powder_recipe')
  BLACK_CONCRETE_SLAB_FROM_BLACK_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'black_concrete_slab_from_black_concrete_stonecutting_recipe')
  BLACK_CONCRETE_SLAB_RECIPE = Kee[str]('black_concrete_slab_recipe')
  BLACK_CONCRETE_STAIRS_FROM_BLACK_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'black_concrete_stairs_from_black_concrete_stonecutting_recipe')
  BLACK_CONCRETE_STAIRS_RECIPE = Kee[str]('black_concrete_stairs_recipe')
  BLACK_CUSHION_RECIPE = Kee[str]('black_cushion_recipe')
  BLACK_DYE_FROM_WITHER_ROSE_RECIPE = Kee[str](
    'black_dye_from_wither_rose_recipe')
  BLACK_DYE_RECIPE = Kee[str]('black_dye_recipe')
  BLACK_GLAZED_TERRACOTTA_RECIPE = Kee[str]('black_glazed_terracotta_recipe')
  BLACK_HARNESS_RECIPE = Kee[str]('black_harness_recipe')
  BLACK_SHULKER_BOX_RECIPE = Kee[str]('black_shulker_box_recipe')
  BLACK_STAINED_GLASS_PANE_FROM_GLASS_PANE_RECIPE = Kee[str](
    'black_stained_glass_pane_from_glass_pane_recipe')
  BLACK_STAINED_GLASS_PANE_RECIPE = Kee[str]('black_stained_glass_pane_recipe')
  BLACK_STAINED_GLASS_RECIPE = Kee[str]('black_stained_glass_recipe')
  BLACK_TERRACOTTA_RECIPE = Kee[str]('black_terracotta_recipe')
  BLACK_WOOL_RECIPE = Kee[str]('black_wool_recipe')
  BLACK_WOOL_SLAB_RECIPE = Kee[str]('black_wool_slab_recipe')
  BLACK_WOOL_STAIRS_RECIPE = Kee[str]('black_wool_stairs_recipe')
  BLACKSTONE_SLAB_FROM_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'blackstone_slab_from_blackstone_stonecutting_recipe')
  BLACKSTONE_SLAB_RECIPE = Kee[str]('blackstone_slab_recipe')
  BLACKSTONE_STAIRS_FROM_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'blackstone_stairs_from_blackstone_stonecutting_recipe')
  BLACKSTONE_STAIRS_RECIPE = Kee[str]('blackstone_stairs_recipe')
  BLACKSTONE_WALL_FROM_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'blackstone_wall_from_blackstone_stonecutting_recipe')
  BLACKSTONE_WALL_RECIPE = Kee[str]('blackstone_wall_recipe')
  BLAST_FURNACE_RECIPE = Kee[str]('blast_furnace_recipe')
  BLAZE_POWDER_RECIPE = Kee[str]('blaze_powder_recipe')
  BLOWBACK = Kee[str]('blowback')
  BLUE_BANNER_RECIPE = Kee[str]('blue_banner_recipe')
  BLUE_BED_FROM_WHITE_BED_RECIPE = Kee[str]('blue_bed_from_white_bed_recipe')
  BLUE_BED_RECIPE = Kee[str]('blue_bed_recipe')
  BLUE_BUNDLE_RECIPE = Kee[str]('blue_bundle_recipe')
  BLUE_CANDLE_RECIPE = Kee[str]('blue_candle_recipe')
  BLUE_CARPET_FROM_WHITE_CARPET_RECIPE = Kee[str](
    'blue_carpet_from_white_carpet_recipe')
  BLUE_CARPET_RECIPE = Kee[str]('blue_carpet_recipe')
  BLUE_CONCRETE_POWDER_RECIPE = Kee[str]('blue_concrete_powder_recipe')
  BLUE_CONCRETE_SLAB_FROM_BLUE_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'blue_concrete_slab_from_blue_concrete_stonecutting_recipe')
  BLUE_CONCRETE_SLAB_RECIPE = Kee[str]('blue_concrete_slab_recipe')
  BLUE_CONCRETE_STAIRS_FROM_BLUE_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'blue_concrete_stairs_from_blue_concrete_stonecutting_recipe')
  BLUE_CONCRETE_STAIRS_RECIPE = Kee[str]('blue_concrete_stairs_recipe')
  BLUE_CUSHION_RECIPE = Kee[str]('blue_cushion_recipe')
  BLUE_DYE_FROM_CORNFLOWER_RECIPE = Kee[str]('blue_dye_from_cornflower_recipe')
  BLUE_DYE_RECIPE = Kee[str]('blue_dye_recipe')
  BLUE_GLAZED_TERRACOTTA_RECIPE = Kee[str]('blue_glazed_terracotta_recipe')
  BLUE_HARNESS_RECIPE = Kee[str]('blue_harness_recipe')
  BLUE_ICE_RECIPE = Kee[str]('blue_ice_recipe')
  BLUE_SHULKER_BOX_RECIPE = Kee[str]('blue_shulker_box_recipe')
  BLUE_STAINED_GLASS_PANE_FROM_GLASS_PANE_RECIPE = Kee[str](
    'blue_stained_glass_pane_from_glass_pane_recipe')
  BLUE_STAINED_GLASS_PANE_RECIPE = Kee[str]('blue_stained_glass_pane_recipe')
  BLUE_STAINED_GLASS_RECIPE = Kee[str]('blue_stained_glass_recipe')
  BLUE_TERRACOTTA_RECIPE = Kee[str]('blue_terracotta_recipe')
  BLUE_WOOL_RECIPE = Kee[str]('blue_wool_recipe')
  BLUE_WOOL_SLAB_RECIPE = Kee[str]('blue_wool_slab_recipe')
  BLUE_WOOL_STAIRS_RECIPE = Kee[str]('blue_wool_stairs_recipe')
  BOLT_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'bolt_armor_trim_smithing_template_recipe')
  BOLT_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'bolt_armor_trim_smithing_template_smithing_trim_recipe')
  BONE_BLOCK_RECIPE = Kee[str]('bone_block_recipe')
  BONE_MEAL_FROM_BONE_BLOCK_RECIPE = Kee[str](
    'bone_meal_from_bone_block_recipe')
  BONE_MEAL_RECIPE = Kee[str]('bone_meal_recipe')
  BOOK_RECIPE = Kee[str]('book_recipe')
  BOOKSHELF_RECIPE = Kee[str]('bookshelf_recipe')
  BORDURE_INDENTED_BANNER_PATTERN_RECIPE = Kee[str](
    'bordure_indented_banner_pattern_recipe')
  BOW_RECIPE = Kee[str]('bow_recipe')
  BOWL_RECIPE = Kee[str]('bowl_recipe')
  BREAD_RECIPE = Kee[str]('bread_recipe')
  BREWING_STAND_RECIPE = Kee[str]('brewing_stand_recipe')
  BRICK_RECIPE = Kee[str]('brick_recipe')
  BRICK_SLAB_FROM_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'brick_slab_from_bricks_stonecutting_recipe')
  BRICK_SLAB_RECIPE = Kee[str]('brick_slab_recipe')
  BRICK_STAIRS_FROM_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'brick_stairs_from_bricks_stonecutting_recipe')
  BRICK_STAIRS_RECIPE = Kee[str]('brick_stairs_recipe')
  BRICK_WALL_FROM_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'brick_wall_from_bricks_stonecutting_recipe')
  BRICK_WALL_RECIPE = Kee[str]('brick_wall_recipe')
  BRICKS_RECIPE = Kee[str]('bricks_recipe')
  BRING_HOME_THE_BEACON = Kee[str]('bring_home_the_beacon')
  BROWN_BANNER_RECIPE = Kee[str]('brown_banner_recipe')
  BROWN_BED_FROM_WHITE_BED_RECIPE = Kee[str]('brown_bed_from_white_bed_recipe')
  BROWN_BED_RECIPE = Kee[str]('brown_bed_recipe')
  BROWN_BUNDLE_RECIPE = Kee[str]('brown_bundle_recipe')
  BROWN_CANDLE_RECIPE = Kee[str]('brown_candle_recipe')
  BROWN_CARPET_FROM_WHITE_CARPET_RECIPE = Kee[str](
    'brown_carpet_from_white_carpet_recipe')
  BROWN_CARPET_RECIPE = Kee[str]('brown_carpet_recipe')
  BROWN_CONCRETE_POWDER_RECIPE = Kee[str]('brown_concrete_powder_recipe')
  BROWN_CONCRETE_SLAB_FROM_BROWN_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'brown_concrete_slab_from_brown_concrete_stonecutting_recipe')
  BROWN_CONCRETE_SLAB_RECIPE = Kee[str]('brown_concrete_slab_recipe')
  BROWN_CONCRETE_STAIRS_FROM_BROWN_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'brown_concrete_stairs_from_brown_concrete_stonecutting_recipe')
  BROWN_CONCRETE_STAIRS_RECIPE = Kee[str]('brown_concrete_stairs_recipe')
  BROWN_CUSHION_RECIPE = Kee[str]('brown_cushion_recipe')
  BROWN_DYE_RECIPE = Kee[str]('brown_dye_recipe')
  BROWN_GLAZED_TERRACOTTA_RECIPE = Kee[str]('brown_glazed_terracotta_recipe')
  BROWN_HARNESS_RECIPE = Kee[str]('brown_harness_recipe')
  BROWN_SHULKER_BOX_RECIPE = Kee[str]('brown_shulker_box_recipe')
  BROWN_STAINED_GLASS_PANE_FROM_GLASS_PANE_RECIPE = Kee[str](
    'brown_stained_glass_pane_from_glass_pane_recipe')
  BROWN_STAINED_GLASS_PANE_RECIPE = Kee[str]('brown_stained_glass_pane_recipe')
  BROWN_STAINED_GLASS_RECIPE = Kee[str]('brown_stained_glass_recipe')
  BROWN_TERRACOTTA_RECIPE = Kee[str]('brown_terracotta_recipe')
  BROWN_WOOL_RECIPE = Kee[str]('brown_wool_recipe')
  BROWN_WOOL_SLAB_RECIPE = Kee[str]('brown_wool_slab_recipe')
  BROWN_WOOL_STAIRS_RECIPE = Kee[str]('brown_wool_stairs_recipe')
  BRUSH_RECIPE = Kee[str]('brush_recipe')
  BUCKET_RECIPE = Kee[str]('bucket_recipe')
  BUKKIT_BUKKIT = Kee[str]('bukkit_bukkit')
  BULLSEYE = Kee[str]('bullseye')
  BUNDLE_RECIPE = Kee[str]('bundle_recipe')
  CACTUS_GREEN_RECIPE = Kee[str]('cactus_green_recipe')
  CAKE_RECIPE = Kee[str]('cake_recipe')
  CALIBRATED_SCULK_SENSOR_RECIPE = Kee[str]('calibrated_sculk_sensor_recipe')
  CAMPFIRE_RECIPE = Kee[str]('campfire_recipe')
  CANDLE_RECIPE = Kee[str]('candle_recipe')
  CAREFUL_RESTORATION = Kee[str]('careful_restoration')
  CARROT_ON_A_STICK_RECIPE = Kee[str]('carrot_on_a_stick_recipe')
  CARTOGRAPHY_TABLE_RECIPE = Kee[str]('cartography_table_recipe')
  CAULDRON_RECIPE = Kee[str]('cauldron_recipe')
  CAVES_CLIFFS = Kee[str]('caves_cliffs')
  CHAIN_RECIPE = Kee[str]('chain_recipe')
  CHARCOAL_RECIPE = Kee[str]('charcoal_recipe')
  CHERRY_BOAT_RECIPE = Kee[str]('cherry_boat_recipe')
  CHERRY_BUTTON_RECIPE = Kee[str]('cherry_button_recipe')
  CHERRY_CHEST_BOAT_RECIPE = Kee[str]('cherry_chest_boat_recipe')
  CHERRY_DOOR_RECIPE = Kee[str]('cherry_door_recipe')
  CHERRY_FENCE_GATE_RECIPE = Kee[str]('cherry_fence_gate_recipe')
  CHERRY_FENCE_RECIPE = Kee[str]('cherry_fence_recipe')
  CHERRY_HANGING_SIGN_RECIPE = Kee[str]('cherry_hanging_sign_recipe')
  CHERRY_PLANKS_RECIPE = Kee[str]('cherry_planks_recipe')
  CHERRY_PRESSURE_PLATE_RECIPE = Kee[str]('cherry_pressure_plate_recipe')
  CHERRY_SHELF_RECIPE = Kee[str]('cherry_shelf_recipe')
  CHERRY_SIGN_RECIPE = Kee[str]('cherry_sign_recipe')
  CHERRY_SLAB_RECIPE = Kee[str]('cherry_slab_recipe')
  CHERRY_STAIRS_RECIPE = Kee[str]('cherry_stairs_recipe')
  CHERRY_TRAPDOOR_RECIPE = Kee[str]('cherry_trapdoor_recipe')
  CHERRY_WOOD_RECIPE = Kee[str]('cherry_wood_recipe')
  CHEST_MINECART_RECIPE = Kee[str]('chest_minecart_recipe')
  CHEST_RECIPE = Kee[str]('chest_recipe')
  CHISELED_BOOKSHELF_RECIPE = Kee[str]('chiseled_bookshelf_recipe')
  CHISELED_CINNABAR_FROM_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'chiseled_cinnabar_from_cinnabar_stonecutting_recipe')
  CHISELED_CINNABAR_RECIPE = Kee[str]('chiseled_cinnabar_recipe')
  CHISELED_COPPER_FROM_COPPER_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'chiseled_copper_from_copper_block_stonecutting_recipe')
  CHISELED_COPPER_FROM_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'chiseled_copper_from_cut_copper_stonecutting_recipe')
  CHISELED_COPPER_RECIPE = Kee[str]('chiseled_copper_recipe')
  CHISELED_DEEPSLATE_FROM_COBBLED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'chiseled_deepslate_from_cobbled_deepslate_stonecutting_recipe')
  CHISELED_DEEPSLATE_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'chiseled_deepslate_from_deepslate_stonecutting_recipe')
  CHISELED_DEEPSLATE_RECIPE = Kee[str]('chiseled_deepslate_recipe')
  CHISELED_NETHER_BRICKS_FROM_NETHER_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'chiseled_nether_bricks_from_nether_bricks_stonecutting_recipe')
  CHISELED_NETHER_BRICKS_RECIPE = Kee[str]('chiseled_nether_bricks_recipe')
  CHISELED_POLISHED_BLACKSTONE_FROM_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'chiseled_polished_blackstone_from_blackstone_stonecutting_recipe')
  CHISELED_POLISHED_BLACKSTONE_FROM_POLISHED_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'chiseled_polished_blackstone_from_polished_blackstone_stonecutting_recipe')
  CHISELED_POLISHED_BLACKSTONE_RECIPE = Kee[str](
    'chiseled_polished_blackstone_recipe')
  CHISELED_QUARTZ_BLOCK_FROM_QUARTZ_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'chiseled_quartz_block_from_quartz_block_stonecutting_recipe')
  CHISELED_QUARTZ_BLOCK_RECIPE = Kee[str]('chiseled_quartz_block_recipe')
  CHISELED_RED_SANDSTONE_FROM_RED_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'chiseled_red_sandstone_from_red_sandstone_stonecutting_recipe')
  CHISELED_RED_SANDSTONE_RECIPE = Kee[str]('chiseled_red_sandstone_recipe')
  CHISELED_RESIN_BRICKS_FROM_RESIN_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'chiseled_resin_bricks_from_resin_bricks_stonecutting_recipe')
  CHISELED_RESIN_BRICKS_RECIPE = Kee[str]('chiseled_resin_bricks_recipe')
  CHISELED_SANDSTONE_FROM_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'chiseled_sandstone_from_sandstone_stonecutting_recipe')
  CHISELED_SANDSTONE_RECIPE = Kee[str]('chiseled_sandstone_recipe')
  CHISELED_STONE_BRICKS_FROM_STONE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'chiseled_stone_bricks_from_stone_bricks_stonecutting_recipe')
  CHISELED_STONE_BRICKS_FROM_STONE_STONECUTTING_RECIPE = Kee[str](
    'chiseled_stone_bricks_from_stone_stonecutting_recipe')
  CHISELED_STONE_BRICKS_RECIPE = Kee[str]('chiseled_stone_bricks_recipe')
  CHISELED_SULFUR_FROM_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'chiseled_sulfur_from_sulfur_stonecutting_recipe')
  CHISELED_SULFUR_RECIPE = Kee[str]('chiseled_sulfur_recipe')
  CHISELED_TUFF_BRICKS_FROM_POLISHED_TUFF_STONECUTTING_RECIPE = Kee[str](
    'chiseled_tuff_bricks_from_polished_tuff_stonecutting_recipe')
  CHISELED_TUFF_BRICKS_FROM_TUFF_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'chiseled_tuff_bricks_from_tuff_bricks_stonecutting_recipe')
  CHISELED_TUFF_BRICKS_FROM_TUFF_STONECUTTING_RECIPE = Kee[str](
    'chiseled_tuff_bricks_from_tuff_stonecutting_recipe')
  CHISELED_TUFF_BRICKS_RECIPE = Kee[str]('chiseled_tuff_bricks_recipe')
  CHISELED_TUFF_FROM_TUFF_STONECUTTING_RECIPE = Kee[str](
    'chiseled_tuff_from_tuff_stonecutting_recipe')
  CHISELED_TUFF_RECIPE = Kee[str]('chiseled_tuff_recipe')
  CINNABAR_BRICK_SLAB_FROM_CINNABAR_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'cinnabar_brick_slab_from_cinnabar_bricks_stonecutting_recipe')
  CINNABAR_BRICK_SLAB_FROM_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'cinnabar_brick_slab_from_cinnabar_stonecutting_recipe')
  CINNABAR_BRICK_SLAB_FROM_POLISHED_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'cinnabar_brick_slab_from_polished_cinnabar_stonecutting_recipe')
  CINNABAR_BRICK_SLAB_RECIPE = Kee[str]('cinnabar_brick_slab_recipe')
  CINNABAR_BRICK_STAIRS_FROM_CINNABAR_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'cinnabar_brick_stairs_from_cinnabar_bricks_stonecutting_recipe')
  CINNABAR_BRICK_STAIRS_FROM_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'cinnabar_brick_stairs_from_cinnabar_stonecutting_recipe')
  CINNABAR_BRICK_STAIRS_FROM_POLISHED_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'cinnabar_brick_stairs_from_polished_cinnabar_stonecutting_recipe')
  CINNABAR_BRICK_STAIRS_RECIPE = Kee[str]('cinnabar_brick_stairs_recipe')
  CINNABAR_BRICK_WALL_FROM_CINNABAR_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'cinnabar_brick_wall_from_cinnabar_bricks_stonecutting_recipe')
  CINNABAR_BRICK_WALL_FROM_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'cinnabar_brick_wall_from_cinnabar_stonecutting_recipe')
  CINNABAR_BRICK_WALL_FROM_POLISHED_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'cinnabar_brick_wall_from_polished_cinnabar_stonecutting_recipe')
  CINNABAR_BRICK_WALL_RECIPE = Kee[str]('cinnabar_brick_wall_recipe')
  CINNABAR_BRICKS_FROM_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'cinnabar_bricks_from_cinnabar_stonecutting_recipe')
  CINNABAR_BRICKS_FROM_POLISHED_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'cinnabar_bricks_from_polished_cinnabar_stonecutting_recipe')
  CINNABAR_BRICKS_RECIPE = Kee[str]('cinnabar_bricks_recipe')
  CINNABAR_SLAB_FROM_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'cinnabar_slab_from_cinnabar_stonecutting_recipe')
  CINNABAR_SLAB_RECIPE = Kee[str]('cinnabar_slab_recipe')
  CINNABAR_STAIRS_FROM_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'cinnabar_stairs_from_cinnabar_stonecutting_recipe')
  CINNABAR_STAIRS_RECIPE = Kee[str]('cinnabar_stairs_recipe')
  CINNABAR_WALL_FROM_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'cinnabar_wall_from_cinnabar_stonecutting_recipe')
  CINNABAR_WALL_RECIPE = Kee[str]('cinnabar_wall_recipe')
  CLAY_RECIPE = Kee[str]('clay_recipe')
  CLOCK_RECIPE = Kee[str]('clock_recipe')
  COAL_BLOCK_RECIPE = Kee[str]('coal_block_recipe')
  COAL_FROM_BLASTING_COAL_ORE_RECIPE = Kee[str](
    'coal_from_blasting_coal_ore_recipe')
  COAL_FROM_BLASTING_DEEPSLATE_COAL_ORE_RECIPE = Kee[str](
    'coal_from_blasting_deepslate_coal_ore_recipe')
  COAL_FROM_BLASTING_RECIPE = Kee[str]('coal_from_blasting_recipe')
  COAL_FROM_SMELTING_COAL_ORE_RECIPE = Kee[str](
    'coal_from_smelting_coal_ore_recipe')
  COAL_FROM_SMELTING_DEEPSLATE_COAL_ORE_RECIPE = Kee[str](
    'coal_from_smelting_deepslate_coal_ore_recipe')
  COAL_FROM_SMELTING_RECIPE = Kee[str]('coal_from_smelting_recipe')
  COAL_RECIPE = Kee[str]('coal_recipe')
  COARSE_DIRT_RECIPE = Kee[str]('coarse_dirt_recipe')
  COAST_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'coast_armor_trim_smithing_template_recipe')
  COAST_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'coast_armor_trim_smithing_template_smithing_trim_recipe')
  COBBLED_DEEPSLATE_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'cobbled_deepslate_from_deepslate_stonecutting_recipe')
  COBBLED_DEEPSLATE_SLAB_FROM_COBBLED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'cobbled_deepslate_slab_from_cobbled_deepslate_stonecutting_recipe')
  COBBLED_DEEPSLATE_SLAB_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'cobbled_deepslate_slab_from_deepslate_stonecutting_recipe')
  COBBLED_DEEPSLATE_SLAB_RECIPE = Kee[str]('cobbled_deepslate_slab_recipe')
  COBBLED_DEEPSLATE_STAIRS_FROM_COBBLED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'cobbled_deepslate_stairs_from_cobbled_deepslate_stonecutting_recipe')
  COBBLED_DEEPSLATE_STAIRS_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'cobbled_deepslate_stairs_from_deepslate_stonecutting_recipe')
  COBBLED_DEEPSLATE_STAIRS_RECIPE = Kee[str]('cobbled_deepslate_stairs_recipe')
  COBBLED_DEEPSLATE_WALL_FROM_COBBLED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'cobbled_deepslate_wall_from_cobbled_deepslate_stonecutting_recipe')
  COBBLED_DEEPSLATE_WALL_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'cobbled_deepslate_wall_from_deepslate_stonecutting_recipe')
  COBBLED_DEEPSLATE_WALL_RECIPE = Kee[str]('cobbled_deepslate_wall_recipe')
  COBBLESTONE_FROM_STONE_STONECUTTING_RECIPE = Kee[str](
    'cobblestone_from_stone_stonecutting_recipe')
  COBBLESTONE_SLAB_FROM_COBBLESTONE_STONECUTTING_RECIPE = Kee[str](
    'cobblestone_slab_from_cobblestone_stonecutting_recipe')
  COBBLESTONE_SLAB_FROM_STONE_STONECUTTING_RECIPE = Kee[str](
    'cobblestone_slab_from_stone_stonecutting_recipe')
  COBBLESTONE_SLAB_RECIPE = Kee[str]('cobblestone_slab_recipe')
  COBBLESTONE_STAIRS_FROM_COBBLESTONE_STONECUTTING_RECIPE = Kee[str](
    'cobblestone_stairs_from_cobblestone_stonecutting_recipe')
  COBBLESTONE_STAIRS_FROM_STONE_STONECUTTING_RECIPE = Kee[str](
    'cobblestone_stairs_from_stone_stonecutting_recipe')
  COBBLESTONE_STAIRS_RECIPE = Kee[str]('cobblestone_stairs_recipe')
  COBBLESTONE_WALL_FROM_COBBLESTONE_STONECUTTING_RECIPE = Kee[str](
    'cobblestone_wall_from_cobblestone_stonecutting_recipe')
  COBBLESTONE_WALL_FROM_STONE_STONECUTTING_RECIPE = Kee[str](
    'cobblestone_wall_from_stone_stonecutting_recipe')
  COBBLESTONE_WALL_RECIPE = Kee[str]('cobblestone_wall_recipe')
  COMPARATOR_RECIPE = Kee[str]('comparator_recipe')
  COMPASS_RECIPE = Kee[str]('compass_recipe')
  COMPOSTER_RECIPE = Kee[str]('composter_recipe')
  CONDUIT_RECIPE = Kee[str]('conduit_recipe')
  COOKED_BEEF_FROM_CAMPFIRE_COOKING_RECIPE = Kee[str](
    'cooked_beef_from_campfire_cooking_recipe')
  COOKED_BEEF_FROM_SMOKING_RECIPE = Kee[str]('cooked_beef_from_smoking_recipe')
  COOKED_BEEF_RECIPE = Kee[str]('cooked_beef_recipe')
  COOKED_CHICKEN_FROM_CAMPFIRE_COOKING_RECIPE = Kee[str](
    'cooked_chicken_from_campfire_cooking_recipe')
  COOKED_CHICKEN_FROM_SMOKING_RECIPE = Kee[str](
    'cooked_chicken_from_smoking_recipe')
  COOKED_CHICKEN_RECIPE = Kee[str]('cooked_chicken_recipe')
  COOKED_COD_FROM_CAMPFIRE_COOKING_RECIPE = Kee[str](
    'cooked_cod_from_campfire_cooking_recipe')
  COOKED_COD_FROM_SMOKING_RECIPE = Kee[str]('cooked_cod_from_smoking_recipe')
  COOKED_COD_RECIPE = Kee[str]('cooked_cod_recipe')
  COOKED_MUTTON_FROM_CAMPFIRE_COOKING_RECIPE = Kee[str](
    'cooked_mutton_from_campfire_cooking_recipe')
  COOKED_MUTTON_FROM_SMOKING_RECIPE = Kee[str](
    'cooked_mutton_from_smoking_recipe')
  COOKED_MUTTON_RECIPE = Kee[str]('cooked_mutton_recipe')
  COOKED_PORKCHOP_FROM_CAMPFIRE_COOKING_RECIPE = Kee[str](
    'cooked_porkchop_from_campfire_cooking_recipe')
  COOKED_PORKCHOP_FROM_SMOKING_RECIPE = Kee[str](
    'cooked_porkchop_from_smoking_recipe')
  COOKED_PORKCHOP_RECIPE = Kee[str]('cooked_porkchop_recipe')
  COOKED_RABBIT_FROM_CAMPFIRE_COOKING_RECIPE = Kee[str](
    'cooked_rabbit_from_campfire_cooking_recipe')
  COOKED_RABBIT_FROM_SMOKING_RECIPE = Kee[str](
    'cooked_rabbit_from_smoking_recipe')
  COOKED_RABBIT_RECIPE = Kee[str]('cooked_rabbit_recipe')
  COOKED_SALMON_FROM_CAMPFIRE_COOKING_RECIPE = Kee[str](
    'cooked_salmon_from_campfire_cooking_recipe')
  COOKED_SALMON_FROM_SMOKING_RECIPE = Kee[str](
    'cooked_salmon_from_smoking_recipe')
  COOKED_SALMON_RECIPE = Kee[str]('cooked_salmon_recipe')
  COOKIE_RECIPE = Kee[str]('cookie_recipe')
  COPPER_AXE_RECIPE = Kee[str]('copper_axe_recipe')
  COPPER_BARS_RECIPE = Kee[str]('copper_bars_recipe')
  COPPER_BLOCK_RECIPE = Kee[str]('copper_block_recipe')
  COPPER_BOOTS_RECIPE = Kee[str]('copper_boots_recipe')
  COPPER_BULB_RECIPE = Kee[str]('copper_bulb_recipe')
  COPPER_CHAIN_RECIPE = Kee[str]('copper_chain_recipe')
  COPPER_CHEST_RECIPE = Kee[str]('copper_chest_recipe')
  COPPER_CHESTPLATE_RECIPE = Kee[str]('copper_chestplate_recipe')
  COPPER_DOOR_RECIPE = Kee[str]('copper_door_recipe')
  COPPER_GRATE_FROM_COPPER_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'copper_grate_from_copper_block_stonecutting_recipe')
  COPPER_GRATE_RECIPE = Kee[str]('copper_grate_recipe')
  COPPER_HELMET_RECIPE = Kee[str]('copper_helmet_recipe')
  COPPER_HOE_RECIPE = Kee[str]('copper_hoe_recipe')
  COPPER_INGOT_FROM_BLASTING_COPPER_ORE_RECIPE = Kee[str](
    'copper_ingot_from_blasting_copper_ore_recipe')
  COPPER_INGOT_FROM_BLASTING_DEEPSLATE_COPPER_ORE_RECIPE = Kee[str](
    'copper_ingot_from_blasting_deepslate_copper_ore_recipe')
  COPPER_INGOT_FROM_BLASTING_RAW_COPPER_RECIPE = Kee[str](
    'copper_ingot_from_blasting_raw_copper_recipe')
  COPPER_INGOT_FROM_NUGGETS_RECIPE = Kee[str](
    'copper_ingot_from_nuggets_recipe')
  COPPER_INGOT_FROM_SMELTING_COPPER_ORE_RECIPE = Kee[str](
    'copper_ingot_from_smelting_copper_ore_recipe')
  COPPER_INGOT_FROM_SMELTING_DEEPSLATE_COPPER_ORE_RECIPE = Kee[str](
    'copper_ingot_from_smelting_deepslate_copper_ore_recipe')
  COPPER_INGOT_FROM_SMELTING_RAW_COPPER_RECIPE = Kee[str](
    'copper_ingot_from_smelting_raw_copper_recipe')
  COPPER_INGOT_FROM_WAXED_COPPER_BLOCK_RECIPE = Kee[str](
    'copper_ingot_from_waxed_copper_block_recipe')
  COPPER_INGOT_RECIPE = Kee[str]('copper_ingot_recipe')
  COPPER_LANTERN_RECIPE = Kee[str]('copper_lantern_recipe')
  COPPER_LEGGINGS_RECIPE = Kee[str]('copper_leggings_recipe')
  COPPER_NUGGET_FROM_BLASTING_RECIPE = Kee[str](
    'copper_nugget_from_blasting_recipe')
  COPPER_NUGGET_FROM_SMELTING_RECIPE = Kee[str](
    'copper_nugget_from_smelting_recipe')
  COPPER_NUGGET_RECIPE = Kee[str]('copper_nugget_recipe')
  COPPER_PICKAXE_RECIPE = Kee[str]('copper_pickaxe_recipe')
  COPPER_SHOVEL_RECIPE = Kee[str]('copper_shovel_recipe')
  COPPER_SPEAR_RECIPE = Kee[str]('copper_spear_recipe')
  COPPER_SWORD_RECIPE = Kee[str]('copper_sword_recipe')
  COPPER_TORCH_RECIPE = Kee[str]('copper_torch_recipe')
  COPPER_TRAPDOOR_RECIPE = Kee[str]('copper_trapdoor_recipe')
  COUNTRY_LODE_TAKE_ME_HOME = Kee[str]('country_lode_take_me_home')
  COVER_ME_IN_DEBRIS = Kee[str]('cover_me_in_debris')
  COVER_ME_WITH_DIAMONDS = Kee[str]('cover_me_with_diamonds')
  CRACKED_DEEPSLATE_BRICKS_RECIPE = Kee[str]('cracked_deepslate_bricks_recipe')
  CRACKED_DEEPSLATE_TILES_RECIPE = Kee[str]('cracked_deepslate_tiles_recipe')
  CRACKED_NETHER_BRICKS_RECIPE = Kee[str]('cracked_nether_bricks_recipe')
  CRACKED_POLISHED_BLACKSTONE_BRICKS_RECIPE = Kee[str](
    'cracked_polished_blackstone_bricks_recipe')
  CRACKED_STONE_BRICKS_RECIPE = Kee[str]('cracked_stone_bricks_recipe')
  CRAFTER_RECIPE = Kee[str]('crafter_recipe')
  CRAFTERS_CRAFTING_CRAFTERS = Kee[str]('crafters_crafting_crafters')
  CRAFTING_A_NEW_LOOK = Kee[str]('crafting_a_new_look')
  CRAFTING_TABLE_RECIPE = Kee[str]('crafting_table_recipe')
  CREAKING_HEART_RECIPE = Kee[str]('creaking_heart_recipe')
  CREEPER_BANNER_PATTERN_RECIPE = Kee[str]('creeper_banner_pattern_recipe')
  CRIMSON_BUTTON_RECIPE = Kee[str]('crimson_button_recipe')
  CRIMSON_DOOR_RECIPE = Kee[str]('crimson_door_recipe')
  CRIMSON_FENCE_GATE_RECIPE = Kee[str]('crimson_fence_gate_recipe')
  CRIMSON_FENCE_RECIPE = Kee[str]('crimson_fence_recipe')
  CRIMSON_HANGING_SIGN_RECIPE = Kee[str]('crimson_hanging_sign_recipe')
  CRIMSON_HYPHAE_RECIPE = Kee[str]('crimson_hyphae_recipe')
  CRIMSON_PLANKS_RECIPE = Kee[str]('crimson_planks_recipe')
  CRIMSON_PRESSURE_PLATE_RECIPE = Kee[str]('crimson_pressure_plate_recipe')
  CRIMSON_SHELF_RECIPE = Kee[str]('crimson_shelf_recipe')
  CRIMSON_SIGN_RECIPE = Kee[str]('crimson_sign_recipe')
  CRIMSON_SLAB_RECIPE = Kee[str]('crimson_slab_recipe')
  CRIMSON_STAIRS_RECIPE = Kee[str]('crimson_stairs_recipe')
  CRIMSON_TRAPDOOR_RECIPE = Kee[str]('crimson_trapdoor_recipe')
  CROSSBOW_RECIPE = Kee[str]('crossbow_recipe')
  CUT_COPPER_FROM_COPPER_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'cut_copper_from_copper_block_stonecutting_recipe')
  CUT_COPPER_RECIPE = Kee[str]('cut_copper_recipe')
  CUT_COPPER_SLAB_FROM_COPPER_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'cut_copper_slab_from_copper_block_stonecutting_recipe')
  CUT_COPPER_SLAB_FROM_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'cut_copper_slab_from_cut_copper_stonecutting_recipe')
  CUT_COPPER_SLAB_RECIPE = Kee[str]('cut_copper_slab_recipe')
  CUT_COPPER_STAIRS_FROM_COPPER_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'cut_copper_stairs_from_copper_block_stonecutting_recipe')
  CUT_COPPER_STAIRS_FROM_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'cut_copper_stairs_from_cut_copper_stonecutting_recipe')
  CUT_COPPER_STAIRS_RECIPE = Kee[str]('cut_copper_stairs_recipe')
  CUT_RED_SANDSTONE_FROM_RED_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'cut_red_sandstone_from_red_sandstone_stonecutting_recipe')
  CUT_RED_SANDSTONE_RECIPE = Kee[str]('cut_red_sandstone_recipe')
  CUT_RED_SANDSTONE_SLAB_FROM_CUT_RED_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'cut_red_sandstone_slab_from_cut_red_sandstone_stonecutting_recipe')
  CUT_RED_SANDSTONE_SLAB_FROM_RED_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'cut_red_sandstone_slab_from_red_sandstone_stonecutting_recipe')
  CUT_RED_SANDSTONE_SLAB_RECIPE = Kee[str]('cut_red_sandstone_slab_recipe')
  CUT_SANDSTONE_FROM_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'cut_sandstone_from_sandstone_stonecutting_recipe')
  CUT_SANDSTONE_RECIPE = Kee[str]('cut_sandstone_recipe')
  CUT_SANDSTONE_SLAB_FROM_CUT_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'cut_sandstone_slab_from_cut_sandstone_stonecutting_recipe')
  CUT_SANDSTONE_SLAB_FROM_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'cut_sandstone_slab_from_sandstone_stonecutting_recipe')
  CUT_SANDSTONE_SLAB_RECIPE = Kee[str]('cut_sandstone_slab_recipe')
  CYAN_BANNER_RECIPE = Kee[str]('cyan_banner_recipe')
  CYAN_BED_FROM_WHITE_BED_RECIPE = Kee[str]('cyan_bed_from_white_bed_recipe')
  CYAN_BED_RECIPE = Kee[str]('cyan_bed_recipe')
  CYAN_BUNDLE_RECIPE = Kee[str]('cyan_bundle_recipe')
  CYAN_CANDLE_RECIPE = Kee[str]('cyan_candle_recipe')
  CYAN_CARPET_FROM_WHITE_CARPET_RECIPE = Kee[str](
    'cyan_carpet_from_white_carpet_recipe')
  CYAN_CARPET_RECIPE = Kee[str]('cyan_carpet_recipe')
  CYAN_CONCRETE_POWDER_RECIPE = Kee[str]('cyan_concrete_powder_recipe')
  CYAN_CONCRETE_SLAB_FROM_CYAN_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'cyan_concrete_slab_from_cyan_concrete_stonecutting_recipe')
  CYAN_CONCRETE_SLAB_RECIPE = Kee[str]('cyan_concrete_slab_recipe')
  CYAN_CONCRETE_STAIRS_FROM_CYAN_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'cyan_concrete_stairs_from_cyan_concrete_stonecutting_recipe')
  CYAN_CONCRETE_STAIRS_RECIPE = Kee[str]('cyan_concrete_stairs_recipe')
  CYAN_CUSHION_RECIPE = Kee[str]('cyan_cushion_recipe')
  CYAN_DYE_FROM_PITCHER_PLANT_RECIPE = Kee[str](
    'cyan_dye_from_pitcher_plant_recipe')
  CYAN_DYE_RECIPE = Kee[str]('cyan_dye_recipe')
  CYAN_GLAZED_TERRACOTTA_RECIPE = Kee[str]('cyan_glazed_terracotta_recipe')
  CYAN_HARNESS_RECIPE = Kee[str]('cyan_harness_recipe')
  CYAN_SHULKER_BOX_RECIPE = Kee[str]('cyan_shulker_box_recipe')
  CYAN_STAINED_GLASS_PANE_FROM_GLASS_PANE_RECIPE = Kee[str](
    'cyan_stained_glass_pane_from_glass_pane_recipe')
  CYAN_STAINED_GLASS_PANE_RECIPE = Kee[str]('cyan_stained_glass_pane_recipe')
  CYAN_STAINED_GLASS_RECIPE = Kee[str]('cyan_stained_glass_recipe')
  CYAN_TERRACOTTA_RECIPE = Kee[str]('cyan_terracotta_recipe')
  CYAN_WOOL_RECIPE = Kee[str]('cyan_wool_recipe')
  CYAN_WOOL_SLAB_RECIPE = Kee[str]('cyan_wool_slab_recipe')
  CYAN_WOOL_STAIRS_RECIPE = Kee[str]('cyan_wool_stairs_recipe')
  DARK_OAK_BOAT_RECIPE = Kee[str]('dark_oak_boat_recipe')
  DARK_OAK_BUTTON_RECIPE = Kee[str]('dark_oak_button_recipe')
  DARK_OAK_CHEST_BOAT_RECIPE = Kee[str]('dark_oak_chest_boat_recipe')
  DARK_OAK_DOOR_RECIPE = Kee[str]('dark_oak_door_recipe')
  DARK_OAK_FENCE_GATE_RECIPE = Kee[str]('dark_oak_fence_gate_recipe')
  DARK_OAK_FENCE_RECIPE = Kee[str]('dark_oak_fence_recipe')
  DARK_OAK_HANGING_SIGN_RECIPE = Kee[str]('dark_oak_hanging_sign_recipe')
  DARK_OAK_PLANKS_RECIPE = Kee[str]('dark_oak_planks_recipe')
  DARK_OAK_PRESSURE_PLATE_RECIPE = Kee[str]('dark_oak_pressure_plate_recipe')
  DARK_OAK_SHELF_RECIPE = Kee[str]('dark_oak_shelf_recipe')
  DARK_OAK_SIGN_RECIPE = Kee[str]('dark_oak_sign_recipe')
  DARK_OAK_SLAB_RECIPE = Kee[str]('dark_oak_slab_recipe')
  DARK_OAK_STAIRS_RECIPE = Kee[str]('dark_oak_stairs_recipe')
  DARK_OAK_TRAPDOOR_RECIPE = Kee[str]('dark_oak_trapdoor_recipe')
  DARK_OAK_WOOD_RECIPE = Kee[str]('dark_oak_wood_recipe')
  DARK_PRISMARINE_RECIPE = Kee[str]('dark_prismarine_recipe')
  DARK_PRISMARINE_SLAB_FROM_DARK_PRISMARINE_STONECUTTING_RECIPE = Kee[str](
    'dark_prismarine_slab_from_dark_prismarine_stonecutting_recipe')
  DARK_PRISMARINE_SLAB_RECIPE = Kee[str]('dark_prismarine_slab_recipe')
  DARK_PRISMARINE_STAIRS_FROM_DARK_PRISMARINE_STONECUTTING_RECIPE = Kee[str](
    'dark_prismarine_stairs_from_dark_prismarine_stonecutting_recipe')
  DARK_PRISMARINE_STAIRS_RECIPE = Kee[str]('dark_prismarine_stairs_recipe')
  DAYLIGHT_DETECTOR_RECIPE = Kee[str]('daylight_detector_recipe')
  DECORATED_POT_SIMPLE_RECIPE = Kee[str]('decorated_pot_simple_recipe')
  DEEPSLATE_BRICK_SLAB_FROM_COBBLED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_brick_slab_from_cobbled_deepslate_stonecutting_recipe')
  DEEPSLATE_BRICK_SLAB_FROM_DEEPSLATE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'deepslate_brick_slab_from_deepslate_bricks_stonecutting_recipe')
  DEEPSLATE_BRICK_SLAB_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_brick_slab_from_deepslate_stonecutting_recipe')
  DEEPSLATE_BRICK_SLAB_FROM_POLISHED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_brick_slab_from_polished_deepslate_stonecutting_recipe')
  DEEPSLATE_BRICK_SLAB_RECIPE = Kee[str]('deepslate_brick_slab_recipe')
  DEEPSLATE_BRICK_STAIRS_FROM_COBBLED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_brick_stairs_from_cobbled_deepslate_stonecutting_recipe')
  DEEPSLATE_BRICK_STAIRS_FROM_DEEPSLATE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'deepslate_brick_stairs_from_deepslate_bricks_stonecutting_recipe')
  DEEPSLATE_BRICK_STAIRS_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_brick_stairs_from_deepslate_stonecutting_recipe')
  DEEPSLATE_BRICK_STAIRS_FROM_POLISHED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_brick_stairs_from_polished_deepslate_stonecutting_recipe')
  DEEPSLATE_BRICK_STAIRS_RECIPE = Kee[str]('deepslate_brick_stairs_recipe')
  DEEPSLATE_BRICK_WALL_FROM_COBBLED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_brick_wall_from_cobbled_deepslate_stonecutting_recipe')
  DEEPSLATE_BRICK_WALL_FROM_DEEPSLATE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'deepslate_brick_wall_from_deepslate_bricks_stonecutting_recipe')
  DEEPSLATE_BRICK_WALL_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_brick_wall_from_deepslate_stonecutting_recipe')
  DEEPSLATE_BRICK_WALL_FROM_POLISHED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_brick_wall_from_polished_deepslate_stonecutting_recipe')
  DEEPSLATE_BRICK_WALL_RECIPE = Kee[str]('deepslate_brick_wall_recipe')
  DEEPSLATE_BRICKS_FROM_COBBLED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_bricks_from_cobbled_deepslate_stonecutting_recipe')
  DEEPSLATE_BRICKS_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_bricks_from_deepslate_stonecutting_recipe')
  DEEPSLATE_BRICKS_FROM_POLISHED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_bricks_from_polished_deepslate_stonecutting_recipe')
  DEEPSLATE_BRICKS_RECIPE = Kee[str]('deepslate_bricks_recipe')
  DEEPSLATE_RECIPE = Kee[str]('deepslate_recipe')
  DEEPSLATE_TILE_SLAB_FROM_COBBLED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tile_slab_from_cobbled_deepslate_stonecutting_recipe')
  DEEPSLATE_TILE_SLAB_FROM_DEEPSLATE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tile_slab_from_deepslate_bricks_stonecutting_recipe')
  DEEPSLATE_TILE_SLAB_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tile_slab_from_deepslate_stonecutting_recipe')
  DEEPSLATE_TILE_SLAB_FROM_DEEPSLATE_TILES_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tile_slab_from_deepslate_tiles_stonecutting_recipe')
  DEEPSLATE_TILE_SLAB_FROM_POLISHED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tile_slab_from_polished_deepslate_stonecutting_recipe')
  DEEPSLATE_TILE_SLAB_RECIPE = Kee[str]('deepslate_tile_slab_recipe')
  DEEPSLATE_TILE_STAIRS_FROM_COBBLED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tile_stairs_from_cobbled_deepslate_stonecutting_recipe')
  DEEPSLATE_TILE_STAIRS_FROM_DEEPSLATE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tile_stairs_from_deepslate_bricks_stonecutting_recipe')
  DEEPSLATE_TILE_STAIRS_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tile_stairs_from_deepslate_stonecutting_recipe')
  DEEPSLATE_TILE_STAIRS_FROM_DEEPSLATE_TILES_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tile_stairs_from_deepslate_tiles_stonecutting_recipe')
  DEEPSLATE_TILE_STAIRS_FROM_POLISHED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tile_stairs_from_polished_deepslate_stonecutting_recipe')
  DEEPSLATE_TILE_STAIRS_RECIPE = Kee[str]('deepslate_tile_stairs_recipe')
  DEEPSLATE_TILE_WALL_FROM_COBBLED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tile_wall_from_cobbled_deepslate_stonecutting_recipe')
  DEEPSLATE_TILE_WALL_FROM_DEEPSLATE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tile_wall_from_deepslate_bricks_stonecutting_recipe')
  DEEPSLATE_TILE_WALL_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tile_wall_from_deepslate_stonecutting_recipe')
  DEEPSLATE_TILE_WALL_FROM_DEEPSLATE_TILES_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tile_wall_from_deepslate_tiles_stonecutting_recipe')
  DEEPSLATE_TILE_WALL_FROM_POLISHED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tile_wall_from_polished_deepslate_stonecutting_recipe')
  DEEPSLATE_TILE_WALL_RECIPE = Kee[str]('deepslate_tile_wall_recipe')
  DEEPSLATE_TILES_FROM_COBBLED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tiles_from_cobbled_deepslate_stonecutting_recipe')
  DEEPSLATE_TILES_FROM_DEEPSLATE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tiles_from_deepslate_bricks_stonecutting_recipe')
  DEEPSLATE_TILES_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tiles_from_deepslate_stonecutting_recipe')
  DEEPSLATE_TILES_FROM_POLISHED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'deepslate_tiles_from_polished_deepslate_stonecutting_recipe')
  DEEPSLATE_TILES_RECIPE = Kee[str]('deepslate_tiles_recipe')
  DETECTOR_RAIL_RECIPE = Kee[str]('detector_rail_recipe')
  DIAMOND_AXE_RECIPE = Kee[str]('diamond_axe_recipe')
  DIAMOND_BLOCK_RECIPE = Kee[str]('diamond_block_recipe')
  DIAMOND_BOOTS_RECIPE = Kee[str]('diamond_boots_recipe')
  DIAMOND_CHESTPLATE_RECIPE = Kee[str]('diamond_chestplate_recipe')
  DIAMOND_FROM_BLASTING_DEEPSLATE_DIAMOND_ORE_RECIPE = Kee[str](
    'diamond_from_blasting_deepslate_diamond_ore_recipe')
  DIAMOND_FROM_BLASTING_DIAMOND_ORE_RECIPE = Kee[str](
    'diamond_from_blasting_diamond_ore_recipe')
  DIAMOND_FROM_BLASTING_RECIPE = Kee[str]('diamond_from_blasting_recipe')
  DIAMOND_FROM_SMELTING_DEEPSLATE_DIAMOND_ORE_RECIPE = Kee[str](
    'diamond_from_smelting_deepslate_diamond_ore_recipe')
  DIAMOND_FROM_SMELTING_DIAMOND_ORE_RECIPE = Kee[str](
    'diamond_from_smelting_diamond_ore_recipe')
  DIAMOND_FROM_SMELTING_RECIPE = Kee[str]('diamond_from_smelting_recipe')
  DIAMOND_HELMET_RECIPE = Kee[str]('diamond_helmet_recipe')
  DIAMOND_HOE_RECIPE = Kee[str]('diamond_hoe_recipe')
  DIAMOND_LEGGINGS_RECIPE = Kee[str]('diamond_leggings_recipe')
  DIAMOND_PICKAXE_RECIPE = Kee[str]('diamond_pickaxe_recipe')
  DIAMOND_RECIPE = Kee[str]('diamond_recipe')
  DIAMOND_SHOVEL_RECIPE = Kee[str]('diamond_shovel_recipe')
  DIAMOND_SPEAR_RECIPE = Kee[str]('diamond_spear_recipe')
  DIAMOND_SWORD_RECIPE = Kee[str]('diamond_sword_recipe')
  DIAMONDS = Kee[str]('diamonds')
  DIORITE_RECIPE = Kee[str]('diorite_recipe')
  DIORITE_SLAB_FROM_DIORITE_STONECUTTING_RECIPE = Kee[str](
    'diorite_slab_from_diorite_stonecutting_recipe')
  DIORITE_SLAB_RECIPE = Kee[str]('diorite_slab_recipe')
  DIORITE_STAIRS_FROM_DIORITE_STONECUTTING_RECIPE = Kee[str](
    'diorite_stairs_from_diorite_stonecutting_recipe')
  DIORITE_STAIRS_RECIPE = Kee[str]('diorite_stairs_recipe')
  DIORITE_WALL_FROM_DIORITE_STONECUTTING_RECIPE = Kee[str](
    'diorite_wall_from_diorite_stonecutting_recipe')
  DIORITE_WALL_RECIPE = Kee[str]('diorite_wall_recipe')
  DISPENSER_RECIPE = Kee[str]('dispenser_recipe')
  DRIED_GHAST_RECIPE = Kee[str]('dried_ghast_recipe')
  DRIED_KELP_BLOCK_RECIPE = Kee[str]('dried_kelp_block_recipe')
  DRIED_KELP_FROM_CAMPFIRE_COOKING_RECIPE = Kee[str](
    'dried_kelp_from_campfire_cooking_recipe')
  DRIED_KELP_FROM_SMELTING_RECIPE = Kee[str]('dried_kelp_from_smelting_recipe')
  DRIED_KELP_FROM_SMOKING_RECIPE = Kee[str]('dried_kelp_from_smoking_recipe')
  DRIED_KELP_RECIPE = Kee[str]('dried_kelp_recipe')
  DRIPSTONE_BLOCK_RECIPE = Kee[str]('dripstone_block_recipe')
  DROPPER_RECIPE = Kee[str]('dropper_recipe')
  DUNE_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'dune_armor_trim_smithing_template_recipe')
  DUNE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'dune_armor_trim_smithing_template_smithing_trim_recipe')
  DYE_BLACK_BED_RECIPE = Kee[str]('dye_black_bed_recipe')
  DYE_BLACK_CARPET_RECIPE = Kee[str]('dye_black_carpet_recipe')
  DYE_BLACK_CUSHION_RECIPE = Kee[str]('dye_black_cushion_recipe')
  DYE_BLACK_HARNESS_RECIPE = Kee[str]('dye_black_harness_recipe')
  DYE_BLACK_WOOL_RECIPE = Kee[str]('dye_black_wool_recipe')
  DYE_BLACK_WOOL_SLAB_RECIPE = Kee[str]('dye_black_wool_slab_recipe')
  DYE_BLACK_WOOL_STAIRS_RECIPE = Kee[str]('dye_black_wool_stairs_recipe')
  DYE_BLUE_BED_RECIPE = Kee[str]('dye_blue_bed_recipe')
  DYE_BLUE_CARPET_RECIPE = Kee[str]('dye_blue_carpet_recipe')
  DYE_BLUE_CUSHION_RECIPE = Kee[str]('dye_blue_cushion_recipe')
  DYE_BLUE_HARNESS_RECIPE = Kee[str]('dye_blue_harness_recipe')
  DYE_BLUE_WOOL_RECIPE = Kee[str]('dye_blue_wool_recipe')
  DYE_BLUE_WOOL_SLAB_RECIPE = Kee[str]('dye_blue_wool_slab_recipe')
  DYE_BLUE_WOOL_STAIRS_RECIPE = Kee[str]('dye_blue_wool_stairs_recipe')
  DYE_BROWN_BED_RECIPE = Kee[str]('dye_brown_bed_recipe')
  DYE_BROWN_CARPET_RECIPE = Kee[str]('dye_brown_carpet_recipe')
  DYE_BROWN_CUSHION_RECIPE = Kee[str]('dye_brown_cushion_recipe')
  DYE_BROWN_HARNESS_RECIPE = Kee[str]('dye_brown_harness_recipe')
  DYE_BROWN_WOOL_RECIPE = Kee[str]('dye_brown_wool_recipe')
  DYE_BROWN_WOOL_SLAB_RECIPE = Kee[str]('dye_brown_wool_slab_recipe')
  DYE_BROWN_WOOL_STAIRS_RECIPE = Kee[str]('dye_brown_wool_stairs_recipe')
  DYE_CYAN_BED_RECIPE = Kee[str]('dye_cyan_bed_recipe')
  DYE_CYAN_CARPET_RECIPE = Kee[str]('dye_cyan_carpet_recipe')
  DYE_CYAN_CUSHION_RECIPE = Kee[str]('dye_cyan_cushion_recipe')
  DYE_CYAN_HARNESS_RECIPE = Kee[str]('dye_cyan_harness_recipe')
  DYE_CYAN_WOOL_RECIPE = Kee[str]('dye_cyan_wool_recipe')
  DYE_CYAN_WOOL_SLAB_RECIPE = Kee[str]('dye_cyan_wool_slab_recipe')
  DYE_CYAN_WOOL_STAIRS_RECIPE = Kee[str]('dye_cyan_wool_stairs_recipe')
  DYE_GRAY_BED_RECIPE = Kee[str]('dye_gray_bed_recipe')
  DYE_GRAY_CARPET_RECIPE = Kee[str]('dye_gray_carpet_recipe')
  DYE_GRAY_CUSHION_RECIPE = Kee[str]('dye_gray_cushion_recipe')
  DYE_GRAY_HARNESS_RECIPE = Kee[str]('dye_gray_harness_recipe')
  DYE_GRAY_WOOL_RECIPE = Kee[str]('dye_gray_wool_recipe')
  DYE_GRAY_WOOL_SLAB_RECIPE = Kee[str]('dye_gray_wool_slab_recipe')
  DYE_GRAY_WOOL_STAIRS_RECIPE = Kee[str]('dye_gray_wool_stairs_recipe')
  DYE_GREEN_BED_RECIPE = Kee[str]('dye_green_bed_recipe')
  DYE_GREEN_CARPET_RECIPE = Kee[str]('dye_green_carpet_recipe')
  DYE_GREEN_CUSHION_RECIPE = Kee[str]('dye_green_cushion_recipe')
  DYE_GREEN_HARNESS_RECIPE = Kee[str]('dye_green_harness_recipe')
  DYE_GREEN_WOOL_RECIPE = Kee[str]('dye_green_wool_recipe')
  DYE_GREEN_WOOL_SLAB_RECIPE = Kee[str]('dye_green_wool_slab_recipe')
  DYE_GREEN_WOOL_STAIRS_RECIPE = Kee[str]('dye_green_wool_stairs_recipe')
  DYE_LIGHT_BLUE_BED_RECIPE = Kee[str]('dye_light_blue_bed_recipe')
  DYE_LIGHT_BLUE_CARPET_RECIPE = Kee[str]('dye_light_blue_carpet_recipe')
  DYE_LIGHT_BLUE_CUSHION_RECIPE = Kee[str]('dye_light_blue_cushion_recipe')
  DYE_LIGHT_BLUE_HARNESS_RECIPE = Kee[str]('dye_light_blue_harness_recipe')
  DYE_LIGHT_BLUE_WOOL_RECIPE = Kee[str]('dye_light_blue_wool_recipe')
  DYE_LIGHT_BLUE_WOOL_SLAB_RECIPE = Kee[str]('dye_light_blue_wool_slab_recipe')
  DYE_LIGHT_BLUE_WOOL_STAIRS_RECIPE = Kee[str](
    'dye_light_blue_wool_stairs_recipe')
  DYE_LIGHT_GRAY_BED_RECIPE = Kee[str]('dye_light_gray_bed_recipe')
  DYE_LIGHT_GRAY_CARPET_RECIPE = Kee[str]('dye_light_gray_carpet_recipe')
  DYE_LIGHT_GRAY_CUSHION_RECIPE = Kee[str]('dye_light_gray_cushion_recipe')
  DYE_LIGHT_GRAY_HARNESS_RECIPE = Kee[str]('dye_light_gray_harness_recipe')
  DYE_LIGHT_GRAY_WOOL_RECIPE = Kee[str]('dye_light_gray_wool_recipe')
  DYE_LIGHT_GRAY_WOOL_SLAB_RECIPE = Kee[str]('dye_light_gray_wool_slab_recipe')
  DYE_LIGHT_GRAY_WOOL_STAIRS_RECIPE = Kee[str](
    'dye_light_gray_wool_stairs_recipe')
  DYE_LIME_BED_RECIPE = Kee[str]('dye_lime_bed_recipe')
  DYE_LIME_CARPET_RECIPE = Kee[str]('dye_lime_carpet_recipe')
  DYE_LIME_CUSHION_RECIPE = Kee[str]('dye_lime_cushion_recipe')
  DYE_LIME_HARNESS_RECIPE = Kee[str]('dye_lime_harness_recipe')
  DYE_LIME_WOOL_RECIPE = Kee[str]('dye_lime_wool_recipe')
  DYE_LIME_WOOL_SLAB_RECIPE = Kee[str]('dye_lime_wool_slab_recipe')
  DYE_LIME_WOOL_STAIRS_RECIPE = Kee[str]('dye_lime_wool_stairs_recipe')
  DYE_MAGENTA_BED_RECIPE = Kee[str]('dye_magenta_bed_recipe')
  DYE_MAGENTA_CARPET_RECIPE = Kee[str]('dye_magenta_carpet_recipe')
  DYE_MAGENTA_CUSHION_RECIPE = Kee[str]('dye_magenta_cushion_recipe')
  DYE_MAGENTA_HARNESS_RECIPE = Kee[str]('dye_magenta_harness_recipe')
  DYE_MAGENTA_WOOL_RECIPE = Kee[str]('dye_magenta_wool_recipe')
  DYE_MAGENTA_WOOL_SLAB_RECIPE = Kee[str]('dye_magenta_wool_slab_recipe')
  DYE_MAGENTA_WOOL_STAIRS_RECIPE = Kee[str]('dye_magenta_wool_stairs_recipe')
  DYE_ORANGE_BED_RECIPE = Kee[str]('dye_orange_bed_recipe')
  DYE_ORANGE_CARPET_RECIPE = Kee[str]('dye_orange_carpet_recipe')
  DYE_ORANGE_CUSHION_RECIPE = Kee[str]('dye_orange_cushion_recipe')
  DYE_ORANGE_HARNESS_RECIPE = Kee[str]('dye_orange_harness_recipe')
  DYE_ORANGE_WOOL_RECIPE = Kee[str]('dye_orange_wool_recipe')
  DYE_ORANGE_WOOL_SLAB_RECIPE = Kee[str]('dye_orange_wool_slab_recipe')
  DYE_ORANGE_WOOL_STAIRS_RECIPE = Kee[str]('dye_orange_wool_stairs_recipe')
  DYE_PINK_BED_RECIPE = Kee[str]('dye_pink_bed_recipe')
  DYE_PINK_CARPET_RECIPE = Kee[str]('dye_pink_carpet_recipe')
  DYE_PINK_CUSHION_RECIPE = Kee[str]('dye_pink_cushion_recipe')
  DYE_PINK_HARNESS_RECIPE = Kee[str]('dye_pink_harness_recipe')
  DYE_PINK_WOOL_RECIPE = Kee[str]('dye_pink_wool_recipe')
  DYE_PINK_WOOL_SLAB_RECIPE = Kee[str]('dye_pink_wool_slab_recipe')
  DYE_PINK_WOOL_STAIRS_RECIPE = Kee[str]('dye_pink_wool_stairs_recipe')
  DYE_PURPLE_BED_RECIPE = Kee[str]('dye_purple_bed_recipe')
  DYE_PURPLE_CARPET_RECIPE = Kee[str]('dye_purple_carpet_recipe')
  DYE_PURPLE_CUSHION_RECIPE = Kee[str]('dye_purple_cushion_recipe')
  DYE_PURPLE_HARNESS_RECIPE = Kee[str]('dye_purple_harness_recipe')
  DYE_PURPLE_WOOL_RECIPE = Kee[str]('dye_purple_wool_recipe')
  DYE_PURPLE_WOOL_SLAB_RECIPE = Kee[str]('dye_purple_wool_slab_recipe')
  DYE_PURPLE_WOOL_STAIRS_RECIPE = Kee[str]('dye_purple_wool_stairs_recipe')
  DYE_RED_BED_RECIPE = Kee[str]('dye_red_bed_recipe')
  DYE_RED_CARPET_RECIPE = Kee[str]('dye_red_carpet_recipe')
  DYE_RED_CUSHION_RECIPE = Kee[str]('dye_red_cushion_recipe')
  DYE_RED_HARNESS_RECIPE = Kee[str]('dye_red_harness_recipe')
  DYE_RED_WOOL_RECIPE = Kee[str]('dye_red_wool_recipe')
  DYE_RED_WOOL_SLAB_RECIPE = Kee[str]('dye_red_wool_slab_recipe')
  DYE_RED_WOOL_STAIRS_RECIPE = Kee[str]('dye_red_wool_stairs_recipe')
  DYE_WHITE_BED_RECIPE = Kee[str]('dye_white_bed_recipe')
  DYE_WHITE_CARPET_RECIPE = Kee[str]('dye_white_carpet_recipe')
  DYE_WHITE_CUSHION_RECIPE = Kee[str]('dye_white_cushion_recipe')
  DYE_WHITE_HARNESS_RECIPE = Kee[str]('dye_white_harness_recipe')
  DYE_WHITE_WOOL_RECIPE = Kee[str]('dye_white_wool_recipe')
  DYE_WHITE_WOOL_SLAB_RECIPE = Kee[str]('dye_white_wool_slab_recipe')
  DYE_WHITE_WOOL_STAIRS_RECIPE = Kee[str]('dye_white_wool_stairs_recipe')
  DYE_YELLOW_BED_RECIPE = Kee[str]('dye_yellow_bed_recipe')
  DYE_YELLOW_CARPET_RECIPE = Kee[str]('dye_yellow_carpet_recipe')
  DYE_YELLOW_CUSHION_RECIPE = Kee[str]('dye_yellow_cushion_recipe')
  DYE_YELLOW_HARNESS_RECIPE = Kee[str]('dye_yellow_harness_recipe')
  DYE_YELLOW_WOOL_RECIPE = Kee[str]('dye_yellow_wool_recipe')
  DYE_YELLOW_WOOL_SLAB_RECIPE = Kee[str]('dye_yellow_wool_slab_recipe')
  DYE_YELLOW_WOOL_STAIRS_RECIPE = Kee[str]('dye_yellow_wool_stairs_recipe')
  EMERALD_BLOCK_RECIPE = Kee[str]('emerald_block_recipe')
  EMERALD_FROM_BLASTING_DEEPSLATE_EMERALD_ORE_RECIPE = Kee[str](
    'emerald_from_blasting_deepslate_emerald_ore_recipe')
  EMERALD_FROM_BLASTING_EMERALD_ORE_RECIPE = Kee[str](
    'emerald_from_blasting_emerald_ore_recipe')
  EMERALD_FROM_BLASTING_RECIPE = Kee[str]('emerald_from_blasting_recipe')
  EMERALD_FROM_SMELTING_DEEPSLATE_EMERALD_ORE_RECIPE = Kee[str](
    'emerald_from_smelting_deepslate_emerald_ore_recipe')
  EMERALD_FROM_SMELTING_EMERALD_ORE_RECIPE = Kee[str](
    'emerald_from_smelting_emerald_ore_recipe')
  EMERALD_FROM_SMELTING_RECIPE = Kee[str]('emerald_from_smelting_recipe')
  EMERALD_RECIPE = Kee[str]('emerald_recipe')
  ENCHANTER = Kee[str]('enchanter')
  ENCHANTING_TABLE_RECIPE = Kee[str]('enchanting_table_recipe')
  END_CRYSTAL_RECIPE = Kee[str]('end_crystal_recipe')
  END_ROD_RECIPE = Kee[str]('end_rod_recipe')
  END_ROOT = Kee[str]('end_root')
  END_STONE_BRICK_SLAB_FROM_END_STONE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'end_stone_brick_slab_from_end_stone_bricks_stonecutting_recipe')
  END_STONE_BRICK_SLAB_FROM_END_STONE_STONECUTTING_RECIPE = Kee[str](
    'end_stone_brick_slab_from_end_stone_stonecutting_recipe')
  END_STONE_BRICK_SLAB_RECIPE = Kee[str]('end_stone_brick_slab_recipe')
  END_STONE_BRICK_STAIRS_FROM_END_STONE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'end_stone_brick_stairs_from_end_stone_bricks_stonecutting_recipe')
  END_STONE_BRICK_STAIRS_FROM_END_STONE_STONECUTTING_RECIPE = Kee[str](
    'end_stone_brick_stairs_from_end_stone_stonecutting_recipe')
  END_STONE_BRICK_STAIRS_RECIPE = Kee[str]('end_stone_brick_stairs_recipe')
  END_STONE_BRICK_WALL_FROM_END_STONE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'end_stone_brick_wall_from_end_stone_bricks_stonecutting_recipe')
  END_STONE_BRICK_WALL_FROM_END_STONE_STONECUTTING_RECIPE = Kee[str](
    'end_stone_brick_wall_from_end_stone_stonecutting_recipe')
  END_STONE_BRICK_WALL_RECIPE = Kee[str]('end_stone_brick_wall_recipe')
  END_STONE_BRICKS_FROM_END_STONE_STONECUTTING_RECIPE = Kee[str](
    'end_stone_bricks_from_end_stone_stonecutting_recipe')
  END_STONE_BRICKS_RECIPE = Kee[str]('end_stone_bricks_recipe')
  ENDER_CHEST_RECIPE = Kee[str]('ender_chest_recipe')
  ENDER_EYE_RECIPE = Kee[str]('ender_eye_recipe')
  EXPOSED_CHISELED_COPPER_FROM_EXPOSED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'exposed_chiseled_copper_from_exposed_copper_stonecutting_recipe')
  EXPOSED_CHISELED_COPPER_FROM_EXPOSED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'exposed_chiseled_copper_from_exposed_cut_copper_stonecutting_recipe')
  EXPOSED_CHISELED_COPPER_RECIPE = Kee[str]('exposed_chiseled_copper_recipe')
  EXPOSED_COPPER_BULB_RECIPE = Kee[str]('exposed_copper_bulb_recipe')
  EXPOSED_COPPER_GRATE_FROM_EXPOSED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'exposed_copper_grate_from_exposed_copper_stonecutting_recipe')
  EXPOSED_COPPER_GRATE_RECIPE = Kee[str]('exposed_copper_grate_recipe')
  EXPOSED_CUT_COPPER_FROM_EXPOSED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'exposed_cut_copper_from_exposed_copper_stonecutting_recipe')
  EXPOSED_CUT_COPPER_RECIPE = Kee[str]('exposed_cut_copper_recipe')
  EXPOSED_CUT_COPPER_SLAB_FROM_EXPOSED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'exposed_cut_copper_slab_from_exposed_copper_stonecutting_recipe')
  EXPOSED_CUT_COPPER_SLAB_FROM_EXPOSED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'exposed_cut_copper_slab_from_exposed_cut_copper_stonecutting_recipe')
  EXPOSED_CUT_COPPER_SLAB_RECIPE = Kee[str]('exposed_cut_copper_slab_recipe')
  EXPOSED_CUT_COPPER_STAIRS_FROM_EXPOSED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'exposed_cut_copper_stairs_from_exposed_copper_stonecutting_recipe')
  EXPOSED_CUT_COPPER_STAIRS_FROM_EXPOSED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'exposed_cut_copper_stairs_from_exposed_cut_copper_stonecutting_recipe')
  EXPOSED_CUT_COPPER_STAIRS_RECIPE = Kee[str](
    'exposed_cut_copper_stairs_recipe')
  EYE_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'eye_armor_trim_smithing_template_recipe')
  EYE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'eye_armor_trim_smithing_template_smithing_trim_recipe')
  EYE_SPY = Kee[str]('eye_spy')
  FEELS_LIKE_HOME = Kee[str]('feels_like_home')
  FERMENTED_SPIDER_EYE_RECIPE = Kee[str]('fermented_spider_eye_recipe')
  FIELD_MASONED_BANNER_PATTERN_RECIPE = Kee[str](
    'field_masoned_banner_pattern_recipe')
  FIRE_CHARGE_RECIPE = Kee[str]('fire_charge_recipe')
  FIREWORK_ROCKET_SIMPLE_RECIPE = Kee[str]('firework_rocket_simple_recipe')
  FISHING_ROD_RECIPE = Kee[str]('fishing_rod_recipe')
  FISHY_BUSINESS = Kee[str]('fishy_business')
  FLETCHING_TABLE_RECIPE = Kee[str]('fletching_table_recipe')
  FLINT_AND_STEEL_RECIPE = Kee[str]('flint_and_steel_recipe')
  FLOW_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'flow_armor_trim_smithing_template_recipe')
  FLOW_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'flow_armor_trim_smithing_template_smithing_trim_recipe')
  FLOWER_BANNER_PATTERN_RECIPE = Kee[str]('flower_banner_pattern_recipe')
  FLOWER_POT_RECIPE = Kee[str]('flower_pot_recipe')
  FREE_THE_END = Kee[str]('free_the_end')
  FURNACE_MINECART_RECIPE = Kee[str]('furnace_minecart_recipe')
  FURNACE_RECIPE = Kee[str]('furnace_recipe')
  GETTING_AN_UPGRADE = Kee[str]('getting_an_upgrade')
  GLASS_BOTTLE_RECIPE = Kee[str]('glass_bottle_recipe')
  GLASS_PANE_RECIPE = Kee[str]('glass_pane_recipe')
  GLASS_RECIPE = Kee[str]('glass_recipe')
  GLISTERING_MELON_SLICE_RECIPE = Kee[str]('glistering_melon_slice_recipe')
  GLOW_AND_BEHOLD = Kee[str]('glow_and_behold')
  GLOW_ITEM_FRAME_RECIPE = Kee[str]('glow_item_frame_recipe')
  GLOWSTONE_RECIPE = Kee[str]('glowstone_recipe')
  GOLD_BLOCK_RECIPE = Kee[str]('gold_block_recipe')
  GOLD_INGOT_FROM_BLASTING_DEEPSLATE_GOLD_ORE_RECIPE = Kee[str](
    'gold_ingot_from_blasting_deepslate_gold_ore_recipe')
  GOLD_INGOT_FROM_BLASTING_GOLD_ORE_RECIPE = Kee[str](
    'gold_ingot_from_blasting_gold_ore_recipe')
  GOLD_INGOT_FROM_BLASTING_NETHER_GOLD_ORE_RECIPE = Kee[str](
    'gold_ingot_from_blasting_nether_gold_ore_recipe')
  GOLD_INGOT_FROM_BLASTING_RAW_GOLD_RECIPE = Kee[str](
    'gold_ingot_from_blasting_raw_gold_recipe')
  GOLD_INGOT_FROM_BLASTING_RECIPE = Kee[str]('gold_ingot_from_blasting_recipe')
  GOLD_INGOT_FROM_GOLD_BLOCK_RECIPE = Kee[str](
    'gold_ingot_from_gold_block_recipe')
  GOLD_INGOT_FROM_NUGGETS_RECIPE = Kee[str]('gold_ingot_from_nuggets_recipe')
  GOLD_INGOT_FROM_SMELTING_DEEPSLATE_GOLD_ORE_RECIPE = Kee[str](
    'gold_ingot_from_smelting_deepslate_gold_ore_recipe')
  GOLD_INGOT_FROM_SMELTING_GOLD_ORE_RECIPE = Kee[str](
    'gold_ingot_from_smelting_gold_ore_recipe')
  GOLD_INGOT_FROM_SMELTING_NETHER_GOLD_ORE_RECIPE = Kee[str](
    'gold_ingot_from_smelting_nether_gold_ore_recipe')
  GOLD_INGOT_FROM_SMELTING_RAW_GOLD_RECIPE = Kee[str](
    'gold_ingot_from_smelting_raw_gold_recipe')
  GOLD_INGOT_RECIPE = Kee[str]('gold_ingot_recipe')
  GOLD_NUGGET_FROM_BLASTING_RECIPE = Kee[str](
    'gold_nugget_from_blasting_recipe')
  GOLD_NUGGET_FROM_SMELTING_RECIPE = Kee[str](
    'gold_nugget_from_smelting_recipe')
  GOLD_NUGGET_RECIPE = Kee[str]('gold_nugget_recipe')
  GOLDEN_APPLE_RECIPE = Kee[str]('golden_apple_recipe')
  GOLDEN_AXE_RECIPE = Kee[str]('golden_axe_recipe')
  GOLDEN_BOOTS_RECIPE = Kee[str]('golden_boots_recipe')
  GOLDEN_CARROT_RECIPE = Kee[str]('golden_carrot_recipe')
  GOLDEN_CHESTPLATE_RECIPE = Kee[str]('golden_chestplate_recipe')
  GOLDEN_DANDELION_RECIPE = Kee[str]('golden_dandelion_recipe')
  GOLDEN_HELMET_RECIPE = Kee[str]('golden_helmet_recipe')
  GOLDEN_HOE_RECIPE = Kee[str]('golden_hoe_recipe')
  GOLDEN_LEGGINGS_RECIPE = Kee[str]('golden_leggings_recipe')
  GOLDEN_PICKAXE_RECIPE = Kee[str]('golden_pickaxe_recipe')
  GOLDEN_SHOVEL_RECIPE = Kee[str]('golden_shovel_recipe')
  GOLDEN_SPEAR_RECIPE = Kee[str]('golden_spear_recipe')
  GOLDEN_SWORD_RECIPE = Kee[str]('golden_sword_recipe')
  GOOD_AS_NEW = Kee[str]('good_as_new')
  GRANITE_RECIPE = Kee[str]('granite_recipe')
  GRANITE_SLAB_FROM_GRANITE_STONECUTTING_RECIPE = Kee[str](
    'granite_slab_from_granite_stonecutting_recipe')
  GRANITE_SLAB_RECIPE = Kee[str]('granite_slab_recipe')
  GRANITE_STAIRS_FROM_GRANITE_STONECUTTING_RECIPE = Kee[str](
    'granite_stairs_from_granite_stonecutting_recipe')
  GRANITE_STAIRS_RECIPE = Kee[str]('granite_stairs_recipe')
  GRANITE_WALL_FROM_GRANITE_STONECUTTING_RECIPE = Kee[str](
    'granite_wall_from_granite_stonecutting_recipe')
  GRANITE_WALL_RECIPE = Kee[str]('granite_wall_recipe')
  GRAY_BANNER_RECIPE = Kee[str]('gray_banner_recipe')
  GRAY_BED_FROM_WHITE_BED_RECIPE = Kee[str]('gray_bed_from_white_bed_recipe')
  GRAY_BED_RECIPE = Kee[str]('gray_bed_recipe')
  GRAY_BUNDLE_RECIPE = Kee[str]('gray_bundle_recipe')
  GRAY_CANDLE_RECIPE = Kee[str]('gray_candle_recipe')
  GRAY_CARPET_FROM_WHITE_CARPET_RECIPE = Kee[str](
    'gray_carpet_from_white_carpet_recipe')
  GRAY_CARPET_RECIPE = Kee[str]('gray_carpet_recipe')
  GRAY_CONCRETE_POWDER_RECIPE = Kee[str]('gray_concrete_powder_recipe')
  GRAY_CONCRETE_SLAB_FROM_GRAY_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'gray_concrete_slab_from_gray_concrete_stonecutting_recipe')
  GRAY_CONCRETE_SLAB_RECIPE = Kee[str]('gray_concrete_slab_recipe')
  GRAY_CONCRETE_STAIRS_FROM_GRAY_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'gray_concrete_stairs_from_gray_concrete_stonecutting_recipe')
  GRAY_CONCRETE_STAIRS_RECIPE = Kee[str]('gray_concrete_stairs_recipe')
  GRAY_CUSHION_RECIPE = Kee[str]('gray_cushion_recipe')
  GRAY_DYE_FROM_CLOSED_EYEBLOSSOM_RECIPE = Kee[str](
    'gray_dye_from_closed_eyeblossom_recipe')
  GRAY_DYE_RECIPE = Kee[str]('gray_dye_recipe')
  GRAY_GLAZED_TERRACOTTA_RECIPE = Kee[str]('gray_glazed_terracotta_recipe')
  GRAY_HARNESS_RECIPE = Kee[str]('gray_harness_recipe')
  GRAY_SHULKER_BOX_RECIPE = Kee[str]('gray_shulker_box_recipe')
  GRAY_STAINED_GLASS_PANE_FROM_GLASS_PANE_RECIPE = Kee[str](
    'gray_stained_glass_pane_from_glass_pane_recipe')
  GRAY_STAINED_GLASS_PANE_RECIPE = Kee[str]('gray_stained_glass_pane_recipe')
  GRAY_STAINED_GLASS_RECIPE = Kee[str]('gray_stained_glass_recipe')
  GRAY_TERRACOTTA_RECIPE = Kee[str]('gray_terracotta_recipe')
  GRAY_WOOL_RECIPE = Kee[str]('gray_wool_recipe')
  GRAY_WOOL_SLAB_RECIPE = Kee[str]('gray_wool_slab_recipe')
  GRAY_WOOL_STAIRS_RECIPE = Kee[str]('gray_wool_stairs_recipe')
  GREAT_VIEW_FROM_UP_HERE = Kee[str]('great_view_from_up_here')
  GREEN_BANNER_RECIPE = Kee[str]('green_banner_recipe')
  GREEN_BED_FROM_WHITE_BED_RECIPE = Kee[str]('green_bed_from_white_bed_recipe')
  GREEN_BED_RECIPE = Kee[str]('green_bed_recipe')
  GREEN_BUNDLE_RECIPE = Kee[str]('green_bundle_recipe')
  GREEN_CANDLE_RECIPE = Kee[str]('green_candle_recipe')
  GREEN_CARPET_FROM_WHITE_CARPET_RECIPE = Kee[str](
    'green_carpet_from_white_carpet_recipe')
  GREEN_CARPET_RECIPE = Kee[str]('green_carpet_recipe')
  GREEN_CONCRETE_POWDER_RECIPE = Kee[str]('green_concrete_powder_recipe')
  GREEN_CONCRETE_SLAB_FROM_GREEN_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'green_concrete_slab_from_green_concrete_stonecutting_recipe')
  GREEN_CONCRETE_SLAB_RECIPE = Kee[str]('green_concrete_slab_recipe')
  GREEN_CONCRETE_STAIRS_FROM_GREEN_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'green_concrete_stairs_from_green_concrete_stonecutting_recipe')
  GREEN_CONCRETE_STAIRS_RECIPE = Kee[str]('green_concrete_stairs_recipe')
  GREEN_CUSHION_RECIPE = Kee[str]('green_cushion_recipe')
  GREEN_DYE_RECIPE = Kee[str]('green_dye_recipe')
  GREEN_GLAZED_TERRACOTTA_RECIPE = Kee[str]('green_glazed_terracotta_recipe')
  GREEN_HARNESS_RECIPE = Kee[str]('green_harness_recipe')
  GREEN_SHULKER_BOX_RECIPE = Kee[str]('green_shulker_box_recipe')
  GREEN_STAINED_GLASS_PANE_FROM_GLASS_PANE_RECIPE = Kee[str](
    'green_stained_glass_pane_from_glass_pane_recipe')
  GREEN_STAINED_GLASS_PANE_RECIPE = Kee[str]('green_stained_glass_pane_recipe')
  GREEN_STAINED_GLASS_RECIPE = Kee[str]('green_stained_glass_recipe')
  GREEN_TERRACOTTA_RECIPE = Kee[str]('green_terracotta_recipe')
  GREEN_WOOL_RECIPE = Kee[str]('green_wool_recipe')
  GREEN_WOOL_SLAB_RECIPE = Kee[str]('green_wool_slab_recipe')
  GREEN_WOOL_STAIRS_RECIPE = Kee[str]('green_wool_stairs_recipe')
  GRINDSTONE_RECIPE = Kee[str]('grindstone_recipe')
  HAY_BLOCK_RECIPE = Kee[str]('hay_block_recipe')
  HEART_TRANSPLANTER = Kee[str]('heart_transplanter')
  HEAVY_WEIGHTED_PRESSURE_PLATE_RECIPE = Kee[str](
    'heavy_weighted_pressure_plate_recipe')
  HERO_OF_THE_VILLAGE = Kee[str]('hero_of_the_village')
  HIDDEN_IN_THE_DEPTHS = Kee[str]('hidden_in_the_depths')
  HIRED_HELP = Kee[str]('hired_help')
  HONEY_BLOCK_RECIPE = Kee[str]('honey_block_recipe')
  HONEY_BOTTLE_RECIPE = Kee[str]('honey_bottle_recipe')
  HONEYCOMB_BLOCK_RECIPE = Kee[str]('honeycomb_block_recipe')
  HOPPER_MINECART_RECIPE = Kee[str]('hopper_minecart_recipe')
  HOPPER_RECIPE = Kee[str]('hopper_recipe')
  HOST_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'host_armor_trim_smithing_template_recipe')
  HOST_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'host_armor_trim_smithing_template_smithing_trim_recipe')
  HOT_STUFF = Kee[str]('hot_stuff')
  HOT_TOURIST_DESTINATIONS = Kee[str]('hot_tourist_destinations')
  HOW_DID_WE_GET_HERE = Kee[str]('how_did_we_get_here')
  HUSBANDRY_ROOT = Kee[str]('husbandry_root')
  ICE_BUCKET_CHALLENGE = Kee[str]('ice_bucket_challenge')
  INTO_FIRE = Kee[str]('into_fire')
  IRON_AXE_RECIPE = Kee[str]('iron_axe_recipe')
  IRON_BARS_RECIPE = Kee[str]('iron_bars_recipe')
  IRON_BLOCK_RECIPE = Kee[str]('iron_block_recipe')
  IRON_BOOTS_RECIPE = Kee[str]('iron_boots_recipe')
  IRON_CHAIN_RECIPE = Kee[str]('iron_chain_recipe')
  IRON_CHESTPLATE_RECIPE = Kee[str]('iron_chestplate_recipe')
  IRON_DOOR_RECIPE = Kee[str]('iron_door_recipe')
  IRON_HELMET_RECIPE = Kee[str]('iron_helmet_recipe')
  IRON_HOE_RECIPE = Kee[str]('iron_hoe_recipe')
  IRON_INGOT_FROM_BLASTING_DEEPSLATE_IRON_ORE_RECIPE = Kee[str](
    'iron_ingot_from_blasting_deepslate_iron_ore_recipe')
  IRON_INGOT_FROM_BLASTING_IRON_ORE_RECIPE = Kee[str](
    'iron_ingot_from_blasting_iron_ore_recipe')
  IRON_INGOT_FROM_BLASTING_RAW_IRON_RECIPE = Kee[str](
    'iron_ingot_from_blasting_raw_iron_recipe')
  IRON_INGOT_FROM_BLASTING_RECIPE = Kee[str]('iron_ingot_from_blasting_recipe')
  IRON_INGOT_FROM_IRON_BLOCK_RECIPE = Kee[str](
    'iron_ingot_from_iron_block_recipe')
  IRON_INGOT_FROM_NUGGETS_RECIPE = Kee[str]('iron_ingot_from_nuggets_recipe')
  IRON_INGOT_FROM_SMELTING_DEEPSLATE_IRON_ORE_RECIPE = Kee[str](
    'iron_ingot_from_smelting_deepslate_iron_ore_recipe')
  IRON_INGOT_FROM_SMELTING_IRON_ORE_RECIPE = Kee[str](
    'iron_ingot_from_smelting_iron_ore_recipe')
  IRON_INGOT_FROM_SMELTING_RAW_IRON_RECIPE = Kee[str](
    'iron_ingot_from_smelting_raw_iron_recipe')
  IRON_INGOT_RECIPE = Kee[str]('iron_ingot_recipe')
  IRON_LEGGINGS_RECIPE = Kee[str]('iron_leggings_recipe')
  IRON_NUGGET_FROM_BLASTING_RECIPE = Kee[str](
    'iron_nugget_from_blasting_recipe')
  IRON_NUGGET_FROM_SMELTING_RECIPE = Kee[str](
    'iron_nugget_from_smelting_recipe')
  IRON_NUGGET_RECIPE = Kee[str]('iron_nugget_recipe')
  IRON_PICKAXE_RECIPE = Kee[str]('iron_pickaxe_recipe')
  IRON_SHOVEL_RECIPE = Kee[str]('iron_shovel_recipe')
  IRON_SPEAR_RECIPE = Kee[str]('iron_spear_recipe')
  IRON_SWORD_RECIPE = Kee[str]('iron_sword_recipe')
  IRON_TRAPDOOR_RECIPE = Kee[str]('iron_trapdoor_recipe')
  IS_IT_A_BALLOON = Kee[str]('is_it_a_balloon')
  IS_IT_A_BIRD = Kee[str]('is_it_a_bird')
  IS_IT_A_PLANE = Kee[str]('is_it_a_plane')
  ISNT_IT_IRON_PICK = Kee[str]('isnt_it_iron_pick')
  ISNT_IT_SCUTE = Kee[str]('isnt_it_scute')
  IT_SPREADS = Kee[str]('it_spreads')
  ITEM_FRAME_RECIPE = Kee[str]('item_frame_recipe')
  JACK_O_LANTERN_RECIPE = Kee[str]('jack_o_lantern_recipe')
  JUKEBOX_RECIPE = Kee[str]('jukebox_recipe')
  JUNGLE_BOAT_RECIPE = Kee[str]('jungle_boat_recipe')
  JUNGLE_BUTTON_RECIPE = Kee[str]('jungle_button_recipe')
  JUNGLE_CHEST_BOAT_RECIPE = Kee[str]('jungle_chest_boat_recipe')
  JUNGLE_DOOR_RECIPE = Kee[str]('jungle_door_recipe')
  JUNGLE_FENCE_GATE_RECIPE = Kee[str]('jungle_fence_gate_recipe')
  JUNGLE_FENCE_RECIPE = Kee[str]('jungle_fence_recipe')
  JUNGLE_HANGING_SIGN_RECIPE = Kee[str]('jungle_hanging_sign_recipe')
  JUNGLE_PLANKS_RECIPE = Kee[str]('jungle_planks_recipe')
  JUNGLE_PRESSURE_PLATE_RECIPE = Kee[str]('jungle_pressure_plate_recipe')
  JUNGLE_SHELF_RECIPE = Kee[str]('jungle_shelf_recipe')
  JUNGLE_SIGN_RECIPE = Kee[str]('jungle_sign_recipe')
  JUNGLE_SLAB_RECIPE = Kee[str]('jungle_slab_recipe')
  JUNGLE_STAIRS_RECIPE = Kee[str]('jungle_stairs_recipe')
  JUNGLE_TRAPDOOR_RECIPE = Kee[str]('jungle_trapdoor_recipe')
  JUNGLE_WOOD_RECIPE = Kee[str]('jungle_wood_recipe')
  LADDER_RECIPE = Kee[str]('ladder_recipe')
  LANTERN_RECIPE = Kee[str]('lantern_recipe')
  LAPIS_BLOCK_RECIPE = Kee[str]('lapis_block_recipe')
  LAPIS_FROM_BLASTING_RECIPE = Kee[str]('lapis_from_blasting_recipe')
  LAPIS_FROM_SMELTING_RECIPE = Kee[str]('lapis_from_smelting_recipe')
  LAPIS_LAZULI_FROM_BLASTING_DEEPSLATE_LAPIS_ORE_RECIPE = Kee[str](
    'lapis_lazuli_from_blasting_deepslate_lapis_ore_recipe')
  LAPIS_LAZULI_FROM_BLASTING_LAPIS_ORE_RECIPE = Kee[str](
    'lapis_lazuli_from_blasting_lapis_ore_recipe')
  LAPIS_LAZULI_FROM_SMELTING_DEEPSLATE_LAPIS_ORE_RECIPE = Kee[str](
    'lapis_lazuli_from_smelting_deepslate_lapis_ore_recipe')
  LAPIS_LAZULI_FROM_SMELTING_LAPIS_ORE_RECIPE = Kee[str](
    'lapis_lazuli_from_smelting_lapis_ore_recipe')
  LAPIS_LAZULI_RECIPE = Kee[str]('lapis_lazuli_recipe')
  LEAD_RECIPE = Kee[str]('lead_recipe')
  LEAF_LITTER_RECIPE = Kee[str]('leaf_litter_recipe')
  LEATHER_BOOTS_DYED_RECIPE = Kee[str]('leather_boots_dyed_recipe')
  LEATHER_BOOTS_RECIPE = Kee[str]('leather_boots_recipe')
  LEATHER_CHESTPLATE_DYED_RECIPE = Kee[str]('leather_chestplate_dyed_recipe')
  LEATHER_CHESTPLATE_RECIPE = Kee[str]('leather_chestplate_recipe')
  LEATHER_HELMET_DYED_RECIPE = Kee[str]('leather_helmet_dyed_recipe')
  LEATHER_HELMET_RECIPE = Kee[str]('leather_helmet_recipe')
  LEATHER_HORSE_ARMOR_DYED_RECIPE = Kee[str]('leather_horse_armor_dyed_recipe')
  LEATHER_HORSE_ARMOR_RECIPE = Kee[str]('leather_horse_armor_recipe')
  LEATHER_LEGGINGS_DYED_RECIPE = Kee[str]('leather_leggings_dyed_recipe')
  LEATHER_LEGGINGS_RECIPE = Kee[str]('leather_leggings_recipe')
  LEATHER_RECIPE = Kee[str]('leather_recipe')
  LECTERN_RECIPE = Kee[str]('lectern_recipe')
  LEVER_RECIPE = Kee[str]('lever_recipe')
  LIGHT_AS_A_RABBIT = Kee[str]('light_as_a_rabbit')
  LIGHT_BLUE_BANNER_RECIPE = Kee[str]('light_blue_banner_recipe')
  LIGHT_BLUE_BED_FROM_WHITE_BED_RECIPE = Kee[str](
    'light_blue_bed_from_white_bed_recipe')
  LIGHT_BLUE_BED_RECIPE = Kee[str]('light_blue_bed_recipe')
  LIGHT_BLUE_BUNDLE_RECIPE = Kee[str]('light_blue_bundle_recipe')
  LIGHT_BLUE_CANDLE_RECIPE = Kee[str]('light_blue_candle_recipe')
  LIGHT_BLUE_CARPET_FROM_WHITE_CARPET_RECIPE = Kee[str](
    'light_blue_carpet_from_white_carpet_recipe')
  LIGHT_BLUE_CARPET_RECIPE = Kee[str]('light_blue_carpet_recipe')
  LIGHT_BLUE_CONCRETE_POWDER_RECIPE = Kee[str](
    'light_blue_concrete_powder_recipe')
  LIGHT_BLUE_CONCRETE_SLAB_FROM_LIGHT_BLUE_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'light_blue_concrete_slab_from_light_blue_concrete_stonecutting_recipe')
  LIGHT_BLUE_CONCRETE_SLAB_RECIPE = Kee[str]('light_blue_concrete_slab_recipe')
  LIGHT_BLUE_CONCRETE_STAIRS_FROM_LIGHT_BLUE_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'light_blue_concrete_stairs_from_light_blue_concrete_stonecutting_recipe')
  LIGHT_BLUE_CONCRETE_STAIRS_RECIPE = Kee[str](
    'light_blue_concrete_stairs_recipe')
  LIGHT_BLUE_CUSHION_RECIPE = Kee[str]('light_blue_cushion_recipe')
  LIGHT_BLUE_DYE_FROM_BLUE_ORCHID_RECIPE = Kee[str](
    'light_blue_dye_from_blue_orchid_recipe')
  LIGHT_BLUE_DYE_FROM_BLUE_WHITE_DYE_RECIPE = Kee[str](
    'light_blue_dye_from_blue_white_dye_recipe')
  LIGHT_BLUE_DYE_FROM_LAPIS_BONEMEAL_RECIPE = Kee[str](
    'light_blue_dye_from_lapis_bonemeal_recipe')
  LIGHT_BLUE_GLAZED_TERRACOTTA_RECIPE = Kee[str](
    'light_blue_glazed_terracotta_recipe')
  LIGHT_BLUE_HARNESS_RECIPE = Kee[str]('light_blue_harness_recipe')
  LIGHT_BLUE_SHULKER_BOX_RECIPE = Kee[str]('light_blue_shulker_box_recipe')
  LIGHT_BLUE_STAINED_GLASS_PANE_FROM_GLASS_PANE_RECIPE = Kee[str](
    'light_blue_stained_glass_pane_from_glass_pane_recipe')
  LIGHT_BLUE_STAINED_GLASS_PANE_RECIPE = Kee[str](
    'light_blue_stained_glass_pane_recipe')
  LIGHT_BLUE_STAINED_GLASS_RECIPE = Kee[str]('light_blue_stained_glass_recipe')
  LIGHT_BLUE_TERRACOTTA_RECIPE = Kee[str]('light_blue_terracotta_recipe')
  LIGHT_BLUE_WOOL_RECIPE = Kee[str]('light_blue_wool_recipe')
  LIGHT_BLUE_WOOL_SLAB_RECIPE = Kee[str]('light_blue_wool_slab_recipe')
  LIGHT_BLUE_WOOL_STAIRS_RECIPE = Kee[str]('light_blue_wool_stairs_recipe')
  LIGHT_GRAY_BANNER_RECIPE = Kee[str]('light_gray_banner_recipe')
  LIGHT_GRAY_BED_FROM_WHITE_BED_RECIPE = Kee[str](
    'light_gray_bed_from_white_bed_recipe')
  LIGHT_GRAY_BED_RECIPE = Kee[str]('light_gray_bed_recipe')
  LIGHT_GRAY_BUNDLE_RECIPE = Kee[str]('light_gray_bundle_recipe')
  LIGHT_GRAY_CANDLE_RECIPE = Kee[str]('light_gray_candle_recipe')
  LIGHT_GRAY_CARPET_FROM_WHITE_CARPET_RECIPE = Kee[str](
    'light_gray_carpet_from_white_carpet_recipe')
  LIGHT_GRAY_CARPET_RECIPE = Kee[str]('light_gray_carpet_recipe')
  LIGHT_GRAY_CONCRETE_POWDER_RECIPE = Kee[str](
    'light_gray_concrete_powder_recipe')
  LIGHT_GRAY_CONCRETE_SLAB_FROM_LIGHT_GRAY_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'light_gray_concrete_slab_from_light_gray_concrete_stonecutting_recipe')
  LIGHT_GRAY_CONCRETE_SLAB_RECIPE = Kee[str]('light_gray_concrete_slab_recipe')
  LIGHT_GRAY_CONCRETE_STAIRS_FROM_LIGHT_GRAY_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'light_gray_concrete_stairs_from_light_gray_concrete_stonecutting_recipe')
  LIGHT_GRAY_CONCRETE_STAIRS_RECIPE = Kee[str](
    'light_gray_concrete_stairs_recipe')
  LIGHT_GRAY_CUSHION_RECIPE = Kee[str]('light_gray_cushion_recipe')
  LIGHT_GRAY_DYE_FROM_AZURE_BLUET_RECIPE = Kee[str](
    'light_gray_dye_from_azure_bluet_recipe')
  LIGHT_GRAY_DYE_FROM_BLACK_WHITE_DYE_RECIPE = Kee[str](
    'light_gray_dye_from_black_white_dye_recipe')
  LIGHT_GRAY_DYE_FROM_GRAY_BONEMEAL_RECIPE = Kee[str](
    'light_gray_dye_from_gray_bonemeal_recipe')
  LIGHT_GRAY_DYE_FROM_GRAY_WHITE_DYE_RECIPE = Kee[str](
    'light_gray_dye_from_gray_white_dye_recipe')
  LIGHT_GRAY_DYE_FROM_INK_BONEMEAL_RECIPE = Kee[str](
    'light_gray_dye_from_ink_bonemeal_recipe')
  LIGHT_GRAY_DYE_FROM_OXEYE_DAISY_RECIPE = Kee[str](
    'light_gray_dye_from_oxeye_daisy_recipe')
  LIGHT_GRAY_DYE_FROM_WHITE_TULIP_RECIPE = Kee[str](
    'light_gray_dye_from_white_tulip_recipe')
  LIGHT_GRAY_GLAZED_TERRACOTTA_RECIPE = Kee[str](
    'light_gray_glazed_terracotta_recipe')
  LIGHT_GRAY_HARNESS_RECIPE = Kee[str]('light_gray_harness_recipe')
  LIGHT_GRAY_SHULKER_BOX_RECIPE = Kee[str]('light_gray_shulker_box_recipe')
  LIGHT_GRAY_STAINED_GLASS_PANE_FROM_GLASS_PANE_RECIPE = Kee[str](
    'light_gray_stained_glass_pane_from_glass_pane_recipe')
  LIGHT_GRAY_STAINED_GLASS_PANE_RECIPE = Kee[str](
    'light_gray_stained_glass_pane_recipe')
  LIGHT_GRAY_STAINED_GLASS_RECIPE = Kee[str]('light_gray_stained_glass_recipe')
  LIGHT_GRAY_TERRACOTTA_RECIPE = Kee[str]('light_gray_terracotta_recipe')
  LIGHT_GRAY_WOOL_RECIPE = Kee[str]('light_gray_wool_recipe')
  LIGHT_GRAY_WOOL_SLAB_RECIPE = Kee[str]('light_gray_wool_slab_recipe')
  LIGHT_GRAY_WOOL_STAIRS_RECIPE = Kee[str]('light_gray_wool_stairs_recipe')
  LIGHT_WEIGHTED_PRESSURE_PLATE_RECIPE = Kee[str](
    'light_weighted_pressure_plate_recipe')
  LIGHTEN_UP = Kee[str]('lighten_up')
  LIGHTNING_ROD_RECIPE = Kee[str]('lightning_rod_recipe')
  LIME_BANNER_RECIPE = Kee[str]('lime_banner_recipe')
  LIME_BED_FROM_WHITE_BED_RECIPE = Kee[str]('lime_bed_from_white_bed_recipe')
  LIME_BED_RECIPE = Kee[str]('lime_bed_recipe')
  LIME_BUNDLE_RECIPE = Kee[str]('lime_bundle_recipe')
  LIME_CANDLE_RECIPE = Kee[str]('lime_candle_recipe')
  LIME_CARPET_FROM_WHITE_CARPET_RECIPE = Kee[str](
    'lime_carpet_from_white_carpet_recipe')
  LIME_CARPET_RECIPE = Kee[str]('lime_carpet_recipe')
  LIME_CONCRETE_POWDER_RECIPE = Kee[str]('lime_concrete_powder_recipe')
  LIME_CONCRETE_SLAB_FROM_LIME_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'lime_concrete_slab_from_lime_concrete_stonecutting_recipe')
  LIME_CONCRETE_SLAB_RECIPE = Kee[str]('lime_concrete_slab_recipe')
  LIME_CONCRETE_STAIRS_FROM_LIME_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'lime_concrete_stairs_from_lime_concrete_stonecutting_recipe')
  LIME_CONCRETE_STAIRS_RECIPE = Kee[str]('lime_concrete_stairs_recipe')
  LIME_CUSHION_RECIPE = Kee[str]('lime_cushion_recipe')
  LIME_DYE_FROM_SMELTING_RECIPE = Kee[str]('lime_dye_from_smelting_recipe')
  LIME_DYE_RECIPE = Kee[str]('lime_dye_recipe')
  LIME_GLAZED_TERRACOTTA_RECIPE = Kee[str]('lime_glazed_terracotta_recipe')
  LIME_HARNESS_RECIPE = Kee[str]('lime_harness_recipe')
  LIME_SHULKER_BOX_RECIPE = Kee[str]('lime_shulker_box_recipe')
  LIME_STAINED_GLASS_PANE_FROM_GLASS_PANE_RECIPE = Kee[str](
    'lime_stained_glass_pane_from_glass_pane_recipe')
  LIME_STAINED_GLASS_PANE_RECIPE = Kee[str]('lime_stained_glass_pane_recipe')
  LIME_STAINED_GLASS_RECIPE = Kee[str]('lime_stained_glass_recipe')
  LIME_TERRACOTTA_RECIPE = Kee[str]('lime_terracotta_recipe')
  LIME_WOOL_RECIPE = Kee[str]('lime_wool_recipe')
  LIME_WOOL_SLAB_RECIPE = Kee[str]('lime_wool_slab_recipe')
  LIME_WOOL_STAIRS_RECIPE = Kee[str]('lime_wool_stairs_recipe')
  LITTLE_SNIFFS = Kee[str]('little_sniffs')
  LOCAL_BREWERY = Kee[str]('local_brewery')
  LODESTONE_RECIPE = Kee[str]('lodestone_recipe')
  LOOM_RECIPE = Kee[str]('loom_recipe')
  MACE_RECIPE = Kee[str]('mace_recipe')
  MAGENTA_BANNER_RECIPE = Kee[str]('magenta_banner_recipe')
  MAGENTA_BED_FROM_WHITE_BED_RECIPE = Kee[str](
    'magenta_bed_from_white_bed_recipe')
  MAGENTA_BED_RECIPE = Kee[str]('magenta_bed_recipe')
  MAGENTA_BUNDLE_RECIPE = Kee[str]('magenta_bundle_recipe')
  MAGENTA_CANDLE_RECIPE = Kee[str]('magenta_candle_recipe')
  MAGENTA_CARPET_FROM_WHITE_CARPET_RECIPE = Kee[str](
    'magenta_carpet_from_white_carpet_recipe')
  MAGENTA_CARPET_RECIPE = Kee[str]('magenta_carpet_recipe')
  MAGENTA_CONCRETE_POWDER_RECIPE = Kee[str]('magenta_concrete_powder_recipe')
  MAGENTA_CONCRETE_SLAB_FROM_MAGENTA_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'magenta_concrete_slab_from_magenta_concrete_stonecutting_recipe')
  MAGENTA_CONCRETE_SLAB_RECIPE = Kee[str]('magenta_concrete_slab_recipe')
  MAGENTA_CONCRETE_STAIRS_FROM_MAGENTA_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'magenta_concrete_stairs_from_magenta_concrete_stonecutting_recipe')
  MAGENTA_CONCRETE_STAIRS_RECIPE = Kee[str]('magenta_concrete_stairs_recipe')
  MAGENTA_CUSHION_RECIPE = Kee[str]('magenta_cushion_recipe')
  MAGENTA_DYE_FROM_ALLIUM_RECIPE = Kee[str]('magenta_dye_from_allium_recipe')
  MAGENTA_DYE_FROM_BLUE_RED_PINK_RECIPE = Kee[str](
    'magenta_dye_from_blue_red_pink_recipe')
  MAGENTA_DYE_FROM_BLUE_RED_WHITE_DYE_RECIPE = Kee[str](
    'magenta_dye_from_blue_red_white_dye_recipe')
  MAGENTA_DYE_FROM_LAPIS_INK_BONEMEAL_RECIPE = Kee[str](
    'magenta_dye_from_lapis_ink_bonemeal_recipe')
  MAGENTA_DYE_FROM_LAPIS_RED_PINK_RECIPE = Kee[str](
    'magenta_dye_from_lapis_red_pink_recipe')
  MAGENTA_DYE_FROM_LILAC_RECIPE = Kee[str]('magenta_dye_from_lilac_recipe')
  MAGENTA_DYE_FROM_PURPLE_AND_PINK_RECIPE = Kee[str](
    'magenta_dye_from_purple_and_pink_recipe')
  MAGENTA_GLAZED_TERRACOTTA_RECIPE = Kee[str](
    'magenta_glazed_terracotta_recipe')
  MAGENTA_HARNESS_RECIPE = Kee[str]('magenta_harness_recipe')
  MAGENTA_SHULKER_BOX_RECIPE = Kee[str]('magenta_shulker_box_recipe')
  MAGENTA_STAINED_GLASS_PANE_FROM_GLASS_PANE_RECIPE = Kee[str](
    'magenta_stained_glass_pane_from_glass_pane_recipe')
  MAGENTA_STAINED_GLASS_PANE_RECIPE = Kee[str](
    'magenta_stained_glass_pane_recipe')
  MAGENTA_STAINED_GLASS_RECIPE = Kee[str]('magenta_stained_glass_recipe')
  MAGENTA_TERRACOTTA_RECIPE = Kee[str]('magenta_terracotta_recipe')
  MAGENTA_WOOL_RECIPE = Kee[str]('magenta_wool_recipe')
  MAGENTA_WOOL_SLAB_RECIPE = Kee[str]('magenta_wool_slab_recipe')
  MAGENTA_WOOL_STAIRS_RECIPE = Kee[str]('magenta_wool_stairs_recipe')
  MAGMA_BLOCK_RECIPE = Kee[str]('magma_block_recipe')
  MAGMA_CREAM_RECIPE = Kee[str]('magma_cream_recipe')
  MANGROVE_BOAT_RECIPE = Kee[str]('mangrove_boat_recipe')
  MANGROVE_BUTTON_RECIPE = Kee[str]('mangrove_button_recipe')
  MANGROVE_CHEST_BOAT_RECIPE = Kee[str]('mangrove_chest_boat_recipe')
  MANGROVE_DOOR_RECIPE = Kee[str]('mangrove_door_recipe')
  MANGROVE_FENCE_GATE_RECIPE = Kee[str]('mangrove_fence_gate_recipe')
  MANGROVE_FENCE_RECIPE = Kee[str]('mangrove_fence_recipe')
  MANGROVE_HANGING_SIGN_RECIPE = Kee[str]('mangrove_hanging_sign_recipe')
  MANGROVE_PLANKS_RECIPE = Kee[str]('mangrove_planks_recipe')
  MANGROVE_PRESSURE_PLATE_RECIPE = Kee[str]('mangrove_pressure_plate_recipe')
  MANGROVE_SHELF_RECIPE = Kee[str]('mangrove_shelf_recipe')
  MANGROVE_SIGN_RECIPE = Kee[str]('mangrove_sign_recipe')
  MANGROVE_SLAB_RECIPE = Kee[str]('mangrove_slab_recipe')
  MANGROVE_STAIRS_RECIPE = Kee[str]('mangrove_stairs_recipe')
  MANGROVE_TRAPDOOR_RECIPE = Kee[str]('mangrove_trapdoor_recipe')
  MANGROVE_WOOD_RECIPE = Kee[str]('mangrove_wood_recipe')
  MAP_CLONING_RECIPE = Kee[str]('map_cloning_recipe')
  MAP_RECIPE = Kee[str]('map_recipe')
  MELON_RECIPE = Kee[str]('melon_recipe')
  MELON_SEEDS_RECIPE = Kee[str]('melon_seeds_recipe')
  MINECART_RECIPE = Kee[str]('minecart_recipe')
  MINECRAFT_TRIAL_S_EDITION = Kee[str]('minecraft_trial_s_edition')
  MOB_KABOB = Kee[str]('mob_kabob')
  MOJANG_BANNER_PATTERN_RECIPE = Kee[str]('mojang_banner_pattern_recipe')
  MONSTER_HUNTER = Kee[str]('monster_hunter')
  MONSTERS_HUNTED = Kee[str]('monsters_hunted')
  MOSS_CARPET_RECIPE = Kee[str]('moss_carpet_recipe')
  MOSSY_COBBLESTONE_FROM_MOSS_BLOCK_RECIPE = Kee[str](
    'mossy_cobblestone_from_moss_block_recipe')
  MOSSY_COBBLESTONE_FROM_VINE_RECIPE = Kee[str](
    'mossy_cobblestone_from_vine_recipe')
  MOSSY_COBBLESTONE_RECIPE = Kee[str]('mossy_cobblestone_recipe')
  MOSSY_COBBLESTONE_SLAB_FROM_MOSSY_COBBLESTONE_STONECUTTING_RECIPE = Kee[str](
    'mossy_cobblestone_slab_from_mossy_cobblestone_stonecutting_recipe')
  MOSSY_COBBLESTONE_SLAB_RECIPE = Kee[str]('mossy_cobblestone_slab_recipe')
  MOSSY_COBBLESTONE_STAIRS_FROM_MOSSY_COBBLESTONE_STONECUTTING_RECIPE = Kee[str](
    'mossy_cobblestone_stairs_from_mossy_cobblestone_stonecutting_recipe')
  MOSSY_COBBLESTONE_STAIRS_RECIPE = Kee[str]('mossy_cobblestone_stairs_recipe')
  MOSSY_COBBLESTONE_WALL_FROM_MOSSY_COBBLESTONE_STONECUTTING_RECIPE = Kee[str](
    'mossy_cobblestone_wall_from_mossy_cobblestone_stonecutting_recipe')
  MOSSY_COBBLESTONE_WALL_RECIPE = Kee[str]('mossy_cobblestone_wall_recipe')
  MOSSY_STONE_BRICK_SLAB_FROM_MOSSY_STONE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'mossy_stone_brick_slab_from_mossy_stone_bricks_stonecutting_recipe')
  MOSSY_STONE_BRICK_SLAB_RECIPE = Kee[str]('mossy_stone_brick_slab_recipe')
  MOSSY_STONE_BRICK_STAIRS_FROM_MOSSY_STONE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'mossy_stone_brick_stairs_from_mossy_stone_bricks_stonecutting_recipe')
  MOSSY_STONE_BRICK_STAIRS_RECIPE = Kee[str]('mossy_stone_brick_stairs_recipe')
  MOSSY_STONE_BRICK_WALL_FROM_MOSSY_STONE_BRICK_STONECUTTING_RECIPE = Kee[str](
    'mossy_stone_brick_wall_from_mossy_stone_brick_stonecutting_recipe')
  MOSSY_STONE_BRICK_WALL_FROM_MOSSY_STONE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'mossy_stone_brick_wall_from_mossy_stone_bricks_stonecutting_recipe')
  MOSSY_STONE_BRICK_WALL_RECIPE = Kee[str]('mossy_stone_brick_wall_recipe')
  MOSSY_STONE_BRICKS_FROM_MOSS_BLOCK_RECIPE = Kee[str](
    'mossy_stone_bricks_from_moss_block_recipe')
  MOSSY_STONE_BRICKS_FROM_VINE_RECIPE = Kee[str](
    'mossy_stone_bricks_from_vine_recipe')
  MOSSY_STONE_BRICKS_RECIPE = Kee[str]('mossy_stone_bricks_recipe')
  MUD_BRICK_SLAB_FROM_MUD_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'mud_brick_slab_from_mud_bricks_stonecutting_recipe')
  MUD_BRICK_SLAB_RECIPE = Kee[str]('mud_brick_slab_recipe')
  MUD_BRICK_STAIRS_FROM_MUD_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'mud_brick_stairs_from_mud_bricks_stonecutting_recipe')
  MUD_BRICK_STAIRS_RECIPE = Kee[str]('mud_brick_stairs_recipe')
  MUD_BRICK_WALL_FROM_MUD_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'mud_brick_wall_from_mud_bricks_stonecutting_recipe')
  MUD_BRICK_WALL_RECIPE = Kee[str]('mud_brick_wall_recipe')
  MUD_BRICKS_RECIPE = Kee[str]('mud_bricks_recipe')
  MUDDY_MANGROVE_ROOTS_RECIPE = Kee[str]('muddy_mangrove_roots_recipe')
  MUSHROOM_STEW_RECIPE = Kee[str]('mushroom_stew_recipe')
  MUSIC_DISC_5_RECIPE = Kee[str]('music_disc_5_recipe')
  NAME_TAG_RECIPE = Kee[str]('name_tag_recipe')
  NETHER_BRICK_FENCE_RECIPE = Kee[str]('nether_brick_fence_recipe')
  NETHER_BRICK_RECIPE = Kee[str]('nether_brick_recipe')
  NETHER_BRICK_SLAB_FROM_NETHER_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'nether_brick_slab_from_nether_bricks_stonecutting_recipe')
  NETHER_BRICK_SLAB_RECIPE = Kee[str]('nether_brick_slab_recipe')
  NETHER_BRICK_STAIRS_FROM_NETHER_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'nether_brick_stairs_from_nether_bricks_stonecutting_recipe')
  NETHER_BRICK_STAIRS_RECIPE = Kee[str]('nether_brick_stairs_recipe')
  NETHER_BRICK_WALL_FROM_NETHER_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'nether_brick_wall_from_nether_bricks_stonecutting_recipe')
  NETHER_BRICK_WALL_RECIPE = Kee[str]('nether_brick_wall_recipe')
  NETHER_BRICKS_RECIPE = Kee[str]('nether_bricks_recipe')
  NETHER_ROOT = Kee[str]('nether_root')
  NETHER_WART_BLOCK_RECIPE = Kee[str]('nether_wart_block_recipe')
  NETHERITE_AXE_SMITHING_RECIPE = Kee[str]('netherite_axe_smithing_recipe')
  NETHERITE_BLOCK_RECIPE = Kee[str]('netherite_block_recipe')
  NETHERITE_BOOTS_SMITHING_RECIPE = Kee[str]('netherite_boots_smithing_recipe')
  NETHERITE_CHESTPLATE_SMITHING_RECIPE = Kee[str](
    'netherite_chestplate_smithing_recipe')
  NETHERITE_HELMET_SMITHING_RECIPE = Kee[str](
    'netherite_helmet_smithing_recipe')
  NETHERITE_HOE_SMITHING_RECIPE = Kee[str]('netherite_hoe_smithing_recipe')
  NETHERITE_HORSE_ARMOR_SMITHING_RECIPE = Kee[str](
    'netherite_horse_armor_smithing_recipe')
  NETHERITE_INGOT_FROM_NETHERITE_BLOCK_RECIPE = Kee[str](
    'netherite_ingot_from_netherite_block_recipe')
  NETHERITE_INGOT_RECIPE = Kee[str]('netherite_ingot_recipe')
  NETHERITE_LEGGINGS_SMITHING_RECIPE = Kee[str](
    'netherite_leggings_smithing_recipe')
  NETHERITE_NAUTILUS_ARMOR_SMITHING_RECIPE = Kee[str](
    'netherite_nautilus_armor_smithing_recipe')
  NETHERITE_PICKAXE_SMITHING_RECIPE = Kee[str](
    'netherite_pickaxe_smithing_recipe')
  NETHERITE_SCRAP_FROM_BLASTING_RECIPE = Kee[str](
    'netherite_scrap_from_blasting_recipe')
  NETHERITE_SCRAP_RECIPE = Kee[str]('netherite_scrap_recipe')
  NETHERITE_SHOVEL_SMITHING_RECIPE = Kee[str](
    'netherite_shovel_smithing_recipe')
  NETHERITE_SPEAR_SMITHING_RECIPE = Kee[str]('netherite_spear_smithing_recipe')
  NETHERITE_SWORD_SMITHING_RECIPE = Kee[str]('netherite_sword_smithing_recipe')
  NETHERITE_UPGRADE_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'netherite_upgrade_smithing_template_recipe')
  NOT_QUITE_NINE_LIVES = Kee[str]('not_quite_nine_lives')
  NOT_TODAY_THANK_YOU = Kee[str]('not_today_thank_you')
  NOTE_BLOCK_RECIPE = Kee[str]('note_block_recipe')
  OAK_BOAT_RECIPE = Kee[str]('oak_boat_recipe')
  OAK_BUTTON_RECIPE = Kee[str]('oak_button_recipe')
  OAK_CHEST_BOAT_RECIPE = Kee[str]('oak_chest_boat_recipe')
  OAK_DOOR_RECIPE = Kee[str]('oak_door_recipe')
  OAK_FENCE_GATE_RECIPE = Kee[str]('oak_fence_gate_recipe')
  OAK_FENCE_RECIPE = Kee[str]('oak_fence_recipe')
  OAK_HANGING_SIGN_RECIPE = Kee[str]('oak_hanging_sign_recipe')
  OAK_PLANKS_RECIPE = Kee[str]('oak_planks_recipe')
  OAK_PRESSURE_PLATE_RECIPE = Kee[str]('oak_pressure_plate_recipe')
  OAK_SHELF_RECIPE = Kee[str]('oak_shelf_recipe')
  OAK_SIGN_RECIPE = Kee[str]('oak_sign_recipe')
  OAK_SLAB_RECIPE = Kee[str]('oak_slab_recipe')
  OAK_STAIRS_RECIPE = Kee[str]('oak_stairs_recipe')
  OAK_TRAPDOOR_RECIPE = Kee[str]('oak_trapdoor_recipe')
  OAK_WOOD_RECIPE = Kee[str]('oak_wood_recipe')
  OBSERVER_RECIPE = Kee[str]('observer_recipe')
  OH_SHINY = Kee[str]('oh_shiny')
  OL_BETSY = Kee[str]('ol_betsy')
  ORANGE_BANNER_RECIPE = Kee[str]('orange_banner_recipe')
  ORANGE_BED_FROM_WHITE_BED_RECIPE = Kee[str](
    'orange_bed_from_white_bed_recipe')
  ORANGE_BED_RECIPE = Kee[str]('orange_bed_recipe')
  ORANGE_BUNDLE_RECIPE = Kee[str]('orange_bundle_recipe')
  ORANGE_CANDLE_RECIPE = Kee[str]('orange_candle_recipe')
  ORANGE_CARPET_FROM_WHITE_CARPET_RECIPE = Kee[str](
    'orange_carpet_from_white_carpet_recipe')
  ORANGE_CARPET_RECIPE = Kee[str]('orange_carpet_recipe')
  ORANGE_CONCRETE_POWDER_RECIPE = Kee[str]('orange_concrete_powder_recipe')
  ORANGE_CONCRETE_SLAB_FROM_ORANGE_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'orange_concrete_slab_from_orange_concrete_stonecutting_recipe')
  ORANGE_CONCRETE_SLAB_RECIPE = Kee[str]('orange_concrete_slab_recipe')
  ORANGE_CONCRETE_STAIRS_FROM_ORANGE_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'orange_concrete_stairs_from_orange_concrete_stonecutting_recipe')
  ORANGE_CONCRETE_STAIRS_RECIPE = Kee[str]('orange_concrete_stairs_recipe')
  ORANGE_CUSHION_RECIPE = Kee[str]('orange_cushion_recipe')
  ORANGE_DYE_FROM_OPEN_EYEBLOSSOM_RECIPE = Kee[str](
    'orange_dye_from_open_eyeblossom_recipe')
  ORANGE_DYE_FROM_ORANGE_TULIP_RECIPE = Kee[str](
    'orange_dye_from_orange_tulip_recipe')
  ORANGE_DYE_FROM_RED_YELLOW_RECIPE = Kee[str](
    'orange_dye_from_red_yellow_recipe')
  ORANGE_DYE_FROM_TORCHFLOWER_RECIPE = Kee[str](
    'orange_dye_from_torchflower_recipe')
  ORANGE_GLAZED_TERRACOTTA_RECIPE = Kee[str]('orange_glazed_terracotta_recipe')
  ORANGE_HARNESS_RECIPE = Kee[str]('orange_harness_recipe')
  ORANGE_SHULKER_BOX_RECIPE = Kee[str]('orange_shulker_box_recipe')
  ORANGE_STAINED_GLASS_PANE_FROM_GLASS_PANE_RECIPE = Kee[str](
    'orange_stained_glass_pane_from_glass_pane_recipe')
  ORANGE_STAINED_GLASS_PANE_RECIPE = Kee[str](
    'orange_stained_glass_pane_recipe')
  ORANGE_STAINED_GLASS_RECIPE = Kee[str]('orange_stained_glass_recipe')
  ORANGE_TERRACOTTA_RECIPE = Kee[str]('orange_terracotta_recipe')
  ORANGE_WOOL_RECIPE = Kee[str]('orange_wool_recipe')
  ORANGE_WOOL_SLAB_RECIPE = Kee[str]('orange_wool_slab_recipe')
  ORANGE_WOOL_STAIRS_RECIPE = Kee[str]('orange_wool_stairs_recipe')
  OVER_OVERKILL = Kee[str]('over_overkill')
  OXIDIZED_CHISELED_COPPER_FROM_OXIDIZED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'oxidized_chiseled_copper_from_oxidized_copper_stonecutting_recipe')
  OXIDIZED_CHISELED_COPPER_FROM_OXIDIZED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'oxidized_chiseled_copper_from_oxidized_cut_copper_stonecutting_recipe')
  OXIDIZED_CHISELED_COPPER_RECIPE = Kee[str]('oxidized_chiseled_copper_recipe')
  OXIDIZED_COPPER_BULB_RECIPE = Kee[str]('oxidized_copper_bulb_recipe')
  OXIDIZED_COPPER_GRATE_FROM_OXIDIZED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'oxidized_copper_grate_from_oxidized_copper_stonecutting_recipe')
  OXIDIZED_COPPER_GRATE_RECIPE = Kee[str]('oxidized_copper_grate_recipe')
  OXIDIZED_CUT_COPPER_FROM_OXIDIZED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'oxidized_cut_copper_from_oxidized_copper_stonecutting_recipe')
  OXIDIZED_CUT_COPPER_RECIPE = Kee[str]('oxidized_cut_copper_recipe')
  OXIDIZED_CUT_COPPER_SLAB_FROM_OXIDIZED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'oxidized_cut_copper_slab_from_oxidized_copper_stonecutting_recipe')
  OXIDIZED_CUT_COPPER_SLAB_FROM_OXIDIZED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'oxidized_cut_copper_slab_from_oxidized_cut_copper_stonecutting_recipe')
  OXIDIZED_CUT_COPPER_SLAB_RECIPE = Kee[str]('oxidized_cut_copper_slab_recipe')
  OXIDIZED_CUT_COPPER_STAIRS_FROM_OXIDIZED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'oxidized_cut_copper_stairs_from_oxidized_copper_stonecutting_recipe')
  OXIDIZED_CUT_COPPER_STAIRS_FROM_OXIDIZED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'oxidized_cut_copper_stairs_from_oxidized_cut_copper_stonecutting_recipe')
  OXIDIZED_CUT_COPPER_STAIRS_RECIPE = Kee[str](
    'oxidized_cut_copper_stairs_recipe')
  PACKED_ICE_RECIPE = Kee[str]('packed_ice_recipe')
  PACKED_MUD_RECIPE = Kee[str]('packed_mud_recipe')
  PAINTING_RECIPE = Kee[str]('painting_recipe')
  PALE_MOSS_CARPET_RECIPE = Kee[str]('pale_moss_carpet_recipe')
  PALE_OAK_BOAT_RECIPE = Kee[str]('pale_oak_boat_recipe')
  PALE_OAK_BUTTON_RECIPE = Kee[str]('pale_oak_button_recipe')
  PALE_OAK_CHEST_BOAT_RECIPE = Kee[str]('pale_oak_chest_boat_recipe')
  PALE_OAK_DOOR_RECIPE = Kee[str]('pale_oak_door_recipe')
  PALE_OAK_FENCE_GATE_RECIPE = Kee[str]('pale_oak_fence_gate_recipe')
  PALE_OAK_FENCE_RECIPE = Kee[str]('pale_oak_fence_recipe')
  PALE_OAK_HANGING_SIGN_RECIPE = Kee[str]('pale_oak_hanging_sign_recipe')
  PALE_OAK_PLANKS_RECIPE = Kee[str]('pale_oak_planks_recipe')
  PALE_OAK_PRESSURE_PLATE_RECIPE = Kee[str]('pale_oak_pressure_plate_recipe')
  PALE_OAK_SHELF_RECIPE = Kee[str]('pale_oak_shelf_recipe')
  PALE_OAK_SIGN_RECIPE = Kee[str]('pale_oak_sign_recipe')
  PALE_OAK_SLAB_RECIPE = Kee[str]('pale_oak_slab_recipe')
  PALE_OAK_STAIRS_RECIPE = Kee[str]('pale_oak_stairs_recipe')
  PALE_OAK_TRAPDOOR_RECIPE = Kee[str]('pale_oak_trapdoor_recipe')
  PALE_OAK_WOOD_RECIPE = Kee[str]('pale_oak_wood_recipe')
  PAPER_RECIPE = Kee[str]('paper_recipe')
  PINK_BANNER_RECIPE = Kee[str]('pink_banner_recipe')
  PINK_BED_FROM_WHITE_BED_RECIPE = Kee[str]('pink_bed_from_white_bed_recipe')
  PINK_BED_RECIPE = Kee[str]('pink_bed_recipe')
  PINK_BUNDLE_RECIPE = Kee[str]('pink_bundle_recipe')
  PINK_CANDLE_RECIPE = Kee[str]('pink_candle_recipe')
  PINK_CARPET_FROM_WHITE_CARPET_RECIPE = Kee[str](
    'pink_carpet_from_white_carpet_recipe')
  PINK_CARPET_RECIPE = Kee[str]('pink_carpet_recipe')
  PINK_CONCRETE_POWDER_RECIPE = Kee[str]('pink_concrete_powder_recipe')
  PINK_CONCRETE_SLAB_FROM_PINK_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'pink_concrete_slab_from_pink_concrete_stonecutting_recipe')
  PINK_CONCRETE_SLAB_RECIPE = Kee[str]('pink_concrete_slab_recipe')
  PINK_CONCRETE_STAIRS_FROM_PINK_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'pink_concrete_stairs_from_pink_concrete_stonecutting_recipe')
  PINK_CONCRETE_STAIRS_RECIPE = Kee[str]('pink_concrete_stairs_recipe')
  PINK_CUSHION_RECIPE = Kee[str]('pink_cushion_recipe')
  PINK_DYE_FROM_CACTUS_FLOWER_RECIPE = Kee[str](
    'pink_dye_from_cactus_flower_recipe')
  PINK_DYE_FROM_PEONY_RECIPE = Kee[str]('pink_dye_from_peony_recipe')
  PINK_DYE_FROM_PINK_PETALS_RECIPE = Kee[str](
    'pink_dye_from_pink_petals_recipe')
  PINK_DYE_FROM_PINK_TULIP_RECIPE = Kee[str]('pink_dye_from_pink_tulip_recipe')
  PINK_DYE_FROM_RED_BONEMEAL_RECIPE = Kee[str](
    'pink_dye_from_red_bonemeal_recipe')
  PINK_DYE_FROM_RED_WHITE_DYE_RECIPE = Kee[str](
    'pink_dye_from_red_white_dye_recipe')
  PINK_GLAZED_TERRACOTTA_RECIPE = Kee[str]('pink_glazed_terracotta_recipe')
  PINK_HARNESS_RECIPE = Kee[str]('pink_harness_recipe')
  PINK_SHULKER_BOX_RECIPE = Kee[str]('pink_shulker_box_recipe')
  PINK_STAINED_GLASS_PANE_FROM_GLASS_PANE_RECIPE = Kee[str](
    'pink_stained_glass_pane_from_glass_pane_recipe')
  PINK_STAINED_GLASS_PANE_RECIPE = Kee[str]('pink_stained_glass_pane_recipe')
  PINK_STAINED_GLASS_RECIPE = Kee[str]('pink_stained_glass_recipe')
  PINK_TERRACOTTA_RECIPE = Kee[str]('pink_terracotta_recipe')
  PINK_WOOL_RECIPE = Kee[str]('pink_wool_recipe')
  PINK_WOOL_SLAB_RECIPE = Kee[str]('pink_wool_slab_recipe')
  PINK_WOOL_STAIRS_RECIPE = Kee[str]('pink_wool_stairs_recipe')
  PISTON_RECIPE = Kee[str]('piston_recipe')
  PLANTING_THE_PAST = Kee[str]('planting_the_past')
  POLISHED_ANDESITE_FROM_ANDESITE_STONECUTTING_RECIPE = Kee[str](
    'polished_andesite_from_andesite_stonecutting_recipe')
  POLISHED_ANDESITE_RECIPE = Kee[str]('polished_andesite_recipe')
  POLISHED_ANDESITE_SLAB_FROM_ANDESITE_STONECUTTING_RECIPE = Kee[str](
    'polished_andesite_slab_from_andesite_stonecutting_recipe')
  POLISHED_ANDESITE_SLAB_FROM_POLISHED_ANDESITE_STONECUTTING_RECIPE = Kee[str](
    'polished_andesite_slab_from_polished_andesite_stonecutting_recipe')
  POLISHED_ANDESITE_SLAB_RECIPE = Kee[str]('polished_andesite_slab_recipe')
  POLISHED_ANDESITE_STAIRS_FROM_ANDESITE_STONECUTTING_RECIPE = Kee[str](
    'polished_andesite_stairs_from_andesite_stonecutting_recipe')
  POLISHED_ANDESITE_STAIRS_FROM_POLISHED_ANDESITE_STONECUTTING_RECIPE = Kee[str](
    'polished_andesite_stairs_from_polished_andesite_stonecutting_recipe')
  POLISHED_ANDESITE_STAIRS_RECIPE = Kee[str]('polished_andesite_stairs_recipe')
  POLISHED_BASALT_FROM_BASALT_STONECUTTING_RECIPE = Kee[str](
    'polished_basalt_from_basalt_stonecutting_recipe')
  POLISHED_BASALT_RECIPE = Kee[str]('polished_basalt_recipe')
  POLISHED_BLACKSTONE_BRICK_SLAB_FROM_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_brick_slab_from_blackstone_stonecutting_recipe')
  POLISHED_BLACKSTONE_BRICK_SLAB_FROM_POLISHED_BLACKSTONE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_brick_slab_from_polished_blackstone_bricks_stonecutting_recipe')
  POLISHED_BLACKSTONE_BRICK_SLAB_FROM_POLISHED_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_brick_slab_from_polished_blackstone_stonecutting_recipe')
  POLISHED_BLACKSTONE_BRICK_SLAB_RECIPE = Kee[str](
    'polished_blackstone_brick_slab_recipe')
  POLISHED_BLACKSTONE_BRICK_STAIRS_FROM_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_brick_stairs_from_blackstone_stonecutting_recipe')
  POLISHED_BLACKSTONE_BRICK_STAIRS_FROM_POLISHED_BLACKSTONE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_brick_stairs_from_polished_blackstone_bricks_stonecutting_recipe')
  POLISHED_BLACKSTONE_BRICK_STAIRS_FROM_POLISHED_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_brick_stairs_from_polished_blackstone_stonecutting_recipe')
  POLISHED_BLACKSTONE_BRICK_STAIRS_RECIPE = Kee[str](
    'polished_blackstone_brick_stairs_recipe')
  POLISHED_BLACKSTONE_BRICK_WALL_FROM_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_brick_wall_from_blackstone_stonecutting_recipe')
  POLISHED_BLACKSTONE_BRICK_WALL_FROM_POLISHED_BLACKSTONE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_brick_wall_from_polished_blackstone_bricks_stonecutting_recipe')
  POLISHED_BLACKSTONE_BRICK_WALL_FROM_POLISHED_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_brick_wall_from_polished_blackstone_stonecutting_recipe')
  POLISHED_BLACKSTONE_BRICK_WALL_RECIPE = Kee[str](
    'polished_blackstone_brick_wall_recipe')
  POLISHED_BLACKSTONE_BRICKS_FROM_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_bricks_from_blackstone_stonecutting_recipe')
  POLISHED_BLACKSTONE_BRICKS_FROM_POLISHED_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_bricks_from_polished_blackstone_stonecutting_recipe')
  POLISHED_BLACKSTONE_BRICKS_RECIPE = Kee[str](
    'polished_blackstone_bricks_recipe')
  POLISHED_BLACKSTONE_BUTTON_RECIPE = Kee[str](
    'polished_blackstone_button_recipe')
  POLISHED_BLACKSTONE_FROM_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_from_blackstone_stonecutting_recipe')
  POLISHED_BLACKSTONE_PRESSURE_PLATE_RECIPE = Kee[str](
    'polished_blackstone_pressure_plate_recipe')
  POLISHED_BLACKSTONE_RECIPE = Kee[str]('polished_blackstone_recipe')
  POLISHED_BLACKSTONE_SLAB_FROM_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_slab_from_blackstone_stonecutting_recipe')
  POLISHED_BLACKSTONE_SLAB_FROM_POLISHED_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_slab_from_polished_blackstone_stonecutting_recipe')
  POLISHED_BLACKSTONE_SLAB_RECIPE = Kee[str]('polished_blackstone_slab_recipe')
  POLISHED_BLACKSTONE_STAIRS_FROM_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_stairs_from_blackstone_stonecutting_recipe')
  POLISHED_BLACKSTONE_STAIRS_FROM_POLISHED_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_stairs_from_polished_blackstone_stonecutting_recipe')
  POLISHED_BLACKSTONE_STAIRS_RECIPE = Kee[str](
    'polished_blackstone_stairs_recipe')
  POLISHED_BLACKSTONE_WALL_FROM_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_wall_from_blackstone_stonecutting_recipe')
  POLISHED_BLACKSTONE_WALL_FROM_POLISHED_BLACKSTONE_STONECUTTING_RECIPE = Kee[str](
    'polished_blackstone_wall_from_polished_blackstone_stonecutting_recipe')
  POLISHED_BLACKSTONE_WALL_RECIPE = Kee[str]('polished_blackstone_wall_recipe')
  POLISHED_CINNABAR_FROM_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'polished_cinnabar_from_cinnabar_stonecutting_recipe')
  POLISHED_CINNABAR_RECIPE = Kee[str]('polished_cinnabar_recipe')
  POLISHED_CINNABAR_SLAB_FROM_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'polished_cinnabar_slab_from_cinnabar_stonecutting_recipe')
  POLISHED_CINNABAR_SLAB_FROM_POLISHED_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'polished_cinnabar_slab_from_polished_cinnabar_stonecutting_recipe')
  POLISHED_CINNABAR_SLAB_RECIPE = Kee[str]('polished_cinnabar_slab_recipe')
  POLISHED_CINNABAR_STAIRS_FROM_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'polished_cinnabar_stairs_from_cinnabar_stonecutting_recipe')
  POLISHED_CINNABAR_STAIRS_FROM_POLISHED_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'polished_cinnabar_stairs_from_polished_cinnabar_stonecutting_recipe')
  POLISHED_CINNABAR_STAIRS_RECIPE = Kee[str]('polished_cinnabar_stairs_recipe')
  POLISHED_CINNABAR_WALL_FROM_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'polished_cinnabar_wall_from_cinnabar_stonecutting_recipe')
  POLISHED_CINNABAR_WALL_FROM_POLISHED_CINNABAR_STONECUTTING_RECIPE = Kee[str](
    'polished_cinnabar_wall_from_polished_cinnabar_stonecutting_recipe')
  POLISHED_CINNABAR_WALL_RECIPE = Kee[str]('polished_cinnabar_wall_recipe')
  POLISHED_DEEPSLATE_FROM_COBBLED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'polished_deepslate_from_cobbled_deepslate_stonecutting_recipe')
  POLISHED_DEEPSLATE_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'polished_deepslate_from_deepslate_stonecutting_recipe')
  POLISHED_DEEPSLATE_RECIPE = Kee[str]('polished_deepslate_recipe')
  POLISHED_DEEPSLATE_SLAB_FROM_COBBLED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'polished_deepslate_slab_from_cobbled_deepslate_stonecutting_recipe')
  POLISHED_DEEPSLATE_SLAB_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'polished_deepslate_slab_from_deepslate_stonecutting_recipe')
  POLISHED_DEEPSLATE_SLAB_FROM_POLISHED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'polished_deepslate_slab_from_polished_deepslate_stonecutting_recipe')
  POLISHED_DEEPSLATE_SLAB_RECIPE = Kee[str]('polished_deepslate_slab_recipe')
  POLISHED_DEEPSLATE_STAIRS_FROM_COBBLED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'polished_deepslate_stairs_from_cobbled_deepslate_stonecutting_recipe')
  POLISHED_DEEPSLATE_STAIRS_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'polished_deepslate_stairs_from_deepslate_stonecutting_recipe')
  POLISHED_DEEPSLATE_STAIRS_FROM_POLISHED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'polished_deepslate_stairs_from_polished_deepslate_stonecutting_recipe')
  POLISHED_DEEPSLATE_STAIRS_RECIPE = Kee[str](
    'polished_deepslate_stairs_recipe')
  POLISHED_DEEPSLATE_WALL_FROM_COBBLED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'polished_deepslate_wall_from_cobbled_deepslate_stonecutting_recipe')
  POLISHED_DEEPSLATE_WALL_FROM_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'polished_deepslate_wall_from_deepslate_stonecutting_recipe')
  POLISHED_DEEPSLATE_WALL_FROM_POLISHED_DEEPSLATE_STONECUTTING_RECIPE = Kee[str](
    'polished_deepslate_wall_from_polished_deepslate_stonecutting_recipe')
  POLISHED_DEEPSLATE_WALL_RECIPE = Kee[str]('polished_deepslate_wall_recipe')
  POLISHED_DIORITE_FROM_DIORITE_STONECUTTING_RECIPE = Kee[str](
    'polished_diorite_from_diorite_stonecutting_recipe')
  POLISHED_DIORITE_RECIPE = Kee[str]('polished_diorite_recipe')
  POLISHED_DIORITE_SLAB_FROM_DIORITE_STONECUTTING_RECIPE = Kee[str](
    'polished_diorite_slab_from_diorite_stonecutting_recipe')
  POLISHED_DIORITE_SLAB_FROM_POLISHED_DIORITE_STONECUTTING_RECIPE = Kee[str](
    'polished_diorite_slab_from_polished_diorite_stonecutting_recipe')
  POLISHED_DIORITE_SLAB_RECIPE = Kee[str]('polished_diorite_slab_recipe')
  POLISHED_DIORITE_STAIRS_FROM_DIORITE_STONECUTTING_RECIPE = Kee[str](
    'polished_diorite_stairs_from_diorite_stonecutting_recipe')
  POLISHED_DIORITE_STAIRS_FROM_POLISHED_DIORITE_STONECUTTING_RECIPE = Kee[str](
    'polished_diorite_stairs_from_polished_diorite_stonecutting_recipe')
  POLISHED_DIORITE_STAIRS_RECIPE = Kee[str]('polished_diorite_stairs_recipe')
  POLISHED_GRANITE_FROM_GRANITE_STONECUTTING_RECIPE = Kee[str](
    'polished_granite_from_granite_stonecutting_recipe')
  POLISHED_GRANITE_RECIPE = Kee[str]('polished_granite_recipe')
  POLISHED_GRANITE_SLAB_FROM_GRANITE_STONECUTTING_RECIPE = Kee[str](
    'polished_granite_slab_from_granite_stonecutting_recipe')
  POLISHED_GRANITE_SLAB_FROM_POLISHED_GRANITE_STONECUTTING_RECIPE = Kee[str](
    'polished_granite_slab_from_polished_granite_stonecutting_recipe')
  POLISHED_GRANITE_SLAB_RECIPE = Kee[str]('polished_granite_slab_recipe')
  POLISHED_GRANITE_STAIRS_FROM_GRANITE_STONECUTTING_RECIPE = Kee[str](
    'polished_granite_stairs_from_granite_stonecutting_recipe')
  POLISHED_GRANITE_STAIRS_FROM_POLISHED_GRANITE_STONECUTTING_RECIPE = Kee[str](
    'polished_granite_stairs_from_polished_granite_stonecutting_recipe')
  POLISHED_GRANITE_STAIRS_RECIPE = Kee[str]('polished_granite_stairs_recipe')
  POLISHED_SULFUR_FROM_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'polished_sulfur_from_sulfur_stonecutting_recipe')
  POLISHED_SULFUR_RECIPE = Kee[str]('polished_sulfur_recipe')
  POLISHED_SULFUR_SLAB_FROM_POLISHED_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'polished_sulfur_slab_from_polished_sulfur_stonecutting_recipe')
  POLISHED_SULFUR_SLAB_FROM_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'polished_sulfur_slab_from_sulfur_stonecutting_recipe')
  POLISHED_SULFUR_SLAB_RECIPE = Kee[str]('polished_sulfur_slab_recipe')
  POLISHED_SULFUR_STAIRS_FROM_POLISHED_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'polished_sulfur_stairs_from_polished_sulfur_stonecutting_recipe')
  POLISHED_SULFUR_STAIRS_FROM_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'polished_sulfur_stairs_from_sulfur_stonecutting_recipe')
  POLISHED_SULFUR_STAIRS_RECIPE = Kee[str]('polished_sulfur_stairs_recipe')
  POLISHED_SULFUR_WALL_FROM_POLISHED_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'polished_sulfur_wall_from_polished_sulfur_stonecutting_recipe')
  POLISHED_SULFUR_WALL_FROM_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'polished_sulfur_wall_from_sulfur_stonecutting_recipe')
  POLISHED_SULFUR_WALL_RECIPE = Kee[str]('polished_sulfur_wall_recipe')
  POLISHED_TUFF_FROM_TUFF_STONECUTTING_RECIPE = Kee[str](
    'polished_tuff_from_tuff_stonecutting_recipe')
  POLISHED_TUFF_RECIPE = Kee[str]('polished_tuff_recipe')
  POLISHED_TUFF_SLAB_FROM_POLISHED_TUFF_STONECUTTING_RECIPE = Kee[str](
    'polished_tuff_slab_from_polished_tuff_stonecutting_recipe')
  POLISHED_TUFF_SLAB_FROM_TUFF_STONECUTTING_RECIPE = Kee[str](
    'polished_tuff_slab_from_tuff_stonecutting_recipe')
  POLISHED_TUFF_SLAB_RECIPE = Kee[str]('polished_tuff_slab_recipe')
  POLISHED_TUFF_STAIRS_FROM_POLISHED_TUFF_STONECUTTING_RECIPE = Kee[str](
    'polished_tuff_stairs_from_polished_tuff_stonecutting_recipe')
  POLISHED_TUFF_STAIRS_FROM_TUFF_STONECUTTING_RECIPE = Kee[str](
    'polished_tuff_stairs_from_tuff_stonecutting_recipe')
  POLISHED_TUFF_STAIRS_RECIPE = Kee[str]('polished_tuff_stairs_recipe')
  POLISHED_TUFF_WALL_FROM_POLISHED_TUFF_STONECUTTING_RECIPE = Kee[str](
    'polished_tuff_wall_from_polished_tuff_stonecutting_recipe')
  POLISHED_TUFF_WALL_FROM_TUFF_STONECUTTING_RECIPE = Kee[str](
    'polished_tuff_wall_from_tuff_stonecutting_recipe')
  POLISHED_TUFF_WALL_RECIPE = Kee[str]('polished_tuff_wall_recipe')
  POPLAR_BOAT_RECIPE = Kee[str]('poplar_boat_recipe')
  POPLAR_BUTTON_RECIPE = Kee[str]('poplar_button_recipe')
  POPLAR_CHEST_BOAT_RECIPE = Kee[str]('poplar_chest_boat_recipe')
  POPLAR_DOOR_RECIPE = Kee[str]('poplar_door_recipe')
  POPLAR_FENCE_GATE_RECIPE = Kee[str]('poplar_fence_gate_recipe')
  POPLAR_FENCE_RECIPE = Kee[str]('poplar_fence_recipe')
  POPLAR_HANGING_SIGN_RECIPE = Kee[str]('poplar_hanging_sign_recipe')
  POPLAR_PLANKS_RECIPE = Kee[str]('poplar_planks_recipe')
  POPLAR_PRESSURE_PLATE_RECIPE = Kee[str]('poplar_pressure_plate_recipe')
  POPLAR_SHELF_RECIPE = Kee[str]('poplar_shelf_recipe')
  POPLAR_SIGN_RECIPE = Kee[str]('poplar_sign_recipe')
  POPLAR_SLAB_RECIPE = Kee[str]('poplar_slab_recipe')
  POPLAR_STAIRS_RECIPE = Kee[str]('poplar_stairs_recipe')
  POPLAR_TRAPDOOR_RECIPE = Kee[str]('poplar_trapdoor_recipe')
  POPLAR_WOOD_RECIPE = Kee[str]('poplar_wood_recipe')
  POPPED_CHORUS_FRUIT_RECIPE = Kee[str]('popped_chorus_fruit_recipe')
  POSTMORTAL = Kee[str]('postmortal')
  POTENT_SULFUR_RECIPE = Kee[str]('potent_sulfur_recipe')
  POWERED_RAIL_RECIPE = Kee[str]('powered_rail_recipe')
  PRISMARINE_BRICK_SLAB_FROM_PRISMARINE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'prismarine_brick_slab_from_prismarine_bricks_stonecutting_recipe')
  PRISMARINE_BRICK_SLAB_RECIPE = Kee[str]('prismarine_brick_slab_recipe')
  PRISMARINE_BRICK_STAIRS_FROM_PRISMARINE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'prismarine_brick_stairs_from_prismarine_bricks_stonecutting_recipe')
  PRISMARINE_BRICK_STAIRS_RECIPE = Kee[str]('prismarine_brick_stairs_recipe')
  PRISMARINE_BRICKS_RECIPE = Kee[str]('prismarine_bricks_recipe')
  PRISMARINE_RECIPE = Kee[str]('prismarine_recipe')
  PRISMARINE_SLAB_FROM_PRISMARINE_STONECUTTING_RECIPE = Kee[str](
    'prismarine_slab_from_prismarine_stonecutting_recipe')
  PRISMARINE_SLAB_RECIPE = Kee[str]('prismarine_slab_recipe')
  PRISMARINE_STAIRS_FROM_PRISMARINE_STONECUTTING_RECIPE = Kee[str](
    'prismarine_stairs_from_prismarine_stonecutting_recipe')
  PRISMARINE_STAIRS_RECIPE = Kee[str]('prismarine_stairs_recipe')
  PRISMARINE_WALL_FROM_PRISMARINE_STONECUTTING_RECIPE = Kee[str](
    'prismarine_wall_from_prismarine_stonecutting_recipe')
  PRISMARINE_WALL_RECIPE = Kee[str]('prismarine_wall_recipe')
  PUMPKIN_PIE_RECIPE = Kee[str]('pumpkin_pie_recipe')
  PUMPKIN_SEEDS_RECIPE = Kee[str]('pumpkin_seeds_recipe')
  PURPLE_BANNER_RECIPE = Kee[str]('purple_banner_recipe')
  PURPLE_BED_FROM_WHITE_BED_RECIPE = Kee[str](
    'purple_bed_from_white_bed_recipe')
  PURPLE_BED_RECIPE = Kee[str]('purple_bed_recipe')
  PURPLE_BUNDLE_RECIPE = Kee[str]('purple_bundle_recipe')
  PURPLE_CANDLE_RECIPE = Kee[str]('purple_candle_recipe')
  PURPLE_CARPET_FROM_WHITE_CARPET_RECIPE = Kee[str](
    'purple_carpet_from_white_carpet_recipe')
  PURPLE_CARPET_RECIPE = Kee[str]('purple_carpet_recipe')
  PURPLE_CONCRETE_POWDER_RECIPE = Kee[str]('purple_concrete_powder_recipe')
  PURPLE_CONCRETE_SLAB_FROM_PURPLE_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'purple_concrete_slab_from_purple_concrete_stonecutting_recipe')
  PURPLE_CONCRETE_SLAB_RECIPE = Kee[str]('purple_concrete_slab_recipe')
  PURPLE_CONCRETE_STAIRS_FROM_PURPLE_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'purple_concrete_stairs_from_purple_concrete_stonecutting_recipe')
  PURPLE_CONCRETE_STAIRS_RECIPE = Kee[str]('purple_concrete_stairs_recipe')
  PURPLE_CUSHION_RECIPE = Kee[str]('purple_cushion_recipe')
  PURPLE_DYE_RECIPE = Kee[str]('purple_dye_recipe')
  PURPLE_GLAZED_TERRACOTTA_RECIPE = Kee[str]('purple_glazed_terracotta_recipe')
  PURPLE_HARNESS_RECIPE = Kee[str]('purple_harness_recipe')
  PURPLE_SHULKER_BOX_RECIPE = Kee[str]('purple_shulker_box_recipe')
  PURPLE_STAINED_GLASS_PANE_FROM_GLASS_PANE_RECIPE = Kee[str](
    'purple_stained_glass_pane_from_glass_pane_recipe')
  PURPLE_STAINED_GLASS_PANE_RECIPE = Kee[str](
    'purple_stained_glass_pane_recipe')
  PURPLE_STAINED_GLASS_RECIPE = Kee[str]('purple_stained_glass_recipe')
  PURPLE_TERRACOTTA_RECIPE = Kee[str]('purple_terracotta_recipe')
  PURPLE_WOOL_RECIPE = Kee[str]('purple_wool_recipe')
  PURPLE_WOOL_SLAB_RECIPE = Kee[str]('purple_wool_slab_recipe')
  PURPLE_WOOL_STAIRS_RECIPE = Kee[str]('purple_wool_stairs_recipe')
  PURPUR_BLOCK_RECIPE = Kee[str]('purpur_block_recipe')
  PURPUR_PILLAR_FROM_PURPUR_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'purpur_pillar_from_purpur_block_stonecutting_recipe')
  PURPUR_PILLAR_RECIPE = Kee[str]('purpur_pillar_recipe')
  PURPUR_SLAB_FROM_PURPUR_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'purpur_slab_from_purpur_block_stonecutting_recipe')
  PURPUR_SLAB_RECIPE = Kee[str]('purpur_slab_recipe')
  PURPUR_STAIRS_FROM_PURPUR_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'purpur_stairs_from_purpur_block_stonecutting_recipe')
  PURPUR_STAIRS_RECIPE = Kee[str]('purpur_stairs_recipe')
  QUARTZ_BLOCK_RECIPE = Kee[str]('quartz_block_recipe')
  QUARTZ_BRICKS_FROM_QUARTZ_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'quartz_bricks_from_quartz_block_stonecutting_recipe')
  QUARTZ_BRICKS_RECIPE = Kee[str]('quartz_bricks_recipe')
  QUARTZ_FROM_BLASTING_RECIPE = Kee[str]('quartz_from_blasting_recipe')
  QUARTZ_PILLAR_FROM_QUARTZ_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'quartz_pillar_from_quartz_block_stonecutting_recipe')
  QUARTZ_PILLAR_RECIPE = Kee[str]('quartz_pillar_recipe')
  QUARTZ_RECIPE = Kee[str]('quartz_recipe')
  QUARTZ_SLAB_FROM_QUARTZ_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'quartz_slab_from_quartz_block_stonecutting_recipe')
  QUARTZ_SLAB_RECIPE = Kee[str]('quartz_slab_recipe')
  QUARTZ_STAIRS_FROM_QUARTZ_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'quartz_stairs_from_quartz_block_stonecutting_recipe')
  QUARTZ_STAIRS_RECIPE = Kee[str]('quartz_stairs_recipe')
  RABBIT_STEW_FROM_BROWN_MUSHROOM_RECIPE = Kee[str](
    'rabbit_stew_from_brown_mushroom_recipe')
  RABBIT_STEW_FROM_RED_MUSHROOM_RECIPE = Kee[str](
    'rabbit_stew_from_red_mushroom_recipe')
  RABBIT_STEW_FROM_SHELF_MUSHROOM_RECIPE = Kee[str](
    'rabbit_stew_from_shelf_mushroom_recipe')
  RAIL_RECIPE = Kee[str]('rail_recipe')
  RAISER_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'raiser_armor_trim_smithing_template_recipe')
  RAISER_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'raiser_armor_trim_smithing_template_smithing_trim_recipe')
  RAW_COPPER_BLOCK_RECIPE = Kee[str]('raw_copper_block_recipe')
  RAW_COPPER_RECIPE = Kee[str]('raw_copper_recipe')
  RAW_GOLD_BLOCK_RECIPE = Kee[str]('raw_gold_block_recipe')
  RAW_GOLD_RECIPE = Kee[str]('raw_gold_recipe')
  RAW_IRON_BLOCK_RECIPE = Kee[str]('raw_iron_block_recipe')
  RAW_IRON_RECIPE = Kee[str]('raw_iron_recipe')
  RECOVERY_COMPASS_RECIPE = Kee[str]('recovery_compass_recipe')
  RED_BANNER_RECIPE = Kee[str]('red_banner_recipe')
  RED_BED_FROM_WHITE_BED_RECIPE = Kee[str]('red_bed_from_white_bed_recipe')
  RED_BED_RECIPE = Kee[str]('red_bed_recipe')
  RED_BUNDLE_RECIPE = Kee[str]('red_bundle_recipe')
  RED_CANDLE_RECIPE = Kee[str]('red_candle_recipe')
  RED_CARPET_FROM_WHITE_CARPET_RECIPE = Kee[str](
    'red_carpet_from_white_carpet_recipe')
  RED_CARPET_RECIPE = Kee[str]('red_carpet_recipe')
  RED_CONCRETE_POWDER_RECIPE = Kee[str]('red_concrete_powder_recipe')
  RED_CONCRETE_SLAB_FROM_RED_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'red_concrete_slab_from_red_concrete_stonecutting_recipe')
  RED_CONCRETE_SLAB_RECIPE = Kee[str]('red_concrete_slab_recipe')
  RED_CONCRETE_STAIRS_FROM_RED_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'red_concrete_stairs_from_red_concrete_stonecutting_recipe')
  RED_CONCRETE_STAIRS_RECIPE = Kee[str]('red_concrete_stairs_recipe')
  RED_CUSHION_RECIPE = Kee[str]('red_cushion_recipe')
  RED_DYE_FROM_BEETROOT_RECIPE = Kee[str]('red_dye_from_beetroot_recipe')
  RED_DYE_FROM_POPPY_RECIPE = Kee[str]('red_dye_from_poppy_recipe')
  RED_DYE_FROM_ROSE_BUSH_RECIPE = Kee[str]('red_dye_from_rose_bush_recipe')
  RED_DYE_FROM_TULIP_RECIPE = Kee[str]('red_dye_from_tulip_recipe')
  RED_GLAZED_TERRACOTTA_RECIPE = Kee[str]('red_glazed_terracotta_recipe')
  RED_HARNESS_RECIPE = Kee[str]('red_harness_recipe')
  RED_NETHER_BRICK_SLAB_FROM_RED_NETHER_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'red_nether_brick_slab_from_red_nether_bricks_stonecutting_recipe')
  RED_NETHER_BRICK_SLAB_RECIPE = Kee[str]('red_nether_brick_slab_recipe')
  RED_NETHER_BRICK_STAIRS_FROM_RED_NETHER_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'red_nether_brick_stairs_from_red_nether_bricks_stonecutting_recipe')
  RED_NETHER_BRICK_STAIRS_RECIPE = Kee[str]('red_nether_brick_stairs_recipe')
  RED_NETHER_BRICK_WALL_FROM_RED_NETHER_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'red_nether_brick_wall_from_red_nether_bricks_stonecutting_recipe')
  RED_NETHER_BRICK_WALL_RECIPE = Kee[str]('red_nether_brick_wall_recipe')
  RED_NETHER_BRICKS_RECIPE = Kee[str]('red_nether_bricks_recipe')
  RED_SANDSTONE_RECIPE = Kee[str]('red_sandstone_recipe')
  RED_SANDSTONE_SLAB_FROM_RED_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'red_sandstone_slab_from_red_sandstone_stonecutting_recipe')
  RED_SANDSTONE_SLAB_RECIPE = Kee[str]('red_sandstone_slab_recipe')
  RED_SANDSTONE_STAIRS_FROM_RED_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'red_sandstone_stairs_from_red_sandstone_stonecutting_recipe')
  RED_SANDSTONE_STAIRS_RECIPE = Kee[str]('red_sandstone_stairs_recipe')
  RED_SANDSTONE_WALL_FROM_RED_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'red_sandstone_wall_from_red_sandstone_stonecutting_recipe')
  RED_SANDSTONE_WALL_RECIPE = Kee[str]('red_sandstone_wall_recipe')
  RED_SHULKER_BOX_RECIPE = Kee[str]('red_shulker_box_recipe')
  RED_STAINED_GLASS_PANE_FROM_GLASS_PANE_RECIPE = Kee[str](
    'red_stained_glass_pane_from_glass_pane_recipe')
  RED_STAINED_GLASS_PANE_RECIPE = Kee[str]('red_stained_glass_pane_recipe')
  RED_STAINED_GLASS_RECIPE = Kee[str]('red_stained_glass_recipe')
  RED_TERRACOTTA_RECIPE = Kee[str]('red_terracotta_recipe')
  RED_WOOL_RECIPE = Kee[str]('red_wool_recipe')
  RED_WOOL_SLAB_RECIPE = Kee[str]('red_wool_slab_recipe')
  RED_WOOL_STAIRS_RECIPE = Kee[str]('red_wool_stairs_recipe')
  REDSTONE_BLOCK_RECIPE = Kee[str]('redstone_block_recipe')
  REDSTONE_FROM_BLASTING_DEEPSLATE_REDSTONE_ORE_RECIPE = Kee[str](
    'redstone_from_blasting_deepslate_redstone_ore_recipe')
  REDSTONE_FROM_BLASTING_RECIPE = Kee[str]('redstone_from_blasting_recipe')
  REDSTONE_FROM_BLASTING_REDSTONE_ORE_RECIPE = Kee[str](
    'redstone_from_blasting_redstone_ore_recipe')
  REDSTONE_FROM_SMELTING_DEEPSLATE_REDSTONE_ORE_RECIPE = Kee[str](
    'redstone_from_smelting_deepslate_redstone_ore_recipe')
  REDSTONE_FROM_SMELTING_RECIPE = Kee[str]('redstone_from_smelting_recipe')
  REDSTONE_FROM_SMELTING_REDSTONE_ORE_RECIPE = Kee[str](
    'redstone_from_smelting_redstone_ore_recipe')
  REDSTONE_LAMP_RECIPE = Kee[str]('redstone_lamp_recipe')
  REDSTONE_RECIPE = Kee[str]('redstone_recipe')
  REDSTONE_TORCH_RECIPE = Kee[str]('redstone_torch_recipe')
  REMOTE_GETAWAY = Kee[str]('remote_getaway')
  REPEATER_RECIPE = Kee[str]('repeater_recipe')
  RESIN_BLOCK_RECIPE = Kee[str]('resin_block_recipe')
  RESIN_BRICK_RECIPE = Kee[str]('resin_brick_recipe')
  RESIN_BRICK_SLAB_FROM_RESIN_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'resin_brick_slab_from_resin_bricks_stonecutting_recipe')
  RESIN_BRICK_SLAB_RECIPE = Kee[str]('resin_brick_slab_recipe')
  RESIN_BRICK_STAIRS_FROM_RESIN_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'resin_brick_stairs_from_resin_bricks_stonecutting_recipe')
  RESIN_BRICK_STAIRS_RECIPE = Kee[str]('resin_brick_stairs_recipe')
  RESIN_BRICK_WALL_FROM_RESIN_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'resin_brick_wall_from_resin_bricks_stonecutting_recipe')
  RESIN_BRICK_WALL_RECIPE = Kee[str]('resin_brick_wall_recipe')
  RESIN_BRICKS_RECIPE = Kee[str]('resin_bricks_recipe')
  RESIN_CLUMP_RECIPE = Kee[str]('resin_clump_recipe')
  RESPAWN_ANCHOR_RECIPE = Kee[str]('respawn_anchor_recipe')
  RESPECTING_THE_REMNANTS = Kee[str]('respecting_the_remnants')
  RETURN_TO_SENDER = Kee[str]('return_to_sender')
  REVAULTING = Kee[str]('revaulting')
  RIB_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'rib_armor_trim_smithing_template_recipe')
  RIB_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'rib_armor_trim_smithing_template_smithing_trim_recipe')
  ROOT_RECIPE = Kee[str]('root_recipe')
  SADDLE_RECIPE = Kee[str]('saddle_recipe')
  SANDSTONE_RECIPE = Kee[str]('sandstone_recipe')
  SANDSTONE_SLAB_FROM_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'sandstone_slab_from_sandstone_stonecutting_recipe')
  SANDSTONE_SLAB_RECIPE = Kee[str]('sandstone_slab_recipe')
  SANDSTONE_STAIRS_FROM_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'sandstone_stairs_from_sandstone_stonecutting_recipe')
  SANDSTONE_STAIRS_RECIPE = Kee[str]('sandstone_stairs_recipe')
  SANDSTONE_WALL_FROM_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'sandstone_wall_from_sandstone_stonecutting_recipe')
  SANDSTONE_WALL_RECIPE = Kee[str]('sandstone_wall_recipe')
  SCAFFOLDING_RECIPE = Kee[str]('scaffolding_recipe')
  SEA_LANTERN_RECIPE = Kee[str]('sea_lantern_recipe')
  SENTRY_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'sentry_armor_trim_smithing_template_recipe')
  SENTRY_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'sentry_armor_trim_smithing_template_smithing_trim_recipe')
  SERIOUS_DEDICATION = Kee[str]('serious_dedication')
  SHAPER_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'shaper_armor_trim_smithing_template_recipe')
  SHAPER_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'shaper_armor_trim_smithing_template_smithing_trim_recipe')
  SHEAR_BRILLIANCE = Kee[str]('shear_brilliance')
  SHEARS_RECIPE = Kee[str]('shears_recipe')
  SHIELD_RECIPE = Kee[str]('shield_recipe')
  SHULKER_BOX_RECIPE = Kee[str]('shulker_box_recipe')
  SIGN_RECIPE = Kee[str]('sign_recipe')
  SILENCE_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'silence_armor_trim_smithing_template_recipe')
  SILENCE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'silence_armor_trim_smithing_template_smithing_trim_recipe')
  SKULL_BANNER_PATTERN_RECIPE = Kee[str]('skull_banner_pattern_recipe')
  SKYS_THE_LIMIT = Kee[str]('skys_the_limit')
  SLIME_BALL_RECIPE = Kee[str]('slime_ball_recipe')
  SLIME_BLOCK_RECIPE = Kee[str]('slime_block_recipe')
  SMELLS_INTERESTING = Kee[str]('smells_interesting')
  SMITHING_TABLE_RECIPE = Kee[str]('smithing_table_recipe')
  SMITHING_WITH_STYLE = Kee[str]('smithing_with_style')
  SMOKER_RECIPE = Kee[str]('smoker_recipe')
  SMOOTH_BASALT_RECIPE = Kee[str]('smooth_basalt_recipe')
  SMOOTH_QUARTZ_RECIPE = Kee[str]('smooth_quartz_recipe')
  SMOOTH_QUARTZ_SLAB_FROM_SMOOTH_QUARTZ_STONECUTTING_RECIPE = Kee[str](
    'smooth_quartz_slab_from_smooth_quartz_stonecutting_recipe')
  SMOOTH_QUARTZ_SLAB_RECIPE = Kee[str]('smooth_quartz_slab_recipe')
  SMOOTH_QUARTZ_STAIRS_FROM_SMOOTH_QUARTZ_STONECUTTING_RECIPE = Kee[str](
    'smooth_quartz_stairs_from_smooth_quartz_stonecutting_recipe')
  SMOOTH_QUARTZ_STAIRS_RECIPE = Kee[str]('smooth_quartz_stairs_recipe')
  SMOOTH_RED_SANDSTONE_RECIPE = Kee[str]('smooth_red_sandstone_recipe')
  SMOOTH_RED_SANDSTONE_SLAB_FROM_SMOOTH_RED_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'smooth_red_sandstone_slab_from_smooth_red_sandstone_stonecutting_recipe')
  SMOOTH_RED_SANDSTONE_SLAB_RECIPE = Kee[str](
    'smooth_red_sandstone_slab_recipe')
  SMOOTH_RED_SANDSTONE_STAIRS_FROM_SMOOTH_RED_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'smooth_red_sandstone_stairs_from_smooth_red_sandstone_stonecutting_recipe')
  SMOOTH_RED_SANDSTONE_STAIRS_RECIPE = Kee[str](
    'smooth_red_sandstone_stairs_recipe')
  SMOOTH_SANDSTONE_RECIPE = Kee[str]('smooth_sandstone_recipe')
  SMOOTH_SANDSTONE_SLAB_FROM_SMOOTH_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'smooth_sandstone_slab_from_smooth_sandstone_stonecutting_recipe')
  SMOOTH_SANDSTONE_SLAB_RECIPE = Kee[str]('smooth_sandstone_slab_recipe')
  SMOOTH_SANDSTONE_STAIRS_FROM_SMOOTH_SANDSTONE_STONECUTTING_RECIPE = Kee[str](
    'smooth_sandstone_stairs_from_smooth_sandstone_stonecutting_recipe')
  SMOOTH_SANDSTONE_STAIRS_RECIPE = Kee[str]('smooth_sandstone_stairs_recipe')
  SMOOTH_STONE_RECIPE = Kee[str]('smooth_stone_recipe')
  SMOOTH_STONE_SLAB_FROM_SMOOTH_STONE_STONECUTTING_RECIPE = Kee[str](
    'smooth_stone_slab_from_smooth_stone_stonecutting_recipe')
  SMOOTH_STONE_SLAB_RECIPE = Kee[str]('smooth_stone_slab_recipe')
  SNEAK_100 = Kee[str]('sneak_100')
  SNIPER_DUEL = Kee[str]('sniper_duel')
  SNOUT_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'snout_armor_trim_smithing_template_recipe')
  SNOUT_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'snout_armor_trim_smithing_template_smithing_trim_recipe')
  SNOW_BLOCK_RECIPE = Kee[str]('snow_block_recipe')
  SNOW_RECIPE = Kee[str]('snow_recipe')
  SOUL_CAMPFIRE_RECIPE = Kee[str]('soul_campfire_recipe')
  SOUL_LANTERN_RECIPE = Kee[str]('soul_lantern_recipe')
  SOUL_TORCH_RECIPE = Kee[str]('soul_torch_recipe')
  SOUND_OF_MUSIC = Kee[str]('sound_of_music')
  SPECTRAL_ARROW_RECIPE = Kee[str]('spectral_arrow_recipe')
  SPIRE_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'spire_armor_trim_smithing_template_recipe')
  SPIRE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'spire_armor_trim_smithing_template_smithing_trim_recipe')
  SPONGE_RECIPE = Kee[str]('sponge_recipe')
  SPOOKY_SCARY_SKELETON = Kee[str]('spooky_scary_skeleton')
  SPRUCE_BOAT_RECIPE = Kee[str]('spruce_boat_recipe')
  SPRUCE_BUTTON_RECIPE = Kee[str]('spruce_button_recipe')
  SPRUCE_CHEST_BOAT_RECIPE = Kee[str]('spruce_chest_boat_recipe')
  SPRUCE_DOOR_RECIPE = Kee[str]('spruce_door_recipe')
  SPRUCE_FENCE_GATE_RECIPE = Kee[str]('spruce_fence_gate_recipe')
  SPRUCE_FENCE_RECIPE = Kee[str]('spruce_fence_recipe')
  SPRUCE_HANGING_SIGN_RECIPE = Kee[str]('spruce_hanging_sign_recipe')
  SPRUCE_PLANKS_RECIPE = Kee[str]('spruce_planks_recipe')
  SPRUCE_PRESSURE_PLATE_RECIPE = Kee[str]('spruce_pressure_plate_recipe')
  SPRUCE_SHELF_RECIPE = Kee[str]('spruce_shelf_recipe')
  SPRUCE_SIGN_RECIPE = Kee[str]('spruce_sign_recipe')
  SPRUCE_SLAB_RECIPE = Kee[str]('spruce_slab_recipe')
  SPRUCE_STAIRS_RECIPE = Kee[str]('spruce_stairs_recipe')
  SPRUCE_TRAPDOOR_RECIPE = Kee[str]('spruce_trapdoor_recipe')
  SPRUCE_WOOD_RECIPE = Kee[str]('spruce_wood_recipe')
  SPYGLASS_RECIPE = Kee[str]('spyglass_recipe')
  STAR_TRADER = Kee[str]('star_trader')
  STAY_HYDRATED = Kee[str]('stay_hydrated')
  STICK_FROM_BAMBOO_ITEM_RECIPE = Kee[str]('stick_from_bamboo_item_recipe')
  STICK_RECIPE = Kee[str]('stick_recipe')
  STICKY_PISTON_RECIPE = Kee[str]('sticky_piston_recipe')
  STICKY_SITUATION = Kee[str]('sticky_situation')
  STONE_AGE = Kee[str]('stone_age')
  STONE_AXE_RECIPE = Kee[str]('stone_axe_recipe')
  STONE_BRICK_SLAB_FROM_STONE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'stone_brick_slab_from_stone_bricks_stonecutting_recipe')
  STONE_BRICK_SLAB_FROM_STONE_STONECUTTING_RECIPE = Kee[str](
    'stone_brick_slab_from_stone_stonecutting_recipe')
  STONE_BRICK_SLAB_RECIPE = Kee[str]('stone_brick_slab_recipe')
  STONE_BRICK_STAIRS_FROM_STONE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'stone_brick_stairs_from_stone_bricks_stonecutting_recipe')
  STONE_BRICK_STAIRS_FROM_STONE_STONECUTTING_RECIPE = Kee[str](
    'stone_brick_stairs_from_stone_stonecutting_recipe')
  STONE_BRICK_STAIRS_RECIPE = Kee[str]('stone_brick_stairs_recipe')
  STONE_BRICK_WALL_FROM_STONE_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'stone_brick_wall_from_stone_bricks_stonecutting_recipe')
  STONE_BRICK_WALL_FROM_STONE_STONECUTTING_RECIPE = Kee[str](
    'stone_brick_wall_from_stone_stonecutting_recipe')
  STONE_BRICK_WALL_RECIPE = Kee[str]('stone_brick_wall_recipe')
  STONE_BRICKS_FROM_STONE_STONECUTTING_RECIPE = Kee[str](
    'stone_bricks_from_stone_stonecutting_recipe')
  STONE_BRICKS_RECIPE = Kee[str]('stone_bricks_recipe')
  STONE_BUTTON_RECIPE = Kee[str]('stone_button_recipe')
  STONE_HOE_RECIPE = Kee[str]('stone_hoe_recipe')
  STONE_PICKAXE_RECIPE = Kee[str]('stone_pickaxe_recipe')
  STONE_PRESSURE_PLATE_RECIPE = Kee[str]('stone_pressure_plate_recipe')
  STONE_RECIPE = Kee[str]('stone_recipe')
  STONE_SHOVEL_RECIPE = Kee[str]('stone_shovel_recipe')
  STONE_SLAB_FROM_STONE_STONECUTTING_RECIPE = Kee[str](
    'stone_slab_from_stone_stonecutting_recipe')
  STONE_SLAB_RECIPE = Kee[str]('stone_slab_recipe')
  STONE_SPEAR_RECIPE = Kee[str]('stone_spear_recipe')
  STONE_STAIRS_FROM_STONE_STONECUTTING_RECIPE = Kee[str](
    'stone_stairs_from_stone_stonecutting_recipe')
  STONE_STAIRS_RECIPE = Kee[str]('stone_stairs_recipe')
  STONE_SWORD_RECIPE = Kee[str]('stone_sword_recipe')
  STONECUTTER_RECIPE = Kee[str]('stonecutter_recipe')
  STORY_ROOT = Kee[str]('story_root')
  STRAW_BED_RECIPE = Kee[str]('straw_bed_recipe')
  STRIPPED_ACACIA_WOOD_RECIPE = Kee[str]('stripped_acacia_wood_recipe')
  STRIPPED_BIRCH_WOOD_RECIPE = Kee[str]('stripped_birch_wood_recipe')
  STRIPPED_CHERRY_WOOD_RECIPE = Kee[str]('stripped_cherry_wood_recipe')
  STRIPPED_CRIMSON_HYPHAE_RECIPE = Kee[str]('stripped_crimson_hyphae_recipe')
  STRIPPED_DARK_OAK_WOOD_RECIPE = Kee[str]('stripped_dark_oak_wood_recipe')
  STRIPPED_JUNGLE_WOOD_RECIPE = Kee[str]('stripped_jungle_wood_recipe')
  STRIPPED_MANGROVE_WOOD_RECIPE = Kee[str]('stripped_mangrove_wood_recipe')
  STRIPPED_OAK_WOOD_RECIPE = Kee[str]('stripped_oak_wood_recipe')
  STRIPPED_PALE_OAK_WOOD_RECIPE = Kee[str]('stripped_pale_oak_wood_recipe')
  STRIPPED_POPLAR_WOOD_RECIPE = Kee[str]('stripped_poplar_wood_recipe')
  STRIPPED_SPRUCE_WOOD_RECIPE = Kee[str]('stripped_spruce_wood_recipe')
  STRIPPED_WARPED_HYPHAE_RECIPE = Kee[str]('stripped_warped_hyphae_recipe')
  SUBSPACE_BUBBLE = Kee[str]('subspace_bubble')
  SUGAR_FROM_HONEY_BOTTLE_RECIPE = Kee[str]('sugar_from_honey_bottle_recipe')
  SUGAR_FROM_SUGAR_CANE_RECIPE = Kee[str]('sugar_from_sugar_cane_recipe')
  SUIT_UP = Kee[str]('suit_up')
  SULFUR_BRICK_SLAB_FROM_POLISHED_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'sulfur_brick_slab_from_polished_sulfur_stonecutting_recipe')
  SULFUR_BRICK_SLAB_FROM_SULFUR_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'sulfur_brick_slab_from_sulfur_bricks_stonecutting_recipe')
  SULFUR_BRICK_SLAB_FROM_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'sulfur_brick_slab_from_sulfur_stonecutting_recipe')
  SULFUR_BRICK_SLAB_RECIPE = Kee[str]('sulfur_brick_slab_recipe')
  SULFUR_BRICK_STAIRS_FROM_POLISHED_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'sulfur_brick_stairs_from_polished_sulfur_stonecutting_recipe')
  SULFUR_BRICK_STAIRS_FROM_SULFUR_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'sulfur_brick_stairs_from_sulfur_bricks_stonecutting_recipe')
  SULFUR_BRICK_STAIRS_FROM_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'sulfur_brick_stairs_from_sulfur_stonecutting_recipe')
  SULFUR_BRICK_STAIRS_RECIPE = Kee[str]('sulfur_brick_stairs_recipe')
  SULFUR_BRICK_WALL_FROM_POLISHED_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'sulfur_brick_wall_from_polished_sulfur_stonecutting_recipe')
  SULFUR_BRICK_WALL_FROM_SULFUR_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'sulfur_brick_wall_from_sulfur_bricks_stonecutting_recipe')
  SULFUR_BRICK_WALL_FROM_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'sulfur_brick_wall_from_sulfur_stonecutting_recipe')
  SULFUR_BRICK_WALL_RECIPE = Kee[str]('sulfur_brick_wall_recipe')
  SULFUR_BRICKS_FROM_POLISHED_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'sulfur_bricks_from_polished_sulfur_stonecutting_recipe')
  SULFUR_BRICKS_FROM_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'sulfur_bricks_from_sulfur_stonecutting_recipe')
  SULFUR_BRICKS_RECIPE = Kee[str]('sulfur_bricks_recipe')
  SULFUR_FROM_SULFUR_SPIKES_RECIPE = Kee[str](
    'sulfur_from_sulfur_spikes_recipe')
  SULFUR_SLAB_FROM_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'sulfur_slab_from_sulfur_stonecutting_recipe')
  SULFUR_SLAB_RECIPE = Kee[str]('sulfur_slab_recipe')
  SULFUR_STAIRS_FROM_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'sulfur_stairs_from_sulfur_stonecutting_recipe')
  SULFUR_STAIRS_RECIPE = Kee[str]('sulfur_stairs_recipe')
  SULFUR_WALL_FROM_SULFUR_STONECUTTING_RECIPE = Kee[str](
    'sulfur_wall_from_sulfur_stonecutting_recipe')
  SULFUR_WALL_RECIPE = Kee[str]('sulfur_wall_recipe')
  SURGE_PROTECTOR = Kee[str]('surge_protector')
  SUSPICIOUS_STEW_FROM_ALLIUM_RECIPE = Kee[str](
    'suspicious_stew_from_allium_recipe')
  SUSPICIOUS_STEW_FROM_AZURE_BLUET_RECIPE = Kee[str](
    'suspicious_stew_from_azure_bluet_recipe')
  SUSPICIOUS_STEW_FROM_BLUE_ORCHID_RECIPE = Kee[str](
    'suspicious_stew_from_blue_orchid_recipe')
  SUSPICIOUS_STEW_FROM_CLOSED_EYEBLOSSOM_RECIPE = Kee[str](
    'suspicious_stew_from_closed_eyeblossom_recipe')
  SUSPICIOUS_STEW_FROM_CORNFLOWER_RECIPE = Kee[str](
    'suspicious_stew_from_cornflower_recipe')
  SUSPICIOUS_STEW_FROM_DANDELION_RECIPE = Kee[str](
    'suspicious_stew_from_dandelion_recipe')
  SUSPICIOUS_STEW_FROM_GOLDEN_DANDELION_RECIPE = Kee[str](
    'suspicious_stew_from_golden_dandelion_recipe')
  SUSPICIOUS_STEW_FROM_LILY_OF_THE_VALLEY_RECIPE = Kee[str](
    'suspicious_stew_from_lily_of_the_valley_recipe')
  SUSPICIOUS_STEW_FROM_OPEN_EYEBLOSSOM_RECIPE = Kee[str](
    'suspicious_stew_from_open_eyeblossom_recipe')
  SUSPICIOUS_STEW_FROM_ORANGE_TULIP_RECIPE = Kee[str](
    'suspicious_stew_from_orange_tulip_recipe')
  SUSPICIOUS_STEW_FROM_OXEYE_DAISY_RECIPE = Kee[str](
    'suspicious_stew_from_oxeye_daisy_recipe')
  SUSPICIOUS_STEW_FROM_PINK_TULIP_RECIPE = Kee[str](
    'suspicious_stew_from_pink_tulip_recipe')
  SUSPICIOUS_STEW_FROM_POPPY_RECIPE = Kee[str](
    'suspicious_stew_from_poppy_recipe')
  SUSPICIOUS_STEW_FROM_RED_TULIP_RECIPE = Kee[str](
    'suspicious_stew_from_red_tulip_recipe')
  SUSPICIOUS_STEW_FROM_TORCHFLOWER_RECIPE = Kee[str](
    'suspicious_stew_from_torchflower_recipe')
  SUSPICIOUS_STEW_FROM_WHITE_TULIP_RECIPE = Kee[str](
    'suspicious_stew_from_white_tulip_recipe')
  SUSPICIOUS_STEW_FROM_WITHER_ROSE_RECIPE = Kee[str](
    'suspicious_stew_from_wither_rose_recipe')
  SWEET_DREAMS = Kee[str]('sweet_dreams')
  TACTICAL_FISHING = Kee[str]('tactical_fishing')
  TAKE_AIM = Kee[str]('take_aim')
  TARGET_RECIPE = Kee[str]('target_recipe')
  TERRACOTTA_RECIPE = Kee[str]('terracotta_recipe')
  THE_CITY_AT_THE_END_OF_THE_GAME = Kee[str]('the_city_at_the_end_of_the_game')
  THE_CUTEST_PREDATOR = Kee[str]('the_cutest_predator')
  THE_END = Kee[str]('the_end')
  THE_END_AGAIN = Kee[str]('the_end_again')
  THE_HEALING_POWER_OF_FRIENDSHIP = Kee[str]('the_healing_power_of_friendship')
  THE_NEXT_GENERATION = Kee[str]('the_next_generation')
  THE_PARROTS_AND_THE_BATS = Kee[str]('the_parrots_and_the_bats')
  THE_POWER_OF_BOOKS = Kee[str]('the_power_of_books')
  THE_WHOLE_PACK = Kee[str]('the_whole_pack')
  THIS_BOAT_HAS_LEGS = Kee[str]('this_boat_has_legs')
  THOSE_WERE_THE_DAYS = Kee[str]('those_were_the_days')
  TIDE_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'tide_armor_trim_smithing_template_recipe')
  TIDE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'tide_armor_trim_smithing_template_smithing_trim_recipe')
  TINTED_GLASS_RECIPE = Kee[str]('tinted_glass_recipe')
  TIPPED_ARROW_RECIPE = Kee[str]('tipped_arrow_recipe')
  TNT_MINECART_RECIPE = Kee[str]('tnt_minecart_recipe')
  TNT_RECIPE = Kee[str]('tnt_recipe')
  TORCH_RECIPE = Kee[str]('torch_recipe')
  TOTAL_BEELOCATION = Kee[str]('total_beelocation')
  TRAPPED_CHEST_RECIPE = Kee[str]('trapped_chest_recipe')
  TRIPWIRE_HOOK_RECIPE = Kee[str]('tripwire_hook_recipe')
  TUFF_BRICK_SLAB_FROM_POLISHED_TUFF_STONECUTTING_RECIPE = Kee[str](
    'tuff_brick_slab_from_polished_tuff_stonecutting_recipe')
  TUFF_BRICK_SLAB_FROM_TUFF_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'tuff_brick_slab_from_tuff_bricks_stonecutting_recipe')
  TUFF_BRICK_SLAB_FROM_TUFF_STONECUTTING_RECIPE = Kee[str](
    'tuff_brick_slab_from_tuff_stonecutting_recipe')
  TUFF_BRICK_SLAB_RECIPE = Kee[str]('tuff_brick_slab_recipe')
  TUFF_BRICK_STAIRS_FROM_POLISHED_TUFF_STONECUTTING_RECIPE = Kee[str](
    'tuff_brick_stairs_from_polished_tuff_stonecutting_recipe')
  TUFF_BRICK_STAIRS_FROM_TUFF_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'tuff_brick_stairs_from_tuff_bricks_stonecutting_recipe')
  TUFF_BRICK_STAIRS_FROM_TUFF_STONECUTTING_RECIPE = Kee[str](
    'tuff_brick_stairs_from_tuff_stonecutting_recipe')
  TUFF_BRICK_STAIRS_RECIPE = Kee[str]('tuff_brick_stairs_recipe')
  TUFF_BRICK_WALL_FROM_POLISHED_TUFF_STONECUTTING_RECIPE = Kee[str](
    'tuff_brick_wall_from_polished_tuff_stonecutting_recipe')
  TUFF_BRICK_WALL_FROM_TUFF_BRICKS_STONECUTTING_RECIPE = Kee[str](
    'tuff_brick_wall_from_tuff_bricks_stonecutting_recipe')
  TUFF_BRICK_WALL_FROM_TUFF_STONECUTTING_RECIPE = Kee[str](
    'tuff_brick_wall_from_tuff_stonecutting_recipe')
  TUFF_BRICK_WALL_RECIPE = Kee[str]('tuff_brick_wall_recipe')
  TUFF_BRICKS_FROM_POLISHED_TUFF_STONECUTTING_RECIPE = Kee[str](
    'tuff_bricks_from_polished_tuff_stonecutting_recipe')
  TUFF_BRICKS_FROM_TUFF_STONECUTTING_RECIPE = Kee[str](
    'tuff_bricks_from_tuff_stonecutting_recipe')
  TUFF_BRICKS_RECIPE = Kee[str]('tuff_bricks_recipe')
  TUFF_SLAB_FROM_TUFF_STONECUTTING_RECIPE = Kee[str](
    'tuff_slab_from_tuff_stonecutting_recipe')
  TUFF_SLAB_RECIPE = Kee[str]('tuff_slab_recipe')
  TUFF_STAIRS_FROM_TUFF_STONECUTTING_RECIPE = Kee[str](
    'tuff_stairs_from_tuff_stonecutting_recipe')
  TUFF_STAIRS_RECIPE = Kee[str]('tuff_stairs_recipe')
  TUFF_WALL_FROM_TUFF_STONECUTTING_RECIPE = Kee[str](
    'tuff_wall_from_tuff_stonecutting_recipe')
  TUFF_WALL_RECIPE = Kee[str]('tuff_wall_recipe')
  TURTLE_HELMET_RECIPE = Kee[str]('turtle_helmet_recipe')
  TWO_BIRDS_ONE_ARROW = Kee[str]('two_birds_one_arrow')
  TWO_BY_TWO = Kee[str]('two_by_two')
  UH_OH = Kee[str]('uh_oh')
  UNDER_LOCK_AND_KEY = Kee[str]('under_lock_and_key')
  UNEASY_ALLIANCE = Kee[str]('uneasy_alliance')
  VERY_VERY_FRIGHTENING = Kee[str]('very_very_frightening')
  VEX_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'vex_armor_trim_smithing_template_recipe')
  VEX_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'vex_armor_trim_smithing_template_smithing_trim_recipe')
  VOLUNTARY_EXILE = Kee[str]('voluntary_exile')
  WAR_PIGS = Kee[str]('war_pigs')
  WARD_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'ward_armor_trim_smithing_template_recipe')
  WARD_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'ward_armor_trim_smithing_template_smithing_trim_recipe')
  WARPED_BUTTON_RECIPE = Kee[str]('warped_button_recipe')
  WARPED_DOOR_RECIPE = Kee[str]('warped_door_recipe')
  WARPED_FENCE_GATE_RECIPE = Kee[str]('warped_fence_gate_recipe')
  WARPED_FENCE_RECIPE = Kee[str]('warped_fence_recipe')
  WARPED_FUNGUS_ON_A_STICK_RECIPE = Kee[str]('warped_fungus_on_a_stick_recipe')
  WARPED_HANGING_SIGN_RECIPE = Kee[str]('warped_hanging_sign_recipe')
  WARPED_HYPHAE_RECIPE = Kee[str]('warped_hyphae_recipe')
  WARPED_PLANKS_RECIPE = Kee[str]('warped_planks_recipe')
  WARPED_PRESSURE_PLATE_RECIPE = Kee[str]('warped_pressure_plate_recipe')
  WARPED_SHELF_RECIPE = Kee[str]('warped_shelf_recipe')
  WARPED_SIGN_RECIPE = Kee[str]('warped_sign_recipe')
  WARPED_SLAB_RECIPE = Kee[str]('warped_slab_recipe')
  WARPED_STAIRS_RECIPE = Kee[str]('warped_stairs_recipe')
  WARPED_TRAPDOOR_RECIPE = Kee[str]('warped_trapdoor_recipe')
  WAX_OFF = Kee[str]('wax_off')
  WAX_ON = Kee[str]('wax_on')
  WAXED_CHISELED_COPPER_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_chiseled_copper_from_honeycomb_recipe')
  WAXED_CHISELED_COPPER_FROM_WAXED_COPPER_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'waxed_chiseled_copper_from_waxed_copper_block_stonecutting_recipe')
  WAXED_CHISELED_COPPER_FROM_WAXED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_chiseled_copper_from_waxed_cut_copper_stonecutting_recipe')
  WAXED_CHISELED_COPPER_RECIPE = Kee[str]('waxed_chiseled_copper_recipe')
  WAXED_COPPER_BARS_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_copper_bars_from_honeycomb_recipe')
  WAXED_COPPER_BLOCK_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_copper_block_from_honeycomb_recipe')
  WAXED_COPPER_BULB_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_copper_bulb_from_honeycomb_recipe')
  WAXED_COPPER_BULB_RECIPE = Kee[str]('waxed_copper_bulb_recipe')
  WAXED_COPPER_CHAIN_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_copper_chain_from_honeycomb_recipe')
  WAXED_COPPER_CHEST_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_copper_chest_from_honeycomb_recipe')
  WAXED_COPPER_DOOR_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_copper_door_from_honeycomb_recipe')
  WAXED_COPPER_GOLEM_STATUE_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_copper_golem_statue_from_honeycomb_recipe')
  WAXED_COPPER_GRATE_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_copper_grate_from_honeycomb_recipe')
  WAXED_COPPER_GRATE_FROM_WAXED_COPPER_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'waxed_copper_grate_from_waxed_copper_block_stonecutting_recipe')
  WAXED_COPPER_GRATE_RECIPE = Kee[str]('waxed_copper_grate_recipe')
  WAXED_COPPER_LANTERN_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_copper_lantern_from_honeycomb_recipe')
  WAXED_COPPER_TRAPDOOR_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_copper_trapdoor_from_honeycomb_recipe')
  WAXED_CUT_COPPER_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_cut_copper_from_honeycomb_recipe')
  WAXED_CUT_COPPER_FROM_WAXED_COPPER_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'waxed_cut_copper_from_waxed_copper_block_stonecutting_recipe')
  WAXED_CUT_COPPER_RECIPE = Kee[str]('waxed_cut_copper_recipe')
  WAXED_CUT_COPPER_SLAB_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_cut_copper_slab_from_honeycomb_recipe')
  WAXED_CUT_COPPER_SLAB_FROM_WAXED_COPPER_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'waxed_cut_copper_slab_from_waxed_copper_block_stonecutting_recipe')
  WAXED_CUT_COPPER_SLAB_FROM_WAXED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_cut_copper_slab_from_waxed_cut_copper_stonecutting_recipe')
  WAXED_CUT_COPPER_SLAB_RECIPE = Kee[str]('waxed_cut_copper_slab_recipe')
  WAXED_CUT_COPPER_STAIRS_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_cut_copper_stairs_from_honeycomb_recipe')
  WAXED_CUT_COPPER_STAIRS_FROM_WAXED_COPPER_BLOCK_STONECUTTING_RECIPE = Kee[str](
    'waxed_cut_copper_stairs_from_waxed_copper_block_stonecutting_recipe')
  WAXED_CUT_COPPER_STAIRS_FROM_WAXED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_cut_copper_stairs_from_waxed_cut_copper_stonecutting_recipe')
  WAXED_CUT_COPPER_STAIRS_RECIPE = Kee[str]('waxed_cut_copper_stairs_recipe')
  WAXED_EXPOSED_CHISELED_COPPER_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_exposed_chiseled_copper_from_honeycomb_recipe')
  WAXED_EXPOSED_CHISELED_COPPER_FROM_WAXED_EXPOSED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_exposed_chiseled_copper_from_waxed_exposed_copper_stonecutting_recipe')
  WAXED_EXPOSED_CHISELED_COPPER_FROM_WAXED_EXPOSED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_exposed_chiseled_copper_from_waxed_exposed_cut_copper_stonecutting_recipe')
  WAXED_EXPOSED_CHISELED_COPPER_RECIPE = Kee[str](
    'waxed_exposed_chiseled_copper_recipe')
  WAXED_EXPOSED_COPPER_BARS_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_exposed_copper_bars_from_honeycomb_recipe')
  WAXED_EXPOSED_COPPER_BULB_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_exposed_copper_bulb_from_honeycomb_recipe')
  WAXED_EXPOSED_COPPER_BULB_RECIPE = Kee[str](
    'waxed_exposed_copper_bulb_recipe')
  WAXED_EXPOSED_COPPER_CHAIN_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_exposed_copper_chain_from_honeycomb_recipe')
  WAXED_EXPOSED_COPPER_CHEST_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_exposed_copper_chest_from_honeycomb_recipe')
  WAXED_EXPOSED_COPPER_DOOR_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_exposed_copper_door_from_honeycomb_recipe')
  WAXED_EXPOSED_COPPER_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_exposed_copper_from_honeycomb_recipe')
  WAXED_EXPOSED_COPPER_GOLEM_STATUE_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_exposed_copper_golem_statue_from_honeycomb_recipe')
  WAXED_EXPOSED_COPPER_GRATE_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_exposed_copper_grate_from_honeycomb_recipe')
  WAXED_EXPOSED_COPPER_GRATE_FROM_WAXED_EXPOSED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_exposed_copper_grate_from_waxed_exposed_copper_stonecutting_recipe')
  WAXED_EXPOSED_COPPER_GRATE_RECIPE = Kee[str](
    'waxed_exposed_copper_grate_recipe')
  WAXED_EXPOSED_COPPER_LANTERN_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_exposed_copper_lantern_from_honeycomb_recipe')
  WAXED_EXPOSED_COPPER_TRAPDOOR_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_exposed_copper_trapdoor_from_honeycomb_recipe')
  WAXED_EXPOSED_CUT_COPPER_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_exposed_cut_copper_from_honeycomb_recipe')
  WAXED_EXPOSED_CUT_COPPER_FROM_WAXED_EXPOSED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_exposed_cut_copper_from_waxed_exposed_copper_stonecutting_recipe')
  WAXED_EXPOSED_CUT_COPPER_RECIPE = Kee[str]('waxed_exposed_cut_copper_recipe')
  WAXED_EXPOSED_CUT_COPPER_SLAB_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_exposed_cut_copper_slab_from_honeycomb_recipe')
  WAXED_EXPOSED_CUT_COPPER_SLAB_FROM_WAXED_EXPOSED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_exposed_cut_copper_slab_from_waxed_exposed_copper_stonecutting_recipe')
  WAXED_EXPOSED_CUT_COPPER_SLAB_FROM_WAXED_EXPOSED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_exposed_cut_copper_slab_from_waxed_exposed_cut_copper_stonecutting_recipe')
  WAXED_EXPOSED_CUT_COPPER_SLAB_RECIPE = Kee[str](
    'waxed_exposed_cut_copper_slab_recipe')
  WAXED_EXPOSED_CUT_COPPER_STAIRS_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_exposed_cut_copper_stairs_from_honeycomb_recipe')
  WAXED_EXPOSED_CUT_COPPER_STAIRS_FROM_WAXED_EXPOSED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_exposed_cut_copper_stairs_from_waxed_exposed_copper_stonecutting_recipe')
  WAXED_EXPOSED_CUT_COPPER_STAIRS_FROM_WAXED_EXPOSED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_exposed_cut_copper_stairs_from_waxed_exposed_cut_copper_stonecutting_recipe')
  WAXED_EXPOSED_CUT_COPPER_STAIRS_RECIPE = Kee[str](
    'waxed_exposed_cut_copper_stairs_recipe')
  WAXED_EXPOSED_LIGHTNING_ROD_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_exposed_lightning_rod_from_honeycomb_recipe')
  WAXED_LIGHTNING_ROD_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_lightning_rod_from_honeycomb_recipe')
  WAXED_OXIDIZED_CHISELED_COPPER_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_oxidized_chiseled_copper_from_honeycomb_recipe')
  WAXED_OXIDIZED_CHISELED_COPPER_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_oxidized_chiseled_copper_from_waxed_oxidized_copper_stonecutting_recipe')
  WAXED_OXIDIZED_CHISELED_COPPER_FROM_WAXED_OXIDIZED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_oxidized_chiseled_copper_from_waxed_oxidized_cut_copper_stonecutting_recipe')
  WAXED_OXIDIZED_CHISELED_COPPER_RECIPE = Kee[str](
    'waxed_oxidized_chiseled_copper_recipe')
  WAXED_OXIDIZED_COPPER_BARS_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_oxidized_copper_bars_from_honeycomb_recipe')
  WAXED_OXIDIZED_COPPER_BULB_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_oxidized_copper_bulb_from_honeycomb_recipe')
  WAXED_OXIDIZED_COPPER_BULB_RECIPE = Kee[str](
    'waxed_oxidized_copper_bulb_recipe')
  WAXED_OXIDIZED_COPPER_CHAIN_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_oxidized_copper_chain_from_honeycomb_recipe')
  WAXED_OXIDIZED_COPPER_CHEST_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_oxidized_copper_chest_from_honeycomb_recipe')
  WAXED_OXIDIZED_COPPER_DOOR_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_oxidized_copper_door_from_honeycomb_recipe')
  WAXED_OXIDIZED_COPPER_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_oxidized_copper_from_honeycomb_recipe')
  WAXED_OXIDIZED_COPPER_GOLEM_STATUE_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_oxidized_copper_golem_statue_from_honeycomb_recipe')
  WAXED_OXIDIZED_COPPER_GRATE_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_oxidized_copper_grate_from_honeycomb_recipe')
  WAXED_OXIDIZED_COPPER_GRATE_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_oxidized_copper_grate_from_waxed_oxidized_copper_stonecutting_recipe')
  WAXED_OXIDIZED_COPPER_GRATE_RECIPE = Kee[str](
    'waxed_oxidized_copper_grate_recipe')
  WAXED_OXIDIZED_COPPER_LANTERN_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_oxidized_copper_lantern_from_honeycomb_recipe')
  WAXED_OXIDIZED_COPPER_TRAPDOOR_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_oxidized_copper_trapdoor_from_honeycomb_recipe')
  WAXED_OXIDIZED_CUT_COPPER_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_oxidized_cut_copper_from_honeycomb_recipe')
  WAXED_OXIDIZED_CUT_COPPER_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_oxidized_cut_copper_from_waxed_oxidized_copper_stonecutting_recipe')
  WAXED_OXIDIZED_CUT_COPPER_RECIPE = Kee[str](
    'waxed_oxidized_cut_copper_recipe')
  WAXED_OXIDIZED_CUT_COPPER_SLAB_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_oxidized_cut_copper_slab_from_honeycomb_recipe')
  WAXED_OXIDIZED_CUT_COPPER_SLAB_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_oxidized_cut_copper_slab_from_waxed_oxidized_copper_stonecutting_recipe')
  WAXED_OXIDIZED_CUT_COPPER_SLAB_FROM_WAXED_OXIDIZED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_oxidized_cut_copper_slab_from_waxed_oxidized_cut_copper_stonecutting_recipe')
  WAXED_OXIDIZED_CUT_COPPER_SLAB_RECIPE = Kee[str](
    'waxed_oxidized_cut_copper_slab_recipe')
  WAXED_OXIDIZED_CUT_COPPER_STAIRS_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_oxidized_cut_copper_stairs_from_honeycomb_recipe')
  WAXED_OXIDIZED_CUT_COPPER_STAIRS_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_copper_stonecutting_recipe')
  WAXED_OXIDIZED_CUT_COPPER_STAIRS_FROM_WAXED_OXIDIZED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_cut_copper_stonecutting_recipe')
  WAXED_OXIDIZED_CUT_COPPER_STAIRS_RECIPE = Kee[str](
    'waxed_oxidized_cut_copper_stairs_recipe')
  WAXED_OXIDIZED_LIGHTNING_ROD_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_oxidized_lightning_rod_from_honeycomb_recipe')
  WAXED_WEATHERED_CHISELED_COPPER_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_weathered_chiseled_copper_from_honeycomb_recipe')
  WAXED_WEATHERED_CHISELED_COPPER_FROM_WAXED_WEATHERED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_weathered_chiseled_copper_from_waxed_weathered_copper_stonecutting_recipe')
  WAXED_WEATHERED_CHISELED_COPPER_FROM_WAXED_WEATHERED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_weathered_chiseled_copper_from_waxed_weathered_cut_copper_stonecutting_recipe')
  WAXED_WEATHERED_CHISELED_COPPER_RECIPE = Kee[str](
    'waxed_weathered_chiseled_copper_recipe')
  WAXED_WEATHERED_COPPER_BARS_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_weathered_copper_bars_from_honeycomb_recipe')
  WAXED_WEATHERED_COPPER_BULB_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_weathered_copper_bulb_from_honeycomb_recipe')
  WAXED_WEATHERED_COPPER_BULB_RECIPE = Kee[str](
    'waxed_weathered_copper_bulb_recipe')
  WAXED_WEATHERED_COPPER_CHAIN_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_weathered_copper_chain_from_honeycomb_recipe')
  WAXED_WEATHERED_COPPER_CHEST_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_weathered_copper_chest_from_honeycomb_recipe')
  WAXED_WEATHERED_COPPER_DOOR_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_weathered_copper_door_from_honeycomb_recipe')
  WAXED_WEATHERED_COPPER_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_weathered_copper_from_honeycomb_recipe')
  WAXED_WEATHERED_COPPER_GOLEM_STATUE_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_weathered_copper_golem_statue_from_honeycomb_recipe')
  WAXED_WEATHERED_COPPER_GRATE_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_weathered_copper_grate_from_honeycomb_recipe')
  WAXED_WEATHERED_COPPER_GRATE_FROM_WAXED_WEATHERED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_weathered_copper_grate_from_waxed_weathered_copper_stonecutting_recipe')
  WAXED_WEATHERED_COPPER_GRATE_RECIPE = Kee[str](
    'waxed_weathered_copper_grate_recipe')
  WAXED_WEATHERED_COPPER_LANTERN_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_weathered_copper_lantern_from_honeycomb_recipe')
  WAXED_WEATHERED_COPPER_TRAPDOOR_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_weathered_copper_trapdoor_from_honeycomb_recipe')
  WAXED_WEATHERED_CUT_COPPER_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_weathered_cut_copper_from_honeycomb_recipe')
  WAXED_WEATHERED_CUT_COPPER_FROM_WAXED_WEATHERED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_weathered_cut_copper_from_waxed_weathered_copper_stonecutting_recipe')
  WAXED_WEATHERED_CUT_COPPER_RECIPE = Kee[str](
    'waxed_weathered_cut_copper_recipe')
  WAXED_WEATHERED_CUT_COPPER_SLAB_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_weathered_cut_copper_slab_from_honeycomb_recipe')
  WAXED_WEATHERED_CUT_COPPER_SLAB_FROM_WAXED_WEATHERED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_weathered_cut_copper_slab_from_waxed_weathered_copper_stonecutting_recipe')
  WAXED_WEATHERED_CUT_COPPER_SLAB_FROM_WAXED_WEATHERED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_weathered_cut_copper_slab_from_waxed_weathered_cut_copper_stonecutting_recipe')
  WAXED_WEATHERED_CUT_COPPER_SLAB_RECIPE = Kee[str](
    'waxed_weathered_cut_copper_slab_recipe')
  WAXED_WEATHERED_CUT_COPPER_STAIRS_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_weathered_cut_copper_stairs_from_honeycomb_recipe')
  WAXED_WEATHERED_CUT_COPPER_STAIRS_FROM_WAXED_WEATHERED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_weathered_cut_copper_stairs_from_waxed_weathered_copper_stonecutting_recipe')
  WAXED_WEATHERED_CUT_COPPER_STAIRS_FROM_WAXED_WEATHERED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'waxed_weathered_cut_copper_stairs_from_waxed_weathered_cut_copper_stonecutting_recipe')
  WAXED_WEATHERED_CUT_COPPER_STAIRS_RECIPE = Kee[str](
    'waxed_weathered_cut_copper_stairs_recipe')
  WAXED_WEATHERED_LIGHTNING_ROD_FROM_HONEYCOMB_RECIPE = Kee[str](
    'waxed_weathered_lightning_rod_from_honeycomb_recipe')
  WAYFINDER_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'wayfinder_armor_trim_smithing_template_recipe')
  WAYFINDER_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'wayfinder_armor_trim_smithing_template_smithing_trim_recipe')
  WE_NEED_TO_GO_DEEPER = Kee[str]('we_need_to_go_deeper')
  WEATHERED_CHISELED_COPPER_FROM_WEATHERED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'weathered_chiseled_copper_from_weathered_copper_stonecutting_recipe')
  WEATHERED_CHISELED_COPPER_FROM_WEATHERED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'weathered_chiseled_copper_from_weathered_cut_copper_stonecutting_recipe')
  WEATHERED_CHISELED_COPPER_RECIPE = Kee[str](
    'weathered_chiseled_copper_recipe')
  WEATHERED_COPPER_BULB_RECIPE = Kee[str]('weathered_copper_bulb_recipe')
  WEATHERED_COPPER_GRATE_FROM_WEATHERED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'weathered_copper_grate_from_weathered_copper_stonecutting_recipe')
  WEATHERED_COPPER_GRATE_RECIPE = Kee[str]('weathered_copper_grate_recipe')
  WEATHERED_CUT_COPPER_FROM_WEATHERED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'weathered_cut_copper_from_weathered_copper_stonecutting_recipe')
  WEATHERED_CUT_COPPER_RECIPE = Kee[str]('weathered_cut_copper_recipe')
  WEATHERED_CUT_COPPER_SLAB_FROM_WEATHERED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'weathered_cut_copper_slab_from_weathered_copper_stonecutting_recipe')
  WEATHERED_CUT_COPPER_SLAB_FROM_WEATHERED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'weathered_cut_copper_slab_from_weathered_cut_copper_stonecutting_recipe')
  WEATHERED_CUT_COPPER_SLAB_RECIPE = Kee[str](
    'weathered_cut_copper_slab_recipe')
  WEATHERED_CUT_COPPER_STAIRS_FROM_WEATHERED_COPPER_STONECUTTING_RECIPE = Kee[str](
    'weathered_cut_copper_stairs_from_weathered_copper_stonecutting_recipe')
  WEATHERED_CUT_COPPER_STAIRS_FROM_WEATHERED_CUT_COPPER_STONECUTTING_RECIPE = Kee[str](
    'weathered_cut_copper_stairs_from_weathered_cut_copper_stonecutting_recipe')
  WEATHERED_CUT_COPPER_STAIRS_RECIPE = Kee[str](
    'weathered_cut_copper_stairs_recipe')
  WHAT_A_DEAL = Kee[str]('what_a_deal')
  WHATEVER_FLOATS_YOUR_GOAT = Kee[str]('whatever_floats_your_goat')
  WHEAT_RECIPE = Kee[str]('wheat_recipe')
  WHEN_THE_SQUAD_HOPS_INTO_TOWN = Kee[str]('when_the_squad_hops_into_town')
  WHITE_BANNER_RECIPE = Kee[str]('white_banner_recipe')
  WHITE_BED_RECIPE = Kee[str]('white_bed_recipe')
  WHITE_BUNDLE_RECIPE = Kee[str]('white_bundle_recipe')
  WHITE_CANDLE_RECIPE = Kee[str]('white_candle_recipe')
  WHITE_CARPET_RECIPE = Kee[str]('white_carpet_recipe')
  WHITE_CONCRETE_POWDER_RECIPE = Kee[str]('white_concrete_powder_recipe')
  WHITE_CONCRETE_SLAB_FROM_WHITE_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'white_concrete_slab_from_white_concrete_stonecutting_recipe')
  WHITE_CONCRETE_SLAB_RECIPE = Kee[str]('white_concrete_slab_recipe')
  WHITE_CONCRETE_STAIRS_FROM_WHITE_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'white_concrete_stairs_from_white_concrete_stonecutting_recipe')
  WHITE_CONCRETE_STAIRS_RECIPE = Kee[str]('white_concrete_stairs_recipe')
  WHITE_CUSHION_RECIPE = Kee[str]('white_cushion_recipe')
  WHITE_DYE_FROM_LILY_OF_THE_VALLEY_RECIPE = Kee[str](
    'white_dye_from_lily_of_the_valley_recipe')
  WHITE_DYE_RECIPE = Kee[str]('white_dye_recipe')
  WHITE_GLAZED_TERRACOTTA_RECIPE = Kee[str]('white_glazed_terracotta_recipe')
  WHITE_HARNESS_RECIPE = Kee[str]('white_harness_recipe')
  WHITE_SHULKER_BOX_RECIPE = Kee[str]('white_shulker_box_recipe')
  WHITE_STAINED_GLASS_PANE_FROM_GLASS_PANE_RECIPE = Kee[str](
    'white_stained_glass_pane_from_glass_pane_recipe')
  WHITE_STAINED_GLASS_PANE_RECIPE = Kee[str]('white_stained_glass_pane_recipe')
  WHITE_STAINED_GLASS_RECIPE = Kee[str]('white_stained_glass_recipe')
  WHITE_TERRACOTTA_RECIPE = Kee[str]('white_terracotta_recipe')
  WHITE_WOOL_FROM_STRING_RECIPE = Kee[str]('white_wool_from_string_recipe')
  WHITE_WOOL_SLAB_RECIPE = Kee[str]('white_wool_slab_recipe')
  WHITE_WOOL_STAIRS_RECIPE = Kee[str]('white_wool_stairs_recipe')
  WHO_IS_CUTTING_ONIONS = Kee[str]('who_is_cutting_onions')
  WHO_NEEDS_ROCKETS = Kee[str]('who_needs_rockets')
  WHOS_THE_PILLAGER_NOW = Kee[str]('whos_the_pillager_now')
  WILD_ARMOR_TRIM_SMITHING_TEMPLATE_RECIPE = Kee[str](
    'wild_armor_trim_smithing_template_recipe')
  WILD_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM_RECIPE = Kee[str](
    'wild_armor_trim_smithing_template_smithing_trim_recipe')
  WIND_CHARGE_RECIPE = Kee[str]('wind_charge_recipe')
  WITH_OUR_POWERS_COMBINED = Kee[str]('with_our_powers_combined')
  WITHERING_HEIGHTS = Kee[str]('withering_heights')
  WOLF_ARMOR_DYED_RECIPE = Kee[str]('wolf_armor_dyed_recipe')
  WOLF_ARMOR_RECIPE = Kee[str]('wolf_armor_recipe')
  WOODEN_AXE_RECIPE = Kee[str]('wooden_axe_recipe')
  WOODEN_HOE_RECIPE = Kee[str]('wooden_hoe_recipe')
  WOODEN_PICKAXE_RECIPE = Kee[str]('wooden_pickaxe_recipe')
  WOODEN_SHOVEL_RECIPE = Kee[str]('wooden_shovel_recipe')
  WOODEN_SPEAR_RECIPE = Kee[str]('wooden_spear_recipe')
  WOODEN_SWORD_RECIPE = Kee[str]('wooden_sword_recipe')
  WRITABLE_BOOK_RECIPE = Kee[str]('writable_book_recipe')
  YELLOW_BANNER_RECIPE = Kee[str]('yellow_banner_recipe')
  YELLOW_BED_FROM_WHITE_BED_RECIPE = Kee[str](
    'yellow_bed_from_white_bed_recipe')
  YELLOW_BED_RECIPE = Kee[str]('yellow_bed_recipe')
  YELLOW_BUNDLE_RECIPE = Kee[str]('yellow_bundle_recipe')
  YELLOW_CANDLE_RECIPE = Kee[str]('yellow_candle_recipe')
  YELLOW_CARPET_FROM_WHITE_CARPET_RECIPE = Kee[str](
    'yellow_carpet_from_white_carpet_recipe')
  YELLOW_CARPET_RECIPE = Kee[str]('yellow_carpet_recipe')
  YELLOW_CONCRETE_POWDER_RECIPE = Kee[str]('yellow_concrete_powder_recipe')
  YELLOW_CONCRETE_SLAB_FROM_YELLOW_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'yellow_concrete_slab_from_yellow_concrete_stonecutting_recipe')
  YELLOW_CONCRETE_SLAB_RECIPE = Kee[str]('yellow_concrete_slab_recipe')
  YELLOW_CONCRETE_STAIRS_FROM_YELLOW_CONCRETE_STONECUTTING_RECIPE = Kee[str](
    'yellow_concrete_stairs_from_yellow_concrete_stonecutting_recipe')
  YELLOW_CONCRETE_STAIRS_RECIPE = Kee[str]('yellow_concrete_stairs_recipe')
  YELLOW_CUSHION_RECIPE = Kee[str]('yellow_cushion_recipe')
  YELLOW_DYE_FROM_DANDELION_RECIPE = Kee[str](
    'yellow_dye_from_dandelion_recipe')
  YELLOW_DYE_FROM_GOLDEN_DANDELION_RECIPE = Kee[str](
    'yellow_dye_from_golden_dandelion_recipe')
  YELLOW_DYE_FROM_SUNFLOWER_RECIPE = Kee[str](
    'yellow_dye_from_sunflower_recipe')
  YELLOW_DYE_FROM_WILDFLOWERS_RECIPE = Kee[str](
    'yellow_dye_from_wildflowers_recipe')
  YELLOW_GLAZED_TERRACOTTA_RECIPE = Kee[str]('yellow_glazed_terracotta_recipe')
  YELLOW_HARNESS_RECIPE = Kee[str]('yellow_harness_recipe')
  YELLOW_SHULKER_BOX_RECIPE = Kee[str]('yellow_shulker_box_recipe')
  YELLOW_STAINED_GLASS_PANE_FROM_GLASS_PANE_RECIPE = Kee[str](
    'yellow_stained_glass_pane_from_glass_pane_recipe')
  YELLOW_STAINED_GLASS_PANE_RECIPE = Kee[str](
    'yellow_stained_glass_pane_recipe')
  YELLOW_STAINED_GLASS_RECIPE = Kee[str]('yellow_stained_glass_recipe')
  YELLOW_TERRACOTTA_RECIPE = Kee[str]('yellow_terracotta_recipe')
  YELLOW_WOOL_RECIPE = Kee[str]('yellow_wool_recipe')
  YELLOW_WOOL_SLAB_RECIPE = Kee[str]('yellow_wool_slab_recipe')
  YELLOW_WOOL_STAIRS_RECIPE = Kee[str]('yellow_wool_stairs_recipe')
  YOU_NEED_A_MINT = Kee[str]('you_need_a_mint')
  YOUVE_GOT_A_FRIEND_IN_ME = Kee[str]('youve_got_a_friend_in_me')
  ZOMBIE_DOCTOR = Kee[str]('zombie_doctor')
