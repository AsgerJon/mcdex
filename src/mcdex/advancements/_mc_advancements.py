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


class MCAdvancements(MCThing, strictCase=False):
  """
  The catalogue of the game's advancements, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    stoneAge = MCAdvancements.StoneAge
    stoneAge is MCAdvancements['stone_age']  # True
    stoneAge[Version.V1_12]
    # AdvancementId('stone_age', 'minecraft:story/mine_stone')
    len(MCAdvancements)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'advancements.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'advancements.json'
  __data_key__ = 'advancements'
  __id_class__ = AdvancementId
  __kind__ = 'advancement'
  __game_names__ = True

  #  Members, one for every thing of 'advancements.json'
  ABalancedDiet = Kee[str]('a_balanced_diet')
  ACompleteCatalogue = Kee[str]('a_complete_catalogue')
  AFuriousCocktail = Kee[str]('a_furious_cocktail')
  ASeedyPlace = Kee[str]('a_seedy_place')
  ATerribleFortress = Kee[str]('a_terrible_fortress')
  AThrowawayJoke = Kee[str]('a_throwaway_joke')
  AcaciaBoatRecipe = Kee[str]('acacia_boat_recipe')
  AcaciaButtonRecipe = Kee[str]('acacia_button_recipe')
  AcaciaChestBoatRecipe = Kee[str]('acacia_chest_boat_recipe')
  AcaciaDoorRecipe = Kee[str]('acacia_door_recipe')
  AcaciaFenceGateRecipe = Kee[str]('acacia_fence_gate_recipe')
  AcaciaFenceRecipe = Kee[str]('acacia_fence_recipe')
  AcaciaHangingSignRecipe = Kee[str]('acacia_hanging_sign_recipe')
  AcaciaPlanksRecipe = Kee[str]('acacia_planks_recipe')
  AcaciaPressurePlateRecipe = Kee[str]('acacia_pressure_plate_recipe')
  AcaciaShelfRecipe = Kee[str]('acacia_shelf_recipe')
  AcaciaSignRecipe = Kee[str]('acacia_sign_recipe')
  AcaciaSlabRecipe = Kee[str]('acacia_slab_recipe')
  AcaciaStairsRecipe = Kee[str]('acacia_stairs_recipe')
  AcaciaTrapdoorRecipe = Kee[str]('acacia_trapdoor_recipe')
  AcaciaWoodRecipe = Kee[str]('acacia_wood_recipe')
  AcquireHardware = Kee[str]('acquire_hardware')
  ActivatorRailRecipe = Kee[str]('activator_rail_recipe')
  AdventureRoot = Kee[str]('adventure_root')
  AdventuringTime = Kee[str]('adventuring_time')
  AmethystBlockRecipe = Kee[str]('amethyst_block_recipe')
  AndesiteRecipe = Kee[str]('andesite_recipe')
  AndesiteSlabFromAndesiteStonecuttingRecipe = Kee[str](
    'andesite_slab_from_andesite_stonecutting_recipe')
  AndesiteSlabRecipe = Kee[str]('andesite_slab_recipe')
  AndesiteStairsFromAndesiteStonecuttingRecipe = Kee[str](
    'andesite_stairs_from_andesite_stonecutting_recipe')
  AndesiteStairsRecipe = Kee[str]('andesite_stairs_recipe')
  AndesiteWallFromAndesiteStonecuttingRecipe = Kee[str](
    'andesite_wall_from_andesite_stonecutting_recipe')
  AndesiteWallRecipe = Kee[str]('andesite_wall_recipe')
  AnvilRecipe = Kee[str]('anvil_recipe')
  Arbalistic = Kee[str]('arbalistic')
  ArmorStandRecipe = Kee[str]('armor_stand_recipe')
  ArrowRecipe = Kee[str]('arrow_recipe')
  BakedPotatoFromCampfireCookingRecipe = Kee[str](
    'baked_potato_from_campfire_cooking_recipe')
  BakedPotatoFromSmokingRecipe = Kee[str]('baked_potato_from_smoking_recipe')
  BakedPotatoRecipe = Kee[str]('baked_potato_recipe')
  BambooBlockRecipe = Kee[str]('bamboo_block_recipe')
  BambooButtonRecipe = Kee[str]('bamboo_button_recipe')
  BambooChestRaftRecipe = Kee[str]('bamboo_chest_raft_recipe')
  BambooDoorRecipe = Kee[str]('bamboo_door_recipe')
  BambooFenceGateRecipe = Kee[str]('bamboo_fence_gate_recipe')
  BambooFenceRecipe = Kee[str]('bamboo_fence_recipe')
  BambooHangingSignRecipe = Kee[str]('bamboo_hanging_sign_recipe')
  BambooMosaicRecipe = Kee[str]('bamboo_mosaic_recipe')
  BambooMosaicSlabRecipe = Kee[str]('bamboo_mosaic_slab_recipe')
  BambooMosaicStairsRecipe = Kee[str]('bamboo_mosaic_stairs_recipe')
  BambooPlanksRecipe = Kee[str]('bamboo_planks_recipe')
  BambooPressurePlateRecipe = Kee[str]('bamboo_pressure_plate_recipe')
  BambooRaftRecipe = Kee[str]('bamboo_raft_recipe')
  BambooShelfRecipe = Kee[str]('bamboo_shelf_recipe')
  BambooSignRecipe = Kee[str]('bamboo_sign_recipe')
  BambooSlabRecipe = Kee[str]('bamboo_slab_recipe')
  BambooStairsRecipe = Kee[str]('bamboo_stairs_recipe')
  BambooTrapdoorRecipe = Kee[str]('bamboo_trapdoor_recipe')
  BarrelRecipe = Kee[str]('barrel_recipe')
  BeaconRecipe = Kee[str]('beacon_recipe')
  Beaconator = Kee[str]('beaconator')
  BeeOurGuest = Kee[str]('bee_our_guest')
  BeehiveRecipe = Kee[str]('beehive_recipe')
  BeetrootSoupRecipe = Kee[str]('beetroot_soup_recipe')
  BestFriendsForever = Kee[str]('best_friends_forever')
  BirchBoatRecipe = Kee[str]('birch_boat_recipe')
  BirchButtonRecipe = Kee[str]('birch_button_recipe')
  BirchChestBoatRecipe = Kee[str]('birch_chest_boat_recipe')
  BirchDoorRecipe = Kee[str]('birch_door_recipe')
  BirchFenceGateRecipe = Kee[str]('birch_fence_gate_recipe')
  BirchFenceRecipe = Kee[str]('birch_fence_recipe')
  BirchHangingSignRecipe = Kee[str]('birch_hanging_sign_recipe')
  BirchPlanksRecipe = Kee[str]('birch_planks_recipe')
  BirchPressurePlateRecipe = Kee[str]('birch_pressure_plate_recipe')
  BirchShelfRecipe = Kee[str]('birch_shelf_recipe')
  BirchSignRecipe = Kee[str]('birch_sign_recipe')
  BirchSlabRecipe = Kee[str]('birch_slab_recipe')
  BirchStairsRecipe = Kee[str]('birch_stairs_recipe')
  BirchTrapdoorRecipe = Kee[str]('birch_trapdoor_recipe')
  BirchWoodRecipe = Kee[str]('birch_wood_recipe')
  BirthdaySong = Kee[str]('birthday_song')
  BlackBannerRecipe = Kee[str]('black_banner_recipe')
  BlackBedFromWhiteBedRecipe = Kee[str]('black_bed_from_white_bed_recipe')
  BlackBedRecipe = Kee[str]('black_bed_recipe')
  BlackBundleRecipe = Kee[str]('black_bundle_recipe')
  BlackCandleRecipe = Kee[str]('black_candle_recipe')
  BlackCarpetFromWhiteCarpetRecipe = Kee[str](
    'black_carpet_from_white_carpet_recipe')
  BlackCarpetRecipe = Kee[str]('black_carpet_recipe')
  BlackConcretePowderRecipe = Kee[str]('black_concrete_powder_recipe')
  BlackConcreteSlabFromBlackConcreteStonecuttingRecipe = Kee[str](
    'black_concrete_slab_from_black_concrete_stonecutting_recipe')
  BlackConcreteSlabRecipe = Kee[str]('black_concrete_slab_recipe')
  BlackConcreteStairsFromBlackConcreteStonecuttingRecipe = Kee[str](
    'black_concrete_stairs_from_black_concrete_stonecutting_recipe')
  BlackConcreteStairsRecipe = Kee[str]('black_concrete_stairs_recipe')
  BlackCushionRecipe = Kee[str]('black_cushion_recipe')
  BlackDyeFromWitherRoseRecipe = Kee[str]('black_dye_from_wither_rose_recipe')
  BlackDyeRecipe = Kee[str]('black_dye_recipe')
  BlackGlazedTerracottaRecipe = Kee[str]('black_glazed_terracotta_recipe')
  BlackHarnessRecipe = Kee[str]('black_harness_recipe')
  BlackShulkerBoxRecipe = Kee[str]('black_shulker_box_recipe')
  BlackStainedGlassPaneFromGlassPaneRecipe = Kee[str](
    'black_stained_glass_pane_from_glass_pane_recipe')
  BlackStainedGlassPaneRecipe = Kee[str]('black_stained_glass_pane_recipe')
  BlackStainedGlassRecipe = Kee[str]('black_stained_glass_recipe')
  BlackTerracottaRecipe = Kee[str]('black_terracotta_recipe')
  BlackWoolRecipe = Kee[str]('black_wool_recipe')
  BlackWoolSlabRecipe = Kee[str]('black_wool_slab_recipe')
  BlackWoolStairsRecipe = Kee[str]('black_wool_stairs_recipe')
  BlackstoneSlabFromBlackstoneStonecuttingRecipe = Kee[str](
    'blackstone_slab_from_blackstone_stonecutting_recipe')
  BlackstoneSlabRecipe = Kee[str]('blackstone_slab_recipe')
  BlackstoneStairsFromBlackstoneStonecuttingRecipe = Kee[str](
    'blackstone_stairs_from_blackstone_stonecutting_recipe')
  BlackstoneStairsRecipe = Kee[str]('blackstone_stairs_recipe')
  BlackstoneWallFromBlackstoneStonecuttingRecipe = Kee[str](
    'blackstone_wall_from_blackstone_stonecutting_recipe')
  BlackstoneWallRecipe = Kee[str]('blackstone_wall_recipe')
  BlastFurnaceRecipe = Kee[str]('blast_furnace_recipe')
  BlazePowderRecipe = Kee[str]('blaze_powder_recipe')
  Blowback = Kee[str]('blowback')
  BlueBannerRecipe = Kee[str]('blue_banner_recipe')
  BlueBedFromWhiteBedRecipe = Kee[str]('blue_bed_from_white_bed_recipe')
  BlueBedRecipe = Kee[str]('blue_bed_recipe')
  BlueBundleRecipe = Kee[str]('blue_bundle_recipe')
  BlueCandleRecipe = Kee[str]('blue_candle_recipe')
  BlueCarpetFromWhiteCarpetRecipe = Kee[str](
    'blue_carpet_from_white_carpet_recipe')
  BlueCarpetRecipe = Kee[str]('blue_carpet_recipe')
  BlueConcretePowderRecipe = Kee[str]('blue_concrete_powder_recipe')
  BlueConcreteSlabFromBlueConcreteStonecuttingRecipe = Kee[str](
    'blue_concrete_slab_from_blue_concrete_stonecutting_recipe')
  BlueConcreteSlabRecipe = Kee[str]('blue_concrete_slab_recipe')
  BlueConcreteStairsFromBlueConcreteStonecuttingRecipe = Kee[str](
    'blue_concrete_stairs_from_blue_concrete_stonecutting_recipe')
  BlueConcreteStairsRecipe = Kee[str]('blue_concrete_stairs_recipe')
  BlueCushionRecipe = Kee[str]('blue_cushion_recipe')
  BlueDyeFromCornflowerRecipe = Kee[str]('blue_dye_from_cornflower_recipe')
  BlueDyeRecipe = Kee[str]('blue_dye_recipe')
  BlueGlazedTerracottaRecipe = Kee[str]('blue_glazed_terracotta_recipe')
  BlueHarnessRecipe = Kee[str]('blue_harness_recipe')
  BlueIceRecipe = Kee[str]('blue_ice_recipe')
  BlueShulkerBoxRecipe = Kee[str]('blue_shulker_box_recipe')
  BlueStainedGlassPaneFromGlassPaneRecipe = Kee[str](
    'blue_stained_glass_pane_from_glass_pane_recipe')
  BlueStainedGlassPaneRecipe = Kee[str]('blue_stained_glass_pane_recipe')
  BlueStainedGlassRecipe = Kee[str]('blue_stained_glass_recipe')
  BlueTerracottaRecipe = Kee[str]('blue_terracotta_recipe')
  BlueWoolRecipe = Kee[str]('blue_wool_recipe')
  BlueWoolSlabRecipe = Kee[str]('blue_wool_slab_recipe')
  BlueWoolStairsRecipe = Kee[str]('blue_wool_stairs_recipe')
  BoltArmorTrimSmithingTemplateRecipe = Kee[str](
    'bolt_armor_trim_smithing_template_recipe')
  BoltArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'bolt_armor_trim_smithing_template_smithing_trim_recipe')
  BoneBlockRecipe = Kee[str]('bone_block_recipe')
  BoneMealFromBoneBlockRecipe = Kee[str]('bone_meal_from_bone_block_recipe')
  BoneMealRecipe = Kee[str]('bone_meal_recipe')
  BookRecipe = Kee[str]('book_recipe')
  BookshelfRecipe = Kee[str]('bookshelf_recipe')
  BordureIndentedBannerPatternRecipe = Kee[str](
    'bordure_indented_banner_pattern_recipe')
  BowRecipe = Kee[str]('bow_recipe')
  BowlRecipe = Kee[str]('bowl_recipe')
  BreadRecipe = Kee[str]('bread_recipe')
  BrewingStandRecipe = Kee[str]('brewing_stand_recipe')
  BrickRecipe = Kee[str]('brick_recipe')
  BrickSlabFromBricksStonecuttingRecipe = Kee[str](
    'brick_slab_from_bricks_stonecutting_recipe')
  BrickSlabRecipe = Kee[str]('brick_slab_recipe')
  BrickStairsFromBricksStonecuttingRecipe = Kee[str](
    'brick_stairs_from_bricks_stonecutting_recipe')
  BrickStairsRecipe = Kee[str]('brick_stairs_recipe')
  BrickWallFromBricksStonecuttingRecipe = Kee[str](
    'brick_wall_from_bricks_stonecutting_recipe')
  BrickWallRecipe = Kee[str]('brick_wall_recipe')
  BricksRecipe = Kee[str]('bricks_recipe')
  BringHomeTheBeacon = Kee[str]('bring_home_the_beacon')
  BrownBannerRecipe = Kee[str]('brown_banner_recipe')
  BrownBedFromWhiteBedRecipe = Kee[str]('brown_bed_from_white_bed_recipe')
  BrownBedRecipe = Kee[str]('brown_bed_recipe')
  BrownBundleRecipe = Kee[str]('brown_bundle_recipe')
  BrownCandleRecipe = Kee[str]('brown_candle_recipe')
  BrownCarpetFromWhiteCarpetRecipe = Kee[str](
    'brown_carpet_from_white_carpet_recipe')
  BrownCarpetRecipe = Kee[str]('brown_carpet_recipe')
  BrownConcretePowderRecipe = Kee[str]('brown_concrete_powder_recipe')
  BrownConcreteSlabFromBrownConcreteStonecuttingRecipe = Kee[str](
    'brown_concrete_slab_from_brown_concrete_stonecutting_recipe')
  BrownConcreteSlabRecipe = Kee[str]('brown_concrete_slab_recipe')
  BrownConcreteStairsFromBrownConcreteStonecuttingRecipe = Kee[str](
    'brown_concrete_stairs_from_brown_concrete_stonecutting_recipe')
  BrownConcreteStairsRecipe = Kee[str]('brown_concrete_stairs_recipe')
  BrownCushionRecipe = Kee[str]('brown_cushion_recipe')
  BrownDyeRecipe = Kee[str]('brown_dye_recipe')
  BrownGlazedTerracottaRecipe = Kee[str]('brown_glazed_terracotta_recipe')
  BrownHarnessRecipe = Kee[str]('brown_harness_recipe')
  BrownShulkerBoxRecipe = Kee[str]('brown_shulker_box_recipe')
  BrownStainedGlassPaneFromGlassPaneRecipe = Kee[str](
    'brown_stained_glass_pane_from_glass_pane_recipe')
  BrownStainedGlassPaneRecipe = Kee[str]('brown_stained_glass_pane_recipe')
  BrownStainedGlassRecipe = Kee[str]('brown_stained_glass_recipe')
  BrownTerracottaRecipe = Kee[str]('brown_terracotta_recipe')
  BrownWoolRecipe = Kee[str]('brown_wool_recipe')
  BrownWoolSlabRecipe = Kee[str]('brown_wool_slab_recipe')
  BrownWoolStairsRecipe = Kee[str]('brown_wool_stairs_recipe')
  BrushRecipe = Kee[str]('brush_recipe')
  BucketRecipe = Kee[str]('bucket_recipe')
  BukkitBukkit = Kee[str]('bukkit_bukkit')
  Bullseye = Kee[str]('bullseye')
  BundleRecipe = Kee[str]('bundle_recipe')
  CactusGreenRecipe = Kee[str]('cactus_green_recipe')
  CakeRecipe = Kee[str]('cake_recipe')
  CalibratedSculkSensorRecipe = Kee[str]('calibrated_sculk_sensor_recipe')
  CampfireRecipe = Kee[str]('campfire_recipe')
  CandleRecipe = Kee[str]('candle_recipe')
  CarefulRestoration = Kee[str]('careful_restoration')
  CarrotOnAStickRecipe = Kee[str]('carrot_on_a_stick_recipe')
  CartographyTableRecipe = Kee[str]('cartography_table_recipe')
  CauldronRecipe = Kee[str]('cauldron_recipe')
  CavesCliffs = Kee[str]('caves_cliffs')
  ChainRecipe = Kee[str]('chain_recipe')
  CharcoalRecipe = Kee[str]('charcoal_recipe')
  CherryBoatRecipe = Kee[str]('cherry_boat_recipe')
  CherryButtonRecipe = Kee[str]('cherry_button_recipe')
  CherryChestBoatRecipe = Kee[str]('cherry_chest_boat_recipe')
  CherryDoorRecipe = Kee[str]('cherry_door_recipe')
  CherryFenceGateRecipe = Kee[str]('cherry_fence_gate_recipe')
  CherryFenceRecipe = Kee[str]('cherry_fence_recipe')
  CherryHangingSignRecipe = Kee[str]('cherry_hanging_sign_recipe')
  CherryPlanksRecipe = Kee[str]('cherry_planks_recipe')
  CherryPressurePlateRecipe = Kee[str]('cherry_pressure_plate_recipe')
  CherryShelfRecipe = Kee[str]('cherry_shelf_recipe')
  CherrySignRecipe = Kee[str]('cherry_sign_recipe')
  CherrySlabRecipe = Kee[str]('cherry_slab_recipe')
  CherryStairsRecipe = Kee[str]('cherry_stairs_recipe')
  CherryTrapdoorRecipe = Kee[str]('cherry_trapdoor_recipe')
  CherryWoodRecipe = Kee[str]('cherry_wood_recipe')
  ChestMinecartRecipe = Kee[str]('chest_minecart_recipe')
  ChestRecipe = Kee[str]('chest_recipe')
  ChiseledBookshelfRecipe = Kee[str]('chiseled_bookshelf_recipe')
  ChiseledCinnabarFromCinnabarStonecuttingRecipe = Kee[str](
    'chiseled_cinnabar_from_cinnabar_stonecutting_recipe')
  ChiseledCinnabarRecipe = Kee[str]('chiseled_cinnabar_recipe')
  ChiseledCopperFromCopperBlockStonecuttingRecipe = Kee[str](
    'chiseled_copper_from_copper_block_stonecutting_recipe')
  ChiseledCopperFromCutCopperStonecuttingRecipe = Kee[str](
    'chiseled_copper_from_cut_copper_stonecutting_recipe')
  ChiseledCopperRecipe = Kee[str]('chiseled_copper_recipe')
  ChiseledDeepslateFromCobbledDeepslateStonecuttingRecipe = Kee[str](
    'chiseled_deepslate_from_cobbled_deepslate_stonecutting_recipe')
  ChiseledDeepslateFromDeepslateStonecuttingRecipe = Kee[str](
    'chiseled_deepslate_from_deepslate_stonecutting_recipe')
  ChiseledDeepslateRecipe = Kee[str]('chiseled_deepslate_recipe')
  ChiseledNetherBricksFromNetherBricksStonecuttingRecipe = Kee[str](
    'chiseled_nether_bricks_from_nether_bricks_stonecutting_recipe')
  ChiseledNetherBricksRecipe = Kee[str]('chiseled_nether_bricks_recipe')
  ChiseledPolishedBlackstoneFromBlackstoneStonecuttingRecipe = Kee[str](
    'chiseled_polished_blackstone_from_blackstone_stonecutting_recipe')
  ChiseledPolishedBlackstoneFromPolishedBlackstoneStonecuttingRecipe = Kee[str](
    'chiseled_polished_blackstone_from_polished_blackstone_stonecutting_recipe')
  ChiseledPolishedBlackstoneRecipe = Kee[str](
    'chiseled_polished_blackstone_recipe')
  ChiseledQuartzBlockFromQuartzBlockStonecuttingRecipe = Kee[str](
    'chiseled_quartz_block_from_quartz_block_stonecutting_recipe')
  ChiseledQuartzBlockRecipe = Kee[str]('chiseled_quartz_block_recipe')
  ChiseledRedSandstoneFromRedSandstoneStonecuttingRecipe = Kee[str](
    'chiseled_red_sandstone_from_red_sandstone_stonecutting_recipe')
  ChiseledRedSandstoneRecipe = Kee[str]('chiseled_red_sandstone_recipe')
  ChiseledResinBricksFromResinBricksStonecuttingRecipe = Kee[str](
    'chiseled_resin_bricks_from_resin_bricks_stonecutting_recipe')
  ChiseledResinBricksRecipe = Kee[str]('chiseled_resin_bricks_recipe')
  ChiseledSandstoneFromSandstoneStonecuttingRecipe = Kee[str](
    'chiseled_sandstone_from_sandstone_stonecutting_recipe')
  ChiseledSandstoneRecipe = Kee[str]('chiseled_sandstone_recipe')
  ChiseledStoneBricksFromStoneBricksStonecuttingRecipe = Kee[str](
    'chiseled_stone_bricks_from_stone_bricks_stonecutting_recipe')
  ChiseledStoneBricksFromStoneStonecuttingRecipe = Kee[str](
    'chiseled_stone_bricks_from_stone_stonecutting_recipe')
  ChiseledStoneBricksRecipe = Kee[str]('chiseled_stone_bricks_recipe')
  ChiseledSulfurFromSulfurStonecuttingRecipe = Kee[str](
    'chiseled_sulfur_from_sulfur_stonecutting_recipe')
  ChiseledSulfurRecipe = Kee[str]('chiseled_sulfur_recipe')
  ChiseledTuffBricksFromPolishedTuffStonecuttingRecipe = Kee[str](
    'chiseled_tuff_bricks_from_polished_tuff_stonecutting_recipe')
  ChiseledTuffBricksFromTuffBricksStonecuttingRecipe = Kee[str](
    'chiseled_tuff_bricks_from_tuff_bricks_stonecutting_recipe')
  ChiseledTuffBricksFromTuffStonecuttingRecipe = Kee[str](
    'chiseled_tuff_bricks_from_tuff_stonecutting_recipe')
  ChiseledTuffBricksRecipe = Kee[str]('chiseled_tuff_bricks_recipe')
  ChiseledTuffFromTuffStonecuttingRecipe = Kee[str](
    'chiseled_tuff_from_tuff_stonecutting_recipe')
  ChiseledTuffRecipe = Kee[str]('chiseled_tuff_recipe')
  CinnabarBrickSlabFromCinnabarBricksStonecuttingRecipe = Kee[str](
    'cinnabar_brick_slab_from_cinnabar_bricks_stonecutting_recipe')
  CinnabarBrickSlabFromCinnabarStonecuttingRecipe = Kee[str](
    'cinnabar_brick_slab_from_cinnabar_stonecutting_recipe')
  CinnabarBrickSlabFromPolishedCinnabarStonecuttingRecipe = Kee[str](
    'cinnabar_brick_slab_from_polished_cinnabar_stonecutting_recipe')
  CinnabarBrickSlabRecipe = Kee[str]('cinnabar_brick_slab_recipe')
  CinnabarBrickStairsFromCinnabarBricksStonecuttingRecipe = Kee[str](
    'cinnabar_brick_stairs_from_cinnabar_bricks_stonecutting_recipe')
  CinnabarBrickStairsFromCinnabarStonecuttingRecipe = Kee[str](
    'cinnabar_brick_stairs_from_cinnabar_stonecutting_recipe')
  CinnabarBrickStairsFromPolishedCinnabarStonecuttingRecipe = Kee[str](
    'cinnabar_brick_stairs_from_polished_cinnabar_stonecutting_recipe')
  CinnabarBrickStairsRecipe = Kee[str]('cinnabar_brick_stairs_recipe')
  CinnabarBrickWallFromCinnabarBricksStonecuttingRecipe = Kee[str](
    'cinnabar_brick_wall_from_cinnabar_bricks_stonecutting_recipe')
  CinnabarBrickWallFromCinnabarStonecuttingRecipe = Kee[str](
    'cinnabar_brick_wall_from_cinnabar_stonecutting_recipe')
  CinnabarBrickWallFromPolishedCinnabarStonecuttingRecipe = Kee[str](
    'cinnabar_brick_wall_from_polished_cinnabar_stonecutting_recipe')
  CinnabarBrickWallRecipe = Kee[str]('cinnabar_brick_wall_recipe')
  CinnabarBricksFromCinnabarStonecuttingRecipe = Kee[str](
    'cinnabar_bricks_from_cinnabar_stonecutting_recipe')
  CinnabarBricksFromPolishedCinnabarStonecuttingRecipe = Kee[str](
    'cinnabar_bricks_from_polished_cinnabar_stonecutting_recipe')
  CinnabarBricksRecipe = Kee[str]('cinnabar_bricks_recipe')
  CinnabarSlabFromCinnabarStonecuttingRecipe = Kee[str](
    'cinnabar_slab_from_cinnabar_stonecutting_recipe')
  CinnabarSlabRecipe = Kee[str]('cinnabar_slab_recipe')
  CinnabarStairsFromCinnabarStonecuttingRecipe = Kee[str](
    'cinnabar_stairs_from_cinnabar_stonecutting_recipe')
  CinnabarStairsRecipe = Kee[str]('cinnabar_stairs_recipe')
  CinnabarWallFromCinnabarStonecuttingRecipe = Kee[str](
    'cinnabar_wall_from_cinnabar_stonecutting_recipe')
  CinnabarWallRecipe = Kee[str]('cinnabar_wall_recipe')
  ClayRecipe = Kee[str]('clay_recipe')
  ClockRecipe = Kee[str]('clock_recipe')
  CoalBlockRecipe = Kee[str]('coal_block_recipe')
  CoalFromBlastingCoalOreRecipe = Kee[str](
    'coal_from_blasting_coal_ore_recipe')
  CoalFromBlastingDeepslateCoalOreRecipe = Kee[str](
    'coal_from_blasting_deepslate_coal_ore_recipe')
  CoalFromBlastingRecipe = Kee[str]('coal_from_blasting_recipe')
  CoalFromSmeltingCoalOreRecipe = Kee[str](
    'coal_from_smelting_coal_ore_recipe')
  CoalFromSmeltingDeepslateCoalOreRecipe = Kee[str](
    'coal_from_smelting_deepslate_coal_ore_recipe')
  CoalFromSmeltingRecipe = Kee[str]('coal_from_smelting_recipe')
  CoalRecipe = Kee[str]('coal_recipe')
  CoarseDirtRecipe = Kee[str]('coarse_dirt_recipe')
  CoastArmorTrimSmithingTemplateRecipe = Kee[str](
    'coast_armor_trim_smithing_template_recipe')
  CoastArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'coast_armor_trim_smithing_template_smithing_trim_recipe')
  CobbledDeepslateFromDeepslateStonecuttingRecipe = Kee[str](
    'cobbled_deepslate_from_deepslate_stonecutting_recipe')
  CobbledDeepslateSlabFromCobbledDeepslateStonecuttingRecipe = Kee[str](
    'cobbled_deepslate_slab_from_cobbled_deepslate_stonecutting_recipe')
  CobbledDeepslateSlabFromDeepslateStonecuttingRecipe = Kee[str](
    'cobbled_deepslate_slab_from_deepslate_stonecutting_recipe')
  CobbledDeepslateSlabRecipe = Kee[str]('cobbled_deepslate_slab_recipe')
  CobbledDeepslateStairsFromCobbledDeepslateStonecuttingRecipe = Kee[str](
    'cobbled_deepslate_stairs_from_cobbled_deepslate_stonecutting_recipe')
  CobbledDeepslateStairsFromDeepslateStonecuttingRecipe = Kee[str](
    'cobbled_deepslate_stairs_from_deepslate_stonecutting_recipe')
  CobbledDeepslateStairsRecipe = Kee[str]('cobbled_deepslate_stairs_recipe')
  CobbledDeepslateWallFromCobbledDeepslateStonecuttingRecipe = Kee[str](
    'cobbled_deepslate_wall_from_cobbled_deepslate_stonecutting_recipe')
  CobbledDeepslateWallFromDeepslateStonecuttingRecipe = Kee[str](
    'cobbled_deepslate_wall_from_deepslate_stonecutting_recipe')
  CobbledDeepslateWallRecipe = Kee[str]('cobbled_deepslate_wall_recipe')
  CobblestoneFromStoneStonecuttingRecipe = Kee[str](
    'cobblestone_from_stone_stonecutting_recipe')
  CobblestoneSlabFromCobblestoneStonecuttingRecipe = Kee[str](
    'cobblestone_slab_from_cobblestone_stonecutting_recipe')
  CobblestoneSlabFromStoneStonecuttingRecipe = Kee[str](
    'cobblestone_slab_from_stone_stonecutting_recipe')
  CobblestoneSlabRecipe = Kee[str]('cobblestone_slab_recipe')
  CobblestoneStairsFromCobblestoneStonecuttingRecipe = Kee[str](
    'cobblestone_stairs_from_cobblestone_stonecutting_recipe')
  CobblestoneStairsFromStoneStonecuttingRecipe = Kee[str](
    'cobblestone_stairs_from_stone_stonecutting_recipe')
  CobblestoneStairsRecipe = Kee[str]('cobblestone_stairs_recipe')
  CobblestoneWallFromCobblestoneStonecuttingRecipe = Kee[str](
    'cobblestone_wall_from_cobblestone_stonecutting_recipe')
  CobblestoneWallFromStoneStonecuttingRecipe = Kee[str](
    'cobblestone_wall_from_stone_stonecutting_recipe')
  CobblestoneWallRecipe = Kee[str]('cobblestone_wall_recipe')
  ComparatorRecipe = Kee[str]('comparator_recipe')
  CompassRecipe = Kee[str]('compass_recipe')
  ComposterRecipe = Kee[str]('composter_recipe')
  ConduitRecipe = Kee[str]('conduit_recipe')
  CookedBeefFromCampfireCookingRecipe = Kee[str](
    'cooked_beef_from_campfire_cooking_recipe')
  CookedBeefFromSmokingRecipe = Kee[str]('cooked_beef_from_smoking_recipe')
  CookedBeefRecipe = Kee[str]('cooked_beef_recipe')
  CookedChickenFromCampfireCookingRecipe = Kee[str](
    'cooked_chicken_from_campfire_cooking_recipe')
  CookedChickenFromSmokingRecipe = Kee[str](
    'cooked_chicken_from_smoking_recipe')
  CookedChickenRecipe = Kee[str]('cooked_chicken_recipe')
  CookedCodFromCampfireCookingRecipe = Kee[str](
    'cooked_cod_from_campfire_cooking_recipe')
  CookedCodFromSmokingRecipe = Kee[str]('cooked_cod_from_smoking_recipe')
  CookedCodRecipe = Kee[str]('cooked_cod_recipe')
  CookedMuttonFromCampfireCookingRecipe = Kee[str](
    'cooked_mutton_from_campfire_cooking_recipe')
  CookedMuttonFromSmokingRecipe = Kee[str]('cooked_mutton_from_smoking_recipe')
  CookedMuttonRecipe = Kee[str]('cooked_mutton_recipe')
  CookedPorkchopFromCampfireCookingRecipe = Kee[str](
    'cooked_porkchop_from_campfire_cooking_recipe')
  CookedPorkchopFromSmokingRecipe = Kee[str](
    'cooked_porkchop_from_smoking_recipe')
  CookedPorkchopRecipe = Kee[str]('cooked_porkchop_recipe')
  CookedRabbitFromCampfireCookingRecipe = Kee[str](
    'cooked_rabbit_from_campfire_cooking_recipe')
  CookedRabbitFromSmokingRecipe = Kee[str]('cooked_rabbit_from_smoking_recipe')
  CookedRabbitRecipe = Kee[str]('cooked_rabbit_recipe')
  CookedSalmonFromCampfireCookingRecipe = Kee[str](
    'cooked_salmon_from_campfire_cooking_recipe')
  CookedSalmonFromSmokingRecipe = Kee[str]('cooked_salmon_from_smoking_recipe')
  CookedSalmonRecipe = Kee[str]('cooked_salmon_recipe')
  CookieRecipe = Kee[str]('cookie_recipe')
  CopperAxeRecipe = Kee[str]('copper_axe_recipe')
  CopperBarsRecipe = Kee[str]('copper_bars_recipe')
  CopperBlockRecipe = Kee[str]('copper_block_recipe')
  CopperBootsRecipe = Kee[str]('copper_boots_recipe')
  CopperBulbRecipe = Kee[str]('copper_bulb_recipe')
  CopperChainRecipe = Kee[str]('copper_chain_recipe')
  CopperChestRecipe = Kee[str]('copper_chest_recipe')
  CopperChestplateRecipe = Kee[str]('copper_chestplate_recipe')
  CopperDoorRecipe = Kee[str]('copper_door_recipe')
  CopperGrateFromCopperBlockStonecuttingRecipe = Kee[str](
    'copper_grate_from_copper_block_stonecutting_recipe')
  CopperGrateRecipe = Kee[str]('copper_grate_recipe')
  CopperHelmetRecipe = Kee[str]('copper_helmet_recipe')
  CopperHoeRecipe = Kee[str]('copper_hoe_recipe')
  CopperIngotFromBlastingCopperOreRecipe = Kee[str](
    'copper_ingot_from_blasting_copper_ore_recipe')
  CopperIngotFromBlastingDeepslateCopperOreRecipe = Kee[str](
    'copper_ingot_from_blasting_deepslate_copper_ore_recipe')
  CopperIngotFromBlastingRawCopperRecipe = Kee[str](
    'copper_ingot_from_blasting_raw_copper_recipe')
  CopperIngotFromNuggetsRecipe = Kee[str]('copper_ingot_from_nuggets_recipe')
  CopperIngotFromSmeltingCopperOreRecipe = Kee[str](
    'copper_ingot_from_smelting_copper_ore_recipe')
  CopperIngotFromSmeltingDeepslateCopperOreRecipe = Kee[str](
    'copper_ingot_from_smelting_deepslate_copper_ore_recipe')
  CopperIngotFromSmeltingRawCopperRecipe = Kee[str](
    'copper_ingot_from_smelting_raw_copper_recipe')
  CopperIngotFromWaxedCopperBlockRecipe = Kee[str](
    'copper_ingot_from_waxed_copper_block_recipe')
  CopperIngotRecipe = Kee[str]('copper_ingot_recipe')
  CopperLanternRecipe = Kee[str]('copper_lantern_recipe')
  CopperLeggingsRecipe = Kee[str]('copper_leggings_recipe')
  CopperNuggetFromBlastingRecipe = Kee[str](
    'copper_nugget_from_blasting_recipe')
  CopperNuggetFromSmeltingRecipe = Kee[str](
    'copper_nugget_from_smelting_recipe')
  CopperNuggetRecipe = Kee[str]('copper_nugget_recipe')
  CopperPickaxeRecipe = Kee[str]('copper_pickaxe_recipe')
  CopperShovelRecipe = Kee[str]('copper_shovel_recipe')
  CopperSpearRecipe = Kee[str]('copper_spear_recipe')
  CopperSwordRecipe = Kee[str]('copper_sword_recipe')
  CopperTorchRecipe = Kee[str]('copper_torch_recipe')
  CopperTrapdoorRecipe = Kee[str]('copper_trapdoor_recipe')
  CountryLodeTakeMeHome = Kee[str]('country_lode_take_me_home')
  CoverMeInDebris = Kee[str]('cover_me_in_debris')
  CoverMeWithDiamonds = Kee[str]('cover_me_with_diamonds')
  CrackedDeepslateBricksRecipe = Kee[str]('cracked_deepslate_bricks_recipe')
  CrackedDeepslateTilesRecipe = Kee[str]('cracked_deepslate_tiles_recipe')
  CrackedNetherBricksRecipe = Kee[str]('cracked_nether_bricks_recipe')
  CrackedPolishedBlackstoneBricksRecipe = Kee[str](
    'cracked_polished_blackstone_bricks_recipe')
  CrackedStoneBricksRecipe = Kee[str]('cracked_stone_bricks_recipe')
  CrafterRecipe = Kee[str]('crafter_recipe')
  CraftersCraftingCrafters = Kee[str]('crafters_crafting_crafters')
  CraftingANewLook = Kee[str]('crafting_a_new_look')
  CraftingTableRecipe = Kee[str]('crafting_table_recipe')
  CreakingHeartRecipe = Kee[str]('creaking_heart_recipe')
  CreeperBannerPatternRecipe = Kee[str]('creeper_banner_pattern_recipe')
  CrimsonButtonRecipe = Kee[str]('crimson_button_recipe')
  CrimsonDoorRecipe = Kee[str]('crimson_door_recipe')
  CrimsonFenceGateRecipe = Kee[str]('crimson_fence_gate_recipe')
  CrimsonFenceRecipe = Kee[str]('crimson_fence_recipe')
  CrimsonHangingSignRecipe = Kee[str]('crimson_hanging_sign_recipe')
  CrimsonHyphaeRecipe = Kee[str]('crimson_hyphae_recipe')
  CrimsonPlanksRecipe = Kee[str]('crimson_planks_recipe')
  CrimsonPressurePlateRecipe = Kee[str]('crimson_pressure_plate_recipe')
  CrimsonShelfRecipe = Kee[str]('crimson_shelf_recipe')
  CrimsonSignRecipe = Kee[str]('crimson_sign_recipe')
  CrimsonSlabRecipe = Kee[str]('crimson_slab_recipe')
  CrimsonStairsRecipe = Kee[str]('crimson_stairs_recipe')
  CrimsonTrapdoorRecipe = Kee[str]('crimson_trapdoor_recipe')
  CrossbowRecipe = Kee[str]('crossbow_recipe')
  CutCopperFromCopperBlockStonecuttingRecipe = Kee[str](
    'cut_copper_from_copper_block_stonecutting_recipe')
  CutCopperRecipe = Kee[str]('cut_copper_recipe')
  CutCopperSlabFromCopperBlockStonecuttingRecipe = Kee[str](
    'cut_copper_slab_from_copper_block_stonecutting_recipe')
  CutCopperSlabFromCutCopperStonecuttingRecipe = Kee[str](
    'cut_copper_slab_from_cut_copper_stonecutting_recipe')
  CutCopperSlabRecipe = Kee[str]('cut_copper_slab_recipe')
  CutCopperStairsFromCopperBlockStonecuttingRecipe = Kee[str](
    'cut_copper_stairs_from_copper_block_stonecutting_recipe')
  CutCopperStairsFromCutCopperStonecuttingRecipe = Kee[str](
    'cut_copper_stairs_from_cut_copper_stonecutting_recipe')
  CutCopperStairsRecipe = Kee[str]('cut_copper_stairs_recipe')
  CutRedSandstoneFromRedSandstoneStonecuttingRecipe = Kee[str](
    'cut_red_sandstone_from_red_sandstone_stonecutting_recipe')
  CutRedSandstoneRecipe = Kee[str]('cut_red_sandstone_recipe')
  CutRedSandstoneSlabFromCutRedSandstoneStonecuttingRecipe = Kee[str](
    'cut_red_sandstone_slab_from_cut_red_sandstone_stonecutting_recipe')
  CutRedSandstoneSlabFromRedSandstoneStonecuttingRecipe = Kee[str](
    'cut_red_sandstone_slab_from_red_sandstone_stonecutting_recipe')
  CutRedSandstoneSlabRecipe = Kee[str]('cut_red_sandstone_slab_recipe')
  CutSandstoneFromSandstoneStonecuttingRecipe = Kee[str](
    'cut_sandstone_from_sandstone_stonecutting_recipe')
  CutSandstoneRecipe = Kee[str]('cut_sandstone_recipe')
  CutSandstoneSlabFromCutSandstoneStonecuttingRecipe = Kee[str](
    'cut_sandstone_slab_from_cut_sandstone_stonecutting_recipe')
  CutSandstoneSlabFromSandstoneStonecuttingRecipe = Kee[str](
    'cut_sandstone_slab_from_sandstone_stonecutting_recipe')
  CutSandstoneSlabRecipe = Kee[str]('cut_sandstone_slab_recipe')
  CyanBannerRecipe = Kee[str]('cyan_banner_recipe')
  CyanBedFromWhiteBedRecipe = Kee[str]('cyan_bed_from_white_bed_recipe')
  CyanBedRecipe = Kee[str]('cyan_bed_recipe')
  CyanBundleRecipe = Kee[str]('cyan_bundle_recipe')
  CyanCandleRecipe = Kee[str]('cyan_candle_recipe')
  CyanCarpetFromWhiteCarpetRecipe = Kee[str](
    'cyan_carpet_from_white_carpet_recipe')
  CyanCarpetRecipe = Kee[str]('cyan_carpet_recipe')
  CyanConcretePowderRecipe = Kee[str]('cyan_concrete_powder_recipe')
  CyanConcreteSlabFromCyanConcreteStonecuttingRecipe = Kee[str](
    'cyan_concrete_slab_from_cyan_concrete_stonecutting_recipe')
  CyanConcreteSlabRecipe = Kee[str]('cyan_concrete_slab_recipe')
  CyanConcreteStairsFromCyanConcreteStonecuttingRecipe = Kee[str](
    'cyan_concrete_stairs_from_cyan_concrete_stonecutting_recipe')
  CyanConcreteStairsRecipe = Kee[str]('cyan_concrete_stairs_recipe')
  CyanCushionRecipe = Kee[str]('cyan_cushion_recipe')
  CyanDyeFromPitcherPlantRecipe = Kee[str](
    'cyan_dye_from_pitcher_plant_recipe')
  CyanDyeRecipe = Kee[str]('cyan_dye_recipe')
  CyanGlazedTerracottaRecipe = Kee[str]('cyan_glazed_terracotta_recipe')
  CyanHarnessRecipe = Kee[str]('cyan_harness_recipe')
  CyanShulkerBoxRecipe = Kee[str]('cyan_shulker_box_recipe')
  CyanStainedGlassPaneFromGlassPaneRecipe = Kee[str](
    'cyan_stained_glass_pane_from_glass_pane_recipe')
  CyanStainedGlassPaneRecipe = Kee[str]('cyan_stained_glass_pane_recipe')
  CyanStainedGlassRecipe = Kee[str]('cyan_stained_glass_recipe')
  CyanTerracottaRecipe = Kee[str]('cyan_terracotta_recipe')
  CyanWoolRecipe = Kee[str]('cyan_wool_recipe')
  CyanWoolSlabRecipe = Kee[str]('cyan_wool_slab_recipe')
  CyanWoolStairsRecipe = Kee[str]('cyan_wool_stairs_recipe')
  DarkOakBoatRecipe = Kee[str]('dark_oak_boat_recipe')
  DarkOakButtonRecipe = Kee[str]('dark_oak_button_recipe')
  DarkOakChestBoatRecipe = Kee[str]('dark_oak_chest_boat_recipe')
  DarkOakDoorRecipe = Kee[str]('dark_oak_door_recipe')
  DarkOakFenceGateRecipe = Kee[str]('dark_oak_fence_gate_recipe')
  DarkOakFenceRecipe = Kee[str]('dark_oak_fence_recipe')
  DarkOakHangingSignRecipe = Kee[str]('dark_oak_hanging_sign_recipe')
  DarkOakPlanksRecipe = Kee[str]('dark_oak_planks_recipe')
  DarkOakPressurePlateRecipe = Kee[str]('dark_oak_pressure_plate_recipe')
  DarkOakShelfRecipe = Kee[str]('dark_oak_shelf_recipe')
  DarkOakSignRecipe = Kee[str]('dark_oak_sign_recipe')
  DarkOakSlabRecipe = Kee[str]('dark_oak_slab_recipe')
  DarkOakStairsRecipe = Kee[str]('dark_oak_stairs_recipe')
  DarkOakTrapdoorRecipe = Kee[str]('dark_oak_trapdoor_recipe')
  DarkOakWoodRecipe = Kee[str]('dark_oak_wood_recipe')
  DarkPrismarineRecipe = Kee[str]('dark_prismarine_recipe')
  DarkPrismarineSlabFromDarkPrismarineStonecuttingRecipe = Kee[str](
    'dark_prismarine_slab_from_dark_prismarine_stonecutting_recipe')
  DarkPrismarineSlabRecipe = Kee[str]('dark_prismarine_slab_recipe')
  DarkPrismarineStairsFromDarkPrismarineStonecuttingRecipe = Kee[str](
    'dark_prismarine_stairs_from_dark_prismarine_stonecutting_recipe')
  DarkPrismarineStairsRecipe = Kee[str]('dark_prismarine_stairs_recipe')
  DaylightDetectorRecipe = Kee[str]('daylight_detector_recipe')
  DecoratedPotSimpleRecipe = Kee[str]('decorated_pot_simple_recipe')
  DeepslateBrickSlabFromCobbledDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_brick_slab_from_cobbled_deepslate_stonecutting_recipe')
  DeepslateBrickSlabFromDeepslateBricksStonecuttingRecipe = Kee[str](
    'deepslate_brick_slab_from_deepslate_bricks_stonecutting_recipe')
  DeepslateBrickSlabFromDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_brick_slab_from_deepslate_stonecutting_recipe')
  DeepslateBrickSlabFromPolishedDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_brick_slab_from_polished_deepslate_stonecutting_recipe')
  DeepslateBrickSlabRecipe = Kee[str]('deepslate_brick_slab_recipe')
  DeepslateBrickStairsFromCobbledDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_brick_stairs_from_cobbled_deepslate_stonecutting_recipe')
  DeepslateBrickStairsFromDeepslateBricksStonecuttingRecipe = Kee[str](
    'deepslate_brick_stairs_from_deepslate_bricks_stonecutting_recipe')
  DeepslateBrickStairsFromDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_brick_stairs_from_deepslate_stonecutting_recipe')
  DeepslateBrickStairsFromPolishedDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_brick_stairs_from_polished_deepslate_stonecutting_recipe')
  DeepslateBrickStairsRecipe = Kee[str]('deepslate_brick_stairs_recipe')
  DeepslateBrickWallFromCobbledDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_brick_wall_from_cobbled_deepslate_stonecutting_recipe')
  DeepslateBrickWallFromDeepslateBricksStonecuttingRecipe = Kee[str](
    'deepslate_brick_wall_from_deepslate_bricks_stonecutting_recipe')
  DeepslateBrickWallFromDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_brick_wall_from_deepslate_stonecutting_recipe')
  DeepslateBrickWallFromPolishedDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_brick_wall_from_polished_deepslate_stonecutting_recipe')
  DeepslateBrickWallRecipe = Kee[str]('deepslate_brick_wall_recipe')
  DeepslateBricksFromCobbledDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_bricks_from_cobbled_deepslate_stonecutting_recipe')
  DeepslateBricksFromDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_bricks_from_deepslate_stonecutting_recipe')
  DeepslateBricksFromPolishedDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_bricks_from_polished_deepslate_stonecutting_recipe')
  DeepslateBricksRecipe = Kee[str]('deepslate_bricks_recipe')
  DeepslateRecipe = Kee[str]('deepslate_recipe')
  DeepslateTileSlabFromCobbledDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_tile_slab_from_cobbled_deepslate_stonecutting_recipe')
  DeepslateTileSlabFromDeepslateBricksStonecuttingRecipe = Kee[str](
    'deepslate_tile_slab_from_deepslate_bricks_stonecutting_recipe')
  DeepslateTileSlabFromDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_tile_slab_from_deepslate_stonecutting_recipe')
  DeepslateTileSlabFromDeepslateTilesStonecuttingRecipe = Kee[str](
    'deepslate_tile_slab_from_deepslate_tiles_stonecutting_recipe')
  DeepslateTileSlabFromPolishedDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_tile_slab_from_polished_deepslate_stonecutting_recipe')
  DeepslateTileSlabRecipe = Kee[str]('deepslate_tile_slab_recipe')
  DeepslateTileStairsFromCobbledDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_tile_stairs_from_cobbled_deepslate_stonecutting_recipe')
  DeepslateTileStairsFromDeepslateBricksStonecuttingRecipe = Kee[str](
    'deepslate_tile_stairs_from_deepslate_bricks_stonecutting_recipe')
  DeepslateTileStairsFromDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_tile_stairs_from_deepslate_stonecutting_recipe')
  DeepslateTileStairsFromDeepslateTilesStonecuttingRecipe = Kee[str](
    'deepslate_tile_stairs_from_deepslate_tiles_stonecutting_recipe')
  DeepslateTileStairsFromPolishedDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_tile_stairs_from_polished_deepslate_stonecutting_recipe')
  DeepslateTileStairsRecipe = Kee[str]('deepslate_tile_stairs_recipe')
  DeepslateTileWallFromCobbledDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_tile_wall_from_cobbled_deepslate_stonecutting_recipe')
  DeepslateTileWallFromDeepslateBricksStonecuttingRecipe = Kee[str](
    'deepslate_tile_wall_from_deepslate_bricks_stonecutting_recipe')
  DeepslateTileWallFromDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_tile_wall_from_deepslate_stonecutting_recipe')
  DeepslateTileWallFromDeepslateTilesStonecuttingRecipe = Kee[str](
    'deepslate_tile_wall_from_deepslate_tiles_stonecutting_recipe')
  DeepslateTileWallFromPolishedDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_tile_wall_from_polished_deepslate_stonecutting_recipe')
  DeepslateTileWallRecipe = Kee[str]('deepslate_tile_wall_recipe')
  DeepslateTilesFromCobbledDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_tiles_from_cobbled_deepslate_stonecutting_recipe')
  DeepslateTilesFromDeepslateBricksStonecuttingRecipe = Kee[str](
    'deepslate_tiles_from_deepslate_bricks_stonecutting_recipe')
  DeepslateTilesFromDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_tiles_from_deepslate_stonecutting_recipe')
  DeepslateTilesFromPolishedDeepslateStonecuttingRecipe = Kee[str](
    'deepslate_tiles_from_polished_deepslate_stonecutting_recipe')
  DeepslateTilesRecipe = Kee[str]('deepslate_tiles_recipe')
  DetectorRailRecipe = Kee[str]('detector_rail_recipe')
  DiamondAxeRecipe = Kee[str]('diamond_axe_recipe')
  DiamondBlockRecipe = Kee[str]('diamond_block_recipe')
  DiamondBootsRecipe = Kee[str]('diamond_boots_recipe')
  DiamondChestplateRecipe = Kee[str]('diamond_chestplate_recipe')
  DiamondFromBlastingDeepslateDiamondOreRecipe = Kee[str](
    'diamond_from_blasting_deepslate_diamond_ore_recipe')
  DiamondFromBlastingDiamondOreRecipe = Kee[str](
    'diamond_from_blasting_diamond_ore_recipe')
  DiamondFromBlastingRecipe = Kee[str]('diamond_from_blasting_recipe')
  DiamondFromSmeltingDeepslateDiamondOreRecipe = Kee[str](
    'diamond_from_smelting_deepslate_diamond_ore_recipe')
  DiamondFromSmeltingDiamondOreRecipe = Kee[str](
    'diamond_from_smelting_diamond_ore_recipe')
  DiamondFromSmeltingRecipe = Kee[str]('diamond_from_smelting_recipe')
  DiamondHelmetRecipe = Kee[str]('diamond_helmet_recipe')
  DiamondHoeRecipe = Kee[str]('diamond_hoe_recipe')
  DiamondLeggingsRecipe = Kee[str]('diamond_leggings_recipe')
  DiamondPickaxeRecipe = Kee[str]('diamond_pickaxe_recipe')
  DiamondRecipe = Kee[str]('diamond_recipe')
  DiamondShovelRecipe = Kee[str]('diamond_shovel_recipe')
  DiamondSpearRecipe = Kee[str]('diamond_spear_recipe')
  DiamondSwordRecipe = Kee[str]('diamond_sword_recipe')
  Diamonds = Kee[str]('diamonds')
  DioriteRecipe = Kee[str]('diorite_recipe')
  DioriteSlabFromDioriteStonecuttingRecipe = Kee[str](
    'diorite_slab_from_diorite_stonecutting_recipe')
  DioriteSlabRecipe = Kee[str]('diorite_slab_recipe')
  DioriteStairsFromDioriteStonecuttingRecipe = Kee[str](
    'diorite_stairs_from_diorite_stonecutting_recipe')
  DioriteStairsRecipe = Kee[str]('diorite_stairs_recipe')
  DioriteWallFromDioriteStonecuttingRecipe = Kee[str](
    'diorite_wall_from_diorite_stonecutting_recipe')
  DioriteWallRecipe = Kee[str]('diorite_wall_recipe')
  DispenserRecipe = Kee[str]('dispenser_recipe')
  DriedGhastRecipe = Kee[str]('dried_ghast_recipe')
  DriedKelpBlockRecipe = Kee[str]('dried_kelp_block_recipe')
  DriedKelpFromCampfireCookingRecipe = Kee[str](
    'dried_kelp_from_campfire_cooking_recipe')
  DriedKelpFromSmeltingRecipe = Kee[str]('dried_kelp_from_smelting_recipe')
  DriedKelpFromSmokingRecipe = Kee[str]('dried_kelp_from_smoking_recipe')
  DriedKelpRecipe = Kee[str]('dried_kelp_recipe')
  DripstoneBlockRecipe = Kee[str]('dripstone_block_recipe')
  DropperRecipe = Kee[str]('dropper_recipe')
  DuneArmorTrimSmithingTemplateRecipe = Kee[str](
    'dune_armor_trim_smithing_template_recipe')
  DuneArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'dune_armor_trim_smithing_template_smithing_trim_recipe')
  DyeBlackBedRecipe = Kee[str]('dye_black_bed_recipe')
  DyeBlackCarpetRecipe = Kee[str]('dye_black_carpet_recipe')
  DyeBlackCushionRecipe = Kee[str]('dye_black_cushion_recipe')
  DyeBlackHarnessRecipe = Kee[str]('dye_black_harness_recipe')
  DyeBlackWoolRecipe = Kee[str]('dye_black_wool_recipe')
  DyeBlackWoolSlabRecipe = Kee[str]('dye_black_wool_slab_recipe')
  DyeBlackWoolStairsRecipe = Kee[str]('dye_black_wool_stairs_recipe')
  DyeBlueBedRecipe = Kee[str]('dye_blue_bed_recipe')
  DyeBlueCarpetRecipe = Kee[str]('dye_blue_carpet_recipe')
  DyeBlueCushionRecipe = Kee[str]('dye_blue_cushion_recipe')
  DyeBlueHarnessRecipe = Kee[str]('dye_blue_harness_recipe')
  DyeBlueWoolRecipe = Kee[str]('dye_blue_wool_recipe')
  DyeBlueWoolSlabRecipe = Kee[str]('dye_blue_wool_slab_recipe')
  DyeBlueWoolStairsRecipe = Kee[str]('dye_blue_wool_stairs_recipe')
  DyeBrownBedRecipe = Kee[str]('dye_brown_bed_recipe')
  DyeBrownCarpetRecipe = Kee[str]('dye_brown_carpet_recipe')
  DyeBrownCushionRecipe = Kee[str]('dye_brown_cushion_recipe')
  DyeBrownHarnessRecipe = Kee[str]('dye_brown_harness_recipe')
  DyeBrownWoolRecipe = Kee[str]('dye_brown_wool_recipe')
  DyeBrownWoolSlabRecipe = Kee[str]('dye_brown_wool_slab_recipe')
  DyeBrownWoolStairsRecipe = Kee[str]('dye_brown_wool_stairs_recipe')
  DyeCyanBedRecipe = Kee[str]('dye_cyan_bed_recipe')
  DyeCyanCarpetRecipe = Kee[str]('dye_cyan_carpet_recipe')
  DyeCyanCushionRecipe = Kee[str]('dye_cyan_cushion_recipe')
  DyeCyanHarnessRecipe = Kee[str]('dye_cyan_harness_recipe')
  DyeCyanWoolRecipe = Kee[str]('dye_cyan_wool_recipe')
  DyeCyanWoolSlabRecipe = Kee[str]('dye_cyan_wool_slab_recipe')
  DyeCyanWoolStairsRecipe = Kee[str]('dye_cyan_wool_stairs_recipe')
  DyeGrayBedRecipe = Kee[str]('dye_gray_bed_recipe')
  DyeGrayCarpetRecipe = Kee[str]('dye_gray_carpet_recipe')
  DyeGrayCushionRecipe = Kee[str]('dye_gray_cushion_recipe')
  DyeGrayHarnessRecipe = Kee[str]('dye_gray_harness_recipe')
  DyeGrayWoolRecipe = Kee[str]('dye_gray_wool_recipe')
  DyeGrayWoolSlabRecipe = Kee[str]('dye_gray_wool_slab_recipe')
  DyeGrayWoolStairsRecipe = Kee[str]('dye_gray_wool_stairs_recipe')
  DyeGreenBedRecipe = Kee[str]('dye_green_bed_recipe')
  DyeGreenCarpetRecipe = Kee[str]('dye_green_carpet_recipe')
  DyeGreenCushionRecipe = Kee[str]('dye_green_cushion_recipe')
  DyeGreenHarnessRecipe = Kee[str]('dye_green_harness_recipe')
  DyeGreenWoolRecipe = Kee[str]('dye_green_wool_recipe')
  DyeGreenWoolSlabRecipe = Kee[str]('dye_green_wool_slab_recipe')
  DyeGreenWoolStairsRecipe = Kee[str]('dye_green_wool_stairs_recipe')
  DyeLightBlueBedRecipe = Kee[str]('dye_light_blue_bed_recipe')
  DyeLightBlueCarpetRecipe = Kee[str]('dye_light_blue_carpet_recipe')
  DyeLightBlueCushionRecipe = Kee[str]('dye_light_blue_cushion_recipe')
  DyeLightBlueHarnessRecipe = Kee[str]('dye_light_blue_harness_recipe')
  DyeLightBlueWoolRecipe = Kee[str]('dye_light_blue_wool_recipe')
  DyeLightBlueWoolSlabRecipe = Kee[str]('dye_light_blue_wool_slab_recipe')
  DyeLightBlueWoolStairsRecipe = Kee[str]('dye_light_blue_wool_stairs_recipe')
  DyeLightGrayBedRecipe = Kee[str]('dye_light_gray_bed_recipe')
  DyeLightGrayCarpetRecipe = Kee[str]('dye_light_gray_carpet_recipe')
  DyeLightGrayCushionRecipe = Kee[str]('dye_light_gray_cushion_recipe')
  DyeLightGrayHarnessRecipe = Kee[str]('dye_light_gray_harness_recipe')
  DyeLightGrayWoolRecipe = Kee[str]('dye_light_gray_wool_recipe')
  DyeLightGrayWoolSlabRecipe = Kee[str]('dye_light_gray_wool_slab_recipe')
  DyeLightGrayWoolStairsRecipe = Kee[str]('dye_light_gray_wool_stairs_recipe')
  DyeLimeBedRecipe = Kee[str]('dye_lime_bed_recipe')
  DyeLimeCarpetRecipe = Kee[str]('dye_lime_carpet_recipe')
  DyeLimeCushionRecipe = Kee[str]('dye_lime_cushion_recipe')
  DyeLimeHarnessRecipe = Kee[str]('dye_lime_harness_recipe')
  DyeLimeWoolRecipe = Kee[str]('dye_lime_wool_recipe')
  DyeLimeWoolSlabRecipe = Kee[str]('dye_lime_wool_slab_recipe')
  DyeLimeWoolStairsRecipe = Kee[str]('dye_lime_wool_stairs_recipe')
  DyeMagentaBedRecipe = Kee[str]('dye_magenta_bed_recipe')
  DyeMagentaCarpetRecipe = Kee[str]('dye_magenta_carpet_recipe')
  DyeMagentaCushionRecipe = Kee[str]('dye_magenta_cushion_recipe')
  DyeMagentaHarnessRecipe = Kee[str]('dye_magenta_harness_recipe')
  DyeMagentaWoolRecipe = Kee[str]('dye_magenta_wool_recipe')
  DyeMagentaWoolSlabRecipe = Kee[str]('dye_magenta_wool_slab_recipe')
  DyeMagentaWoolStairsRecipe = Kee[str]('dye_magenta_wool_stairs_recipe')
  DyeOrangeBedRecipe = Kee[str]('dye_orange_bed_recipe')
  DyeOrangeCarpetRecipe = Kee[str]('dye_orange_carpet_recipe')
  DyeOrangeCushionRecipe = Kee[str]('dye_orange_cushion_recipe')
  DyeOrangeHarnessRecipe = Kee[str]('dye_orange_harness_recipe')
  DyeOrangeWoolRecipe = Kee[str]('dye_orange_wool_recipe')
  DyeOrangeWoolSlabRecipe = Kee[str]('dye_orange_wool_slab_recipe')
  DyeOrangeWoolStairsRecipe = Kee[str]('dye_orange_wool_stairs_recipe')
  DyePinkBedRecipe = Kee[str]('dye_pink_bed_recipe')
  DyePinkCarpetRecipe = Kee[str]('dye_pink_carpet_recipe')
  DyePinkCushionRecipe = Kee[str]('dye_pink_cushion_recipe')
  DyePinkHarnessRecipe = Kee[str]('dye_pink_harness_recipe')
  DyePinkWoolRecipe = Kee[str]('dye_pink_wool_recipe')
  DyePinkWoolSlabRecipe = Kee[str]('dye_pink_wool_slab_recipe')
  DyePinkWoolStairsRecipe = Kee[str]('dye_pink_wool_stairs_recipe')
  DyePurpleBedRecipe = Kee[str]('dye_purple_bed_recipe')
  DyePurpleCarpetRecipe = Kee[str]('dye_purple_carpet_recipe')
  DyePurpleCushionRecipe = Kee[str]('dye_purple_cushion_recipe')
  DyePurpleHarnessRecipe = Kee[str]('dye_purple_harness_recipe')
  DyePurpleWoolRecipe = Kee[str]('dye_purple_wool_recipe')
  DyePurpleWoolSlabRecipe = Kee[str]('dye_purple_wool_slab_recipe')
  DyePurpleWoolStairsRecipe = Kee[str]('dye_purple_wool_stairs_recipe')
  DyeRedBedRecipe = Kee[str]('dye_red_bed_recipe')
  DyeRedCarpetRecipe = Kee[str]('dye_red_carpet_recipe')
  DyeRedCushionRecipe = Kee[str]('dye_red_cushion_recipe')
  DyeRedHarnessRecipe = Kee[str]('dye_red_harness_recipe')
  DyeRedWoolRecipe = Kee[str]('dye_red_wool_recipe')
  DyeRedWoolSlabRecipe = Kee[str]('dye_red_wool_slab_recipe')
  DyeRedWoolStairsRecipe = Kee[str]('dye_red_wool_stairs_recipe')
  DyeWhiteBedRecipe = Kee[str]('dye_white_bed_recipe')
  DyeWhiteCarpetRecipe = Kee[str]('dye_white_carpet_recipe')
  DyeWhiteCushionRecipe = Kee[str]('dye_white_cushion_recipe')
  DyeWhiteHarnessRecipe = Kee[str]('dye_white_harness_recipe')
  DyeWhiteWoolRecipe = Kee[str]('dye_white_wool_recipe')
  DyeWhiteWoolSlabRecipe = Kee[str]('dye_white_wool_slab_recipe')
  DyeWhiteWoolStairsRecipe = Kee[str]('dye_white_wool_stairs_recipe')
  DyeYellowBedRecipe = Kee[str]('dye_yellow_bed_recipe')
  DyeYellowCarpetRecipe = Kee[str]('dye_yellow_carpet_recipe')
  DyeYellowCushionRecipe = Kee[str]('dye_yellow_cushion_recipe')
  DyeYellowHarnessRecipe = Kee[str]('dye_yellow_harness_recipe')
  DyeYellowWoolRecipe = Kee[str]('dye_yellow_wool_recipe')
  DyeYellowWoolSlabRecipe = Kee[str]('dye_yellow_wool_slab_recipe')
  DyeYellowWoolStairsRecipe = Kee[str]('dye_yellow_wool_stairs_recipe')
  EmeraldBlockRecipe = Kee[str]('emerald_block_recipe')
  EmeraldFromBlastingDeepslateEmeraldOreRecipe = Kee[str](
    'emerald_from_blasting_deepslate_emerald_ore_recipe')
  EmeraldFromBlastingEmeraldOreRecipe = Kee[str](
    'emerald_from_blasting_emerald_ore_recipe')
  EmeraldFromBlastingRecipe = Kee[str]('emerald_from_blasting_recipe')
  EmeraldFromSmeltingDeepslateEmeraldOreRecipe = Kee[str](
    'emerald_from_smelting_deepslate_emerald_ore_recipe')
  EmeraldFromSmeltingEmeraldOreRecipe = Kee[str](
    'emerald_from_smelting_emerald_ore_recipe')
  EmeraldFromSmeltingRecipe = Kee[str]('emerald_from_smelting_recipe')
  EmeraldRecipe = Kee[str]('emerald_recipe')
  Enchanter = Kee[str]('enchanter')
  EnchantingTableRecipe = Kee[str]('enchanting_table_recipe')
  EndCrystalRecipe = Kee[str]('end_crystal_recipe')
  EndRodRecipe = Kee[str]('end_rod_recipe')
  EndRoot = Kee[str]('end_root')
  EndStoneBrickSlabFromEndStoneBricksStonecuttingRecipe = Kee[str](
    'end_stone_brick_slab_from_end_stone_bricks_stonecutting_recipe')
  EndStoneBrickSlabFromEndStoneStonecuttingRecipe = Kee[str](
    'end_stone_brick_slab_from_end_stone_stonecutting_recipe')
  EndStoneBrickSlabRecipe = Kee[str]('end_stone_brick_slab_recipe')
  EndStoneBrickStairsFromEndStoneBricksStonecuttingRecipe = Kee[str](
    'end_stone_brick_stairs_from_end_stone_bricks_stonecutting_recipe')
  EndStoneBrickStairsFromEndStoneStonecuttingRecipe = Kee[str](
    'end_stone_brick_stairs_from_end_stone_stonecutting_recipe')
  EndStoneBrickStairsRecipe = Kee[str]('end_stone_brick_stairs_recipe')
  EndStoneBrickWallFromEndStoneBricksStonecuttingRecipe = Kee[str](
    'end_stone_brick_wall_from_end_stone_bricks_stonecutting_recipe')
  EndStoneBrickWallFromEndStoneStonecuttingRecipe = Kee[str](
    'end_stone_brick_wall_from_end_stone_stonecutting_recipe')
  EndStoneBrickWallRecipe = Kee[str]('end_stone_brick_wall_recipe')
  EndStoneBricksFromEndStoneStonecuttingRecipe = Kee[str](
    'end_stone_bricks_from_end_stone_stonecutting_recipe')
  EndStoneBricksRecipe = Kee[str]('end_stone_bricks_recipe')
  EnderChestRecipe = Kee[str]('ender_chest_recipe')
  EnderEyeRecipe = Kee[str]('ender_eye_recipe')
  ExposedChiseledCopperFromExposedCopperStonecuttingRecipe = Kee[str](
    'exposed_chiseled_copper_from_exposed_copper_stonecutting_recipe')
  ExposedChiseledCopperFromExposedCutCopperStonecuttingRecipe = Kee[str](
    'exposed_chiseled_copper_from_exposed_cut_copper_stonecutting_recipe')
  ExposedChiseledCopperRecipe = Kee[str]('exposed_chiseled_copper_recipe')
  ExposedCopperBulbRecipe = Kee[str]('exposed_copper_bulb_recipe')
  ExposedCopperGrateFromExposedCopperStonecuttingRecipe = Kee[str](
    'exposed_copper_grate_from_exposed_copper_stonecutting_recipe')
  ExposedCopperGrateRecipe = Kee[str]('exposed_copper_grate_recipe')
  ExposedCutCopperFromExposedCopperStonecuttingRecipe = Kee[str](
    'exposed_cut_copper_from_exposed_copper_stonecutting_recipe')
  ExposedCutCopperRecipe = Kee[str]('exposed_cut_copper_recipe')
  ExposedCutCopperSlabFromExposedCopperStonecuttingRecipe = Kee[str](
    'exposed_cut_copper_slab_from_exposed_copper_stonecutting_recipe')
  ExposedCutCopperSlabFromExposedCutCopperStonecuttingRecipe = Kee[str](
    'exposed_cut_copper_slab_from_exposed_cut_copper_stonecutting_recipe')
  ExposedCutCopperSlabRecipe = Kee[str]('exposed_cut_copper_slab_recipe')
  ExposedCutCopperStairsFromExposedCopperStonecuttingRecipe = Kee[str](
    'exposed_cut_copper_stairs_from_exposed_copper_stonecutting_recipe')
  ExposedCutCopperStairsFromExposedCutCopperStonecuttingRecipe = Kee[str](
    'exposed_cut_copper_stairs_from_exposed_cut_copper_stonecutting_recipe')
  ExposedCutCopperStairsRecipe = Kee[str]('exposed_cut_copper_stairs_recipe')
  EyeArmorTrimSmithingTemplateRecipe = Kee[str](
    'eye_armor_trim_smithing_template_recipe')
  EyeArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'eye_armor_trim_smithing_template_smithing_trim_recipe')
  EyeSpy = Kee[str]('eye_spy')
  FeelsLikeHome = Kee[str]('feels_like_home')
  FermentedSpiderEyeRecipe = Kee[str]('fermented_spider_eye_recipe')
  FieldMasonedBannerPatternRecipe = Kee[str](
    'field_masoned_banner_pattern_recipe')
  FireChargeRecipe = Kee[str]('fire_charge_recipe')
  FireworkRocketSimpleRecipe = Kee[str]('firework_rocket_simple_recipe')
  FishingRodRecipe = Kee[str]('fishing_rod_recipe')
  FishyBusiness = Kee[str]('fishy_business')
  FletchingTableRecipe = Kee[str]('fletching_table_recipe')
  FlintAndSteelRecipe = Kee[str]('flint_and_steel_recipe')
  FlowArmorTrimSmithingTemplateRecipe = Kee[str](
    'flow_armor_trim_smithing_template_recipe')
  FlowArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'flow_armor_trim_smithing_template_smithing_trim_recipe')
  FlowerBannerPatternRecipe = Kee[str]('flower_banner_pattern_recipe')
  FlowerPotRecipe = Kee[str]('flower_pot_recipe')
  FreeTheEnd = Kee[str]('free_the_end')
  FurnaceMinecartRecipe = Kee[str]('furnace_minecart_recipe')
  FurnaceRecipe = Kee[str]('furnace_recipe')
  GettingAnUpgrade = Kee[str]('getting_an_upgrade')
  GlassBottleRecipe = Kee[str]('glass_bottle_recipe')
  GlassPaneRecipe = Kee[str]('glass_pane_recipe')
  GlassRecipe = Kee[str]('glass_recipe')
  GlisteringMelonSliceRecipe = Kee[str]('glistering_melon_slice_recipe')
  GlowAndBehold = Kee[str]('glow_and_behold')
  GlowItemFrameRecipe = Kee[str]('glow_item_frame_recipe')
  GlowstoneRecipe = Kee[str]('glowstone_recipe')
  GoldBlockRecipe = Kee[str]('gold_block_recipe')
  GoldIngotFromBlastingDeepslateGoldOreRecipe = Kee[str](
    'gold_ingot_from_blasting_deepslate_gold_ore_recipe')
  GoldIngotFromBlastingGoldOreRecipe = Kee[str](
    'gold_ingot_from_blasting_gold_ore_recipe')
  GoldIngotFromBlastingNetherGoldOreRecipe = Kee[str](
    'gold_ingot_from_blasting_nether_gold_ore_recipe')
  GoldIngotFromBlastingRawGoldRecipe = Kee[str](
    'gold_ingot_from_blasting_raw_gold_recipe')
  GoldIngotFromBlastingRecipe = Kee[str]('gold_ingot_from_blasting_recipe')
  GoldIngotFromGoldBlockRecipe = Kee[str]('gold_ingot_from_gold_block_recipe')
  GoldIngotFromNuggetsRecipe = Kee[str]('gold_ingot_from_nuggets_recipe')
  GoldIngotFromSmeltingDeepslateGoldOreRecipe = Kee[str](
    'gold_ingot_from_smelting_deepslate_gold_ore_recipe')
  GoldIngotFromSmeltingGoldOreRecipe = Kee[str](
    'gold_ingot_from_smelting_gold_ore_recipe')
  GoldIngotFromSmeltingNetherGoldOreRecipe = Kee[str](
    'gold_ingot_from_smelting_nether_gold_ore_recipe')
  GoldIngotFromSmeltingRawGoldRecipe = Kee[str](
    'gold_ingot_from_smelting_raw_gold_recipe')
  GoldIngotRecipe = Kee[str]('gold_ingot_recipe')
  GoldNuggetFromBlastingRecipe = Kee[str]('gold_nugget_from_blasting_recipe')
  GoldNuggetFromSmeltingRecipe = Kee[str]('gold_nugget_from_smelting_recipe')
  GoldNuggetRecipe = Kee[str]('gold_nugget_recipe')
  GoldenAppleRecipe = Kee[str]('golden_apple_recipe')
  GoldenAxeRecipe = Kee[str]('golden_axe_recipe')
  GoldenBootsRecipe = Kee[str]('golden_boots_recipe')
  GoldenCarrotRecipe = Kee[str]('golden_carrot_recipe')
  GoldenChestplateRecipe = Kee[str]('golden_chestplate_recipe')
  GoldenDandelionRecipe = Kee[str]('golden_dandelion_recipe')
  GoldenHelmetRecipe = Kee[str]('golden_helmet_recipe')
  GoldenHoeRecipe = Kee[str]('golden_hoe_recipe')
  GoldenLeggingsRecipe = Kee[str]('golden_leggings_recipe')
  GoldenPickaxeRecipe = Kee[str]('golden_pickaxe_recipe')
  GoldenShovelRecipe = Kee[str]('golden_shovel_recipe')
  GoldenSpearRecipe = Kee[str]('golden_spear_recipe')
  GoldenSwordRecipe = Kee[str]('golden_sword_recipe')
  GoodAsNew = Kee[str]('good_as_new')
  GraniteRecipe = Kee[str]('granite_recipe')
  GraniteSlabFromGraniteStonecuttingRecipe = Kee[str](
    'granite_slab_from_granite_stonecutting_recipe')
  GraniteSlabRecipe = Kee[str]('granite_slab_recipe')
  GraniteStairsFromGraniteStonecuttingRecipe = Kee[str](
    'granite_stairs_from_granite_stonecutting_recipe')
  GraniteStairsRecipe = Kee[str]('granite_stairs_recipe')
  GraniteWallFromGraniteStonecuttingRecipe = Kee[str](
    'granite_wall_from_granite_stonecutting_recipe')
  GraniteWallRecipe = Kee[str]('granite_wall_recipe')
  GrayBannerRecipe = Kee[str]('gray_banner_recipe')
  GrayBedFromWhiteBedRecipe = Kee[str]('gray_bed_from_white_bed_recipe')
  GrayBedRecipe = Kee[str]('gray_bed_recipe')
  GrayBundleRecipe = Kee[str]('gray_bundle_recipe')
  GrayCandleRecipe = Kee[str]('gray_candle_recipe')
  GrayCarpetFromWhiteCarpetRecipe = Kee[str](
    'gray_carpet_from_white_carpet_recipe')
  GrayCarpetRecipe = Kee[str]('gray_carpet_recipe')
  GrayConcretePowderRecipe = Kee[str]('gray_concrete_powder_recipe')
  GrayConcreteSlabFromGrayConcreteStonecuttingRecipe = Kee[str](
    'gray_concrete_slab_from_gray_concrete_stonecutting_recipe')
  GrayConcreteSlabRecipe = Kee[str]('gray_concrete_slab_recipe')
  GrayConcreteStairsFromGrayConcreteStonecuttingRecipe = Kee[str](
    'gray_concrete_stairs_from_gray_concrete_stonecutting_recipe')
  GrayConcreteStairsRecipe = Kee[str]('gray_concrete_stairs_recipe')
  GrayCushionRecipe = Kee[str]('gray_cushion_recipe')
  GrayDyeFromClosedEyeblossomRecipe = Kee[str](
    'gray_dye_from_closed_eyeblossom_recipe')
  GrayDyeRecipe = Kee[str]('gray_dye_recipe')
  GrayGlazedTerracottaRecipe = Kee[str]('gray_glazed_terracotta_recipe')
  GrayHarnessRecipe = Kee[str]('gray_harness_recipe')
  GrayShulkerBoxRecipe = Kee[str]('gray_shulker_box_recipe')
  GrayStainedGlassPaneFromGlassPaneRecipe = Kee[str](
    'gray_stained_glass_pane_from_glass_pane_recipe')
  GrayStainedGlassPaneRecipe = Kee[str]('gray_stained_glass_pane_recipe')
  GrayStainedGlassRecipe = Kee[str]('gray_stained_glass_recipe')
  GrayTerracottaRecipe = Kee[str]('gray_terracotta_recipe')
  GrayWoolRecipe = Kee[str]('gray_wool_recipe')
  GrayWoolSlabRecipe = Kee[str]('gray_wool_slab_recipe')
  GrayWoolStairsRecipe = Kee[str]('gray_wool_stairs_recipe')
  GreatViewFromUpHere = Kee[str]('great_view_from_up_here')
  GreenBannerRecipe = Kee[str]('green_banner_recipe')
  GreenBedFromWhiteBedRecipe = Kee[str]('green_bed_from_white_bed_recipe')
  GreenBedRecipe = Kee[str]('green_bed_recipe')
  GreenBundleRecipe = Kee[str]('green_bundle_recipe')
  GreenCandleRecipe = Kee[str]('green_candle_recipe')
  GreenCarpetFromWhiteCarpetRecipe = Kee[str](
    'green_carpet_from_white_carpet_recipe')
  GreenCarpetRecipe = Kee[str]('green_carpet_recipe')
  GreenConcretePowderRecipe = Kee[str]('green_concrete_powder_recipe')
  GreenConcreteSlabFromGreenConcreteStonecuttingRecipe = Kee[str](
    'green_concrete_slab_from_green_concrete_stonecutting_recipe')
  GreenConcreteSlabRecipe = Kee[str]('green_concrete_slab_recipe')
  GreenConcreteStairsFromGreenConcreteStonecuttingRecipe = Kee[str](
    'green_concrete_stairs_from_green_concrete_stonecutting_recipe')
  GreenConcreteStairsRecipe = Kee[str]('green_concrete_stairs_recipe')
  GreenCushionRecipe = Kee[str]('green_cushion_recipe')
  GreenDyeRecipe = Kee[str]('green_dye_recipe')
  GreenGlazedTerracottaRecipe = Kee[str]('green_glazed_terracotta_recipe')
  GreenHarnessRecipe = Kee[str]('green_harness_recipe')
  GreenShulkerBoxRecipe = Kee[str]('green_shulker_box_recipe')
  GreenStainedGlassPaneFromGlassPaneRecipe = Kee[str](
    'green_stained_glass_pane_from_glass_pane_recipe')
  GreenStainedGlassPaneRecipe = Kee[str]('green_stained_glass_pane_recipe')
  GreenStainedGlassRecipe = Kee[str]('green_stained_glass_recipe')
  GreenTerracottaRecipe = Kee[str]('green_terracotta_recipe')
  GreenWoolRecipe = Kee[str]('green_wool_recipe')
  GreenWoolSlabRecipe = Kee[str]('green_wool_slab_recipe')
  GreenWoolStairsRecipe = Kee[str]('green_wool_stairs_recipe')
  GrindstoneRecipe = Kee[str]('grindstone_recipe')
  HayBlockRecipe = Kee[str]('hay_block_recipe')
  HeartTransplanter = Kee[str]('heart_transplanter')
  HeavyWeightedPressurePlateRecipe = Kee[str](
    'heavy_weighted_pressure_plate_recipe')
  HeroOfTheVillage = Kee[str]('hero_of_the_village')
  HiddenInTheDepths = Kee[str]('hidden_in_the_depths')
  HiredHelp = Kee[str]('hired_help')
  HoneyBlockRecipe = Kee[str]('honey_block_recipe')
  HoneyBottleRecipe = Kee[str]('honey_bottle_recipe')
  HoneycombBlockRecipe = Kee[str]('honeycomb_block_recipe')
  HopperMinecartRecipe = Kee[str]('hopper_minecart_recipe')
  HopperRecipe = Kee[str]('hopper_recipe')
  HostArmorTrimSmithingTemplateRecipe = Kee[str](
    'host_armor_trim_smithing_template_recipe')
  HostArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'host_armor_trim_smithing_template_smithing_trim_recipe')
  HotStuff = Kee[str]('hot_stuff')
  HotTouristDestinations = Kee[str]('hot_tourist_destinations')
  HowDidWeGetHere = Kee[str]('how_did_we_get_here')
  HusbandryRoot = Kee[str]('husbandry_root')
  IceBucketChallenge = Kee[str]('ice_bucket_challenge')
  IntoFire = Kee[str]('into_fire')
  IronAxeRecipe = Kee[str]('iron_axe_recipe')
  IronBarsRecipe = Kee[str]('iron_bars_recipe')
  IronBlockRecipe = Kee[str]('iron_block_recipe')
  IronBootsRecipe = Kee[str]('iron_boots_recipe')
  IronChainRecipe = Kee[str]('iron_chain_recipe')
  IronChestplateRecipe = Kee[str]('iron_chestplate_recipe')
  IronDoorRecipe = Kee[str]('iron_door_recipe')
  IronHelmetRecipe = Kee[str]('iron_helmet_recipe')
  IronHoeRecipe = Kee[str]('iron_hoe_recipe')
  IronIngotFromBlastingDeepslateIronOreRecipe = Kee[str](
    'iron_ingot_from_blasting_deepslate_iron_ore_recipe')
  IronIngotFromBlastingIronOreRecipe = Kee[str](
    'iron_ingot_from_blasting_iron_ore_recipe')
  IronIngotFromBlastingRawIronRecipe = Kee[str](
    'iron_ingot_from_blasting_raw_iron_recipe')
  IronIngotFromBlastingRecipe = Kee[str]('iron_ingot_from_blasting_recipe')
  IronIngotFromIronBlockRecipe = Kee[str]('iron_ingot_from_iron_block_recipe')
  IronIngotFromNuggetsRecipe = Kee[str]('iron_ingot_from_nuggets_recipe')
  IronIngotFromSmeltingDeepslateIronOreRecipe = Kee[str](
    'iron_ingot_from_smelting_deepslate_iron_ore_recipe')
  IronIngotFromSmeltingIronOreRecipe = Kee[str](
    'iron_ingot_from_smelting_iron_ore_recipe')
  IronIngotFromSmeltingRawIronRecipe = Kee[str](
    'iron_ingot_from_smelting_raw_iron_recipe')
  IronIngotRecipe = Kee[str]('iron_ingot_recipe')
  IronLeggingsRecipe = Kee[str]('iron_leggings_recipe')
  IronNuggetFromBlastingRecipe = Kee[str]('iron_nugget_from_blasting_recipe')
  IronNuggetFromSmeltingRecipe = Kee[str]('iron_nugget_from_smelting_recipe')
  IronNuggetRecipe = Kee[str]('iron_nugget_recipe')
  IronPickaxeRecipe = Kee[str]('iron_pickaxe_recipe')
  IronShovelRecipe = Kee[str]('iron_shovel_recipe')
  IronSpearRecipe = Kee[str]('iron_spear_recipe')
  IronSwordRecipe = Kee[str]('iron_sword_recipe')
  IronTrapdoorRecipe = Kee[str]('iron_trapdoor_recipe')
  IsItABalloon = Kee[str]('is_it_a_balloon')
  IsItABird = Kee[str]('is_it_a_bird')
  IsItAPlane = Kee[str]('is_it_a_plane')
  IsntItIronPick = Kee[str]('isnt_it_iron_pick')
  IsntItScute = Kee[str]('isnt_it_scute')
  ItSpreads = Kee[str]('it_spreads')
  ItemFrameRecipe = Kee[str]('item_frame_recipe')
  JackOLanternRecipe = Kee[str]('jack_o_lantern_recipe')
  JukeboxRecipe = Kee[str]('jukebox_recipe')
  JungleBoatRecipe = Kee[str]('jungle_boat_recipe')
  JungleButtonRecipe = Kee[str]('jungle_button_recipe')
  JungleChestBoatRecipe = Kee[str]('jungle_chest_boat_recipe')
  JungleDoorRecipe = Kee[str]('jungle_door_recipe')
  JungleFenceGateRecipe = Kee[str]('jungle_fence_gate_recipe')
  JungleFenceRecipe = Kee[str]('jungle_fence_recipe')
  JungleHangingSignRecipe = Kee[str]('jungle_hanging_sign_recipe')
  JunglePlanksRecipe = Kee[str]('jungle_planks_recipe')
  JunglePressurePlateRecipe = Kee[str]('jungle_pressure_plate_recipe')
  JungleShelfRecipe = Kee[str]('jungle_shelf_recipe')
  JungleSignRecipe = Kee[str]('jungle_sign_recipe')
  JungleSlabRecipe = Kee[str]('jungle_slab_recipe')
  JungleStairsRecipe = Kee[str]('jungle_stairs_recipe')
  JungleTrapdoorRecipe = Kee[str]('jungle_trapdoor_recipe')
  JungleWoodRecipe = Kee[str]('jungle_wood_recipe')
  LadderRecipe = Kee[str]('ladder_recipe')
  LanternRecipe = Kee[str]('lantern_recipe')
  LapisBlockRecipe = Kee[str]('lapis_block_recipe')
  LapisFromBlastingRecipe = Kee[str]('lapis_from_blasting_recipe')
  LapisFromSmeltingRecipe = Kee[str]('lapis_from_smelting_recipe')
  LapisLazuliFromBlastingDeepslateLapisOreRecipe = Kee[str](
    'lapis_lazuli_from_blasting_deepslate_lapis_ore_recipe')
  LapisLazuliFromBlastingLapisOreRecipe = Kee[str](
    'lapis_lazuli_from_blasting_lapis_ore_recipe')
  LapisLazuliFromSmeltingDeepslateLapisOreRecipe = Kee[str](
    'lapis_lazuli_from_smelting_deepslate_lapis_ore_recipe')
  LapisLazuliFromSmeltingLapisOreRecipe = Kee[str](
    'lapis_lazuli_from_smelting_lapis_ore_recipe')
  LapisLazuliRecipe = Kee[str]('lapis_lazuli_recipe')
  LeadRecipe = Kee[str]('lead_recipe')
  LeafLitterRecipe = Kee[str]('leaf_litter_recipe')
  LeatherBootsDyedRecipe = Kee[str]('leather_boots_dyed_recipe')
  LeatherBootsRecipe = Kee[str]('leather_boots_recipe')
  LeatherChestplateDyedRecipe = Kee[str]('leather_chestplate_dyed_recipe')
  LeatherChestplateRecipe = Kee[str]('leather_chestplate_recipe')
  LeatherHelmetDyedRecipe = Kee[str]('leather_helmet_dyed_recipe')
  LeatherHelmetRecipe = Kee[str]('leather_helmet_recipe')
  LeatherHorseArmorDyedRecipe = Kee[str]('leather_horse_armor_dyed_recipe')
  LeatherHorseArmorRecipe = Kee[str]('leather_horse_armor_recipe')
  LeatherLeggingsDyedRecipe = Kee[str]('leather_leggings_dyed_recipe')
  LeatherLeggingsRecipe = Kee[str]('leather_leggings_recipe')
  LeatherRecipe = Kee[str]('leather_recipe')
  LecternRecipe = Kee[str]('lectern_recipe')
  LeverRecipe = Kee[str]('lever_recipe')
  LightAsARabbit = Kee[str]('light_as_a_rabbit')
  LightBlueBannerRecipe = Kee[str]('light_blue_banner_recipe')
  LightBlueBedFromWhiteBedRecipe = Kee[str](
    'light_blue_bed_from_white_bed_recipe')
  LightBlueBedRecipe = Kee[str]('light_blue_bed_recipe')
  LightBlueBundleRecipe = Kee[str]('light_blue_bundle_recipe')
  LightBlueCandleRecipe = Kee[str]('light_blue_candle_recipe')
  LightBlueCarpetFromWhiteCarpetRecipe = Kee[str](
    'light_blue_carpet_from_white_carpet_recipe')
  LightBlueCarpetRecipe = Kee[str]('light_blue_carpet_recipe')
  LightBlueConcretePowderRecipe = Kee[str]('light_blue_concrete_powder_recipe')
  LightBlueConcreteSlabFromLightBlueConcreteStonecuttingRecipe = Kee[str](
    'light_blue_concrete_slab_from_light_blue_concrete_stonecutting_recipe')
  LightBlueConcreteSlabRecipe = Kee[str]('light_blue_concrete_slab_recipe')
  LightBlueConcreteStairsFromLightBlueConcreteStonecuttingRecipe = Kee[str](
    'light_blue_concrete_stairs_from_light_blue_concrete_stonecutting_recipe')
  LightBlueConcreteStairsRecipe = Kee[str]('light_blue_concrete_stairs_recipe')
  LightBlueCushionRecipe = Kee[str]('light_blue_cushion_recipe')
  LightBlueDyeFromBlueOrchidRecipe = Kee[str](
    'light_blue_dye_from_blue_orchid_recipe')
  LightBlueDyeFromBlueWhiteDyeRecipe = Kee[str](
    'light_blue_dye_from_blue_white_dye_recipe')
  LightBlueDyeFromLapisBonemealRecipe = Kee[str](
    'light_blue_dye_from_lapis_bonemeal_recipe')
  LightBlueGlazedTerracottaRecipe = Kee[str](
    'light_blue_glazed_terracotta_recipe')
  LightBlueHarnessRecipe = Kee[str]('light_blue_harness_recipe')
  LightBlueShulkerBoxRecipe = Kee[str]('light_blue_shulker_box_recipe')
  LightBlueStainedGlassPaneFromGlassPaneRecipe = Kee[str](
    'light_blue_stained_glass_pane_from_glass_pane_recipe')
  LightBlueStainedGlassPaneRecipe = Kee[str](
    'light_blue_stained_glass_pane_recipe')
  LightBlueStainedGlassRecipe = Kee[str]('light_blue_stained_glass_recipe')
  LightBlueTerracottaRecipe = Kee[str]('light_blue_terracotta_recipe')
  LightBlueWoolRecipe = Kee[str]('light_blue_wool_recipe')
  LightBlueWoolSlabRecipe = Kee[str]('light_blue_wool_slab_recipe')
  LightBlueWoolStairsRecipe = Kee[str]('light_blue_wool_stairs_recipe')
  LightGrayBannerRecipe = Kee[str]('light_gray_banner_recipe')
  LightGrayBedFromWhiteBedRecipe = Kee[str](
    'light_gray_bed_from_white_bed_recipe')
  LightGrayBedRecipe = Kee[str]('light_gray_bed_recipe')
  LightGrayBundleRecipe = Kee[str]('light_gray_bundle_recipe')
  LightGrayCandleRecipe = Kee[str]('light_gray_candle_recipe')
  LightGrayCarpetFromWhiteCarpetRecipe = Kee[str](
    'light_gray_carpet_from_white_carpet_recipe')
  LightGrayCarpetRecipe = Kee[str]('light_gray_carpet_recipe')
  LightGrayConcretePowderRecipe = Kee[str]('light_gray_concrete_powder_recipe')
  LightGrayConcreteSlabFromLightGrayConcreteStonecuttingRecipe = Kee[str](
    'light_gray_concrete_slab_from_light_gray_concrete_stonecutting_recipe')
  LightGrayConcreteSlabRecipe = Kee[str]('light_gray_concrete_slab_recipe')
  LightGrayConcreteStairsFromLightGrayConcreteStonecuttingRecipe = Kee[str](
    'light_gray_concrete_stairs_from_light_gray_concrete_stonecutting_recipe')
  LightGrayConcreteStairsRecipe = Kee[str]('light_gray_concrete_stairs_recipe')
  LightGrayCushionRecipe = Kee[str]('light_gray_cushion_recipe')
  LightGrayDyeFromAzureBluetRecipe = Kee[str](
    'light_gray_dye_from_azure_bluet_recipe')
  LightGrayDyeFromBlackWhiteDyeRecipe = Kee[str](
    'light_gray_dye_from_black_white_dye_recipe')
  LightGrayDyeFromGrayBonemealRecipe = Kee[str](
    'light_gray_dye_from_gray_bonemeal_recipe')
  LightGrayDyeFromGrayWhiteDyeRecipe = Kee[str](
    'light_gray_dye_from_gray_white_dye_recipe')
  LightGrayDyeFromInkBonemealRecipe = Kee[str](
    'light_gray_dye_from_ink_bonemeal_recipe')
  LightGrayDyeFromOxeyeDaisyRecipe = Kee[str](
    'light_gray_dye_from_oxeye_daisy_recipe')
  LightGrayDyeFromWhiteTulipRecipe = Kee[str](
    'light_gray_dye_from_white_tulip_recipe')
  LightGrayGlazedTerracottaRecipe = Kee[str](
    'light_gray_glazed_terracotta_recipe')
  LightGrayHarnessRecipe = Kee[str]('light_gray_harness_recipe')
  LightGrayShulkerBoxRecipe = Kee[str]('light_gray_shulker_box_recipe')
  LightGrayStainedGlassPaneFromGlassPaneRecipe = Kee[str](
    'light_gray_stained_glass_pane_from_glass_pane_recipe')
  LightGrayStainedGlassPaneRecipe = Kee[str](
    'light_gray_stained_glass_pane_recipe')
  LightGrayStainedGlassRecipe = Kee[str]('light_gray_stained_glass_recipe')
  LightGrayTerracottaRecipe = Kee[str]('light_gray_terracotta_recipe')
  LightGrayWoolRecipe = Kee[str]('light_gray_wool_recipe')
  LightGrayWoolSlabRecipe = Kee[str]('light_gray_wool_slab_recipe')
  LightGrayWoolStairsRecipe = Kee[str]('light_gray_wool_stairs_recipe')
  LightWeightedPressurePlateRecipe = Kee[str](
    'light_weighted_pressure_plate_recipe')
  LightenUp = Kee[str]('lighten_up')
  LightningRodRecipe = Kee[str]('lightning_rod_recipe')
  LimeBannerRecipe = Kee[str]('lime_banner_recipe')
  LimeBedFromWhiteBedRecipe = Kee[str]('lime_bed_from_white_bed_recipe')
  LimeBedRecipe = Kee[str]('lime_bed_recipe')
  LimeBundleRecipe = Kee[str]('lime_bundle_recipe')
  LimeCandleRecipe = Kee[str]('lime_candle_recipe')
  LimeCarpetFromWhiteCarpetRecipe = Kee[str](
    'lime_carpet_from_white_carpet_recipe')
  LimeCarpetRecipe = Kee[str]('lime_carpet_recipe')
  LimeConcretePowderRecipe = Kee[str]('lime_concrete_powder_recipe')
  LimeConcreteSlabFromLimeConcreteStonecuttingRecipe = Kee[str](
    'lime_concrete_slab_from_lime_concrete_stonecutting_recipe')
  LimeConcreteSlabRecipe = Kee[str]('lime_concrete_slab_recipe')
  LimeConcreteStairsFromLimeConcreteStonecuttingRecipe = Kee[str](
    'lime_concrete_stairs_from_lime_concrete_stonecutting_recipe')
  LimeConcreteStairsRecipe = Kee[str]('lime_concrete_stairs_recipe')
  LimeCushionRecipe = Kee[str]('lime_cushion_recipe')
  LimeDyeFromSmeltingRecipe = Kee[str]('lime_dye_from_smelting_recipe')
  LimeDyeRecipe = Kee[str]('lime_dye_recipe')
  LimeGlazedTerracottaRecipe = Kee[str]('lime_glazed_terracotta_recipe')
  LimeHarnessRecipe = Kee[str]('lime_harness_recipe')
  LimeShulkerBoxRecipe = Kee[str]('lime_shulker_box_recipe')
  LimeStainedGlassPaneFromGlassPaneRecipe = Kee[str](
    'lime_stained_glass_pane_from_glass_pane_recipe')
  LimeStainedGlassPaneRecipe = Kee[str]('lime_stained_glass_pane_recipe')
  LimeStainedGlassRecipe = Kee[str]('lime_stained_glass_recipe')
  LimeTerracottaRecipe = Kee[str]('lime_terracotta_recipe')
  LimeWoolRecipe = Kee[str]('lime_wool_recipe')
  LimeWoolSlabRecipe = Kee[str]('lime_wool_slab_recipe')
  LimeWoolStairsRecipe = Kee[str]('lime_wool_stairs_recipe')
  LittleSniffs = Kee[str]('little_sniffs')
  LocalBrewery = Kee[str]('local_brewery')
  LodestoneRecipe = Kee[str]('lodestone_recipe')
  LoomRecipe = Kee[str]('loom_recipe')
  MaceRecipe = Kee[str]('mace_recipe')
  MagentaBannerRecipe = Kee[str]('magenta_banner_recipe')
  MagentaBedFromWhiteBedRecipe = Kee[str]('magenta_bed_from_white_bed_recipe')
  MagentaBedRecipe = Kee[str]('magenta_bed_recipe')
  MagentaBundleRecipe = Kee[str]('magenta_bundle_recipe')
  MagentaCandleRecipe = Kee[str]('magenta_candle_recipe')
  MagentaCarpetFromWhiteCarpetRecipe = Kee[str](
    'magenta_carpet_from_white_carpet_recipe')
  MagentaCarpetRecipe = Kee[str]('magenta_carpet_recipe')
  MagentaConcretePowderRecipe = Kee[str]('magenta_concrete_powder_recipe')
  MagentaConcreteSlabFromMagentaConcreteStonecuttingRecipe = Kee[str](
    'magenta_concrete_slab_from_magenta_concrete_stonecutting_recipe')
  MagentaConcreteSlabRecipe = Kee[str]('magenta_concrete_slab_recipe')
  MagentaConcreteStairsFromMagentaConcreteStonecuttingRecipe = Kee[str](
    'magenta_concrete_stairs_from_magenta_concrete_stonecutting_recipe')
  MagentaConcreteStairsRecipe = Kee[str]('magenta_concrete_stairs_recipe')
  MagentaCushionRecipe = Kee[str]('magenta_cushion_recipe')
  MagentaDyeFromAlliumRecipe = Kee[str]('magenta_dye_from_allium_recipe')
  MagentaDyeFromBlueRedPinkRecipe = Kee[str](
    'magenta_dye_from_blue_red_pink_recipe')
  MagentaDyeFromBlueRedWhiteDyeRecipe = Kee[str](
    'magenta_dye_from_blue_red_white_dye_recipe')
  MagentaDyeFromLapisInkBonemealRecipe = Kee[str](
    'magenta_dye_from_lapis_ink_bonemeal_recipe')
  MagentaDyeFromLapisRedPinkRecipe = Kee[str](
    'magenta_dye_from_lapis_red_pink_recipe')
  MagentaDyeFromLilacRecipe = Kee[str]('magenta_dye_from_lilac_recipe')
  MagentaDyeFromPurpleAndPinkRecipe = Kee[str](
    'magenta_dye_from_purple_and_pink_recipe')
  MagentaGlazedTerracottaRecipe = Kee[str]('magenta_glazed_terracotta_recipe')
  MagentaHarnessRecipe = Kee[str]('magenta_harness_recipe')
  MagentaShulkerBoxRecipe = Kee[str]('magenta_shulker_box_recipe')
  MagentaStainedGlassPaneFromGlassPaneRecipe = Kee[str](
    'magenta_stained_glass_pane_from_glass_pane_recipe')
  MagentaStainedGlassPaneRecipe = Kee[str]('magenta_stained_glass_pane_recipe')
  MagentaStainedGlassRecipe = Kee[str]('magenta_stained_glass_recipe')
  MagentaTerracottaRecipe = Kee[str]('magenta_terracotta_recipe')
  MagentaWoolRecipe = Kee[str]('magenta_wool_recipe')
  MagentaWoolSlabRecipe = Kee[str]('magenta_wool_slab_recipe')
  MagentaWoolStairsRecipe = Kee[str]('magenta_wool_stairs_recipe')
  MagmaBlockRecipe = Kee[str]('magma_block_recipe')
  MagmaCreamRecipe = Kee[str]('magma_cream_recipe')
  MangroveBoatRecipe = Kee[str]('mangrove_boat_recipe')
  MangroveButtonRecipe = Kee[str]('mangrove_button_recipe')
  MangroveChestBoatRecipe = Kee[str]('mangrove_chest_boat_recipe')
  MangroveDoorRecipe = Kee[str]('mangrove_door_recipe')
  MangroveFenceGateRecipe = Kee[str]('mangrove_fence_gate_recipe')
  MangroveFenceRecipe = Kee[str]('mangrove_fence_recipe')
  MangroveHangingSignRecipe = Kee[str]('mangrove_hanging_sign_recipe')
  MangrovePlanksRecipe = Kee[str]('mangrove_planks_recipe')
  MangrovePressurePlateRecipe = Kee[str]('mangrove_pressure_plate_recipe')
  MangroveShelfRecipe = Kee[str]('mangrove_shelf_recipe')
  MangroveSignRecipe = Kee[str]('mangrove_sign_recipe')
  MangroveSlabRecipe = Kee[str]('mangrove_slab_recipe')
  MangroveStairsRecipe = Kee[str]('mangrove_stairs_recipe')
  MangroveTrapdoorRecipe = Kee[str]('mangrove_trapdoor_recipe')
  MangroveWoodRecipe = Kee[str]('mangrove_wood_recipe')
  MapCloningRecipe = Kee[str]('map_cloning_recipe')
  MapRecipe = Kee[str]('map_recipe')
  MelonRecipe = Kee[str]('melon_recipe')
  MelonSeedsRecipe = Kee[str]('melon_seeds_recipe')
  MinecartRecipe = Kee[str]('minecart_recipe')
  MinecraftTrialSEdition = Kee[str]('minecraft_trial_s_edition')
  MobKabob = Kee[str]('mob_kabob')
  MojangBannerPatternRecipe = Kee[str]('mojang_banner_pattern_recipe')
  MonsterHunter = Kee[str]('monster_hunter')
  MonstersHunted = Kee[str]('monsters_hunted')
  MossCarpetRecipe = Kee[str]('moss_carpet_recipe')
  MossyCobblestoneFromMossBlockRecipe = Kee[str](
    'mossy_cobblestone_from_moss_block_recipe')
  MossyCobblestoneFromVineRecipe = Kee[str](
    'mossy_cobblestone_from_vine_recipe')
  MossyCobblestoneRecipe = Kee[str]('mossy_cobblestone_recipe')
  MossyCobblestoneSlabFromMossyCobblestoneStonecuttingRecipe = Kee[str](
    'mossy_cobblestone_slab_from_mossy_cobblestone_stonecutting_recipe')
  MossyCobblestoneSlabRecipe = Kee[str]('mossy_cobblestone_slab_recipe')
  MossyCobblestoneStairsFromMossyCobblestoneStonecuttingRecipe = Kee[str](
    'mossy_cobblestone_stairs_from_mossy_cobblestone_stonecutting_recipe')
  MossyCobblestoneStairsRecipe = Kee[str]('mossy_cobblestone_stairs_recipe')
  MossyCobblestoneWallFromMossyCobblestoneStonecuttingRecipe = Kee[str](
    'mossy_cobblestone_wall_from_mossy_cobblestone_stonecutting_recipe')
  MossyCobblestoneWallRecipe = Kee[str]('mossy_cobblestone_wall_recipe')
  MossyStoneBrickSlabFromMossyStoneBricksStonecuttingRecipe = Kee[str](
    'mossy_stone_brick_slab_from_mossy_stone_bricks_stonecutting_recipe')
  MossyStoneBrickSlabRecipe = Kee[str]('mossy_stone_brick_slab_recipe')
  MossyStoneBrickStairsFromMossyStoneBricksStonecuttingRecipe = Kee[str](
    'mossy_stone_brick_stairs_from_mossy_stone_bricks_stonecutting_recipe')
  MossyStoneBrickStairsRecipe = Kee[str]('mossy_stone_brick_stairs_recipe')
  MossyStoneBrickWallFromMossyStoneBrickStonecuttingRecipe = Kee[str](
    'mossy_stone_brick_wall_from_mossy_stone_brick_stonecutting_recipe')
  MossyStoneBrickWallFromMossyStoneBricksStonecuttingRecipe = Kee[str](
    'mossy_stone_brick_wall_from_mossy_stone_bricks_stonecutting_recipe')
  MossyStoneBrickWallRecipe = Kee[str]('mossy_stone_brick_wall_recipe')
  MossyStoneBricksFromMossBlockRecipe = Kee[str](
    'mossy_stone_bricks_from_moss_block_recipe')
  MossyStoneBricksFromVineRecipe = Kee[str](
    'mossy_stone_bricks_from_vine_recipe')
  MossyStoneBricksRecipe = Kee[str]('mossy_stone_bricks_recipe')
  MudBrickSlabFromMudBricksStonecuttingRecipe = Kee[str](
    'mud_brick_slab_from_mud_bricks_stonecutting_recipe')
  MudBrickSlabRecipe = Kee[str]('mud_brick_slab_recipe')
  MudBrickStairsFromMudBricksStonecuttingRecipe = Kee[str](
    'mud_brick_stairs_from_mud_bricks_stonecutting_recipe')
  MudBrickStairsRecipe = Kee[str]('mud_brick_stairs_recipe')
  MudBrickWallFromMudBricksStonecuttingRecipe = Kee[str](
    'mud_brick_wall_from_mud_bricks_stonecutting_recipe')
  MudBrickWallRecipe = Kee[str]('mud_brick_wall_recipe')
  MudBricksRecipe = Kee[str]('mud_bricks_recipe')
  MuddyMangroveRootsRecipe = Kee[str]('muddy_mangrove_roots_recipe')
  MushroomStewRecipe = Kee[str]('mushroom_stew_recipe')
  MusicDisc5Recipe = Kee[str]('music_disc_5_recipe')
  NameTagRecipe = Kee[str]('name_tag_recipe')
  NetherBrickFenceRecipe = Kee[str]('nether_brick_fence_recipe')
  NetherBrickRecipe = Kee[str]('nether_brick_recipe')
  NetherBrickSlabFromNetherBricksStonecuttingRecipe = Kee[str](
    'nether_brick_slab_from_nether_bricks_stonecutting_recipe')
  NetherBrickSlabRecipe = Kee[str]('nether_brick_slab_recipe')
  NetherBrickStairsFromNetherBricksStonecuttingRecipe = Kee[str](
    'nether_brick_stairs_from_nether_bricks_stonecutting_recipe')
  NetherBrickStairsRecipe = Kee[str]('nether_brick_stairs_recipe')
  NetherBrickWallFromNetherBricksStonecuttingRecipe = Kee[str](
    'nether_brick_wall_from_nether_bricks_stonecutting_recipe')
  NetherBrickWallRecipe = Kee[str]('nether_brick_wall_recipe')
  NetherBricksRecipe = Kee[str]('nether_bricks_recipe')
  NetherRoot = Kee[str]('nether_root')
  NetherWartBlockRecipe = Kee[str]('nether_wart_block_recipe')
  NetheriteAxeSmithingRecipe = Kee[str]('netherite_axe_smithing_recipe')
  NetheriteBlockRecipe = Kee[str]('netherite_block_recipe')
  NetheriteBootsSmithingRecipe = Kee[str]('netherite_boots_smithing_recipe')
  NetheriteChestplateSmithingRecipe = Kee[str](
    'netherite_chestplate_smithing_recipe')
  NetheriteHelmetSmithingRecipe = Kee[str]('netherite_helmet_smithing_recipe')
  NetheriteHoeSmithingRecipe = Kee[str]('netherite_hoe_smithing_recipe')
  NetheriteHorseArmorSmithingRecipe = Kee[str](
    'netherite_horse_armor_smithing_recipe')
  NetheriteIngotFromNetheriteBlockRecipe = Kee[str](
    'netherite_ingot_from_netherite_block_recipe')
  NetheriteIngotRecipe = Kee[str]('netherite_ingot_recipe')
  NetheriteLeggingsSmithingRecipe = Kee[str](
    'netherite_leggings_smithing_recipe')
  NetheriteNautilusArmorSmithingRecipe = Kee[str](
    'netherite_nautilus_armor_smithing_recipe')
  NetheritePickaxeSmithingRecipe = Kee[str](
    'netherite_pickaxe_smithing_recipe')
  NetheriteScrapFromBlastingRecipe = Kee[str](
    'netherite_scrap_from_blasting_recipe')
  NetheriteScrapRecipe = Kee[str]('netherite_scrap_recipe')
  NetheriteShovelSmithingRecipe = Kee[str]('netherite_shovel_smithing_recipe')
  NetheriteSpearSmithingRecipe = Kee[str]('netherite_spear_smithing_recipe')
  NetheriteSwordSmithingRecipe = Kee[str]('netherite_sword_smithing_recipe')
  NetheriteUpgradeSmithingTemplateRecipe = Kee[str](
    'netherite_upgrade_smithing_template_recipe')
  NotQuiteNineLives = Kee[str]('not_quite_nine_lives')
  NotTodayThankYou = Kee[str]('not_today_thank_you')
  NoteBlockRecipe = Kee[str]('note_block_recipe')
  OakBoatRecipe = Kee[str]('oak_boat_recipe')
  OakButtonRecipe = Kee[str]('oak_button_recipe')
  OakChestBoatRecipe = Kee[str]('oak_chest_boat_recipe')
  OakDoorRecipe = Kee[str]('oak_door_recipe')
  OakFenceGateRecipe = Kee[str]('oak_fence_gate_recipe')
  OakFenceRecipe = Kee[str]('oak_fence_recipe')
  OakHangingSignRecipe = Kee[str]('oak_hanging_sign_recipe')
  OakPlanksRecipe = Kee[str]('oak_planks_recipe')
  OakPressurePlateRecipe = Kee[str]('oak_pressure_plate_recipe')
  OakShelfRecipe = Kee[str]('oak_shelf_recipe')
  OakSignRecipe = Kee[str]('oak_sign_recipe')
  OakSlabRecipe = Kee[str]('oak_slab_recipe')
  OakStairsRecipe = Kee[str]('oak_stairs_recipe')
  OakTrapdoorRecipe = Kee[str]('oak_trapdoor_recipe')
  OakWoodRecipe = Kee[str]('oak_wood_recipe')
  ObserverRecipe = Kee[str]('observer_recipe')
  OhShiny = Kee[str]('oh_shiny')
  OlBetsy = Kee[str]('ol_betsy')
  OrangeBannerRecipe = Kee[str]('orange_banner_recipe')
  OrangeBedFromWhiteBedRecipe = Kee[str]('orange_bed_from_white_bed_recipe')
  OrangeBedRecipe = Kee[str]('orange_bed_recipe')
  OrangeBundleRecipe = Kee[str]('orange_bundle_recipe')
  OrangeCandleRecipe = Kee[str]('orange_candle_recipe')
  OrangeCarpetFromWhiteCarpetRecipe = Kee[str](
    'orange_carpet_from_white_carpet_recipe')
  OrangeCarpetRecipe = Kee[str]('orange_carpet_recipe')
  OrangeConcretePowderRecipe = Kee[str]('orange_concrete_powder_recipe')
  OrangeConcreteSlabFromOrangeConcreteStonecuttingRecipe = Kee[str](
    'orange_concrete_slab_from_orange_concrete_stonecutting_recipe')
  OrangeConcreteSlabRecipe = Kee[str]('orange_concrete_slab_recipe')
  OrangeConcreteStairsFromOrangeConcreteStonecuttingRecipe = Kee[str](
    'orange_concrete_stairs_from_orange_concrete_stonecutting_recipe')
  OrangeConcreteStairsRecipe = Kee[str]('orange_concrete_stairs_recipe')
  OrangeCushionRecipe = Kee[str]('orange_cushion_recipe')
  OrangeDyeFromOpenEyeblossomRecipe = Kee[str](
    'orange_dye_from_open_eyeblossom_recipe')
  OrangeDyeFromOrangeTulipRecipe = Kee[str](
    'orange_dye_from_orange_tulip_recipe')
  OrangeDyeFromRedYellowRecipe = Kee[str]('orange_dye_from_red_yellow_recipe')
  OrangeDyeFromTorchflowerRecipe = Kee[str](
    'orange_dye_from_torchflower_recipe')
  OrangeGlazedTerracottaRecipe = Kee[str]('orange_glazed_terracotta_recipe')
  OrangeHarnessRecipe = Kee[str]('orange_harness_recipe')
  OrangeShulkerBoxRecipe = Kee[str]('orange_shulker_box_recipe')
  OrangeStainedGlassPaneFromGlassPaneRecipe = Kee[str](
    'orange_stained_glass_pane_from_glass_pane_recipe')
  OrangeStainedGlassPaneRecipe = Kee[str]('orange_stained_glass_pane_recipe')
  OrangeStainedGlassRecipe = Kee[str]('orange_stained_glass_recipe')
  OrangeTerracottaRecipe = Kee[str]('orange_terracotta_recipe')
  OrangeWoolRecipe = Kee[str]('orange_wool_recipe')
  OrangeWoolSlabRecipe = Kee[str]('orange_wool_slab_recipe')
  OrangeWoolStairsRecipe = Kee[str]('orange_wool_stairs_recipe')
  OverOverkill = Kee[str]('over_overkill')
  OxidizedChiseledCopperFromOxidizedCopperStonecuttingRecipe = Kee[str](
    'oxidized_chiseled_copper_from_oxidized_copper_stonecutting_recipe')
  OxidizedChiseledCopperFromOxidizedCutCopperStonecuttingRecipe = Kee[str](
    'oxidized_chiseled_copper_from_oxidized_cut_copper_stonecutting_recipe')
  OxidizedChiseledCopperRecipe = Kee[str]('oxidized_chiseled_copper_recipe')
  OxidizedCopperBulbRecipe = Kee[str]('oxidized_copper_bulb_recipe')
  OxidizedCopperGrateFromOxidizedCopperStonecuttingRecipe = Kee[str](
    'oxidized_copper_grate_from_oxidized_copper_stonecutting_recipe')
  OxidizedCopperGrateRecipe = Kee[str]('oxidized_copper_grate_recipe')
  OxidizedCutCopperFromOxidizedCopperStonecuttingRecipe = Kee[str](
    'oxidized_cut_copper_from_oxidized_copper_stonecutting_recipe')
  OxidizedCutCopperRecipe = Kee[str]('oxidized_cut_copper_recipe')
  OxidizedCutCopperSlabFromOxidizedCopperStonecuttingRecipe = Kee[str](
    'oxidized_cut_copper_slab_from_oxidized_copper_stonecutting_recipe')
  OxidizedCutCopperSlabFromOxidizedCutCopperStonecuttingRecipe = Kee[str](
    'oxidized_cut_copper_slab_from_oxidized_cut_copper_stonecutting_recipe')
  OxidizedCutCopperSlabRecipe = Kee[str]('oxidized_cut_copper_slab_recipe')
  OxidizedCutCopperStairsFromOxidizedCopperStonecuttingRecipe = Kee[str](
    'oxidized_cut_copper_stairs_from_oxidized_copper_stonecutting_recipe')
  OxidizedCutCopperStairsFromOxidizedCutCopperStonecuttingRecipe = Kee[str](
    'oxidized_cut_copper_stairs_from_oxidized_cut_copper_stonecutting_recipe')
  OxidizedCutCopperStairsRecipe = Kee[str]('oxidized_cut_copper_stairs_recipe')
  PackedIceRecipe = Kee[str]('packed_ice_recipe')
  PackedMudRecipe = Kee[str]('packed_mud_recipe')
  PaintingRecipe = Kee[str]('painting_recipe')
  PaleMossCarpetRecipe = Kee[str]('pale_moss_carpet_recipe')
  PaleOakBoatRecipe = Kee[str]('pale_oak_boat_recipe')
  PaleOakButtonRecipe = Kee[str]('pale_oak_button_recipe')
  PaleOakChestBoatRecipe = Kee[str]('pale_oak_chest_boat_recipe')
  PaleOakDoorRecipe = Kee[str]('pale_oak_door_recipe')
  PaleOakFenceGateRecipe = Kee[str]('pale_oak_fence_gate_recipe')
  PaleOakFenceRecipe = Kee[str]('pale_oak_fence_recipe')
  PaleOakHangingSignRecipe = Kee[str]('pale_oak_hanging_sign_recipe')
  PaleOakPlanksRecipe = Kee[str]('pale_oak_planks_recipe')
  PaleOakPressurePlateRecipe = Kee[str]('pale_oak_pressure_plate_recipe')
  PaleOakShelfRecipe = Kee[str]('pale_oak_shelf_recipe')
  PaleOakSignRecipe = Kee[str]('pale_oak_sign_recipe')
  PaleOakSlabRecipe = Kee[str]('pale_oak_slab_recipe')
  PaleOakStairsRecipe = Kee[str]('pale_oak_stairs_recipe')
  PaleOakTrapdoorRecipe = Kee[str]('pale_oak_trapdoor_recipe')
  PaleOakWoodRecipe = Kee[str]('pale_oak_wood_recipe')
  PaperRecipe = Kee[str]('paper_recipe')
  PinkBannerRecipe = Kee[str]('pink_banner_recipe')
  PinkBedFromWhiteBedRecipe = Kee[str]('pink_bed_from_white_bed_recipe')
  PinkBedRecipe = Kee[str]('pink_bed_recipe')
  PinkBundleRecipe = Kee[str]('pink_bundle_recipe')
  PinkCandleRecipe = Kee[str]('pink_candle_recipe')
  PinkCarpetFromWhiteCarpetRecipe = Kee[str](
    'pink_carpet_from_white_carpet_recipe')
  PinkCarpetRecipe = Kee[str]('pink_carpet_recipe')
  PinkConcretePowderRecipe = Kee[str]('pink_concrete_powder_recipe')
  PinkConcreteSlabFromPinkConcreteStonecuttingRecipe = Kee[str](
    'pink_concrete_slab_from_pink_concrete_stonecutting_recipe')
  PinkConcreteSlabRecipe = Kee[str]('pink_concrete_slab_recipe')
  PinkConcreteStairsFromPinkConcreteStonecuttingRecipe = Kee[str](
    'pink_concrete_stairs_from_pink_concrete_stonecutting_recipe')
  PinkConcreteStairsRecipe = Kee[str]('pink_concrete_stairs_recipe')
  PinkCushionRecipe = Kee[str]('pink_cushion_recipe')
  PinkDyeFromCactusFlowerRecipe = Kee[str](
    'pink_dye_from_cactus_flower_recipe')
  PinkDyeFromPeonyRecipe = Kee[str]('pink_dye_from_peony_recipe')
  PinkDyeFromPinkPetalsRecipe = Kee[str]('pink_dye_from_pink_petals_recipe')
  PinkDyeFromPinkTulipRecipe = Kee[str]('pink_dye_from_pink_tulip_recipe')
  PinkDyeFromRedBonemealRecipe = Kee[str]('pink_dye_from_red_bonemeal_recipe')
  PinkDyeFromRedWhiteDyeRecipe = Kee[str]('pink_dye_from_red_white_dye_recipe')
  PinkGlazedTerracottaRecipe = Kee[str]('pink_glazed_terracotta_recipe')
  PinkHarnessRecipe = Kee[str]('pink_harness_recipe')
  PinkShulkerBoxRecipe = Kee[str]('pink_shulker_box_recipe')
  PinkStainedGlassPaneFromGlassPaneRecipe = Kee[str](
    'pink_stained_glass_pane_from_glass_pane_recipe')
  PinkStainedGlassPaneRecipe = Kee[str]('pink_stained_glass_pane_recipe')
  PinkStainedGlassRecipe = Kee[str]('pink_stained_glass_recipe')
  PinkTerracottaRecipe = Kee[str]('pink_terracotta_recipe')
  PinkWoolRecipe = Kee[str]('pink_wool_recipe')
  PinkWoolSlabRecipe = Kee[str]('pink_wool_slab_recipe')
  PinkWoolStairsRecipe = Kee[str]('pink_wool_stairs_recipe')
  PistonRecipe = Kee[str]('piston_recipe')
  PlantingThePast = Kee[str]('planting_the_past')
  PolishedAndesiteFromAndesiteStonecuttingRecipe = Kee[str](
    'polished_andesite_from_andesite_stonecutting_recipe')
  PolishedAndesiteRecipe = Kee[str]('polished_andesite_recipe')
  PolishedAndesiteSlabFromAndesiteStonecuttingRecipe = Kee[str](
    'polished_andesite_slab_from_andesite_stonecutting_recipe')
  PolishedAndesiteSlabFromPolishedAndesiteStonecuttingRecipe = Kee[str](
    'polished_andesite_slab_from_polished_andesite_stonecutting_recipe')
  PolishedAndesiteSlabRecipe = Kee[str]('polished_andesite_slab_recipe')
  PolishedAndesiteStairsFromAndesiteStonecuttingRecipe = Kee[str](
    'polished_andesite_stairs_from_andesite_stonecutting_recipe')
  PolishedAndesiteStairsFromPolishedAndesiteStonecuttingRecipe = Kee[str](
    'polished_andesite_stairs_from_polished_andesite_stonecutting_recipe')
  PolishedAndesiteStairsRecipe = Kee[str]('polished_andesite_stairs_recipe')
  PolishedBasaltFromBasaltStonecuttingRecipe = Kee[str](
    'polished_basalt_from_basalt_stonecutting_recipe')
  PolishedBasaltRecipe = Kee[str]('polished_basalt_recipe')
  PolishedBlackstoneBrickSlabFromBlackstoneStonecuttingRecipe = Kee[str](
    'polished_blackstone_brick_slab_from_blackstone_stonecutting_recipe')
  PolishedBlackstoneBrickSlabFromPolishedBlackstoneBricksStonecuttingRecipe = Kee[str](
    'polished_blackstone_brick_slab_from_polished_blackstone_bricks_stonecutting_recipe')
  PolishedBlackstoneBrickSlabFromPolishedBlackstoneStonecuttingRecipe = Kee[str](
    'polished_blackstone_brick_slab_from_polished_blackstone_stonecutting_recipe')
  PolishedBlackstoneBrickSlabRecipe = Kee[str](
    'polished_blackstone_brick_slab_recipe')
  PolishedBlackstoneBrickStairsFromBlackstoneStonecuttingRecipe = Kee[str](
    'polished_blackstone_brick_stairs_from_blackstone_stonecutting_recipe')
  PolishedBlackstoneBrickStairsFromPolishedBlackstoneBricksStonecuttingRecipe = Kee[str](
    'polished_blackstone_brick_stairs_from_polished_blackstone_bricks_stonecutting_recipe')
  PolishedBlackstoneBrickStairsFromPolishedBlackstoneStonecuttingRecipe = Kee[str](
    'polished_blackstone_brick_stairs_from_polished_blackstone_stonecutting_recipe')
  PolishedBlackstoneBrickStairsRecipe = Kee[str](
    'polished_blackstone_brick_stairs_recipe')
  PolishedBlackstoneBrickWallFromBlackstoneStonecuttingRecipe = Kee[str](
    'polished_blackstone_brick_wall_from_blackstone_stonecutting_recipe')
  PolishedBlackstoneBrickWallFromPolishedBlackstoneBricksStonecuttingRecipe = Kee[str](
    'polished_blackstone_brick_wall_from_polished_blackstone_bricks_stonecutting_recipe')
  PolishedBlackstoneBrickWallFromPolishedBlackstoneStonecuttingRecipe = Kee[str](
    'polished_blackstone_brick_wall_from_polished_blackstone_stonecutting_recipe')
  PolishedBlackstoneBrickWallRecipe = Kee[str](
    'polished_blackstone_brick_wall_recipe')
  PolishedBlackstoneBricksFromBlackstoneStonecuttingRecipe = Kee[str](
    'polished_blackstone_bricks_from_blackstone_stonecutting_recipe')
  PolishedBlackstoneBricksFromPolishedBlackstoneStonecuttingRecipe = Kee[str](
    'polished_blackstone_bricks_from_polished_blackstone_stonecutting_recipe')
  PolishedBlackstoneBricksRecipe = Kee[str](
    'polished_blackstone_bricks_recipe')
  PolishedBlackstoneButtonRecipe = Kee[str](
    'polished_blackstone_button_recipe')
  PolishedBlackstoneFromBlackstoneStonecuttingRecipe = Kee[str](
    'polished_blackstone_from_blackstone_stonecutting_recipe')
  PolishedBlackstonePressurePlateRecipe = Kee[str](
    'polished_blackstone_pressure_plate_recipe')
  PolishedBlackstoneRecipe = Kee[str]('polished_blackstone_recipe')
  PolishedBlackstoneSlabFromBlackstoneStonecuttingRecipe = Kee[str](
    'polished_blackstone_slab_from_blackstone_stonecutting_recipe')
  PolishedBlackstoneSlabFromPolishedBlackstoneStonecuttingRecipe = Kee[str](
    'polished_blackstone_slab_from_polished_blackstone_stonecutting_recipe')
  PolishedBlackstoneSlabRecipe = Kee[str]('polished_blackstone_slab_recipe')
  PolishedBlackstoneStairsFromBlackstoneStonecuttingRecipe = Kee[str](
    'polished_blackstone_stairs_from_blackstone_stonecutting_recipe')
  PolishedBlackstoneStairsFromPolishedBlackstoneStonecuttingRecipe = Kee[str](
    'polished_blackstone_stairs_from_polished_blackstone_stonecutting_recipe')
  PolishedBlackstoneStairsRecipe = Kee[str](
    'polished_blackstone_stairs_recipe')
  PolishedBlackstoneWallFromBlackstoneStonecuttingRecipe = Kee[str](
    'polished_blackstone_wall_from_blackstone_stonecutting_recipe')
  PolishedBlackstoneWallFromPolishedBlackstoneStonecuttingRecipe = Kee[str](
    'polished_blackstone_wall_from_polished_blackstone_stonecutting_recipe')
  PolishedBlackstoneWallRecipe = Kee[str]('polished_blackstone_wall_recipe')
  PolishedCinnabarFromCinnabarStonecuttingRecipe = Kee[str](
    'polished_cinnabar_from_cinnabar_stonecutting_recipe')
  PolishedCinnabarRecipe = Kee[str]('polished_cinnabar_recipe')
  PolishedCinnabarSlabFromCinnabarStonecuttingRecipe = Kee[str](
    'polished_cinnabar_slab_from_cinnabar_stonecutting_recipe')
  PolishedCinnabarSlabFromPolishedCinnabarStonecuttingRecipe = Kee[str](
    'polished_cinnabar_slab_from_polished_cinnabar_stonecutting_recipe')
  PolishedCinnabarSlabRecipe = Kee[str]('polished_cinnabar_slab_recipe')
  PolishedCinnabarStairsFromCinnabarStonecuttingRecipe = Kee[str](
    'polished_cinnabar_stairs_from_cinnabar_stonecutting_recipe')
  PolishedCinnabarStairsFromPolishedCinnabarStonecuttingRecipe = Kee[str](
    'polished_cinnabar_stairs_from_polished_cinnabar_stonecutting_recipe')
  PolishedCinnabarStairsRecipe = Kee[str]('polished_cinnabar_stairs_recipe')
  PolishedCinnabarWallFromCinnabarStonecuttingRecipe = Kee[str](
    'polished_cinnabar_wall_from_cinnabar_stonecutting_recipe')
  PolishedCinnabarWallFromPolishedCinnabarStonecuttingRecipe = Kee[str](
    'polished_cinnabar_wall_from_polished_cinnabar_stonecutting_recipe')
  PolishedCinnabarWallRecipe = Kee[str]('polished_cinnabar_wall_recipe')
  PolishedDeepslateFromCobbledDeepslateStonecuttingRecipe = Kee[str](
    'polished_deepslate_from_cobbled_deepslate_stonecutting_recipe')
  PolishedDeepslateFromDeepslateStonecuttingRecipe = Kee[str](
    'polished_deepslate_from_deepslate_stonecutting_recipe')
  PolishedDeepslateRecipe = Kee[str]('polished_deepslate_recipe')
  PolishedDeepslateSlabFromCobbledDeepslateStonecuttingRecipe = Kee[str](
    'polished_deepslate_slab_from_cobbled_deepslate_stonecutting_recipe')
  PolishedDeepslateSlabFromDeepslateStonecuttingRecipe = Kee[str](
    'polished_deepslate_slab_from_deepslate_stonecutting_recipe')
  PolishedDeepslateSlabFromPolishedDeepslateStonecuttingRecipe = Kee[str](
    'polished_deepslate_slab_from_polished_deepslate_stonecutting_recipe')
  PolishedDeepslateSlabRecipe = Kee[str]('polished_deepslate_slab_recipe')
  PolishedDeepslateStairsFromCobbledDeepslateStonecuttingRecipe = Kee[str](
    'polished_deepslate_stairs_from_cobbled_deepslate_stonecutting_recipe')
  PolishedDeepslateStairsFromDeepslateStonecuttingRecipe = Kee[str](
    'polished_deepslate_stairs_from_deepslate_stonecutting_recipe')
  PolishedDeepslateStairsFromPolishedDeepslateStonecuttingRecipe = Kee[str](
    'polished_deepslate_stairs_from_polished_deepslate_stonecutting_recipe')
  PolishedDeepslateStairsRecipe = Kee[str]('polished_deepslate_stairs_recipe')
  PolishedDeepslateWallFromCobbledDeepslateStonecuttingRecipe = Kee[str](
    'polished_deepslate_wall_from_cobbled_deepslate_stonecutting_recipe')
  PolishedDeepslateWallFromDeepslateStonecuttingRecipe = Kee[str](
    'polished_deepslate_wall_from_deepslate_stonecutting_recipe')
  PolishedDeepslateWallFromPolishedDeepslateStonecuttingRecipe = Kee[str](
    'polished_deepslate_wall_from_polished_deepslate_stonecutting_recipe')
  PolishedDeepslateWallRecipe = Kee[str]('polished_deepslate_wall_recipe')
  PolishedDioriteFromDioriteStonecuttingRecipe = Kee[str](
    'polished_diorite_from_diorite_stonecutting_recipe')
  PolishedDioriteRecipe = Kee[str]('polished_diorite_recipe')
  PolishedDioriteSlabFromDioriteStonecuttingRecipe = Kee[str](
    'polished_diorite_slab_from_diorite_stonecutting_recipe')
  PolishedDioriteSlabFromPolishedDioriteStonecuttingRecipe = Kee[str](
    'polished_diorite_slab_from_polished_diorite_stonecutting_recipe')
  PolishedDioriteSlabRecipe = Kee[str]('polished_diorite_slab_recipe')
  PolishedDioriteStairsFromDioriteStonecuttingRecipe = Kee[str](
    'polished_diorite_stairs_from_diorite_stonecutting_recipe')
  PolishedDioriteStairsFromPolishedDioriteStonecuttingRecipe = Kee[str](
    'polished_diorite_stairs_from_polished_diorite_stonecutting_recipe')
  PolishedDioriteStairsRecipe = Kee[str]('polished_diorite_stairs_recipe')
  PolishedGraniteFromGraniteStonecuttingRecipe = Kee[str](
    'polished_granite_from_granite_stonecutting_recipe')
  PolishedGraniteRecipe = Kee[str]('polished_granite_recipe')
  PolishedGraniteSlabFromGraniteStonecuttingRecipe = Kee[str](
    'polished_granite_slab_from_granite_stonecutting_recipe')
  PolishedGraniteSlabFromPolishedGraniteStonecuttingRecipe = Kee[str](
    'polished_granite_slab_from_polished_granite_stonecutting_recipe')
  PolishedGraniteSlabRecipe = Kee[str]('polished_granite_slab_recipe')
  PolishedGraniteStairsFromGraniteStonecuttingRecipe = Kee[str](
    'polished_granite_stairs_from_granite_stonecutting_recipe')
  PolishedGraniteStairsFromPolishedGraniteStonecuttingRecipe = Kee[str](
    'polished_granite_stairs_from_polished_granite_stonecutting_recipe')
  PolishedGraniteStairsRecipe = Kee[str]('polished_granite_stairs_recipe')
  PolishedSulfurFromSulfurStonecuttingRecipe = Kee[str](
    'polished_sulfur_from_sulfur_stonecutting_recipe')
  PolishedSulfurRecipe = Kee[str]('polished_sulfur_recipe')
  PolishedSulfurSlabFromPolishedSulfurStonecuttingRecipe = Kee[str](
    'polished_sulfur_slab_from_polished_sulfur_stonecutting_recipe')
  PolishedSulfurSlabFromSulfurStonecuttingRecipe = Kee[str](
    'polished_sulfur_slab_from_sulfur_stonecutting_recipe')
  PolishedSulfurSlabRecipe = Kee[str]('polished_sulfur_slab_recipe')
  PolishedSulfurStairsFromPolishedSulfurStonecuttingRecipe = Kee[str](
    'polished_sulfur_stairs_from_polished_sulfur_stonecutting_recipe')
  PolishedSulfurStairsFromSulfurStonecuttingRecipe = Kee[str](
    'polished_sulfur_stairs_from_sulfur_stonecutting_recipe')
  PolishedSulfurStairsRecipe = Kee[str]('polished_sulfur_stairs_recipe')
  PolishedSulfurWallFromPolishedSulfurStonecuttingRecipe = Kee[str](
    'polished_sulfur_wall_from_polished_sulfur_stonecutting_recipe')
  PolishedSulfurWallFromSulfurStonecuttingRecipe = Kee[str](
    'polished_sulfur_wall_from_sulfur_stonecutting_recipe')
  PolishedSulfurWallRecipe = Kee[str]('polished_sulfur_wall_recipe')
  PolishedTuffFromTuffStonecuttingRecipe = Kee[str](
    'polished_tuff_from_tuff_stonecutting_recipe')
  PolishedTuffRecipe = Kee[str]('polished_tuff_recipe')
  PolishedTuffSlabFromPolishedTuffStonecuttingRecipe = Kee[str](
    'polished_tuff_slab_from_polished_tuff_stonecutting_recipe')
  PolishedTuffSlabFromTuffStonecuttingRecipe = Kee[str](
    'polished_tuff_slab_from_tuff_stonecutting_recipe')
  PolishedTuffSlabRecipe = Kee[str]('polished_tuff_slab_recipe')
  PolishedTuffStairsFromPolishedTuffStonecuttingRecipe = Kee[str](
    'polished_tuff_stairs_from_polished_tuff_stonecutting_recipe')
  PolishedTuffStairsFromTuffStonecuttingRecipe = Kee[str](
    'polished_tuff_stairs_from_tuff_stonecutting_recipe')
  PolishedTuffStairsRecipe = Kee[str]('polished_tuff_stairs_recipe')
  PolishedTuffWallFromPolishedTuffStonecuttingRecipe = Kee[str](
    'polished_tuff_wall_from_polished_tuff_stonecutting_recipe')
  PolishedTuffWallFromTuffStonecuttingRecipe = Kee[str](
    'polished_tuff_wall_from_tuff_stonecutting_recipe')
  PolishedTuffWallRecipe = Kee[str]('polished_tuff_wall_recipe')
  PoplarBoatRecipe = Kee[str]('poplar_boat_recipe')
  PoplarButtonRecipe = Kee[str]('poplar_button_recipe')
  PoplarChestBoatRecipe = Kee[str]('poplar_chest_boat_recipe')
  PoplarDoorRecipe = Kee[str]('poplar_door_recipe')
  PoplarFenceGateRecipe = Kee[str]('poplar_fence_gate_recipe')
  PoplarFenceRecipe = Kee[str]('poplar_fence_recipe')
  PoplarHangingSignRecipe = Kee[str]('poplar_hanging_sign_recipe')
  PoplarPlanksRecipe = Kee[str]('poplar_planks_recipe')
  PoplarPressurePlateRecipe = Kee[str]('poplar_pressure_plate_recipe')
  PoplarShelfRecipe = Kee[str]('poplar_shelf_recipe')
  PoplarSignRecipe = Kee[str]('poplar_sign_recipe')
  PoplarSlabRecipe = Kee[str]('poplar_slab_recipe')
  PoplarStairsRecipe = Kee[str]('poplar_stairs_recipe')
  PoplarTrapdoorRecipe = Kee[str]('poplar_trapdoor_recipe')
  PoplarWoodRecipe = Kee[str]('poplar_wood_recipe')
  PoppedChorusFruitRecipe = Kee[str]('popped_chorus_fruit_recipe')
  Postmortal = Kee[str]('postmortal')
  PotentSulfurRecipe = Kee[str]('potent_sulfur_recipe')
  PoweredRailRecipe = Kee[str]('powered_rail_recipe')
  PrismarineBrickSlabFromPrismarineBricksStonecuttingRecipe = Kee[str](
    'prismarine_brick_slab_from_prismarine_bricks_stonecutting_recipe')
  PrismarineBrickSlabRecipe = Kee[str]('prismarine_brick_slab_recipe')
  PrismarineBrickStairsFromPrismarineBricksStonecuttingRecipe = Kee[str](
    'prismarine_brick_stairs_from_prismarine_bricks_stonecutting_recipe')
  PrismarineBrickStairsRecipe = Kee[str]('prismarine_brick_stairs_recipe')
  PrismarineBricksRecipe = Kee[str]('prismarine_bricks_recipe')
  PrismarineRecipe = Kee[str]('prismarine_recipe')
  PrismarineSlabFromPrismarineStonecuttingRecipe = Kee[str](
    'prismarine_slab_from_prismarine_stonecutting_recipe')
  PrismarineSlabRecipe = Kee[str]('prismarine_slab_recipe')
  PrismarineStairsFromPrismarineStonecuttingRecipe = Kee[str](
    'prismarine_stairs_from_prismarine_stonecutting_recipe')
  PrismarineStairsRecipe = Kee[str]('prismarine_stairs_recipe')
  PrismarineWallFromPrismarineStonecuttingRecipe = Kee[str](
    'prismarine_wall_from_prismarine_stonecutting_recipe')
  PrismarineWallRecipe = Kee[str]('prismarine_wall_recipe')
  PumpkinPieRecipe = Kee[str]('pumpkin_pie_recipe')
  PumpkinSeedsRecipe = Kee[str]('pumpkin_seeds_recipe')
  PurpleBannerRecipe = Kee[str]('purple_banner_recipe')
  PurpleBedFromWhiteBedRecipe = Kee[str]('purple_bed_from_white_bed_recipe')
  PurpleBedRecipe = Kee[str]('purple_bed_recipe')
  PurpleBundleRecipe = Kee[str]('purple_bundle_recipe')
  PurpleCandleRecipe = Kee[str]('purple_candle_recipe')
  PurpleCarpetFromWhiteCarpetRecipe = Kee[str](
    'purple_carpet_from_white_carpet_recipe')
  PurpleCarpetRecipe = Kee[str]('purple_carpet_recipe')
  PurpleConcretePowderRecipe = Kee[str]('purple_concrete_powder_recipe')
  PurpleConcreteSlabFromPurpleConcreteStonecuttingRecipe = Kee[str](
    'purple_concrete_slab_from_purple_concrete_stonecutting_recipe')
  PurpleConcreteSlabRecipe = Kee[str]('purple_concrete_slab_recipe')
  PurpleConcreteStairsFromPurpleConcreteStonecuttingRecipe = Kee[str](
    'purple_concrete_stairs_from_purple_concrete_stonecutting_recipe')
  PurpleConcreteStairsRecipe = Kee[str]('purple_concrete_stairs_recipe')
  PurpleCushionRecipe = Kee[str]('purple_cushion_recipe')
  PurpleDyeRecipe = Kee[str]('purple_dye_recipe')
  PurpleGlazedTerracottaRecipe = Kee[str]('purple_glazed_terracotta_recipe')
  PurpleHarnessRecipe = Kee[str]('purple_harness_recipe')
  PurpleShulkerBoxRecipe = Kee[str]('purple_shulker_box_recipe')
  PurpleStainedGlassPaneFromGlassPaneRecipe = Kee[str](
    'purple_stained_glass_pane_from_glass_pane_recipe')
  PurpleStainedGlassPaneRecipe = Kee[str]('purple_stained_glass_pane_recipe')
  PurpleStainedGlassRecipe = Kee[str]('purple_stained_glass_recipe')
  PurpleTerracottaRecipe = Kee[str]('purple_terracotta_recipe')
  PurpleWoolRecipe = Kee[str]('purple_wool_recipe')
  PurpleWoolSlabRecipe = Kee[str]('purple_wool_slab_recipe')
  PurpleWoolStairsRecipe = Kee[str]('purple_wool_stairs_recipe')
  PurpurBlockRecipe = Kee[str]('purpur_block_recipe')
  PurpurPillarFromPurpurBlockStonecuttingRecipe = Kee[str](
    'purpur_pillar_from_purpur_block_stonecutting_recipe')
  PurpurPillarRecipe = Kee[str]('purpur_pillar_recipe')
  PurpurSlabFromPurpurBlockStonecuttingRecipe = Kee[str](
    'purpur_slab_from_purpur_block_stonecutting_recipe')
  PurpurSlabRecipe = Kee[str]('purpur_slab_recipe')
  PurpurStairsFromPurpurBlockStonecuttingRecipe = Kee[str](
    'purpur_stairs_from_purpur_block_stonecutting_recipe')
  PurpurStairsRecipe = Kee[str]('purpur_stairs_recipe')
  QuartzBlockRecipe = Kee[str]('quartz_block_recipe')
  QuartzBricksFromQuartzBlockStonecuttingRecipe = Kee[str](
    'quartz_bricks_from_quartz_block_stonecutting_recipe')
  QuartzBricksRecipe = Kee[str]('quartz_bricks_recipe')
  QuartzFromBlastingRecipe = Kee[str]('quartz_from_blasting_recipe')
  QuartzPillarFromQuartzBlockStonecuttingRecipe = Kee[str](
    'quartz_pillar_from_quartz_block_stonecutting_recipe')
  QuartzPillarRecipe = Kee[str]('quartz_pillar_recipe')
  QuartzRecipe = Kee[str]('quartz_recipe')
  QuartzSlabFromQuartzBlockStonecuttingRecipe = Kee[str](
    'quartz_slab_from_quartz_block_stonecutting_recipe')
  QuartzSlabRecipe = Kee[str]('quartz_slab_recipe')
  QuartzStairsFromQuartzBlockStonecuttingRecipe = Kee[str](
    'quartz_stairs_from_quartz_block_stonecutting_recipe')
  QuartzStairsRecipe = Kee[str]('quartz_stairs_recipe')
  RabbitStewFromBrownMushroomRecipe = Kee[str](
    'rabbit_stew_from_brown_mushroom_recipe')
  RabbitStewFromRedMushroomRecipe = Kee[str](
    'rabbit_stew_from_red_mushroom_recipe')
  RabbitStewFromShelfMushroomRecipe = Kee[str](
    'rabbit_stew_from_shelf_mushroom_recipe')
  RailRecipe = Kee[str]('rail_recipe')
  RaiserArmorTrimSmithingTemplateRecipe = Kee[str](
    'raiser_armor_trim_smithing_template_recipe')
  RaiserArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'raiser_armor_trim_smithing_template_smithing_trim_recipe')
  RawCopperBlockRecipe = Kee[str]('raw_copper_block_recipe')
  RawCopperRecipe = Kee[str]('raw_copper_recipe')
  RawGoldBlockRecipe = Kee[str]('raw_gold_block_recipe')
  RawGoldRecipe = Kee[str]('raw_gold_recipe')
  RawIronBlockRecipe = Kee[str]('raw_iron_block_recipe')
  RawIronRecipe = Kee[str]('raw_iron_recipe')
  RecoveryCompassRecipe = Kee[str]('recovery_compass_recipe')
  RedBannerRecipe = Kee[str]('red_banner_recipe')
  RedBedFromWhiteBedRecipe = Kee[str]('red_bed_from_white_bed_recipe')
  RedBedRecipe = Kee[str]('red_bed_recipe')
  RedBundleRecipe = Kee[str]('red_bundle_recipe')
  RedCandleRecipe = Kee[str]('red_candle_recipe')
  RedCarpetFromWhiteCarpetRecipe = Kee[str](
    'red_carpet_from_white_carpet_recipe')
  RedCarpetRecipe = Kee[str]('red_carpet_recipe')
  RedConcretePowderRecipe = Kee[str]('red_concrete_powder_recipe')
  RedConcreteSlabFromRedConcreteStonecuttingRecipe = Kee[str](
    'red_concrete_slab_from_red_concrete_stonecutting_recipe')
  RedConcreteSlabRecipe = Kee[str]('red_concrete_slab_recipe')
  RedConcreteStairsFromRedConcreteStonecuttingRecipe = Kee[str](
    'red_concrete_stairs_from_red_concrete_stonecutting_recipe')
  RedConcreteStairsRecipe = Kee[str]('red_concrete_stairs_recipe')
  RedCushionRecipe = Kee[str]('red_cushion_recipe')
  RedDyeFromBeetrootRecipe = Kee[str]('red_dye_from_beetroot_recipe')
  RedDyeFromPoppyRecipe = Kee[str]('red_dye_from_poppy_recipe')
  RedDyeFromRoseBushRecipe = Kee[str]('red_dye_from_rose_bush_recipe')
  RedDyeFromTulipRecipe = Kee[str]('red_dye_from_tulip_recipe')
  RedGlazedTerracottaRecipe = Kee[str]('red_glazed_terracotta_recipe')
  RedHarnessRecipe = Kee[str]('red_harness_recipe')
  RedNetherBrickSlabFromRedNetherBricksStonecuttingRecipe = Kee[str](
    'red_nether_brick_slab_from_red_nether_bricks_stonecutting_recipe')
  RedNetherBrickSlabRecipe = Kee[str]('red_nether_brick_slab_recipe')
  RedNetherBrickStairsFromRedNetherBricksStonecuttingRecipe = Kee[str](
    'red_nether_brick_stairs_from_red_nether_bricks_stonecutting_recipe')
  RedNetherBrickStairsRecipe = Kee[str]('red_nether_brick_stairs_recipe')
  RedNetherBrickWallFromRedNetherBricksStonecuttingRecipe = Kee[str](
    'red_nether_brick_wall_from_red_nether_bricks_stonecutting_recipe')
  RedNetherBrickWallRecipe = Kee[str]('red_nether_brick_wall_recipe')
  RedNetherBricksRecipe = Kee[str]('red_nether_bricks_recipe')
  RedSandstoneRecipe = Kee[str]('red_sandstone_recipe')
  RedSandstoneSlabFromRedSandstoneStonecuttingRecipe = Kee[str](
    'red_sandstone_slab_from_red_sandstone_stonecutting_recipe')
  RedSandstoneSlabRecipe = Kee[str]('red_sandstone_slab_recipe')
  RedSandstoneStairsFromRedSandstoneStonecuttingRecipe = Kee[str](
    'red_sandstone_stairs_from_red_sandstone_stonecutting_recipe')
  RedSandstoneStairsRecipe = Kee[str]('red_sandstone_stairs_recipe')
  RedSandstoneWallFromRedSandstoneStonecuttingRecipe = Kee[str](
    'red_sandstone_wall_from_red_sandstone_stonecutting_recipe')
  RedSandstoneWallRecipe = Kee[str]('red_sandstone_wall_recipe')
  RedShulkerBoxRecipe = Kee[str]('red_shulker_box_recipe')
  RedStainedGlassPaneFromGlassPaneRecipe = Kee[str](
    'red_stained_glass_pane_from_glass_pane_recipe')
  RedStainedGlassPaneRecipe = Kee[str]('red_stained_glass_pane_recipe')
  RedStainedGlassRecipe = Kee[str]('red_stained_glass_recipe')
  RedTerracottaRecipe = Kee[str]('red_terracotta_recipe')
  RedWoolRecipe = Kee[str]('red_wool_recipe')
  RedWoolSlabRecipe = Kee[str]('red_wool_slab_recipe')
  RedWoolStairsRecipe = Kee[str]('red_wool_stairs_recipe')
  RedstoneBlockRecipe = Kee[str]('redstone_block_recipe')
  RedstoneFromBlastingDeepslateRedstoneOreRecipe = Kee[str](
    'redstone_from_blasting_deepslate_redstone_ore_recipe')
  RedstoneFromBlastingRecipe = Kee[str]('redstone_from_blasting_recipe')
  RedstoneFromBlastingRedstoneOreRecipe = Kee[str](
    'redstone_from_blasting_redstone_ore_recipe')
  RedstoneFromSmeltingDeepslateRedstoneOreRecipe = Kee[str](
    'redstone_from_smelting_deepslate_redstone_ore_recipe')
  RedstoneFromSmeltingRecipe = Kee[str]('redstone_from_smelting_recipe')
  RedstoneFromSmeltingRedstoneOreRecipe = Kee[str](
    'redstone_from_smelting_redstone_ore_recipe')
  RedstoneLampRecipe = Kee[str]('redstone_lamp_recipe')
  RedstoneRecipe = Kee[str]('redstone_recipe')
  RedstoneTorchRecipe = Kee[str]('redstone_torch_recipe')
  RemoteGetaway = Kee[str]('remote_getaway')
  RepeaterRecipe = Kee[str]('repeater_recipe')
  ResinBlockRecipe = Kee[str]('resin_block_recipe')
  ResinBrickRecipe = Kee[str]('resin_brick_recipe')
  ResinBrickSlabFromResinBricksStonecuttingRecipe = Kee[str](
    'resin_brick_slab_from_resin_bricks_stonecutting_recipe')
  ResinBrickSlabRecipe = Kee[str]('resin_brick_slab_recipe')
  ResinBrickStairsFromResinBricksStonecuttingRecipe = Kee[str](
    'resin_brick_stairs_from_resin_bricks_stonecutting_recipe')
  ResinBrickStairsRecipe = Kee[str]('resin_brick_stairs_recipe')
  ResinBrickWallFromResinBricksStonecuttingRecipe = Kee[str](
    'resin_brick_wall_from_resin_bricks_stonecutting_recipe')
  ResinBrickWallRecipe = Kee[str]('resin_brick_wall_recipe')
  ResinBricksRecipe = Kee[str]('resin_bricks_recipe')
  ResinClumpRecipe = Kee[str]('resin_clump_recipe')
  RespawnAnchorRecipe = Kee[str]('respawn_anchor_recipe')
  RespectingTheRemnants = Kee[str]('respecting_the_remnants')
  ReturnToSender = Kee[str]('return_to_sender')
  Revaulting = Kee[str]('revaulting')
  RibArmorTrimSmithingTemplateRecipe = Kee[str](
    'rib_armor_trim_smithing_template_recipe')
  RibArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'rib_armor_trim_smithing_template_smithing_trim_recipe')
  RootRecipe = Kee[str]('root_recipe')
  SaddleRecipe = Kee[str]('saddle_recipe')
  SandstoneRecipe = Kee[str]('sandstone_recipe')
  SandstoneSlabFromSandstoneStonecuttingRecipe = Kee[str](
    'sandstone_slab_from_sandstone_stonecutting_recipe')
  SandstoneSlabRecipe = Kee[str]('sandstone_slab_recipe')
  SandstoneStairsFromSandstoneStonecuttingRecipe = Kee[str](
    'sandstone_stairs_from_sandstone_stonecutting_recipe')
  SandstoneStairsRecipe = Kee[str]('sandstone_stairs_recipe')
  SandstoneWallFromSandstoneStonecuttingRecipe = Kee[str](
    'sandstone_wall_from_sandstone_stonecutting_recipe')
  SandstoneWallRecipe = Kee[str]('sandstone_wall_recipe')
  ScaffoldingRecipe = Kee[str]('scaffolding_recipe')
  SeaLanternRecipe = Kee[str]('sea_lantern_recipe')
  SentryArmorTrimSmithingTemplateRecipe = Kee[str](
    'sentry_armor_trim_smithing_template_recipe')
  SentryArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'sentry_armor_trim_smithing_template_smithing_trim_recipe')
  BreakDiamondHoe = Kee[str]('break_diamond_hoe')
  SeriousDedication = Kee[str]('serious_dedication')
  ShaperArmorTrimSmithingTemplateRecipe = Kee[str](
    'shaper_armor_trim_smithing_template_recipe')
  ShaperArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'shaper_armor_trim_smithing_template_smithing_trim_recipe')
  ShearBrilliance = Kee[str]('shear_brilliance')
  ShearsRecipe = Kee[str]('shears_recipe')
  ShieldRecipe = Kee[str]('shield_recipe')
  ShulkerBoxRecipe = Kee[str]('shulker_box_recipe')
  SignRecipe = Kee[str]('sign_recipe')
  SilenceArmorTrimSmithingTemplateRecipe = Kee[str](
    'silence_armor_trim_smithing_template_recipe')
  SilenceArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'silence_armor_trim_smithing_template_smithing_trim_recipe')
  SkullBannerPatternRecipe = Kee[str]('skull_banner_pattern_recipe')
  SkysTheLimit = Kee[str]('skys_the_limit')
  SlimeBallRecipe = Kee[str]('slime_ball_recipe')
  SlimeBlockRecipe = Kee[str]('slime_block_recipe')
  SmellsInteresting = Kee[str]('smells_interesting')
  SmithingTableRecipe = Kee[str]('smithing_table_recipe')
  SmithingWithStyle = Kee[str]('smithing_with_style')
  SmokerRecipe = Kee[str]('smoker_recipe')
  SmoothBasaltRecipe = Kee[str]('smooth_basalt_recipe')
  SmoothQuartzRecipe = Kee[str]('smooth_quartz_recipe')
  SmoothQuartzSlabFromSmoothQuartzStonecuttingRecipe = Kee[str](
    'smooth_quartz_slab_from_smooth_quartz_stonecutting_recipe')
  SmoothQuartzSlabRecipe = Kee[str]('smooth_quartz_slab_recipe')
  SmoothQuartzStairsFromSmoothQuartzStonecuttingRecipe = Kee[str](
    'smooth_quartz_stairs_from_smooth_quartz_stonecutting_recipe')
  SmoothQuartzStairsRecipe = Kee[str]('smooth_quartz_stairs_recipe')
  SmoothRedSandstoneRecipe = Kee[str]('smooth_red_sandstone_recipe')
  SmoothRedSandstoneSlabFromSmoothRedSandstoneStonecuttingRecipe = Kee[str](
    'smooth_red_sandstone_slab_from_smooth_red_sandstone_stonecutting_recipe')
  SmoothRedSandstoneSlabRecipe = Kee[str]('smooth_red_sandstone_slab_recipe')
  SmoothRedSandstoneStairsFromSmoothRedSandstoneStonecuttingRecipe = Kee[str](
    'smooth_red_sandstone_stairs_from_smooth_red_sandstone_stonecutting_recipe')
  SmoothRedSandstoneStairsRecipe = Kee[str](
    'smooth_red_sandstone_stairs_recipe')
  SmoothSandstoneRecipe = Kee[str]('smooth_sandstone_recipe')
  SmoothSandstoneSlabFromSmoothSandstoneStonecuttingRecipe = Kee[str](
    'smooth_sandstone_slab_from_smooth_sandstone_stonecutting_recipe')
  SmoothSandstoneSlabRecipe = Kee[str]('smooth_sandstone_slab_recipe')
  SmoothSandstoneStairsFromSmoothSandstoneStonecuttingRecipe = Kee[str](
    'smooth_sandstone_stairs_from_smooth_sandstone_stonecutting_recipe')
  SmoothSandstoneStairsRecipe = Kee[str]('smooth_sandstone_stairs_recipe')
  SmoothStoneRecipe = Kee[str]('smooth_stone_recipe')
  SmoothStoneSlabFromSmoothStoneStonecuttingRecipe = Kee[str](
    'smooth_stone_slab_from_smooth_stone_stonecutting_recipe')
  SmoothStoneSlabRecipe = Kee[str]('smooth_stone_slab_recipe')
  Sneak100 = Kee[str]('sneak_100')
  SniperDuel = Kee[str]('sniper_duel')
  SnoutArmorTrimSmithingTemplateRecipe = Kee[str](
    'snout_armor_trim_smithing_template_recipe')
  SnoutArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'snout_armor_trim_smithing_template_smithing_trim_recipe')
  SnowBlockRecipe = Kee[str]('snow_block_recipe')
  SnowRecipe = Kee[str]('snow_recipe')
  SoulCampfireRecipe = Kee[str]('soul_campfire_recipe')
  SoulLanternRecipe = Kee[str]('soul_lantern_recipe')
  SoulTorchRecipe = Kee[str]('soul_torch_recipe')
  SoundOfMusic = Kee[str]('sound_of_music')
  SpectralArrowRecipe = Kee[str]('spectral_arrow_recipe')
  SpireArmorTrimSmithingTemplateRecipe = Kee[str](
    'spire_armor_trim_smithing_template_recipe')
  SpireArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'spire_armor_trim_smithing_template_smithing_trim_recipe')
  SpongeRecipe = Kee[str]('sponge_recipe')
  SpookyScarySkeleton = Kee[str]('spooky_scary_skeleton')
  SpruceBoatRecipe = Kee[str]('spruce_boat_recipe')
  SpruceButtonRecipe = Kee[str]('spruce_button_recipe')
  SpruceChestBoatRecipe = Kee[str]('spruce_chest_boat_recipe')
  SpruceDoorRecipe = Kee[str]('spruce_door_recipe')
  SpruceFenceGateRecipe = Kee[str]('spruce_fence_gate_recipe')
  SpruceFenceRecipe = Kee[str]('spruce_fence_recipe')
  SpruceHangingSignRecipe = Kee[str]('spruce_hanging_sign_recipe')
  SprucePlanksRecipe = Kee[str]('spruce_planks_recipe')
  SprucePressurePlateRecipe = Kee[str]('spruce_pressure_plate_recipe')
  SpruceShelfRecipe = Kee[str]('spruce_shelf_recipe')
  SpruceSignRecipe = Kee[str]('spruce_sign_recipe')
  SpruceSlabRecipe = Kee[str]('spruce_slab_recipe')
  SpruceStairsRecipe = Kee[str]('spruce_stairs_recipe')
  SpruceTrapdoorRecipe = Kee[str]('spruce_trapdoor_recipe')
  SpruceWoodRecipe = Kee[str]('spruce_wood_recipe')
  SpyglassRecipe = Kee[str]('spyglass_recipe')
  StarTrader = Kee[str]('star_trader')
  StayHydrated = Kee[str]('stay_hydrated')
  StickFromBambooItemRecipe = Kee[str]('stick_from_bamboo_item_recipe')
  StickRecipe = Kee[str]('stick_recipe')
  StickyPistonRecipe = Kee[str]('sticky_piston_recipe')
  StickySituation = Kee[str]('sticky_situation')
  StoneAge = Kee[str]('stone_age')
  StoneAxeRecipe = Kee[str]('stone_axe_recipe')
  StoneBrickSlabFromStoneBricksStonecuttingRecipe = Kee[str](
    'stone_brick_slab_from_stone_bricks_stonecutting_recipe')
  StoneBrickSlabFromStoneStonecuttingRecipe = Kee[str](
    'stone_brick_slab_from_stone_stonecutting_recipe')
  StoneBrickSlabRecipe = Kee[str]('stone_brick_slab_recipe')
  StoneBrickStairsFromStoneBricksStonecuttingRecipe = Kee[str](
    'stone_brick_stairs_from_stone_bricks_stonecutting_recipe')
  StoneBrickStairsFromStoneStonecuttingRecipe = Kee[str](
    'stone_brick_stairs_from_stone_stonecutting_recipe')
  StoneBrickStairsRecipe = Kee[str]('stone_brick_stairs_recipe')
  StoneBrickWallFromStoneBricksStonecuttingRecipe = Kee[str](
    'stone_brick_wall_from_stone_bricks_stonecutting_recipe')
  StoneBrickWallFromStoneStonecuttingRecipe = Kee[str](
    'stone_brick_wall_from_stone_stonecutting_recipe')
  StoneBrickWallRecipe = Kee[str]('stone_brick_wall_recipe')
  StoneBricksFromStoneStonecuttingRecipe = Kee[str](
    'stone_bricks_from_stone_stonecutting_recipe')
  StoneBricksRecipe = Kee[str]('stone_bricks_recipe')
  StoneButtonRecipe = Kee[str]('stone_button_recipe')
  StoneHoeRecipe = Kee[str]('stone_hoe_recipe')
  StonePickaxeRecipe = Kee[str]('stone_pickaxe_recipe')
  StonePressurePlateRecipe = Kee[str]('stone_pressure_plate_recipe')
  StoneRecipe = Kee[str]('stone_recipe')
  StoneShovelRecipe = Kee[str]('stone_shovel_recipe')
  StoneSlabFromStoneStonecuttingRecipe = Kee[str](
    'stone_slab_from_stone_stonecutting_recipe')
  StoneSlabRecipe = Kee[str]('stone_slab_recipe')
  StoneSpearRecipe = Kee[str]('stone_spear_recipe')
  StoneStairsFromStoneStonecuttingRecipe = Kee[str](
    'stone_stairs_from_stone_stonecutting_recipe')
  StoneStairsRecipe = Kee[str]('stone_stairs_recipe')
  StoneSwordRecipe = Kee[str]('stone_sword_recipe')
  StonecutterRecipe = Kee[str]('stonecutter_recipe')
  StoryRoot = Kee[str]('story_root')
  StrawBedRecipe = Kee[str]('straw_bed_recipe')
  StrippedAcaciaWoodRecipe = Kee[str]('stripped_acacia_wood_recipe')
  StrippedBirchWoodRecipe = Kee[str]('stripped_birch_wood_recipe')
  StrippedCherryWoodRecipe = Kee[str]('stripped_cherry_wood_recipe')
  StrippedCrimsonHyphaeRecipe = Kee[str]('stripped_crimson_hyphae_recipe')
  StrippedDarkOakWoodRecipe = Kee[str]('stripped_dark_oak_wood_recipe')
  StrippedJungleWoodRecipe = Kee[str]('stripped_jungle_wood_recipe')
  StrippedMangroveWoodRecipe = Kee[str]('stripped_mangrove_wood_recipe')
  StrippedOakWoodRecipe = Kee[str]('stripped_oak_wood_recipe')
  StrippedPaleOakWoodRecipe = Kee[str]('stripped_pale_oak_wood_recipe')
  StrippedPoplarWoodRecipe = Kee[str]('stripped_poplar_wood_recipe')
  StrippedSpruceWoodRecipe = Kee[str]('stripped_spruce_wood_recipe')
  StrippedWarpedHyphaeRecipe = Kee[str]('stripped_warped_hyphae_recipe')
  SubspaceBubble = Kee[str]('subspace_bubble')
  SugarFromHoneyBottleRecipe = Kee[str]('sugar_from_honey_bottle_recipe')
  SugarFromSugarCaneRecipe = Kee[str]('sugar_from_sugar_cane_recipe')
  SuitUp = Kee[str]('suit_up')
  SulfurBrickSlabFromPolishedSulfurStonecuttingRecipe = Kee[str](
    'sulfur_brick_slab_from_polished_sulfur_stonecutting_recipe')
  SulfurBrickSlabFromSulfurBricksStonecuttingRecipe = Kee[str](
    'sulfur_brick_slab_from_sulfur_bricks_stonecutting_recipe')
  SulfurBrickSlabFromSulfurStonecuttingRecipe = Kee[str](
    'sulfur_brick_slab_from_sulfur_stonecutting_recipe')
  SulfurBrickSlabRecipe = Kee[str]('sulfur_brick_slab_recipe')
  SulfurBrickStairsFromPolishedSulfurStonecuttingRecipe = Kee[str](
    'sulfur_brick_stairs_from_polished_sulfur_stonecutting_recipe')
  SulfurBrickStairsFromSulfurBricksStonecuttingRecipe = Kee[str](
    'sulfur_brick_stairs_from_sulfur_bricks_stonecutting_recipe')
  SulfurBrickStairsFromSulfurStonecuttingRecipe = Kee[str](
    'sulfur_brick_stairs_from_sulfur_stonecutting_recipe')
  SulfurBrickStairsRecipe = Kee[str]('sulfur_brick_stairs_recipe')
  SulfurBrickWallFromPolishedSulfurStonecuttingRecipe = Kee[str](
    'sulfur_brick_wall_from_polished_sulfur_stonecutting_recipe')
  SulfurBrickWallFromSulfurBricksStonecuttingRecipe = Kee[str](
    'sulfur_brick_wall_from_sulfur_bricks_stonecutting_recipe')
  SulfurBrickWallFromSulfurStonecuttingRecipe = Kee[str](
    'sulfur_brick_wall_from_sulfur_stonecutting_recipe')
  SulfurBrickWallRecipe = Kee[str]('sulfur_brick_wall_recipe')
  SulfurBricksFromPolishedSulfurStonecuttingRecipe = Kee[str](
    'sulfur_bricks_from_polished_sulfur_stonecutting_recipe')
  SulfurBricksFromSulfurStonecuttingRecipe = Kee[str](
    'sulfur_bricks_from_sulfur_stonecutting_recipe')
  SulfurBricksRecipe = Kee[str]('sulfur_bricks_recipe')
  SulfurFromSulfurSpikesRecipe = Kee[str]('sulfur_from_sulfur_spikes_recipe')
  SulfurSlabFromSulfurStonecuttingRecipe = Kee[str](
    'sulfur_slab_from_sulfur_stonecutting_recipe')
  SulfurSlabRecipe = Kee[str]('sulfur_slab_recipe')
  SulfurStairsFromSulfurStonecuttingRecipe = Kee[str](
    'sulfur_stairs_from_sulfur_stonecutting_recipe')
  SulfurStairsRecipe = Kee[str]('sulfur_stairs_recipe')
  SulfurWallFromSulfurStonecuttingRecipe = Kee[str](
    'sulfur_wall_from_sulfur_stonecutting_recipe')
  SulfurWallRecipe = Kee[str]('sulfur_wall_recipe')
  SurgeProtector = Kee[str]('surge_protector')
  SuspiciousStewFromAlliumRecipe = Kee[str](
    'suspicious_stew_from_allium_recipe')
  SuspiciousStewFromAzureBluetRecipe = Kee[str](
    'suspicious_stew_from_azure_bluet_recipe')
  SuspiciousStewFromBlueOrchidRecipe = Kee[str](
    'suspicious_stew_from_blue_orchid_recipe')
  SuspiciousStewFromClosedEyeblossomRecipe = Kee[str](
    'suspicious_stew_from_closed_eyeblossom_recipe')
  SuspiciousStewFromCornflowerRecipe = Kee[str](
    'suspicious_stew_from_cornflower_recipe')
  SuspiciousStewFromDandelionRecipe = Kee[str](
    'suspicious_stew_from_dandelion_recipe')
  SuspiciousStewFromGoldenDandelionRecipe = Kee[str](
    'suspicious_stew_from_golden_dandelion_recipe')
  SuspiciousStewFromLilyOfTheValleyRecipe = Kee[str](
    'suspicious_stew_from_lily_of_the_valley_recipe')
  SuspiciousStewFromOpenEyeblossomRecipe = Kee[str](
    'suspicious_stew_from_open_eyeblossom_recipe')
  SuspiciousStewFromOrangeTulipRecipe = Kee[str](
    'suspicious_stew_from_orange_tulip_recipe')
  SuspiciousStewFromOxeyeDaisyRecipe = Kee[str](
    'suspicious_stew_from_oxeye_daisy_recipe')
  SuspiciousStewFromPinkTulipRecipe = Kee[str](
    'suspicious_stew_from_pink_tulip_recipe')
  SuspiciousStewFromPoppyRecipe = Kee[str]('suspicious_stew_from_poppy_recipe')
  SuspiciousStewFromRedTulipRecipe = Kee[str](
    'suspicious_stew_from_red_tulip_recipe')
  SuspiciousStewFromTorchflowerRecipe = Kee[str](
    'suspicious_stew_from_torchflower_recipe')
  SuspiciousStewFromWhiteTulipRecipe = Kee[str](
    'suspicious_stew_from_white_tulip_recipe')
  SuspiciousStewFromWitherRoseRecipe = Kee[str](
    'suspicious_stew_from_wither_rose_recipe')
  SweetDreams = Kee[str]('sweet_dreams')
  TacticalFishing = Kee[str]('tactical_fishing')
  TakeAim = Kee[str]('take_aim')
  TargetRecipe = Kee[str]('target_recipe')
  TerracottaRecipe = Kee[str]('terracotta_recipe')
  TheCityAtTheEndOfTheGame = Kee[str]('the_city_at_the_end_of_the_game')
  TheCutestPredator = Kee[str]('the_cutest_predator')
  TheEnd = Kee[str]('the_end')
  TheEndAgain = Kee[str]('the_end_again')
  TheHealingPowerOfFriendship = Kee[str]('the_healing_power_of_friendship')
  TheNextGeneration = Kee[str]('the_next_generation')
  TheParrotsAndTheBats = Kee[str]('the_parrots_and_the_bats')
  ThePowerOfBooks = Kee[str]('the_power_of_books')
  TheWholePack = Kee[str]('the_whole_pack')
  ThisBoatHasLegs = Kee[str]('this_boat_has_legs')
  ThoseWereTheDays = Kee[str]('those_were_the_days')
  TideArmorTrimSmithingTemplateRecipe = Kee[str](
    'tide_armor_trim_smithing_template_recipe')
  TideArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'tide_armor_trim_smithing_template_smithing_trim_recipe')
  TintedGlassRecipe = Kee[str]('tinted_glass_recipe')
  TippedArrowRecipe = Kee[str]('tipped_arrow_recipe')
  TntMinecartRecipe = Kee[str]('tnt_minecart_recipe')
  TntRecipe = Kee[str]('tnt_recipe')
  TorchRecipe = Kee[str]('torch_recipe')
  TotalBeelocation = Kee[str]('total_beelocation')
  TrappedChestRecipe = Kee[str]('trapped_chest_recipe')
  TripwireHookRecipe = Kee[str]('tripwire_hook_recipe')
  TuffBrickSlabFromPolishedTuffStonecuttingRecipe = Kee[str](
    'tuff_brick_slab_from_polished_tuff_stonecutting_recipe')
  TuffBrickSlabFromTuffBricksStonecuttingRecipe = Kee[str](
    'tuff_brick_slab_from_tuff_bricks_stonecutting_recipe')
  TuffBrickSlabFromTuffStonecuttingRecipe = Kee[str](
    'tuff_brick_slab_from_tuff_stonecutting_recipe')
  TuffBrickSlabRecipe = Kee[str]('tuff_brick_slab_recipe')
  TuffBrickStairsFromPolishedTuffStonecuttingRecipe = Kee[str](
    'tuff_brick_stairs_from_polished_tuff_stonecutting_recipe')
  TuffBrickStairsFromTuffBricksStonecuttingRecipe = Kee[str](
    'tuff_brick_stairs_from_tuff_bricks_stonecutting_recipe')
  TuffBrickStairsFromTuffStonecuttingRecipe = Kee[str](
    'tuff_brick_stairs_from_tuff_stonecutting_recipe')
  TuffBrickStairsRecipe = Kee[str]('tuff_brick_stairs_recipe')
  TuffBrickWallFromPolishedTuffStonecuttingRecipe = Kee[str](
    'tuff_brick_wall_from_polished_tuff_stonecutting_recipe')
  TuffBrickWallFromTuffBricksStonecuttingRecipe = Kee[str](
    'tuff_brick_wall_from_tuff_bricks_stonecutting_recipe')
  TuffBrickWallFromTuffStonecuttingRecipe = Kee[str](
    'tuff_brick_wall_from_tuff_stonecutting_recipe')
  TuffBrickWallRecipe = Kee[str]('tuff_brick_wall_recipe')
  TuffBricksFromPolishedTuffStonecuttingRecipe = Kee[str](
    'tuff_bricks_from_polished_tuff_stonecutting_recipe')
  TuffBricksFromTuffStonecuttingRecipe = Kee[str](
    'tuff_bricks_from_tuff_stonecutting_recipe')
  TuffBricksRecipe = Kee[str]('tuff_bricks_recipe')
  TuffSlabFromTuffStonecuttingRecipe = Kee[str](
    'tuff_slab_from_tuff_stonecutting_recipe')
  TuffSlabRecipe = Kee[str]('tuff_slab_recipe')
  TuffStairsFromTuffStonecuttingRecipe = Kee[str](
    'tuff_stairs_from_tuff_stonecutting_recipe')
  TuffStairsRecipe = Kee[str]('tuff_stairs_recipe')
  TuffWallFromTuffStonecuttingRecipe = Kee[str](
    'tuff_wall_from_tuff_stonecutting_recipe')
  TuffWallRecipe = Kee[str]('tuff_wall_recipe')
  TurtleHelmetRecipe = Kee[str]('turtle_helmet_recipe')
  TwoBirdsOneArrow = Kee[str]('two_birds_one_arrow')
  TwoByTwo = Kee[str]('two_by_two')
  UhOh = Kee[str]('uh_oh')
  UnderLockAndKey = Kee[str]('under_lock_and_key')
  UneasyAlliance = Kee[str]('uneasy_alliance')
  VeryVeryFrightening = Kee[str]('very_very_frightening')
  VexArmorTrimSmithingTemplateRecipe = Kee[str](
    'vex_armor_trim_smithing_template_recipe')
  VexArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'vex_armor_trim_smithing_template_smithing_trim_recipe')
  VoluntaryExile = Kee[str]('voluntary_exile')
  WarPigs = Kee[str]('war_pigs')
  WardArmorTrimSmithingTemplateRecipe = Kee[str](
    'ward_armor_trim_smithing_template_recipe')
  WardArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'ward_armor_trim_smithing_template_smithing_trim_recipe')
  WarpedButtonRecipe = Kee[str]('warped_button_recipe')
  WarpedDoorRecipe = Kee[str]('warped_door_recipe')
  WarpedFenceGateRecipe = Kee[str]('warped_fence_gate_recipe')
  WarpedFenceRecipe = Kee[str]('warped_fence_recipe')
  WarpedFungusOnAStickRecipe = Kee[str]('warped_fungus_on_a_stick_recipe')
  WarpedHangingSignRecipe = Kee[str]('warped_hanging_sign_recipe')
  WarpedHyphaeRecipe = Kee[str]('warped_hyphae_recipe')
  WarpedPlanksRecipe = Kee[str]('warped_planks_recipe')
  WarpedPressurePlateRecipe = Kee[str]('warped_pressure_plate_recipe')
  WarpedShelfRecipe = Kee[str]('warped_shelf_recipe')
  WarpedSignRecipe = Kee[str]('warped_sign_recipe')
  WarpedSlabRecipe = Kee[str]('warped_slab_recipe')
  WarpedStairsRecipe = Kee[str]('warped_stairs_recipe')
  WarpedTrapdoorRecipe = Kee[str]('warped_trapdoor_recipe')
  WaxOff = Kee[str]('wax_off')
  WaxOn = Kee[str]('wax_on')
  WaxedChiseledCopperFromHoneycombRecipe = Kee[str](
    'waxed_chiseled_copper_from_honeycomb_recipe')
  WaxedChiseledCopperFromWaxedCopperBlockStonecuttingRecipe = Kee[str](
    'waxed_chiseled_copper_from_waxed_copper_block_stonecutting_recipe')
  WaxedChiseledCopperFromWaxedCutCopperStonecuttingRecipe = Kee[str](
    'waxed_chiseled_copper_from_waxed_cut_copper_stonecutting_recipe')
  WaxedChiseledCopperRecipe = Kee[str]('waxed_chiseled_copper_recipe')
  WaxedCopperBarsFromHoneycombRecipe = Kee[str](
    'waxed_copper_bars_from_honeycomb_recipe')
  WaxedCopperBlockFromHoneycombRecipe = Kee[str](
    'waxed_copper_block_from_honeycomb_recipe')
  WaxedCopperBulbFromHoneycombRecipe = Kee[str](
    'waxed_copper_bulb_from_honeycomb_recipe')
  WaxedCopperBulbRecipe = Kee[str]('waxed_copper_bulb_recipe')
  WaxedCopperChainFromHoneycombRecipe = Kee[str](
    'waxed_copper_chain_from_honeycomb_recipe')
  WaxedCopperChestFromHoneycombRecipe = Kee[str](
    'waxed_copper_chest_from_honeycomb_recipe')
  WaxedCopperDoorFromHoneycombRecipe = Kee[str](
    'waxed_copper_door_from_honeycomb_recipe')
  WaxedCopperGolemStatueFromHoneycombRecipe = Kee[str](
    'waxed_copper_golem_statue_from_honeycomb_recipe')
  WaxedCopperGrateFromHoneycombRecipe = Kee[str](
    'waxed_copper_grate_from_honeycomb_recipe')
  WaxedCopperGrateFromWaxedCopperBlockStonecuttingRecipe = Kee[str](
    'waxed_copper_grate_from_waxed_copper_block_stonecutting_recipe')
  WaxedCopperGrateRecipe = Kee[str]('waxed_copper_grate_recipe')
  WaxedCopperLanternFromHoneycombRecipe = Kee[str](
    'waxed_copper_lantern_from_honeycomb_recipe')
  WaxedCopperTrapdoorFromHoneycombRecipe = Kee[str](
    'waxed_copper_trapdoor_from_honeycomb_recipe')
  WaxedCutCopperFromHoneycombRecipe = Kee[str](
    'waxed_cut_copper_from_honeycomb_recipe')
  WaxedCutCopperFromWaxedCopperBlockStonecuttingRecipe = Kee[str](
    'waxed_cut_copper_from_waxed_copper_block_stonecutting_recipe')
  WaxedCutCopperRecipe = Kee[str]('waxed_cut_copper_recipe')
  WaxedCutCopperSlabFromHoneycombRecipe = Kee[str](
    'waxed_cut_copper_slab_from_honeycomb_recipe')
  WaxedCutCopperSlabFromWaxedCopperBlockStonecuttingRecipe = Kee[str](
    'waxed_cut_copper_slab_from_waxed_copper_block_stonecutting_recipe')
  WaxedCutCopperSlabFromWaxedCutCopperStonecuttingRecipe = Kee[str](
    'waxed_cut_copper_slab_from_waxed_cut_copper_stonecutting_recipe')
  WaxedCutCopperSlabRecipe = Kee[str]('waxed_cut_copper_slab_recipe')
  WaxedCutCopperStairsFromHoneycombRecipe = Kee[str](
    'waxed_cut_copper_stairs_from_honeycomb_recipe')
  WaxedCutCopperStairsFromWaxedCopperBlockStonecuttingRecipe = Kee[str](
    'waxed_cut_copper_stairs_from_waxed_copper_block_stonecutting_recipe')
  WaxedCutCopperStairsFromWaxedCutCopperStonecuttingRecipe = Kee[str](
    'waxed_cut_copper_stairs_from_waxed_cut_copper_stonecutting_recipe')
  WaxedCutCopperStairsRecipe = Kee[str]('waxed_cut_copper_stairs_recipe')
  WaxedExposedChiseledCopperFromHoneycombRecipe = Kee[str](
    'waxed_exposed_chiseled_copper_from_honeycomb_recipe')
  WaxedExposedChiseledCopperFromWaxedExposedCopperStonecuttingRecipe = Kee[str](
    'waxed_exposed_chiseled_copper_from_waxed_exposed_copper_stonecutting_recipe')
  WaxedExposedChiseledCopperFromWaxedExposedCutCopperStonecuttingRecipe = Kee[str](
    'waxed_exposed_chiseled_copper_from_waxed_exposed_cut_copper_stonecutting_recipe')
  WaxedExposedChiseledCopperRecipe = Kee[str](
    'waxed_exposed_chiseled_copper_recipe')
  WaxedExposedCopperBarsFromHoneycombRecipe = Kee[str](
    'waxed_exposed_copper_bars_from_honeycomb_recipe')
  WaxedExposedCopperBulbFromHoneycombRecipe = Kee[str](
    'waxed_exposed_copper_bulb_from_honeycomb_recipe')
  WaxedExposedCopperBulbRecipe = Kee[str]('waxed_exposed_copper_bulb_recipe')
  WaxedExposedCopperChainFromHoneycombRecipe = Kee[str](
    'waxed_exposed_copper_chain_from_honeycomb_recipe')
  WaxedExposedCopperChestFromHoneycombRecipe = Kee[str](
    'waxed_exposed_copper_chest_from_honeycomb_recipe')
  WaxedExposedCopperDoorFromHoneycombRecipe = Kee[str](
    'waxed_exposed_copper_door_from_honeycomb_recipe')
  WaxedExposedCopperFromHoneycombRecipe = Kee[str](
    'waxed_exposed_copper_from_honeycomb_recipe')
  WaxedExposedCopperGolemStatueFromHoneycombRecipe = Kee[str](
    'waxed_exposed_copper_golem_statue_from_honeycomb_recipe')
  WaxedExposedCopperGrateFromHoneycombRecipe = Kee[str](
    'waxed_exposed_copper_grate_from_honeycomb_recipe')
  WaxedExposedCopperGrateFromWaxedExposedCopperStonecuttingRecipe = Kee[str](
    'waxed_exposed_copper_grate_from_waxed_exposed_copper_stonecutting_recipe')
  WaxedExposedCopperGrateRecipe = Kee[str]('waxed_exposed_copper_grate_recipe')
  WaxedExposedCopperLanternFromHoneycombRecipe = Kee[str](
    'waxed_exposed_copper_lantern_from_honeycomb_recipe')
  WaxedExposedCopperTrapdoorFromHoneycombRecipe = Kee[str](
    'waxed_exposed_copper_trapdoor_from_honeycomb_recipe')
  WaxedExposedCutCopperFromHoneycombRecipe = Kee[str](
    'waxed_exposed_cut_copper_from_honeycomb_recipe')
  WaxedExposedCutCopperFromWaxedExposedCopperStonecuttingRecipe = Kee[str](
    'waxed_exposed_cut_copper_from_waxed_exposed_copper_stonecutting_recipe')
  WaxedExposedCutCopperRecipe = Kee[str]('waxed_exposed_cut_copper_recipe')
  WaxedExposedCutCopperSlabFromHoneycombRecipe = Kee[str](
    'waxed_exposed_cut_copper_slab_from_honeycomb_recipe')
  WaxedExposedCutCopperSlabFromWaxedExposedCopperStonecuttingRecipe = Kee[str](
    'waxed_exposed_cut_copper_slab_from_waxed_exposed_copper_stonecutting_recipe')
  WaxedExposedCutCopperSlabFromWaxedExposedCutCopperStonecuttingRecipe = Kee[str](
    'waxed_exposed_cut_copper_slab_from_waxed_exposed_cut_copper_stonecutting_recipe')
  WaxedExposedCutCopperSlabRecipe = Kee[str](
    'waxed_exposed_cut_copper_slab_recipe')
  WaxedExposedCutCopperStairsFromHoneycombRecipe = Kee[str](
    'waxed_exposed_cut_copper_stairs_from_honeycomb_recipe')
  WaxedExposedCutCopperStairsFromWaxedExposedCopperStonecuttingRecipe = Kee[str](
    'waxed_exposed_cut_copper_stairs_from_waxed_exposed_copper_stonecutting_recipe')
  WaxedExposedCutCopperStairsFromWaxedExposedCutCopperStonecuttingRecipe = Kee[str](
    'waxed_exposed_cut_copper_stairs_from_waxed_exposed_cut_copper_stonecutting_recipe')
  WaxedExposedCutCopperStairsRecipe = Kee[str](
    'waxed_exposed_cut_copper_stairs_recipe')
  WaxedExposedLightningRodFromHoneycombRecipe = Kee[str](
    'waxed_exposed_lightning_rod_from_honeycomb_recipe')
  WaxedLightningRodFromHoneycombRecipe = Kee[str](
    'waxed_lightning_rod_from_honeycomb_recipe')
  WaxedOxidizedChiseledCopperFromHoneycombRecipe = Kee[str](
    'waxed_oxidized_chiseled_copper_from_honeycomb_recipe')
  WaxedOxidizedChiseledCopperFromWaxedOxidizedCopperStonecuttingRecipe = Kee[str](
    'waxed_oxidized_chiseled_copper_from_waxed_oxidized_copper_stonecutting_recipe')
  WaxedOxidizedChiseledCopperFromWaxedOxidizedCutCopperStonecuttingRecipe = Kee[str](
    'waxed_oxidized_chiseled_copper_from_waxed_oxidized_cut_copper_stonecutting_recipe')
  WaxedOxidizedChiseledCopperRecipe = Kee[str](
    'waxed_oxidized_chiseled_copper_recipe')
  WaxedOxidizedCopperBarsFromHoneycombRecipe = Kee[str](
    'waxed_oxidized_copper_bars_from_honeycomb_recipe')
  WaxedOxidizedCopperBulbFromHoneycombRecipe = Kee[str](
    'waxed_oxidized_copper_bulb_from_honeycomb_recipe')
  WaxedOxidizedCopperBulbRecipe = Kee[str]('waxed_oxidized_copper_bulb_recipe')
  WaxedOxidizedCopperChainFromHoneycombRecipe = Kee[str](
    'waxed_oxidized_copper_chain_from_honeycomb_recipe')
  WaxedOxidizedCopperChestFromHoneycombRecipe = Kee[str](
    'waxed_oxidized_copper_chest_from_honeycomb_recipe')
  WaxedOxidizedCopperDoorFromHoneycombRecipe = Kee[str](
    'waxed_oxidized_copper_door_from_honeycomb_recipe')
  WaxedOxidizedCopperFromHoneycombRecipe = Kee[str](
    'waxed_oxidized_copper_from_honeycomb_recipe')
  WaxedOxidizedCopperGolemStatueFromHoneycombRecipe = Kee[str](
    'waxed_oxidized_copper_golem_statue_from_honeycomb_recipe')
  WaxedOxidizedCopperGrateFromHoneycombRecipe = Kee[str](
    'waxed_oxidized_copper_grate_from_honeycomb_recipe')
  WaxedOxidizedCopperGrateFromWaxedOxidizedCopperStonecuttingRecipe = Kee[str](
    'waxed_oxidized_copper_grate_from_waxed_oxidized_copper_stonecutting_recipe')
  WaxedOxidizedCopperGrateRecipe = Kee[str](
    'waxed_oxidized_copper_grate_recipe')
  WaxedOxidizedCopperLanternFromHoneycombRecipe = Kee[str](
    'waxed_oxidized_copper_lantern_from_honeycomb_recipe')
  WaxedOxidizedCopperTrapdoorFromHoneycombRecipe = Kee[str](
    'waxed_oxidized_copper_trapdoor_from_honeycomb_recipe')
  WaxedOxidizedCutCopperFromHoneycombRecipe = Kee[str](
    'waxed_oxidized_cut_copper_from_honeycomb_recipe')
  WaxedOxidizedCutCopperFromWaxedOxidizedCopperStonecuttingRecipe = Kee[str](
    'waxed_oxidized_cut_copper_from_waxed_oxidized_copper_stonecutting_recipe')
  WaxedOxidizedCutCopperRecipe = Kee[str]('waxed_oxidized_cut_copper_recipe')
  WaxedOxidizedCutCopperSlabFromHoneycombRecipe = Kee[str](
    'waxed_oxidized_cut_copper_slab_from_honeycomb_recipe')
  WaxedOxidizedCutCopperSlabFromWaxedOxidizedCopperStonecuttingRecipe = Kee[str](
    'waxed_oxidized_cut_copper_slab_from_waxed_oxidized_copper_stonecutting_recipe')
  WaxedOxidizedCutCopperSlabFromWaxedOxidizedCutCopperStonecuttingRecipe = Kee[str](
    'waxed_oxidized_cut_copper_slab_from_waxed_oxidized_cut_copper_stonecutting_recipe')
  WaxedOxidizedCutCopperSlabRecipe = Kee[str](
    'waxed_oxidized_cut_copper_slab_recipe')
  WaxedOxidizedCutCopperStairsFromHoneycombRecipe = Kee[str](
    'waxed_oxidized_cut_copper_stairs_from_honeycomb_recipe')
  WaxedOxidizedCutCopperStairsFromWaxedOxidizedCopperStonecuttingRecipe = Kee[str](
    'waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_copper_stonecutting_recipe')
  WaxedOxidizedCutCopperStairsFromWaxedOxidizedCutCopperStonecuttingRecipe = Kee[str](
    'waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_cut_copper_stonecutting_recipe')
  WaxedOxidizedCutCopperStairsRecipe = Kee[str](
    'waxed_oxidized_cut_copper_stairs_recipe')
  WaxedOxidizedLightningRodFromHoneycombRecipe = Kee[str](
    'waxed_oxidized_lightning_rod_from_honeycomb_recipe')
  WaxedWeatheredChiseledCopperFromHoneycombRecipe = Kee[str](
    'waxed_weathered_chiseled_copper_from_honeycomb_recipe')
  WaxedWeatheredChiseledCopperFromWaxedWeatheredCopperStonecuttingRecipe = Kee[str](
    'waxed_weathered_chiseled_copper_from_waxed_weathered_copper_stonecutting_recipe')
  WaxedWeatheredChiseledCopperFromWaxedWeatheredCutCopperStonecuttingRecipe = Kee[str](
    'waxed_weathered_chiseled_copper_from_waxed_weathered_cut_copper_stonecutting_recipe')
  WaxedWeatheredChiseledCopperRecipe = Kee[str](
    'waxed_weathered_chiseled_copper_recipe')
  WaxedWeatheredCopperBarsFromHoneycombRecipe = Kee[str](
    'waxed_weathered_copper_bars_from_honeycomb_recipe')
  WaxedWeatheredCopperBulbFromHoneycombRecipe = Kee[str](
    'waxed_weathered_copper_bulb_from_honeycomb_recipe')
  WaxedWeatheredCopperBulbRecipe = Kee[str](
    'waxed_weathered_copper_bulb_recipe')
  WaxedWeatheredCopperChainFromHoneycombRecipe = Kee[str](
    'waxed_weathered_copper_chain_from_honeycomb_recipe')
  WaxedWeatheredCopperChestFromHoneycombRecipe = Kee[str](
    'waxed_weathered_copper_chest_from_honeycomb_recipe')
  WaxedWeatheredCopperDoorFromHoneycombRecipe = Kee[str](
    'waxed_weathered_copper_door_from_honeycomb_recipe')
  WaxedWeatheredCopperFromHoneycombRecipe = Kee[str](
    'waxed_weathered_copper_from_honeycomb_recipe')
  WaxedWeatheredCopperGolemStatueFromHoneycombRecipe = Kee[str](
    'waxed_weathered_copper_golem_statue_from_honeycomb_recipe')
  WaxedWeatheredCopperGrateFromHoneycombRecipe = Kee[str](
    'waxed_weathered_copper_grate_from_honeycomb_recipe')
  WaxedWeatheredCopperGrateFromWaxedWeatheredCopperStonecuttingRecipe = Kee[str](
    'waxed_weathered_copper_grate_from_waxed_weathered_copper_stonecutting_recipe')
  WaxedWeatheredCopperGrateRecipe = Kee[str](
    'waxed_weathered_copper_grate_recipe')
  WaxedWeatheredCopperLanternFromHoneycombRecipe = Kee[str](
    'waxed_weathered_copper_lantern_from_honeycomb_recipe')
  WaxedWeatheredCopperTrapdoorFromHoneycombRecipe = Kee[str](
    'waxed_weathered_copper_trapdoor_from_honeycomb_recipe')
  WaxedWeatheredCutCopperFromHoneycombRecipe = Kee[str](
    'waxed_weathered_cut_copper_from_honeycomb_recipe')
  WaxedWeatheredCutCopperFromWaxedWeatheredCopperStonecuttingRecipe = Kee[str](
    'waxed_weathered_cut_copper_from_waxed_weathered_copper_stonecutting_recipe')
  WaxedWeatheredCutCopperRecipe = Kee[str]('waxed_weathered_cut_copper_recipe')
  WaxedWeatheredCutCopperSlabFromHoneycombRecipe = Kee[str](
    'waxed_weathered_cut_copper_slab_from_honeycomb_recipe')
  WaxedWeatheredCutCopperSlabFromWaxedWeatheredCopperStonecuttingRecipe = Kee[str](
    'waxed_weathered_cut_copper_slab_from_waxed_weathered_copper_stonecutting_recipe')
  WaxedWeatheredCutCopperSlabFromWaxedWeatheredCutCopperStonecuttingRecipe = Kee[str](
    'waxed_weathered_cut_copper_slab_from_waxed_weathered_cut_copper_stonecutting_recipe')
  WaxedWeatheredCutCopperSlabRecipe = Kee[str](
    'waxed_weathered_cut_copper_slab_recipe')
  WaxedWeatheredCutCopperStairsFromHoneycombRecipe = Kee[str](
    'waxed_weathered_cut_copper_stairs_from_honeycomb_recipe')
  WaxedWeatheredCutCopperStairsFromWaxedWeatheredCopperStonecuttingRecipe = Kee[str](
    'waxed_weathered_cut_copper_stairs_from_waxed_weathered_copper_stonecutting_recipe')
  WaxedWeatheredCutCopperStairsFromWaxedWeatheredCutCopperStonecuttingRecipe = Kee[str](
    'waxed_weathered_cut_copper_stairs_from_waxed_weathered_cut_copper_stonecutting_recipe')
  WaxedWeatheredCutCopperStairsRecipe = Kee[str](
    'waxed_weathered_cut_copper_stairs_recipe')
  WaxedWeatheredLightningRodFromHoneycombRecipe = Kee[str](
    'waxed_weathered_lightning_rod_from_honeycomb_recipe')
  WayfinderArmorTrimSmithingTemplateRecipe = Kee[str](
    'wayfinder_armor_trim_smithing_template_recipe')
  WayfinderArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'wayfinder_armor_trim_smithing_template_smithing_trim_recipe')
  WeNeedToGoDeeper = Kee[str]('we_need_to_go_deeper')
  WeatheredChiseledCopperFromWeatheredCopperStonecuttingRecipe = Kee[str](
    'weathered_chiseled_copper_from_weathered_copper_stonecutting_recipe')
  WeatheredChiseledCopperFromWeatheredCutCopperStonecuttingRecipe = Kee[str](
    'weathered_chiseled_copper_from_weathered_cut_copper_stonecutting_recipe')
  WeatheredChiseledCopperRecipe = Kee[str]('weathered_chiseled_copper_recipe')
  WeatheredCopperBulbRecipe = Kee[str]('weathered_copper_bulb_recipe')
  WeatheredCopperGrateFromWeatheredCopperStonecuttingRecipe = Kee[str](
    'weathered_copper_grate_from_weathered_copper_stonecutting_recipe')
  WeatheredCopperGrateRecipe = Kee[str]('weathered_copper_grate_recipe')
  WeatheredCutCopperFromWeatheredCopperStonecuttingRecipe = Kee[str](
    'weathered_cut_copper_from_weathered_copper_stonecutting_recipe')
  WeatheredCutCopperRecipe = Kee[str]('weathered_cut_copper_recipe')
  WeatheredCutCopperSlabFromWeatheredCopperStonecuttingRecipe = Kee[str](
    'weathered_cut_copper_slab_from_weathered_copper_stonecutting_recipe')
  WeatheredCutCopperSlabFromWeatheredCutCopperStonecuttingRecipe = Kee[str](
    'weathered_cut_copper_slab_from_weathered_cut_copper_stonecutting_recipe')
  WeatheredCutCopperSlabRecipe = Kee[str]('weathered_cut_copper_slab_recipe')
  WeatheredCutCopperStairsFromWeatheredCopperStonecuttingRecipe = Kee[str](
    'weathered_cut_copper_stairs_from_weathered_copper_stonecutting_recipe')
  WeatheredCutCopperStairsFromWeatheredCutCopperStonecuttingRecipe = Kee[str](
    'weathered_cut_copper_stairs_from_weathered_cut_copper_stonecutting_recipe')
  WeatheredCutCopperStairsRecipe = Kee[str](
    'weathered_cut_copper_stairs_recipe')
  WhatADeal = Kee[str]('what_a_deal')
  WhateverFloatsYourGoat = Kee[str]('whatever_floats_your_goat')
  WheatRecipe = Kee[str]('wheat_recipe')
  WhenTheSquadHopsIntoTown = Kee[str]('when_the_squad_hops_into_town')
  WhiteBannerRecipe = Kee[str]('white_banner_recipe')
  WhiteBedRecipe = Kee[str]('white_bed_recipe')
  WhiteBundleRecipe = Kee[str]('white_bundle_recipe')
  WhiteCandleRecipe = Kee[str]('white_candle_recipe')
  WhiteCarpetRecipe = Kee[str]('white_carpet_recipe')
  WhiteConcretePowderRecipe = Kee[str]('white_concrete_powder_recipe')
  WhiteConcreteSlabFromWhiteConcreteStonecuttingRecipe = Kee[str](
    'white_concrete_slab_from_white_concrete_stonecutting_recipe')
  WhiteConcreteSlabRecipe = Kee[str]('white_concrete_slab_recipe')
  WhiteConcreteStairsFromWhiteConcreteStonecuttingRecipe = Kee[str](
    'white_concrete_stairs_from_white_concrete_stonecutting_recipe')
  WhiteConcreteStairsRecipe = Kee[str]('white_concrete_stairs_recipe')
  WhiteCushionRecipe = Kee[str]('white_cushion_recipe')
  WhiteDyeFromLilyOfTheValleyRecipe = Kee[str](
    'white_dye_from_lily_of_the_valley_recipe')
  WhiteDyeRecipe = Kee[str]('white_dye_recipe')
  WhiteGlazedTerracottaRecipe = Kee[str]('white_glazed_terracotta_recipe')
  WhiteHarnessRecipe = Kee[str]('white_harness_recipe')
  WhiteShulkerBoxRecipe = Kee[str]('white_shulker_box_recipe')
  WhiteStainedGlassPaneFromGlassPaneRecipe = Kee[str](
    'white_stained_glass_pane_from_glass_pane_recipe')
  WhiteStainedGlassPaneRecipe = Kee[str]('white_stained_glass_pane_recipe')
  WhiteStainedGlassRecipe = Kee[str]('white_stained_glass_recipe')
  WhiteTerracottaRecipe = Kee[str]('white_terracotta_recipe')
  WhiteWoolFromStringRecipe = Kee[str]('white_wool_from_string_recipe')
  WhiteWoolSlabRecipe = Kee[str]('white_wool_slab_recipe')
  WhiteWoolStairsRecipe = Kee[str]('white_wool_stairs_recipe')
  WhoIsCuttingOnions = Kee[str]('who_is_cutting_onions')
  WhoNeedsRockets = Kee[str]('who_needs_rockets')
  WhosThePillagerNow = Kee[str]('whos_the_pillager_now')
  WildArmorTrimSmithingTemplateRecipe = Kee[str](
    'wild_armor_trim_smithing_template_recipe')
  WildArmorTrimSmithingTemplateSmithingTrimRecipe = Kee[str](
    'wild_armor_trim_smithing_template_smithing_trim_recipe')
  WindChargeRecipe = Kee[str]('wind_charge_recipe')
  WithOurPowersCombined = Kee[str]('with_our_powers_combined')
  WitheringHeights = Kee[str]('withering_heights')
  WolfArmorDyedRecipe = Kee[str]('wolf_armor_dyed_recipe')
  WolfArmorRecipe = Kee[str]('wolf_armor_recipe')
  WoodenAxeRecipe = Kee[str]('wooden_axe_recipe')
  WoodenHoeRecipe = Kee[str]('wooden_hoe_recipe')
  WoodenPickaxeRecipe = Kee[str]('wooden_pickaxe_recipe')
  WoodenShovelRecipe = Kee[str]('wooden_shovel_recipe')
  WoodenSpearRecipe = Kee[str]('wooden_spear_recipe')
  WoodenSwordRecipe = Kee[str]('wooden_sword_recipe')
  WritableBookRecipe = Kee[str]('writable_book_recipe')
  YellowBannerRecipe = Kee[str]('yellow_banner_recipe')
  YellowBedFromWhiteBedRecipe = Kee[str]('yellow_bed_from_white_bed_recipe')
  YellowBedRecipe = Kee[str]('yellow_bed_recipe')
  YellowBundleRecipe = Kee[str]('yellow_bundle_recipe')
  YellowCandleRecipe = Kee[str]('yellow_candle_recipe')
  YellowCarpetFromWhiteCarpetRecipe = Kee[str](
    'yellow_carpet_from_white_carpet_recipe')
  YellowCarpetRecipe = Kee[str]('yellow_carpet_recipe')
  YellowConcretePowderRecipe = Kee[str]('yellow_concrete_powder_recipe')
  YellowConcreteSlabFromYellowConcreteStonecuttingRecipe = Kee[str](
    'yellow_concrete_slab_from_yellow_concrete_stonecutting_recipe')
  YellowConcreteSlabRecipe = Kee[str]('yellow_concrete_slab_recipe')
  YellowConcreteStairsFromYellowConcreteStonecuttingRecipe = Kee[str](
    'yellow_concrete_stairs_from_yellow_concrete_stonecutting_recipe')
  YellowConcreteStairsRecipe = Kee[str]('yellow_concrete_stairs_recipe')
  YellowCushionRecipe = Kee[str]('yellow_cushion_recipe')
  YellowDyeFromDandelionRecipe = Kee[str]('yellow_dye_from_dandelion_recipe')
  YellowDyeFromGoldenDandelionRecipe = Kee[str](
    'yellow_dye_from_golden_dandelion_recipe')
  YellowDyeFromSunflowerRecipe = Kee[str]('yellow_dye_from_sunflower_recipe')
  YellowDyeFromWildflowersRecipe = Kee[str](
    'yellow_dye_from_wildflowers_recipe')
  YellowGlazedTerracottaRecipe = Kee[str]('yellow_glazed_terracotta_recipe')
  YellowHarnessRecipe = Kee[str]('yellow_harness_recipe')
  YellowShulkerBoxRecipe = Kee[str]('yellow_shulker_box_recipe')
  YellowStainedGlassPaneFromGlassPaneRecipe = Kee[str](
    'yellow_stained_glass_pane_from_glass_pane_recipe')
  YellowStainedGlassPaneRecipe = Kee[str]('yellow_stained_glass_pane_recipe')
  YellowStainedGlassRecipe = Kee[str]('yellow_stained_glass_recipe')
  YellowTerracottaRecipe = Kee[str]('yellow_terracotta_recipe')
  YellowWoolRecipe = Kee[str]('yellow_wool_recipe')
  YellowWoolSlabRecipe = Kee[str]('yellow_wool_slab_recipe')
  YellowWoolStairsRecipe = Kee[str]('yellow_wool_stairs_recipe')
  YouNeedAMint = Kee[str]('you_need_a_mint')
  YouveGotAFriendInMe = Kee[str]('youve_got_a_friend_in_me')
  ZombieDoctor = Kee[str]('zombie_doctor')
