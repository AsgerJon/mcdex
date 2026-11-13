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

    storyMineStone = MCAdvancements.STORY_MINE_STONE
    storyMineStone is MCAdvancements['story/mine_stone']  # True
    storyMineStone['1.12']
    # AdvancementId('story/mine_stone', 'minecraft:story/mine_stone')
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
  ADVENTURE_ADVENTURING_TIME = Kee[str]('adventure/adventuring_time')
  ADVENTURE_ARBALISTIC = Kee[str]('adventure/arbalistic')
  ADVENTURE_AVOID_VIBRATION = Kee[str]('adventure/avoid_vibration')
  ADVENTURE_BLOWBACK = Kee[str]('adventure/blowback')
  ADVENTURE_BRUSH_ARMADILLO = Kee[str]('adventure/brush_armadillo')
  ADVENTURE_BULLSEYE = Kee[str]('adventure/bullseye')
  ADVENTURE_CRAFT_DECORATED_POT_USING_ONLY_SHERDS = Kee[str](
    'adventure/craft_decorated_pot_using_only_sherds')
  ADVENTURE_CRAFTERS_CRAFTING_CRAFTERS = Kee[str](
    'adventure/crafters_crafting_crafters')
  ADVENTURE_FALL_FROM_WORLD_HEIGHT = Kee[str](
    'adventure/fall_from_world_height')
  ADVENTURE_HEART_TRANSPLANTER = Kee[str]('adventure/heart_transplanter')
  ADVENTURE_HERO_OF_THE_VILLAGE = Kee[str]('adventure/hero_of_the_village')
  ADVENTURE_HONEY_BLOCK_SLIDE = Kee[str]('adventure/honey_block_slide')
  ADVENTURE_KILL_A_MOB = Kee[str]('adventure/kill_a_mob')
  ADVENTURE_KILL_ALL_MOBS = Kee[str]('adventure/kill_all_mobs')
  ADVENTURE_KILL_MOB_NEAR_SCULK_CATALYST = Kee[str](
    'adventure/kill_mob_near_sculk_catalyst')
  ADVENTURE_LIGHTEN_UP = Kee[str]('adventure/lighten_up')
  ADVENTURE_LIGHTNING_ROD_WITH_VILLAGER_NO_FIRE = Kee[str](
    'adventure/lightning_rod_with_villager_no_fire')
  ADVENTURE_MINECRAFT_TRIALS_EDITION = Kee[str](
    'adventure/minecraft_trials_edition')
  ADVENTURE_OL_BETSY = Kee[str]('adventure/ol_betsy')
  ADVENTURE_OVEROVERKILL = Kee[str]('adventure/overoverkill')
  ADVENTURE_PLAY_JUKEBOX_IN_MEADOWS = Kee[str](
    'adventure/play_jukebox_in_meadows')
  ADVENTURE_READ_POWER_OF_CHISELED_BOOKSHELF = Kee[str](
    'adventure/read_power_of_chiseled_bookshelf')
  ADVENTURE_REVAULTING = Kee[str]('adventure/revaulting')
  ADVENTURE_ROOT = Kee[str]('adventure/root')
  ADVENTURE_SALVAGE_SHERD = Kee[str]('adventure/salvage_sherd')
  ADVENTURE_SHOOT_ARROW = Kee[str]('adventure/shoot_arrow')
  ADVENTURE_SLEEP_IN_BED = Kee[str]('adventure/sleep_in_bed')
  ADVENTURE_SNIPER_DUEL = Kee[str]('adventure/sniper_duel')
  ADVENTURE_SPEAR_MANY_MOBS = Kee[str]('adventure/spear_many_mobs')
  ADVENTURE_SPYGLASS_AT_DRAGON = Kee[str]('adventure/spyglass_at_dragon')
  ADVENTURE_SPYGLASS_AT_GHAST = Kee[str]('adventure/spyglass_at_ghast')
  ADVENTURE_SPYGLASS_AT_PARROT = Kee[str]('adventure/spyglass_at_parrot')
  ADVENTURE_SUMMON_IRON_GOLEM = Kee[str]('adventure/summon_iron_golem')
  ADVENTURE_THROW_TRIDENT = Kee[str]('adventure/throw_trident')
  ADVENTURE_TOTEM_OF_UNDYING = Kee[str]('adventure/totem_of_undying')
  ADVENTURE_TRADE = Kee[str]('adventure/trade')
  ADVENTURE_TRADE_AT_WORLD_HEIGHT = Kee[str]('adventure/trade_at_world_height')
  ADVENTURE_TRIM_WITH_ALL_EXCLUSIVE_ARMOR_PATTERNS = Kee[str](
    'adventure/trim_with_all_exclusive_armor_patterns')
  ADVENTURE_TRIM_WITH_ANY_ARMOR_PATTERN = Kee[str](
    'adventure/trim_with_any_armor_pattern')
  ADVENTURE_TWO_BIRDS_ONE_ARROW = Kee[str]('adventure/two_birds_one_arrow')
  ADVENTURE_UNDER_LOCK_AND_KEY = Kee[str]('adventure/under_lock_and_key')
  ADVENTURE_USE_LODESTONE = Kee[str]('adventure/use_lodestone')
  ADVENTURE_VERY_VERY_FRIGHTENING = Kee[str]('adventure/very_very_frightening')
  ADVENTURE_VOLUNTARY_EXILE = Kee[str]('adventure/voluntary_exile')
  ADVENTURE_WALK_ON_POWDER_SNOW_WITH_LEATHER_BOOTS = Kee[str](
    'adventure/walk_on_powder_snow_with_leather_boots')
  ADVENTURE_WHO_NEEDS_ROCKETS = Kee[str]('adventure/who_needs_rockets')
  ADVENTURE_WHOS_THE_PILLAGER_NOW = Kee[str]('adventure/whos_the_pillager_now')
  END_DRAGON_BREATH = Kee[str]('end/dragon_breath')
  END_DRAGON_EGG = Kee[str]('end/dragon_egg')
  END_ELYTRA = Kee[str]('end/elytra')
  END_ENTER_END_GATEWAY = Kee[str]('end/enter_end_gateway')
  END_FIND_END_CITY = Kee[str]('end/find_end_city')
  END_KILL_DRAGON = Kee[str]('end/kill_dragon')
  END_LEVITATE = Kee[str]('end/levitate')
  END_RESPAWN_DRAGON = Kee[str]('end/respawn_dragon')
  END_ROOT = Kee[str]('end/root')
  HUSBANDRY_ALLAY_DELIVER_CAKE_TO_NOTE_BLOCK = Kee[str](
    'husbandry/allay_deliver_cake_to_note_block')
  HUSBANDRY_ALLAY_DELIVER_ITEM_TO_PLAYER = Kee[str](
    'husbandry/allay_deliver_item_to_player')
  HUSBANDRY_AXOLOTL_IN_A_BUCKET = Kee[str]('husbandry/axolotl_in_a_bucket')
  HUSBANDRY_BALANCED_DIET = Kee[str]('husbandry/balanced_diet')
  HUSBANDRY_BREAK_DIAMOND_HOE = Kee[str]('husbandry/break_diamond_hoe')
  HUSBANDRY_BRED_ALL_ANIMALS = Kee[str]('husbandry/bred_all_animals')
  HUSBANDRY_BREED_AN_ANIMAL = Kee[str]('husbandry/breed_an_animal')
  HUSBANDRY_COMPLETE_CATALOGUE = Kee[str]('husbandry/complete_catalogue')
  HUSBANDRY_FEED_SNIFFLET = Kee[str]('husbandry/feed_snifflet')
  HUSBANDRY_FISHY_BUSINESS = Kee[str]('husbandry/fishy_business')
  HUSBANDRY_FROGLIGHTS = Kee[str]('husbandry/froglights')
  HUSBANDRY_KILL_AXOLOTL_TARGET = Kee[str]('husbandry/kill_axolotl_target')
  HUSBANDRY_LEASH_ALL_FROG_VARIANTS = Kee[str](
    'husbandry/leash_all_frog_variants')
  HUSBANDRY_MAKE_A_SIGN_GLOW = Kee[str]('husbandry/make_a_sign_glow')
  HUSBANDRY_OBTAIN_NETHERITE_HOE = Kee[str]('husbandry/obtain_netherite_hoe')
  HUSBANDRY_OBTAIN_SNIFFER_EGG = Kee[str]('husbandry/obtain_sniffer_egg')
  HUSBANDRY_PLACE_DRIED_GHAST_IN_WATER = Kee[str](
    'husbandry/place_dried_ghast_in_water')
  HUSBANDRY_PLANT_ANY_SNIFFER_SEED = Kee[str](
    'husbandry/plant_any_sniffer_seed')
  HUSBANDRY_PLANT_SEED = Kee[str]('husbandry/plant_seed')
  HUSBANDRY_REMOVE_WOLF_ARMOR = Kee[str]('husbandry/remove_wolf_armor')
  HUSBANDRY_REPAIR_WOLF_ARMOR = Kee[str]('husbandry/repair_wolf_armor')
  HUSBANDRY_RIDE_A_BOAT_WITH_A_GOAT = Kee[str](
    'husbandry/ride_a_boat_with_a_goat')
  HUSBANDRY_ROOT = Kee[str]('husbandry/root')
  HUSBANDRY_SAFELY_HARVEST_HONEY = Kee[str]('husbandry/safely_harvest_honey')
  HUSBANDRY_SILK_TOUCH_NEST = Kee[str]('husbandry/silk_touch_nest')
  HUSBANDRY_TACTICAL_FISHING = Kee[str]('husbandry/tactical_fishing')
  HUSBANDRY_TADPOLE_IN_A_BUCKET = Kee[str]('husbandry/tadpole_in_a_bucket')
  HUSBANDRY_TAME_AN_ANIMAL = Kee[str]('husbandry/tame_an_animal')
  HUSBANDRY_UH_OH = Kee[str]('husbandry/uh_oh')
  HUSBANDRY_WAX_OFF = Kee[str]('husbandry/wax_off')
  HUSBANDRY_WAX_ON = Kee[str]('husbandry/wax_on')
  HUSBANDRY_WHOLE_PACK = Kee[str]('husbandry/whole_pack')
  NETHER_ALL_EFFECTS = Kee[str]('nether/all_effects')
  NETHER_ALL_POTIONS = Kee[str]('nether/all_potions')
  NETHER_BREW_POTION = Kee[str]('nether/brew_potion')
  NETHER_CHARGE_RESPAWN_ANCHOR = Kee[str]('nether/charge_respawn_anchor')
  NETHER_CREATE_BEACON = Kee[str]('nether/create_beacon')
  NETHER_CREATE_FULL_BEACON = Kee[str]('nether/create_full_beacon')
  NETHER_DISTRACT_PIGLIN = Kee[str]('nether/distract_piglin')
  NETHER_EXPLORE_NETHER = Kee[str]('nether/explore_nether')
  NETHER_FAST_TRAVEL = Kee[str]('nether/fast_travel')
  NETHER_FIND_BASTION = Kee[str]('nether/find_bastion')
  NETHER_FIND_FORTRESS = Kee[str]('nether/find_fortress')
  NETHER_GET_WITHER_SKULL = Kee[str]('nether/get_wither_skull')
  NETHER_LOOT_BASTION = Kee[str]('nether/loot_bastion')
  NETHER_NETHERITE_ARMOR = Kee[str]('nether/netherite_armor')
  NETHER_OBTAIN_ANCIENT_DEBRIS = Kee[str]('nether/obtain_ancient_debris')
  NETHER_OBTAIN_BLAZE_ROD = Kee[str]('nether/obtain_blaze_rod')
  NETHER_OBTAIN_CRYING_OBSIDIAN = Kee[str]('nether/obtain_crying_obsidian')
  NETHER_RETURN_TO_SENDER = Kee[str]('nether/return_to_sender')
  NETHER_RIDE_STRIDER = Kee[str]('nether/ride_strider')
  NETHER_RIDE_STRIDER_IN_OVERWORLD_LAVA = Kee[str](
    'nether/ride_strider_in_overworld_lava')
  NETHER_ROOT = Kee[str]('nether/root')
  NETHER_SUMMON_WITHER = Kee[str]('nether/summon_wither')
  NETHER_UNEASY_ALLIANCE = Kee[str]('nether/uneasy_alliance')
  RECIPES_BREWING_BLAZE_POWDER = Kee[str]('recipes/brewing/blaze_powder')
  RECIPES_BREWING_BREWING_STAND = Kee[str]('recipes/brewing/brewing_stand')
  RECIPES_BREWING_CAULDRON = Kee[str]('recipes/brewing/cauldron')
  RECIPES_BREWING_FERMENTED_SPIDER_EYE = Kee[str](
    'recipes/brewing/fermented_spider_eye')
  RECIPES_BREWING_GLASS_BOTTLE = Kee[str]('recipes/brewing/glass_bottle')
  RECIPES_BREWING_GLISTERING_MELON_SLICE = Kee[str](
    'recipes/brewing/glistering_melon_slice')
  RECIPES_BREWING_GOLDEN_CARROT = Kee[str]('recipes/brewing/golden_carrot')
  RECIPES_BREWING_MAGMA_CREAM = Kee[str]('recipes/brewing/magma_cream')
  RECIPES_BUILDING_BLOCKS_ACACIA_PLANKS = Kee[str](
    'recipes/building_blocks/acacia_planks')
  RECIPES_BUILDING_BLOCKS_ACACIA_SLAB = Kee[str](
    'recipes/building_blocks/acacia_slab')
  RECIPES_BUILDING_BLOCKS_ACACIA_STAIRS = Kee[str](
    'recipes/building_blocks/acacia_stairs')
  RECIPES_BUILDING_BLOCKS_ACACIA_WOOD = Kee[str](
    'recipes/building_blocks/acacia_wood')
  RECIPES_BUILDING_BLOCKS_AMETHYST_BLOCK = Kee[str](
    'recipes/building_blocks/amethyst_block')
  RECIPES_BUILDING_BLOCKS_ANDESITE = Kee[str](
    'recipes/building_blocks/andesite')
  RECIPES_BUILDING_BLOCKS_ANDESITE_SLAB = Kee[str](
    'recipes/building_blocks/andesite_slab')
  RECIPES_BUILDING_BLOCKS_ANDESITE_SLAB_FROM_ANDESITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/andesite_slab_from_andesite_stonecutting')
  RECIPES_BUILDING_BLOCKS_ANDESITE_STAIRS = Kee[str](
    'recipes/building_blocks/andesite_stairs')
  RECIPES_BUILDING_BLOCKS_ANDESITE_STAIRS_FROM_ANDESITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/andesite_stairs_from_andesite_stonecutting')
  RECIPES_BUILDING_BLOCKS_BAMBOO_BLOCK = Kee[str](
    'recipes/building_blocks/bamboo_block')
  RECIPES_BUILDING_BLOCKS_BAMBOO_MOSAIC_SLAB = Kee[str](
    'recipes/building_blocks/bamboo_mosaic_slab')
  RECIPES_BUILDING_BLOCKS_BAMBOO_MOSAIC_STAIRS = Kee[str](
    'recipes/building_blocks/bamboo_mosaic_stairs')
  RECIPES_BUILDING_BLOCKS_BAMBOO_PLANKS = Kee[str](
    'recipes/building_blocks/bamboo_planks')
  RECIPES_BUILDING_BLOCKS_BAMBOO_SLAB = Kee[str](
    'recipes/building_blocks/bamboo_slab')
  RECIPES_BUILDING_BLOCKS_BAMBOO_STAIRS = Kee[str](
    'recipes/building_blocks/bamboo_stairs')
  RECIPES_BUILDING_BLOCKS_BIRCH_PLANKS = Kee[str](
    'recipes/building_blocks/birch_planks')
  RECIPES_BUILDING_BLOCKS_BIRCH_SLAB = Kee[str](
    'recipes/building_blocks/birch_slab')
  RECIPES_BUILDING_BLOCKS_BIRCH_STAIRS = Kee[str](
    'recipes/building_blocks/birch_stairs')
  RECIPES_BUILDING_BLOCKS_BIRCH_WOOD = Kee[str](
    'recipes/building_blocks/birch_wood')
  RECIPES_BUILDING_BLOCKS_BLACK_CONCRETE_POWDER = Kee[str](
    'recipes/building_blocks/black_concrete_powder')
  RECIPES_BUILDING_BLOCKS_BLACK_CONCRETE_SLAB = Kee[str](
    'recipes/building_blocks/black_concrete_slab')
  RECIPES_BUILDING_BLOCKS_BLACK_CONCRETE_SLAB_FROM_BLACK_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/black_concrete_slab_from_black_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_BLACK_CONCRETE_STAIRS = Kee[str](
    'recipes/building_blocks/black_concrete_stairs')
  RECIPES_BUILDING_BLOCKS_BLACK_CONCRETE_STAIRS_FROM_BLACK_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/black_concrete_stairs_from_black_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_BLACK_STAINED_GLASS = Kee[str](
    'recipes/building_blocks/black_stained_glass')
  RECIPES_BUILDING_BLOCKS_BLACK_TERRACOTTA = Kee[str](
    'recipes/building_blocks/black_terracotta')
  RECIPES_BUILDING_BLOCKS_BLACK_WOOL = Kee[str](
    'recipes/building_blocks/black_wool')
  RECIPES_BUILDING_BLOCKS_BLACK_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/black_wool_slab')
  RECIPES_BUILDING_BLOCKS_BLACK_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/black_wool_stairs')
  RECIPES_BUILDING_BLOCKS_BLACKSTONE_SLAB = Kee[str](
    'recipes/building_blocks/blackstone_slab')
  RECIPES_BUILDING_BLOCKS_BLACKSTONE_SLAB_FROM_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/blackstone_slab_from_blackstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_BLACKSTONE_STAIRS = Kee[str](
    'recipes/building_blocks/blackstone_stairs')
  RECIPES_BUILDING_BLOCKS_BLACKSTONE_STAIRS_FROM_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/blackstone_stairs_from_blackstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_BLUE_CONCRETE_POWDER = Kee[str](
    'recipes/building_blocks/blue_concrete_powder')
  RECIPES_BUILDING_BLOCKS_BLUE_CONCRETE_SLAB = Kee[str](
    'recipes/building_blocks/blue_concrete_slab')
  RECIPES_BUILDING_BLOCKS_BLUE_CONCRETE_SLAB_FROM_BLUE_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/blue_concrete_slab_from_blue_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_BLUE_CONCRETE_STAIRS = Kee[str](
    'recipes/building_blocks/blue_concrete_stairs')
  RECIPES_BUILDING_BLOCKS_BLUE_CONCRETE_STAIRS_FROM_BLUE_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/blue_concrete_stairs_from_blue_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_BLUE_ICE = Kee[str](
    'recipes/building_blocks/blue_ice')
  RECIPES_BUILDING_BLOCKS_BLUE_STAINED_GLASS = Kee[str](
    'recipes/building_blocks/blue_stained_glass')
  RECIPES_BUILDING_BLOCKS_BLUE_TERRACOTTA = Kee[str](
    'recipes/building_blocks/blue_terracotta')
  RECIPES_BUILDING_BLOCKS_BLUE_WOOL = Kee[str](
    'recipes/building_blocks/blue_wool')
  RECIPES_BUILDING_BLOCKS_BLUE_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/blue_wool_slab')
  RECIPES_BUILDING_BLOCKS_BLUE_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/blue_wool_stairs')
  RECIPES_BUILDING_BLOCKS_BONE_BLOCK = Kee[str](
    'recipes/building_blocks/bone_block')
  RECIPES_BUILDING_BLOCKS_BOOKSHELF = Kee[str](
    'recipes/building_blocks/bookshelf')
  RECIPES_BUILDING_BLOCKS_BRICK_SLAB = Kee[str](
    'recipes/building_blocks/brick_slab')
  RECIPES_BUILDING_BLOCKS_BRICK_SLAB_FROM_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/brick_slab_from_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_BRICK_STAIRS = Kee[str](
    'recipes/building_blocks/brick_stairs')
  RECIPES_BUILDING_BLOCKS_BRICK_STAIRS_FROM_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/brick_stairs_from_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_BRICKS = Kee[str]('recipes/building_blocks/bricks')
  RECIPES_BUILDING_BLOCKS_BROWN_CONCRETE_POWDER = Kee[str](
    'recipes/building_blocks/brown_concrete_powder')
  RECIPES_BUILDING_BLOCKS_BROWN_CONCRETE_SLAB = Kee[str](
    'recipes/building_blocks/brown_concrete_slab')
  RECIPES_BUILDING_BLOCKS_BROWN_CONCRETE_SLAB_FROM_BROWN_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/brown_concrete_slab_from_brown_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_BROWN_CONCRETE_STAIRS = Kee[str](
    'recipes/building_blocks/brown_concrete_stairs')
  RECIPES_BUILDING_BLOCKS_BROWN_CONCRETE_STAIRS_FROM_BROWN_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/brown_concrete_stairs_from_brown_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_BROWN_STAINED_GLASS = Kee[str](
    'recipes/building_blocks/brown_stained_glass')
  RECIPES_BUILDING_BLOCKS_BROWN_TERRACOTTA = Kee[str](
    'recipes/building_blocks/brown_terracotta')
  RECIPES_BUILDING_BLOCKS_BROWN_WOOL = Kee[str](
    'recipes/building_blocks/brown_wool')
  RECIPES_BUILDING_BLOCKS_BROWN_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/brown_wool_slab')
  RECIPES_BUILDING_BLOCKS_BROWN_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/brown_wool_stairs')
  RECIPES_BUILDING_BLOCKS_CHERRY_PLANKS = Kee[str](
    'recipes/building_blocks/cherry_planks')
  RECIPES_BUILDING_BLOCKS_CHERRY_SLAB = Kee[str](
    'recipes/building_blocks/cherry_slab')
  RECIPES_BUILDING_BLOCKS_CHERRY_STAIRS = Kee[str](
    'recipes/building_blocks/cherry_stairs')
  RECIPES_BUILDING_BLOCKS_CHERRY_WOOD = Kee[str](
    'recipes/building_blocks/cherry_wood')
  RECIPES_BUILDING_BLOCKS_CHISELED_BOOKSHELF = Kee[str](
    'recipes/building_blocks/chiseled_bookshelf')
  RECIPES_BUILDING_BLOCKS_CHISELED_CINNABAR = Kee[str](
    'recipes/building_blocks/chiseled_cinnabar')
  RECIPES_BUILDING_BLOCKS_CHISELED_CINNABAR_FROM_CINNABAR_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_cinnabar_from_cinnabar_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_COPPER = Kee[str](
    'recipes/building_blocks/chiseled_copper')
  RECIPES_BUILDING_BLOCKS_CHISELED_COPPER_FROM_COPPER_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_copper_from_copper_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_COPPER_FROM_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_copper_from_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_DEEPSLATE = Kee[str](
    'recipes/building_blocks/chiseled_deepslate')
  RECIPES_BUILDING_BLOCKS_CHISELED_DEEPSLATE_FROM_COBBLED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_deepslate_from_cobbled_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_DEEPSLATE_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_deepslate_from_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_NETHER_BRICKS = Kee[str](
    'recipes/building_blocks/chiseled_nether_bricks')
  RECIPES_BUILDING_BLOCKS_CHISELED_NETHER_BRICKS_FROM_NETHER_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_nether_bricks_from_nether_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_POLISHED_BLACKSTONE = Kee[str](
    'recipes/building_blocks/chiseled_polished_blackstone')
  RECIPES_BUILDING_BLOCKS_CHISELED_POLISHED_BLACKSTONE_FROM_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_polished_blackstone_from_blackstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_POLISHED_BLACKSTONE_FROM_POLISHED_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_polished_blackstone_from_polished_blackstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_QUARTZ_BLOCK = Kee[str](
    'recipes/building_blocks/chiseled_quartz_block')
  RECIPES_BUILDING_BLOCKS_CHISELED_QUARTZ_BLOCK_FROM_QUARTZ_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_quartz_block_from_quartz_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_RED_SANDSTONE = Kee[str](
    'recipes/building_blocks/chiseled_red_sandstone')
  RECIPES_BUILDING_BLOCKS_CHISELED_RED_SANDSTONE_FROM_RED_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_red_sandstone_from_red_sandstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_RESIN_BRICKS = Kee[str](
    'recipes/building_blocks/chiseled_resin_bricks')
  RECIPES_BUILDING_BLOCKS_CHISELED_RESIN_BRICKS_FROM_RESIN_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_resin_bricks_from_resin_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_SANDSTONE = Kee[str](
    'recipes/building_blocks/chiseled_sandstone')
  RECIPES_BUILDING_BLOCKS_CHISELED_SANDSTONE_FROM_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_sandstone_from_sandstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_STONE_BRICKS = Kee[str](
    'recipes/building_blocks/chiseled_stone_bricks')
  RECIPES_BUILDING_BLOCKS_CHISELED_STONE_BRICKS_FROM_STONE_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_stone_bricks_from_stone_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_STONE_BRICKS_FROM_STONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_stone_bricks_from_stone_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_SULFUR = Kee[str](
    'recipes/building_blocks/chiseled_sulfur')
  RECIPES_BUILDING_BLOCKS_CHISELED_SULFUR_FROM_SULFUR_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_sulfur_from_sulfur_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_TUFF = Kee[str](
    'recipes/building_blocks/chiseled_tuff')
  RECIPES_BUILDING_BLOCKS_CHISELED_TUFF_BRICKS = Kee[str](
    'recipes/building_blocks/chiseled_tuff_bricks')
  RECIPES_BUILDING_BLOCKS_CHISELED_TUFF_BRICKS_FROM_POLISHED_TUFF_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_tuff_bricks_from_polished_tuff_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_TUFF_BRICKS_FROM_TUFF_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_tuff_bricks_from_tuff_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_TUFF_BRICKS_FROM_TUFF_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_tuff_bricks_from_tuff_stonecutting')
  RECIPES_BUILDING_BLOCKS_CHISELED_TUFF_FROM_TUFF_STONECUTTING = Kee[str](
    'recipes/building_blocks/chiseled_tuff_from_tuff_stonecutting')
  RECIPES_BUILDING_BLOCKS_CINNABAR_BRICK_SLAB = Kee[str](
    'recipes/building_blocks/cinnabar_brick_slab')
  RECIPES_BUILDING_BLOCKS_CINNABAR_BRICK_SLAB_FROM_CINNABAR_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/cinnabar_brick_slab_from_cinnabar_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_CINNABAR_BRICK_SLAB_FROM_CINNABAR_STONECUTTING = Kee[str](
    'recipes/building_blocks/cinnabar_brick_slab_from_cinnabar_stonecutting')
  RECIPES_BUILDING_BLOCKS_CINNABAR_BRICK_SLAB_FROM_POLISHED_CINNABAR_STONECUTTING = Kee[str](
    'recipes/building_blocks/cinnabar_brick_slab_from_polished_cinnabar_stonecutting')
  RECIPES_BUILDING_BLOCKS_CINNABAR_BRICK_STAIRS = Kee[str](
    'recipes/building_blocks/cinnabar_brick_stairs')
  RECIPES_BUILDING_BLOCKS_CINNABAR_BRICK_STAIRS_FROM_CINNABAR_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/cinnabar_brick_stairs_from_cinnabar_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_CINNABAR_BRICK_STAIRS_FROM_CINNABAR_STONECUTTING = Kee[str](
    'recipes/building_blocks/cinnabar_brick_stairs_from_cinnabar_stonecutting')
  RECIPES_BUILDING_BLOCKS_CINNABAR_BRICK_STAIRS_FROM_POLISHED_CINNABAR_STONECUTTING = Kee[str](
    'recipes/building_blocks/cinnabar_brick_stairs_from_polished_cinnabar_stonecutting')
  RECIPES_BUILDING_BLOCKS_CINNABAR_BRICKS = Kee[str](
    'recipes/building_blocks/cinnabar_bricks')
  RECIPES_BUILDING_BLOCKS_CINNABAR_BRICKS_FROM_CINNABAR_STONECUTTING = Kee[str](
    'recipes/building_blocks/cinnabar_bricks_from_cinnabar_stonecutting')
  RECIPES_BUILDING_BLOCKS_CINNABAR_BRICKS_FROM_POLISHED_CINNABAR_STONECUTTING = Kee[str](
    'recipes/building_blocks/cinnabar_bricks_from_polished_cinnabar_stonecutting')
  RECIPES_BUILDING_BLOCKS_CINNABAR_SLAB = Kee[str](
    'recipes/building_blocks/cinnabar_slab')
  RECIPES_BUILDING_BLOCKS_CINNABAR_SLAB_FROM_CINNABAR_STONECUTTING = Kee[str](
    'recipes/building_blocks/cinnabar_slab_from_cinnabar_stonecutting')
  RECIPES_BUILDING_BLOCKS_CINNABAR_STAIRS = Kee[str](
    'recipes/building_blocks/cinnabar_stairs')
  RECIPES_BUILDING_BLOCKS_CINNABAR_STAIRS_FROM_CINNABAR_STONECUTTING = Kee[str](
    'recipes/building_blocks/cinnabar_stairs_from_cinnabar_stonecutting')
  RECIPES_BUILDING_BLOCKS_CLAY = Kee[str]('recipes/building_blocks/clay')
  RECIPES_BUILDING_BLOCKS_COAL_BLOCK = Kee[str](
    'recipes/building_blocks/coal_block')
  RECIPES_BUILDING_BLOCKS_COARSE_DIRT = Kee[str](
    'recipes/building_blocks/coarse_dirt')
  RECIPES_BUILDING_BLOCKS_COBBLED_DEEPSLATE_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cobbled_deepslate_from_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_COBBLED_DEEPSLATE_SLAB = Kee[str](
    'recipes/building_blocks/cobbled_deepslate_slab')
  RECIPES_BUILDING_BLOCKS_COBBLED_DEEPSLATE_SLAB_FROM_COBBLED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cobbled_deepslate_slab_from_cobbled_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_COBBLED_DEEPSLATE_SLAB_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cobbled_deepslate_slab_from_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_COBBLED_DEEPSLATE_STAIRS = Kee[str](
    'recipes/building_blocks/cobbled_deepslate_stairs')
  RECIPES_BUILDING_BLOCKS_COBBLED_DEEPSLATE_STAIRS_FROM_COBBLED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cobbled_deepslate_stairs_from_cobbled_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_COBBLED_DEEPSLATE_STAIRS_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cobbled_deepslate_stairs_from_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_COBBLESTONE_FROM_STONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cobblestone_from_stone_stonecutting')
  RECIPES_BUILDING_BLOCKS_COBBLESTONE_SLAB = Kee[str](
    'recipes/building_blocks/cobblestone_slab')
  RECIPES_BUILDING_BLOCKS_COBBLESTONE_SLAB_FROM_COBBLESTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cobblestone_slab_from_cobblestone_stonecutting')
  RECIPES_BUILDING_BLOCKS_COBBLESTONE_SLAB_FROM_STONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cobblestone_slab_from_stone_stonecutting')
  RECIPES_BUILDING_BLOCKS_COBBLESTONE_STAIRS = Kee[str](
    'recipes/building_blocks/cobblestone_stairs')
  RECIPES_BUILDING_BLOCKS_COBBLESTONE_STAIRS_FROM_COBBLESTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cobblestone_stairs_from_cobblestone_stonecutting')
  RECIPES_BUILDING_BLOCKS_COBBLESTONE_STAIRS_FROM_STONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cobblestone_stairs_from_stone_stonecutting')
  RECIPES_BUILDING_BLOCKS_COPPER_BLOCK = Kee[str](
    'recipes/building_blocks/copper_block')
  RECIPES_BUILDING_BLOCKS_COPPER_GRATE = Kee[str](
    'recipes/building_blocks/copper_grate')
  RECIPES_BUILDING_BLOCKS_COPPER_GRATE_FROM_COPPER_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/copper_grate_from_copper_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_CRACKED_DEEPSLATE_BRICKS = Kee[str](
    'recipes/building_blocks/cracked_deepslate_bricks')
  RECIPES_BUILDING_BLOCKS_CRACKED_DEEPSLATE_TILES = Kee[str](
    'recipes/building_blocks/cracked_deepslate_tiles')
  RECIPES_BUILDING_BLOCKS_CRACKED_NETHER_BRICKS = Kee[str](
    'recipes/building_blocks/cracked_nether_bricks')
  RECIPES_BUILDING_BLOCKS_CRACKED_POLISHED_BLACKSTONE_BRICKS = Kee[str](
    'recipes/building_blocks/cracked_polished_blackstone_bricks')
  RECIPES_BUILDING_BLOCKS_CRACKED_STONE_BRICKS = Kee[str](
    'recipes/building_blocks/cracked_stone_bricks')
  RECIPES_BUILDING_BLOCKS_CRIMSON_HYPHAE = Kee[str](
    'recipes/building_blocks/crimson_hyphae')
  RECIPES_BUILDING_BLOCKS_CRIMSON_PLANKS = Kee[str](
    'recipes/building_blocks/crimson_planks')
  RECIPES_BUILDING_BLOCKS_CRIMSON_SLAB = Kee[str](
    'recipes/building_blocks/crimson_slab')
  RECIPES_BUILDING_BLOCKS_CRIMSON_STAIRS = Kee[str](
    'recipes/building_blocks/crimson_stairs')
  RECIPES_BUILDING_BLOCKS_CUT_COPPER = Kee[str](
    'recipes/building_blocks/cut_copper')
  RECIPES_BUILDING_BLOCKS_CUT_COPPER_FROM_COPPER_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/cut_copper_from_copper_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_CUT_COPPER_SLAB = Kee[str](
    'recipes/building_blocks/cut_copper_slab')
  RECIPES_BUILDING_BLOCKS_CUT_COPPER_SLAB_FROM_COPPER_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/cut_copper_slab_from_copper_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_CUT_COPPER_SLAB_FROM_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/cut_copper_slab_from_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_CUT_COPPER_STAIRS = Kee[str](
    'recipes/building_blocks/cut_copper_stairs')
  RECIPES_BUILDING_BLOCKS_CUT_COPPER_STAIRS_FROM_COPPER_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/cut_copper_stairs_from_copper_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_CUT_COPPER_STAIRS_FROM_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/cut_copper_stairs_from_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_CUT_RED_SANDSTONE = Kee[str](
    'recipes/building_blocks/cut_red_sandstone')
  RECIPES_BUILDING_BLOCKS_CUT_RED_SANDSTONE_FROM_RED_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cut_red_sandstone_from_red_sandstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_CUT_RED_SANDSTONE_SLAB = Kee[str](
    'recipes/building_blocks/cut_red_sandstone_slab')
  RECIPES_BUILDING_BLOCKS_CUT_RED_SANDSTONE_SLAB_FROM_CUT_RED_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cut_red_sandstone_slab_from_cut_red_sandstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_CUT_RED_SANDSTONE_SLAB_FROM_RED_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cut_red_sandstone_slab_from_red_sandstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_CUT_SANDSTONE = Kee[str](
    'recipes/building_blocks/cut_sandstone')
  RECIPES_BUILDING_BLOCKS_CUT_SANDSTONE_FROM_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cut_sandstone_from_sandstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_CUT_SANDSTONE_SLAB = Kee[str](
    'recipes/building_blocks/cut_sandstone_slab')
  RECIPES_BUILDING_BLOCKS_CUT_SANDSTONE_SLAB_FROM_CUT_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cut_sandstone_slab_from_cut_sandstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_CUT_SANDSTONE_SLAB_FROM_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cut_sandstone_slab_from_sandstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_CYAN_CONCRETE_POWDER = Kee[str](
    'recipes/building_blocks/cyan_concrete_powder')
  RECIPES_BUILDING_BLOCKS_CYAN_CONCRETE_SLAB = Kee[str](
    'recipes/building_blocks/cyan_concrete_slab')
  RECIPES_BUILDING_BLOCKS_CYAN_CONCRETE_SLAB_FROM_CYAN_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cyan_concrete_slab_from_cyan_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_CYAN_CONCRETE_STAIRS = Kee[str](
    'recipes/building_blocks/cyan_concrete_stairs')
  RECIPES_BUILDING_BLOCKS_CYAN_CONCRETE_STAIRS_FROM_CYAN_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/cyan_concrete_stairs_from_cyan_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_CYAN_STAINED_GLASS = Kee[str](
    'recipes/building_blocks/cyan_stained_glass')
  RECIPES_BUILDING_BLOCKS_CYAN_TERRACOTTA = Kee[str](
    'recipes/building_blocks/cyan_terracotta')
  RECIPES_BUILDING_BLOCKS_CYAN_WOOL = Kee[str](
    'recipes/building_blocks/cyan_wool')
  RECIPES_BUILDING_BLOCKS_CYAN_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/cyan_wool_slab')
  RECIPES_BUILDING_BLOCKS_CYAN_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/cyan_wool_stairs')
  RECIPES_BUILDING_BLOCKS_DARK_OAK_PLANKS = Kee[str](
    'recipes/building_blocks/dark_oak_planks')
  RECIPES_BUILDING_BLOCKS_DARK_OAK_SLAB = Kee[str](
    'recipes/building_blocks/dark_oak_slab')
  RECIPES_BUILDING_BLOCKS_DARK_OAK_STAIRS = Kee[str](
    'recipes/building_blocks/dark_oak_stairs')
  RECIPES_BUILDING_BLOCKS_DARK_OAK_WOOD = Kee[str](
    'recipes/building_blocks/dark_oak_wood')
  RECIPES_BUILDING_BLOCKS_DARK_PRISMARINE = Kee[str](
    'recipes/building_blocks/dark_prismarine')
  RECIPES_BUILDING_BLOCKS_DARK_PRISMARINE_SLAB = Kee[str](
    'recipes/building_blocks/dark_prismarine_slab')
  RECIPES_BUILDING_BLOCKS_DARK_PRISMARINE_SLAB_FROM_DARK_PRISMARINE_STONECUTTING = Kee[str](
    'recipes/building_blocks/dark_prismarine_slab_from_dark_prismarine_stonecutting')
  RECIPES_BUILDING_BLOCKS_DARK_PRISMARINE_STAIRS = Kee[str](
    'recipes/building_blocks/dark_prismarine_stairs')
  RECIPES_BUILDING_BLOCKS_DARK_PRISMARINE_STAIRS_FROM_DARK_PRISMARINE_STONECUTTING = Kee[str](
    'recipes/building_blocks/dark_prismarine_stairs_from_dark_prismarine_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE = Kee[str](
    'recipes/building_blocks/deepslate')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_BRICK_SLAB = Kee[str](
    'recipes/building_blocks/deepslate_brick_slab')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_BRICK_SLAB_FROM_COBBLED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_brick_slab_from_cobbled_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_BRICK_SLAB_FROM_DEEPSLATE_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_brick_slab_from_deepslate_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_BRICK_SLAB_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_brick_slab_from_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_BRICK_SLAB_FROM_POLISHED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_brick_slab_from_polished_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_BRICK_STAIRS = Kee[str](
    'recipes/building_blocks/deepslate_brick_stairs')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_BRICK_STAIRS_FROM_COBBLED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_brick_stairs_from_cobbled_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_BRICK_STAIRS_FROM_DEEPSLATE_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_brick_stairs_from_deepslate_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_BRICK_STAIRS_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_brick_stairs_from_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_BRICK_STAIRS_FROM_POLISHED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_brick_stairs_from_polished_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_BRICKS = Kee[str](
    'recipes/building_blocks/deepslate_bricks')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_BRICKS_FROM_COBBLED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_bricks_from_cobbled_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_BRICKS_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_bricks_from_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_BRICKS_FROM_POLISHED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_bricks_from_polished_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILE_SLAB = Kee[str](
    'recipes/building_blocks/deepslate_tile_slab')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILE_SLAB_FROM_COBBLED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_tile_slab_from_cobbled_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILE_SLAB_FROM_DEEPSLATE_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_tile_slab_from_deepslate_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILE_SLAB_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_tile_slab_from_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILE_SLAB_FROM_DEEPSLATE_TILES_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_tile_slab_from_deepslate_tiles_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILE_SLAB_FROM_POLISHED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_tile_slab_from_polished_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILE_STAIRS = Kee[str](
    'recipes/building_blocks/deepslate_tile_stairs')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILE_STAIRS_FROM_COBBLED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_tile_stairs_from_cobbled_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILE_STAIRS_FROM_DEEPSLATE_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_tile_stairs_from_deepslate_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILE_STAIRS_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_tile_stairs_from_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILE_STAIRS_FROM_DEEPSLATE_TILES_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_tile_stairs_from_deepslate_tiles_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILE_STAIRS_FROM_POLISHED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_tile_stairs_from_polished_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILES = Kee[str](
    'recipes/building_blocks/deepslate_tiles')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILES_FROM_COBBLED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_tiles_from_cobbled_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILES_FROM_DEEPSLATE_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_tiles_from_deepslate_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILES_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_tiles_from_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DEEPSLATE_TILES_FROM_POLISHED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/deepslate_tiles_from_polished_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_DIAMOND_BLOCK = Kee[str](
    'recipes/building_blocks/diamond_block')
  RECIPES_BUILDING_BLOCKS_DIORITE = Kee[str]('recipes/building_blocks/diorite')
  RECIPES_BUILDING_BLOCKS_DIORITE_SLAB = Kee[str](
    'recipes/building_blocks/diorite_slab')
  RECIPES_BUILDING_BLOCKS_DIORITE_SLAB_FROM_DIORITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/diorite_slab_from_diorite_stonecutting')
  RECIPES_BUILDING_BLOCKS_DIORITE_STAIRS = Kee[str](
    'recipes/building_blocks/diorite_stairs')
  RECIPES_BUILDING_BLOCKS_DIORITE_STAIRS_FROM_DIORITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/diorite_stairs_from_diorite_stonecutting')
  RECIPES_BUILDING_BLOCKS_DRIED_GHAST = Kee[str](
    'recipes/building_blocks/dried_ghast')
  RECIPES_BUILDING_BLOCKS_DRIED_KELP_BLOCK = Kee[str](
    'recipes/building_blocks/dried_kelp_block')
  RECIPES_BUILDING_BLOCKS_DRIPSTONE_BLOCK = Kee[str](
    'recipes/building_blocks/dripstone_block')
  RECIPES_BUILDING_BLOCKS_DYE_BLACK_BED = Kee[str](
    'recipes/building_blocks/dye_black_bed')
  RECIPES_BUILDING_BLOCKS_DYE_BLACK_CARPET = Kee[str](
    'recipes/building_blocks/dye_black_carpet')
  RECIPES_BUILDING_BLOCKS_DYE_BLACK_WOOL = Kee[str](
    'recipes/building_blocks/dye_black_wool')
  RECIPES_BUILDING_BLOCKS_DYE_BLACK_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/dye_black_wool_slab')
  RECIPES_BUILDING_BLOCKS_DYE_BLACK_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/dye_black_wool_stairs')
  RECIPES_BUILDING_BLOCKS_DYE_BLUE_BED = Kee[str](
    'recipes/building_blocks/dye_blue_bed')
  RECIPES_BUILDING_BLOCKS_DYE_BLUE_CARPET = Kee[str](
    'recipes/building_blocks/dye_blue_carpet')
  RECIPES_BUILDING_BLOCKS_DYE_BLUE_WOOL = Kee[str](
    'recipes/building_blocks/dye_blue_wool')
  RECIPES_BUILDING_BLOCKS_DYE_BLUE_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/dye_blue_wool_slab')
  RECIPES_BUILDING_BLOCKS_DYE_BLUE_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/dye_blue_wool_stairs')
  RECIPES_BUILDING_BLOCKS_DYE_BROWN_BED = Kee[str](
    'recipes/building_blocks/dye_brown_bed')
  RECIPES_BUILDING_BLOCKS_DYE_BROWN_CARPET = Kee[str](
    'recipes/building_blocks/dye_brown_carpet')
  RECIPES_BUILDING_BLOCKS_DYE_BROWN_WOOL = Kee[str](
    'recipes/building_blocks/dye_brown_wool')
  RECIPES_BUILDING_BLOCKS_DYE_BROWN_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/dye_brown_wool_slab')
  RECIPES_BUILDING_BLOCKS_DYE_BROWN_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/dye_brown_wool_stairs')
  RECIPES_BUILDING_BLOCKS_DYE_CYAN_BED = Kee[str](
    'recipes/building_blocks/dye_cyan_bed')
  RECIPES_BUILDING_BLOCKS_DYE_CYAN_CARPET = Kee[str](
    'recipes/building_blocks/dye_cyan_carpet')
  RECIPES_BUILDING_BLOCKS_DYE_CYAN_WOOL = Kee[str](
    'recipes/building_blocks/dye_cyan_wool')
  RECIPES_BUILDING_BLOCKS_DYE_CYAN_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/dye_cyan_wool_slab')
  RECIPES_BUILDING_BLOCKS_DYE_CYAN_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/dye_cyan_wool_stairs')
  RECIPES_BUILDING_BLOCKS_DYE_GRAY_BED = Kee[str](
    'recipes/building_blocks/dye_gray_bed')
  RECIPES_BUILDING_BLOCKS_DYE_GRAY_CARPET = Kee[str](
    'recipes/building_blocks/dye_gray_carpet')
  RECIPES_BUILDING_BLOCKS_DYE_GRAY_WOOL = Kee[str](
    'recipes/building_blocks/dye_gray_wool')
  RECIPES_BUILDING_BLOCKS_DYE_GRAY_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/dye_gray_wool_slab')
  RECIPES_BUILDING_BLOCKS_DYE_GRAY_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/dye_gray_wool_stairs')
  RECIPES_BUILDING_BLOCKS_DYE_GREEN_BED = Kee[str](
    'recipes/building_blocks/dye_green_bed')
  RECIPES_BUILDING_BLOCKS_DYE_GREEN_CARPET = Kee[str](
    'recipes/building_blocks/dye_green_carpet')
  RECIPES_BUILDING_BLOCKS_DYE_GREEN_WOOL = Kee[str](
    'recipes/building_blocks/dye_green_wool')
  RECIPES_BUILDING_BLOCKS_DYE_GREEN_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/dye_green_wool_slab')
  RECIPES_BUILDING_BLOCKS_DYE_GREEN_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/dye_green_wool_stairs')
  RECIPES_BUILDING_BLOCKS_DYE_LIGHT_BLUE_BED = Kee[str](
    'recipes/building_blocks/dye_light_blue_bed')
  RECIPES_BUILDING_BLOCKS_DYE_LIGHT_BLUE_CARPET = Kee[str](
    'recipes/building_blocks/dye_light_blue_carpet')
  RECIPES_BUILDING_BLOCKS_DYE_LIGHT_BLUE_WOOL = Kee[str](
    'recipes/building_blocks/dye_light_blue_wool')
  RECIPES_BUILDING_BLOCKS_DYE_LIGHT_BLUE_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/dye_light_blue_wool_slab')
  RECIPES_BUILDING_BLOCKS_DYE_LIGHT_BLUE_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/dye_light_blue_wool_stairs')
  RECIPES_BUILDING_BLOCKS_DYE_LIGHT_GRAY_BED = Kee[str](
    'recipes/building_blocks/dye_light_gray_bed')
  RECIPES_BUILDING_BLOCKS_DYE_LIGHT_GRAY_CARPET = Kee[str](
    'recipes/building_blocks/dye_light_gray_carpet')
  RECIPES_BUILDING_BLOCKS_DYE_LIGHT_GRAY_WOOL = Kee[str](
    'recipes/building_blocks/dye_light_gray_wool')
  RECIPES_BUILDING_BLOCKS_DYE_LIGHT_GRAY_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/dye_light_gray_wool_slab')
  RECIPES_BUILDING_BLOCKS_DYE_LIGHT_GRAY_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/dye_light_gray_wool_stairs')
  RECIPES_BUILDING_BLOCKS_DYE_LIME_BED = Kee[str](
    'recipes/building_blocks/dye_lime_bed')
  RECIPES_BUILDING_BLOCKS_DYE_LIME_CARPET = Kee[str](
    'recipes/building_blocks/dye_lime_carpet')
  RECIPES_BUILDING_BLOCKS_DYE_LIME_WOOL = Kee[str](
    'recipes/building_blocks/dye_lime_wool')
  RECIPES_BUILDING_BLOCKS_DYE_LIME_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/dye_lime_wool_slab')
  RECIPES_BUILDING_BLOCKS_DYE_LIME_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/dye_lime_wool_stairs')
  RECIPES_BUILDING_BLOCKS_DYE_MAGENTA_BED = Kee[str](
    'recipes/building_blocks/dye_magenta_bed')
  RECIPES_BUILDING_BLOCKS_DYE_MAGENTA_CARPET = Kee[str](
    'recipes/building_blocks/dye_magenta_carpet')
  RECIPES_BUILDING_BLOCKS_DYE_MAGENTA_WOOL = Kee[str](
    'recipes/building_blocks/dye_magenta_wool')
  RECIPES_BUILDING_BLOCKS_DYE_MAGENTA_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/dye_magenta_wool_slab')
  RECIPES_BUILDING_BLOCKS_DYE_MAGENTA_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/dye_magenta_wool_stairs')
  RECIPES_BUILDING_BLOCKS_DYE_ORANGE_BED = Kee[str](
    'recipes/building_blocks/dye_orange_bed')
  RECIPES_BUILDING_BLOCKS_DYE_ORANGE_CARPET = Kee[str](
    'recipes/building_blocks/dye_orange_carpet')
  RECIPES_BUILDING_BLOCKS_DYE_ORANGE_WOOL = Kee[str](
    'recipes/building_blocks/dye_orange_wool')
  RECIPES_BUILDING_BLOCKS_DYE_ORANGE_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/dye_orange_wool_slab')
  RECIPES_BUILDING_BLOCKS_DYE_ORANGE_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/dye_orange_wool_stairs')
  RECIPES_BUILDING_BLOCKS_DYE_PINK_BED = Kee[str](
    'recipes/building_blocks/dye_pink_bed')
  RECIPES_BUILDING_BLOCKS_DYE_PINK_CARPET = Kee[str](
    'recipes/building_blocks/dye_pink_carpet')
  RECIPES_BUILDING_BLOCKS_DYE_PINK_WOOL = Kee[str](
    'recipes/building_blocks/dye_pink_wool')
  RECIPES_BUILDING_BLOCKS_DYE_PINK_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/dye_pink_wool_slab')
  RECIPES_BUILDING_BLOCKS_DYE_PINK_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/dye_pink_wool_stairs')
  RECIPES_BUILDING_BLOCKS_DYE_PURPLE_BED = Kee[str](
    'recipes/building_blocks/dye_purple_bed')
  RECIPES_BUILDING_BLOCKS_DYE_PURPLE_CARPET = Kee[str](
    'recipes/building_blocks/dye_purple_carpet')
  RECIPES_BUILDING_BLOCKS_DYE_PURPLE_WOOL = Kee[str](
    'recipes/building_blocks/dye_purple_wool')
  RECIPES_BUILDING_BLOCKS_DYE_PURPLE_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/dye_purple_wool_slab')
  RECIPES_BUILDING_BLOCKS_DYE_PURPLE_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/dye_purple_wool_stairs')
  RECIPES_BUILDING_BLOCKS_DYE_RED_BED = Kee[str](
    'recipes/building_blocks/dye_red_bed')
  RECIPES_BUILDING_BLOCKS_DYE_RED_CARPET = Kee[str](
    'recipes/building_blocks/dye_red_carpet')
  RECIPES_BUILDING_BLOCKS_DYE_RED_WOOL = Kee[str](
    'recipes/building_blocks/dye_red_wool')
  RECIPES_BUILDING_BLOCKS_DYE_RED_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/dye_red_wool_slab')
  RECIPES_BUILDING_BLOCKS_DYE_RED_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/dye_red_wool_stairs')
  RECIPES_BUILDING_BLOCKS_DYE_WHITE_BED = Kee[str](
    'recipes/building_blocks/dye_white_bed')
  RECIPES_BUILDING_BLOCKS_DYE_WHITE_CARPET = Kee[str](
    'recipes/building_blocks/dye_white_carpet')
  RECIPES_BUILDING_BLOCKS_DYE_WHITE_WOOL = Kee[str](
    'recipes/building_blocks/dye_white_wool')
  RECIPES_BUILDING_BLOCKS_DYE_WHITE_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/dye_white_wool_slab')
  RECIPES_BUILDING_BLOCKS_DYE_WHITE_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/dye_white_wool_stairs')
  RECIPES_BUILDING_BLOCKS_DYE_YELLOW_BED = Kee[str](
    'recipes/building_blocks/dye_yellow_bed')
  RECIPES_BUILDING_BLOCKS_DYE_YELLOW_CARPET = Kee[str](
    'recipes/building_blocks/dye_yellow_carpet')
  RECIPES_BUILDING_BLOCKS_DYE_YELLOW_WOOL = Kee[str](
    'recipes/building_blocks/dye_yellow_wool')
  RECIPES_BUILDING_BLOCKS_DYE_YELLOW_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/dye_yellow_wool_slab')
  RECIPES_BUILDING_BLOCKS_DYE_YELLOW_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/dye_yellow_wool_stairs')
  RECIPES_BUILDING_BLOCKS_EMERALD_BLOCK = Kee[str](
    'recipes/building_blocks/emerald_block')
  RECIPES_BUILDING_BLOCKS_END_STONE_BRICK_SLAB = Kee[str](
    'recipes/building_blocks/end_stone_brick_slab')
  RECIPES_BUILDING_BLOCKS_END_STONE_BRICK_SLAB_FROM_END_STONE_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/end_stone_brick_slab_from_end_stone_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_END_STONE_BRICK_SLAB_FROM_END_STONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/end_stone_brick_slab_from_end_stone_stonecutting')
  RECIPES_BUILDING_BLOCKS_END_STONE_BRICK_STAIRS = Kee[str](
    'recipes/building_blocks/end_stone_brick_stairs')
  RECIPES_BUILDING_BLOCKS_END_STONE_BRICK_STAIRS_FROM_END_STONE_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/end_stone_brick_stairs_from_end_stone_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_END_STONE_BRICK_STAIRS_FROM_END_STONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/end_stone_brick_stairs_from_end_stone_stonecutting')
  RECIPES_BUILDING_BLOCKS_END_STONE_BRICKS = Kee[str](
    'recipes/building_blocks/end_stone_bricks')
  RECIPES_BUILDING_BLOCKS_END_STONE_BRICKS_FROM_END_STONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/end_stone_bricks_from_end_stone_stonecutting')
  RECIPES_BUILDING_BLOCKS_EXPOSED_CHISELED_COPPER = Kee[str](
    'recipes/building_blocks/exposed_chiseled_copper')
  RECIPES_BUILDING_BLOCKS_EXPOSED_CHISELED_COPPER_FROM_EXPOSED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/exposed_chiseled_copper_from_exposed_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_EXPOSED_CHISELED_COPPER_FROM_EXPOSED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/exposed_chiseled_copper_from_exposed_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_EXPOSED_COPPER_GRATE = Kee[str](
    'recipes/building_blocks/exposed_copper_grate')
  RECIPES_BUILDING_BLOCKS_EXPOSED_COPPER_GRATE_FROM_EXPOSED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/exposed_copper_grate_from_exposed_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_EXPOSED_CUT_COPPER = Kee[str](
    'recipes/building_blocks/exposed_cut_copper')
  RECIPES_BUILDING_BLOCKS_EXPOSED_CUT_COPPER_FROM_EXPOSED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/exposed_cut_copper_from_exposed_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_EXPOSED_CUT_COPPER_SLAB = Kee[str](
    'recipes/building_blocks/exposed_cut_copper_slab')
  RECIPES_BUILDING_BLOCKS_EXPOSED_CUT_COPPER_SLAB_FROM_EXPOSED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/exposed_cut_copper_slab_from_exposed_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_EXPOSED_CUT_COPPER_SLAB_FROM_EXPOSED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/exposed_cut_copper_slab_from_exposed_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_EXPOSED_CUT_COPPER_STAIRS = Kee[str](
    'recipes/building_blocks/exposed_cut_copper_stairs')
  RECIPES_BUILDING_BLOCKS_EXPOSED_CUT_COPPER_STAIRS_FROM_EXPOSED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/exposed_cut_copper_stairs_from_exposed_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_EXPOSED_CUT_COPPER_STAIRS_FROM_EXPOSED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/exposed_cut_copper_stairs_from_exposed_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_GLASS = Kee[str]('recipes/building_blocks/glass')
  RECIPES_BUILDING_BLOCKS_GLOWSTONE = Kee[str](
    'recipes/building_blocks/glowstone')
  RECIPES_BUILDING_BLOCKS_GOLD_BLOCK = Kee[str](
    'recipes/building_blocks/gold_block')
  RECIPES_BUILDING_BLOCKS_GRANITE = Kee[str]('recipes/building_blocks/granite')
  RECIPES_BUILDING_BLOCKS_GRANITE_SLAB = Kee[str](
    'recipes/building_blocks/granite_slab')
  RECIPES_BUILDING_BLOCKS_GRANITE_SLAB_FROM_GRANITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/granite_slab_from_granite_stonecutting')
  RECIPES_BUILDING_BLOCKS_GRANITE_STAIRS = Kee[str](
    'recipes/building_blocks/granite_stairs')
  RECIPES_BUILDING_BLOCKS_GRANITE_STAIRS_FROM_GRANITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/granite_stairs_from_granite_stonecutting')
  RECIPES_BUILDING_BLOCKS_GRAY_CONCRETE_POWDER = Kee[str](
    'recipes/building_blocks/gray_concrete_powder')
  RECIPES_BUILDING_BLOCKS_GRAY_CONCRETE_SLAB = Kee[str](
    'recipes/building_blocks/gray_concrete_slab')
  RECIPES_BUILDING_BLOCKS_GRAY_CONCRETE_SLAB_FROM_GRAY_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/gray_concrete_slab_from_gray_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_GRAY_CONCRETE_STAIRS = Kee[str](
    'recipes/building_blocks/gray_concrete_stairs')
  RECIPES_BUILDING_BLOCKS_GRAY_CONCRETE_STAIRS_FROM_GRAY_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/gray_concrete_stairs_from_gray_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_GRAY_STAINED_GLASS = Kee[str](
    'recipes/building_blocks/gray_stained_glass')
  RECIPES_BUILDING_BLOCKS_GRAY_TERRACOTTA = Kee[str](
    'recipes/building_blocks/gray_terracotta')
  RECIPES_BUILDING_BLOCKS_GRAY_WOOL = Kee[str](
    'recipes/building_blocks/gray_wool')
  RECIPES_BUILDING_BLOCKS_GRAY_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/gray_wool_slab')
  RECIPES_BUILDING_BLOCKS_GRAY_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/gray_wool_stairs')
  RECIPES_BUILDING_BLOCKS_GREEN_CONCRETE_POWDER = Kee[str](
    'recipes/building_blocks/green_concrete_powder')
  RECIPES_BUILDING_BLOCKS_GREEN_CONCRETE_SLAB = Kee[str](
    'recipes/building_blocks/green_concrete_slab')
  RECIPES_BUILDING_BLOCKS_GREEN_CONCRETE_SLAB_FROM_GREEN_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/green_concrete_slab_from_green_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_GREEN_CONCRETE_STAIRS = Kee[str](
    'recipes/building_blocks/green_concrete_stairs')
  RECIPES_BUILDING_BLOCKS_GREEN_CONCRETE_STAIRS_FROM_GREEN_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/green_concrete_stairs_from_green_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_GREEN_STAINED_GLASS = Kee[str](
    'recipes/building_blocks/green_stained_glass')
  RECIPES_BUILDING_BLOCKS_GREEN_TERRACOTTA = Kee[str](
    'recipes/building_blocks/green_terracotta')
  RECIPES_BUILDING_BLOCKS_GREEN_WOOL = Kee[str](
    'recipes/building_blocks/green_wool')
  RECIPES_BUILDING_BLOCKS_GREEN_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/green_wool_slab')
  RECIPES_BUILDING_BLOCKS_GREEN_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/green_wool_stairs')
  RECIPES_BUILDING_BLOCKS_HAY_BLOCK = Kee[str](
    'recipes/building_blocks/hay_block')
  RECIPES_BUILDING_BLOCKS_IRON_BLOCK = Kee[str](
    'recipes/building_blocks/iron_block')
  RECIPES_BUILDING_BLOCKS_JACK_O_LANTERN = Kee[str](
    'recipes/building_blocks/jack_o_lantern')
  RECIPES_BUILDING_BLOCKS_JUNGLE_PLANKS = Kee[str](
    'recipes/building_blocks/jungle_planks')
  RECIPES_BUILDING_BLOCKS_JUNGLE_SLAB = Kee[str](
    'recipes/building_blocks/jungle_slab')
  RECIPES_BUILDING_BLOCKS_JUNGLE_STAIRS = Kee[str](
    'recipes/building_blocks/jungle_stairs')
  RECIPES_BUILDING_BLOCKS_JUNGLE_WOOD = Kee[str](
    'recipes/building_blocks/jungle_wood')
  RECIPES_BUILDING_BLOCKS_LAPIS_BLOCK = Kee[str](
    'recipes/building_blocks/lapis_block')
  RECIPES_BUILDING_BLOCKS_LIGHT_BLUE_CONCRETE_POWDER = Kee[str](
    'recipes/building_blocks/light_blue_concrete_powder')
  RECIPES_BUILDING_BLOCKS_LIGHT_BLUE_CONCRETE_SLAB = Kee[str](
    'recipes/building_blocks/light_blue_concrete_slab')
  RECIPES_BUILDING_BLOCKS_LIGHT_BLUE_CONCRETE_SLAB_FROM_LIGHT_BLUE_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/light_blue_concrete_slab_from_light_blue_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_LIGHT_BLUE_CONCRETE_STAIRS = Kee[str](
    'recipes/building_blocks/light_blue_concrete_stairs')
  RECIPES_BUILDING_BLOCKS_LIGHT_BLUE_CONCRETE_STAIRS_FROM_LIGHT_BLUE_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/light_blue_concrete_stairs_from_light_blue_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_LIGHT_BLUE_STAINED_GLASS = Kee[str](
    'recipes/building_blocks/light_blue_stained_glass')
  RECIPES_BUILDING_BLOCKS_LIGHT_BLUE_TERRACOTTA = Kee[str](
    'recipes/building_blocks/light_blue_terracotta')
  RECIPES_BUILDING_BLOCKS_LIGHT_BLUE_WOOL = Kee[str](
    'recipes/building_blocks/light_blue_wool')
  RECIPES_BUILDING_BLOCKS_LIGHT_BLUE_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/light_blue_wool_slab')
  RECIPES_BUILDING_BLOCKS_LIGHT_BLUE_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/light_blue_wool_stairs')
  RECIPES_BUILDING_BLOCKS_LIGHT_GRAY_CONCRETE_POWDER = Kee[str](
    'recipes/building_blocks/light_gray_concrete_powder')
  RECIPES_BUILDING_BLOCKS_LIGHT_GRAY_CONCRETE_SLAB = Kee[str](
    'recipes/building_blocks/light_gray_concrete_slab')
  RECIPES_BUILDING_BLOCKS_LIGHT_GRAY_CONCRETE_SLAB_FROM_LIGHT_GRAY_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/light_gray_concrete_slab_from_light_gray_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_LIGHT_GRAY_CONCRETE_STAIRS = Kee[str](
    'recipes/building_blocks/light_gray_concrete_stairs')
  RECIPES_BUILDING_BLOCKS_LIGHT_GRAY_CONCRETE_STAIRS_FROM_LIGHT_GRAY_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/light_gray_concrete_stairs_from_light_gray_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_LIGHT_GRAY_STAINED_GLASS = Kee[str](
    'recipes/building_blocks/light_gray_stained_glass')
  RECIPES_BUILDING_BLOCKS_LIGHT_GRAY_TERRACOTTA = Kee[str](
    'recipes/building_blocks/light_gray_terracotta')
  RECIPES_BUILDING_BLOCKS_LIGHT_GRAY_WOOL = Kee[str](
    'recipes/building_blocks/light_gray_wool')
  RECIPES_BUILDING_BLOCKS_LIGHT_GRAY_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/light_gray_wool_slab')
  RECIPES_BUILDING_BLOCKS_LIGHT_GRAY_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/light_gray_wool_stairs')
  RECIPES_BUILDING_BLOCKS_LIME_CONCRETE_POWDER = Kee[str](
    'recipes/building_blocks/lime_concrete_powder')
  RECIPES_BUILDING_BLOCKS_LIME_CONCRETE_SLAB = Kee[str](
    'recipes/building_blocks/lime_concrete_slab')
  RECIPES_BUILDING_BLOCKS_LIME_CONCRETE_SLAB_FROM_LIME_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/lime_concrete_slab_from_lime_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_LIME_CONCRETE_STAIRS = Kee[str](
    'recipes/building_blocks/lime_concrete_stairs')
  RECIPES_BUILDING_BLOCKS_LIME_CONCRETE_STAIRS_FROM_LIME_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/lime_concrete_stairs_from_lime_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_LIME_STAINED_GLASS = Kee[str](
    'recipes/building_blocks/lime_stained_glass')
  RECIPES_BUILDING_BLOCKS_LIME_TERRACOTTA = Kee[str](
    'recipes/building_blocks/lime_terracotta')
  RECIPES_BUILDING_BLOCKS_LIME_WOOL = Kee[str](
    'recipes/building_blocks/lime_wool')
  RECIPES_BUILDING_BLOCKS_LIME_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/lime_wool_slab')
  RECIPES_BUILDING_BLOCKS_LIME_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/lime_wool_stairs')
  RECIPES_BUILDING_BLOCKS_MAGENTA_CONCRETE_POWDER = Kee[str](
    'recipes/building_blocks/magenta_concrete_powder')
  RECIPES_BUILDING_BLOCKS_MAGENTA_CONCRETE_SLAB = Kee[str](
    'recipes/building_blocks/magenta_concrete_slab')
  RECIPES_BUILDING_BLOCKS_MAGENTA_CONCRETE_SLAB_FROM_MAGENTA_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/magenta_concrete_slab_from_magenta_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_MAGENTA_CONCRETE_STAIRS = Kee[str](
    'recipes/building_blocks/magenta_concrete_stairs')
  RECIPES_BUILDING_BLOCKS_MAGENTA_CONCRETE_STAIRS_FROM_MAGENTA_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/magenta_concrete_stairs_from_magenta_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_MAGENTA_STAINED_GLASS = Kee[str](
    'recipes/building_blocks/magenta_stained_glass')
  RECIPES_BUILDING_BLOCKS_MAGENTA_TERRACOTTA = Kee[str](
    'recipes/building_blocks/magenta_terracotta')
  RECIPES_BUILDING_BLOCKS_MAGENTA_WOOL = Kee[str](
    'recipes/building_blocks/magenta_wool')
  RECIPES_BUILDING_BLOCKS_MAGENTA_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/magenta_wool_slab')
  RECIPES_BUILDING_BLOCKS_MAGENTA_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/magenta_wool_stairs')
  RECIPES_BUILDING_BLOCKS_MAGMA_BLOCK = Kee[str](
    'recipes/building_blocks/magma_block')
  RECIPES_BUILDING_BLOCKS_MANGROVE_PLANKS = Kee[str](
    'recipes/building_blocks/mangrove_planks')
  RECIPES_BUILDING_BLOCKS_MANGROVE_SLAB = Kee[str](
    'recipes/building_blocks/mangrove_slab')
  RECIPES_BUILDING_BLOCKS_MANGROVE_STAIRS = Kee[str](
    'recipes/building_blocks/mangrove_stairs')
  RECIPES_BUILDING_BLOCKS_MANGROVE_WOOD = Kee[str](
    'recipes/building_blocks/mangrove_wood')
  RECIPES_BUILDING_BLOCKS_MELON = Kee[str]('recipes/building_blocks/melon')
  RECIPES_BUILDING_BLOCKS_MOSSY_COBBLESTONE = Kee[str](
    'recipes/building_blocks/mossy_cobblestone')
  RECIPES_BUILDING_BLOCKS_MOSSY_COBBLESTONE_FROM_MOSS_BLOCK = Kee[str](
    'recipes/building_blocks/mossy_cobblestone_from_moss_block')
  RECIPES_BUILDING_BLOCKS_MOSSY_COBBLESTONE_FROM_VINE = Kee[str](
    'recipes/building_blocks/mossy_cobblestone_from_vine')
  RECIPES_BUILDING_BLOCKS_MOSSY_COBBLESTONE_SLAB = Kee[str](
    'recipes/building_blocks/mossy_cobblestone_slab')
  RECIPES_BUILDING_BLOCKS_MOSSY_COBBLESTONE_SLAB_FROM_MOSSY_COBBLESTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/mossy_cobblestone_slab_from_mossy_cobblestone_stonecutting')
  RECIPES_BUILDING_BLOCKS_MOSSY_COBBLESTONE_STAIRS = Kee[str](
    'recipes/building_blocks/mossy_cobblestone_stairs')
  RECIPES_BUILDING_BLOCKS_MOSSY_COBBLESTONE_STAIRS_FROM_MOSSY_COBBLESTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/mossy_cobblestone_stairs_from_mossy_cobblestone_stonecutting')
  RECIPES_BUILDING_BLOCKS_MOSSY_STONE_BRICK_SLAB = Kee[str](
    'recipes/building_blocks/mossy_stone_brick_slab')
  RECIPES_BUILDING_BLOCKS_MOSSY_STONE_BRICK_SLAB_FROM_MOSSY_STONE_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/mossy_stone_brick_slab_from_mossy_stone_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_MOSSY_STONE_BRICK_STAIRS = Kee[str](
    'recipes/building_blocks/mossy_stone_brick_stairs')
  RECIPES_BUILDING_BLOCKS_MOSSY_STONE_BRICK_STAIRS_FROM_MOSSY_STONE_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/mossy_stone_brick_stairs_from_mossy_stone_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_MOSSY_STONE_BRICKS = Kee[str](
    'recipes/building_blocks/mossy_stone_bricks')
  RECIPES_BUILDING_BLOCKS_MOSSY_STONE_BRICKS_FROM_MOSS_BLOCK = Kee[str](
    'recipes/building_blocks/mossy_stone_bricks_from_moss_block')
  RECIPES_BUILDING_BLOCKS_MOSSY_STONE_BRICKS_FROM_VINE = Kee[str](
    'recipes/building_blocks/mossy_stone_bricks_from_vine')
  RECIPES_BUILDING_BLOCKS_MUD_BRICK_SLAB = Kee[str](
    'recipes/building_blocks/mud_brick_slab')
  RECIPES_BUILDING_BLOCKS_MUD_BRICK_SLAB_FROM_MUD_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/mud_brick_slab_from_mud_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_MUD_BRICK_STAIRS = Kee[str](
    'recipes/building_blocks/mud_brick_stairs')
  RECIPES_BUILDING_BLOCKS_MUD_BRICK_STAIRS_FROM_MUD_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/mud_brick_stairs_from_mud_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_MUD_BRICKS = Kee[str](
    'recipes/building_blocks/mud_bricks')
  RECIPES_BUILDING_BLOCKS_MUDDY_MANGROVE_ROOTS = Kee[str](
    'recipes/building_blocks/muddy_mangrove_roots')
  RECIPES_BUILDING_BLOCKS_NETHER_BRICK_SLAB = Kee[str](
    'recipes/building_blocks/nether_brick_slab')
  RECIPES_BUILDING_BLOCKS_NETHER_BRICK_SLAB_FROM_NETHER_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/nether_brick_slab_from_nether_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_NETHER_BRICK_STAIRS = Kee[str](
    'recipes/building_blocks/nether_brick_stairs')
  RECIPES_BUILDING_BLOCKS_NETHER_BRICK_STAIRS_FROM_NETHER_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/nether_brick_stairs_from_nether_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_NETHER_BRICKS = Kee[str](
    'recipes/building_blocks/nether_bricks')
  RECIPES_BUILDING_BLOCKS_NETHER_WART_BLOCK = Kee[str](
    'recipes/building_blocks/nether_wart_block')
  RECIPES_BUILDING_BLOCKS_NETHERITE_BLOCK = Kee[str](
    'recipes/building_blocks/netherite_block')
  RECIPES_BUILDING_BLOCKS_OAK_PLANKS = Kee[str](
    'recipes/building_blocks/oak_planks')
  RECIPES_BUILDING_BLOCKS_OAK_SLAB = Kee[str](
    'recipes/building_blocks/oak_slab')
  RECIPES_BUILDING_BLOCKS_OAK_STAIRS = Kee[str](
    'recipes/building_blocks/oak_stairs')
  RECIPES_BUILDING_BLOCKS_OAK_WOOD = Kee[str](
    'recipes/building_blocks/oak_wood')
  RECIPES_BUILDING_BLOCKS_ORANGE_CONCRETE_POWDER = Kee[str](
    'recipes/building_blocks/orange_concrete_powder')
  RECIPES_BUILDING_BLOCKS_ORANGE_CONCRETE_SLAB = Kee[str](
    'recipes/building_blocks/orange_concrete_slab')
  RECIPES_BUILDING_BLOCKS_ORANGE_CONCRETE_SLAB_FROM_ORANGE_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/orange_concrete_slab_from_orange_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_ORANGE_CONCRETE_STAIRS = Kee[str](
    'recipes/building_blocks/orange_concrete_stairs')
  RECIPES_BUILDING_BLOCKS_ORANGE_CONCRETE_STAIRS_FROM_ORANGE_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/orange_concrete_stairs_from_orange_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_ORANGE_STAINED_GLASS = Kee[str](
    'recipes/building_blocks/orange_stained_glass')
  RECIPES_BUILDING_BLOCKS_ORANGE_TERRACOTTA = Kee[str](
    'recipes/building_blocks/orange_terracotta')
  RECIPES_BUILDING_BLOCKS_ORANGE_WOOL = Kee[str](
    'recipes/building_blocks/orange_wool')
  RECIPES_BUILDING_BLOCKS_ORANGE_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/orange_wool_slab')
  RECIPES_BUILDING_BLOCKS_ORANGE_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/orange_wool_stairs')
  RECIPES_BUILDING_BLOCKS_OXIDIZED_CHISELED_COPPER = Kee[str](
    'recipes/building_blocks/oxidized_chiseled_copper')
  RECIPES_BUILDING_BLOCKS_OXIDIZED_CHISELED_COPPER_FROM_OXIDIZED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/oxidized_chiseled_copper_from_oxidized_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_OXIDIZED_CHISELED_COPPER_FROM_OXIDIZED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/oxidized_chiseled_copper_from_oxidized_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_OXIDIZED_COPPER_GRATE = Kee[str](
    'recipes/building_blocks/oxidized_copper_grate')
  RECIPES_BUILDING_BLOCKS_OXIDIZED_COPPER_GRATE_FROM_OXIDIZED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/oxidized_copper_grate_from_oxidized_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_OXIDIZED_CUT_COPPER = Kee[str](
    'recipes/building_blocks/oxidized_cut_copper')
  RECIPES_BUILDING_BLOCKS_OXIDIZED_CUT_COPPER_FROM_OXIDIZED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/oxidized_cut_copper_from_oxidized_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_OXIDIZED_CUT_COPPER_SLAB = Kee[str](
    'recipes/building_blocks/oxidized_cut_copper_slab')
  RECIPES_BUILDING_BLOCKS_OXIDIZED_CUT_COPPER_SLAB_FROM_OXIDIZED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/oxidized_cut_copper_slab_from_oxidized_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_OXIDIZED_CUT_COPPER_SLAB_FROM_OXIDIZED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/oxidized_cut_copper_slab_from_oxidized_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_OXIDIZED_CUT_COPPER_STAIRS = Kee[str](
    'recipes/building_blocks/oxidized_cut_copper_stairs')
  RECIPES_BUILDING_BLOCKS_OXIDIZED_CUT_COPPER_STAIRS_FROM_OXIDIZED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/oxidized_cut_copper_stairs_from_oxidized_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_OXIDIZED_CUT_COPPER_STAIRS_FROM_OXIDIZED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/oxidized_cut_copper_stairs_from_oxidized_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_PACKED_ICE = Kee[str](
    'recipes/building_blocks/packed_ice')
  RECIPES_BUILDING_BLOCKS_PACKED_MUD = Kee[str](
    'recipes/building_blocks/packed_mud')
  RECIPES_BUILDING_BLOCKS_PALE_OAK_PLANKS = Kee[str](
    'recipes/building_blocks/pale_oak_planks')
  RECIPES_BUILDING_BLOCKS_PALE_OAK_SLAB = Kee[str](
    'recipes/building_blocks/pale_oak_slab')
  RECIPES_BUILDING_BLOCKS_PALE_OAK_STAIRS = Kee[str](
    'recipes/building_blocks/pale_oak_stairs')
  RECIPES_BUILDING_BLOCKS_PALE_OAK_WOOD = Kee[str](
    'recipes/building_blocks/pale_oak_wood')
  RECIPES_BUILDING_BLOCKS_PINK_CONCRETE_POWDER = Kee[str](
    'recipes/building_blocks/pink_concrete_powder')
  RECIPES_BUILDING_BLOCKS_PINK_CONCRETE_SLAB = Kee[str](
    'recipes/building_blocks/pink_concrete_slab')
  RECIPES_BUILDING_BLOCKS_PINK_CONCRETE_SLAB_FROM_PINK_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/pink_concrete_slab_from_pink_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_PINK_CONCRETE_STAIRS = Kee[str](
    'recipes/building_blocks/pink_concrete_stairs')
  RECIPES_BUILDING_BLOCKS_PINK_CONCRETE_STAIRS_FROM_PINK_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/pink_concrete_stairs_from_pink_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_PINK_STAINED_GLASS = Kee[str](
    'recipes/building_blocks/pink_stained_glass')
  RECIPES_BUILDING_BLOCKS_PINK_TERRACOTTA = Kee[str](
    'recipes/building_blocks/pink_terracotta')
  RECIPES_BUILDING_BLOCKS_PINK_WOOL = Kee[str](
    'recipes/building_blocks/pink_wool')
  RECIPES_BUILDING_BLOCKS_PINK_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/pink_wool_slab')
  RECIPES_BUILDING_BLOCKS_PINK_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/pink_wool_stairs')
  RECIPES_BUILDING_BLOCKS_POLISHED_ANDESITE = Kee[str](
    'recipes/building_blocks/polished_andesite')
  RECIPES_BUILDING_BLOCKS_POLISHED_ANDESITE_FROM_ANDESITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_andesite_from_andesite_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_ANDESITE_SLAB = Kee[str](
    'recipes/building_blocks/polished_andesite_slab')
  RECIPES_BUILDING_BLOCKS_POLISHED_ANDESITE_SLAB_FROM_ANDESITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_andesite_slab_from_andesite_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_ANDESITE_SLAB_FROM_POLISHED_ANDESITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_andesite_slab_from_polished_andesite_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_ANDESITE_STAIRS = Kee[str](
    'recipes/building_blocks/polished_andesite_stairs')
  RECIPES_BUILDING_BLOCKS_POLISHED_ANDESITE_STAIRS_FROM_ANDESITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_andesite_stairs_from_andesite_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_ANDESITE_STAIRS_FROM_POLISHED_ANDESITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_andesite_stairs_from_polished_andesite_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_BASALT = Kee[str](
    'recipes/building_blocks/polished_basalt')
  RECIPES_BUILDING_BLOCKS_POLISHED_BASALT_FROM_BASALT_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_basalt_from_basalt_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE = Kee[str](
    'recipes/building_blocks/polished_blackstone')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_BRICK_SLAB = Kee[str](
    'recipes/building_blocks/polished_blackstone_brick_slab')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_BRICK_SLAB_FROM_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_blackstone_brick_slab_from_blackstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_BRICK_SLAB_FROM_POLISHED_BLACKSTONE_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_blackstone_brick_slab_from_polished_blackstone_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_BRICK_SLAB_FROM_POLISHED_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_blackstone_brick_slab_from_polished_blackstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_BRICK_STAIRS = Kee[str](
    'recipes/building_blocks/polished_blackstone_brick_stairs')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_BRICK_STAIRS_FROM_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_blackstone_brick_stairs_from_blackstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_BRICK_STAIRS_FROM_POLISHED_BLACKSTONE_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_blackstone_brick_stairs_from_polished_blackstone_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_BRICK_STAIRS_FROM_POLISHED_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_blackstone_brick_stairs_from_polished_blackstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_BRICKS = Kee[str](
    'recipes/building_blocks/polished_blackstone_bricks')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_BRICKS_FROM_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_blackstone_bricks_from_blackstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_BRICKS_FROM_POLISHED_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_blackstone_bricks_from_polished_blackstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_FROM_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_blackstone_from_blackstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_SLAB = Kee[str](
    'recipes/building_blocks/polished_blackstone_slab')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_SLAB_FROM_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_blackstone_slab_from_blackstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_SLAB_FROM_POLISHED_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_blackstone_slab_from_polished_blackstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_STAIRS = Kee[str](
    'recipes/building_blocks/polished_blackstone_stairs')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_STAIRS_FROM_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_blackstone_stairs_from_blackstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_BLACKSTONE_STAIRS_FROM_POLISHED_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_blackstone_stairs_from_polished_blackstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_CINNABAR = Kee[str](
    'recipes/building_blocks/polished_cinnabar')
  RECIPES_BUILDING_BLOCKS_POLISHED_CINNABAR_FROM_CINNABAR_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_cinnabar_from_cinnabar_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_CINNABAR_SLAB = Kee[str](
    'recipes/building_blocks/polished_cinnabar_slab')
  RECIPES_BUILDING_BLOCKS_POLISHED_CINNABAR_SLAB_FROM_CINNABAR_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_cinnabar_slab_from_cinnabar_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_CINNABAR_SLAB_FROM_POLISHED_CINNABAR_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_cinnabar_slab_from_polished_cinnabar_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_CINNABAR_STAIRS = Kee[str](
    'recipes/building_blocks/polished_cinnabar_stairs')
  RECIPES_BUILDING_BLOCKS_POLISHED_CINNABAR_STAIRS_FROM_CINNABAR_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_cinnabar_stairs_from_cinnabar_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_CINNABAR_STAIRS_FROM_POLISHED_CINNABAR_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_cinnabar_stairs_from_polished_cinnabar_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_DEEPSLATE = Kee[str](
    'recipes/building_blocks/polished_deepslate')
  RECIPES_BUILDING_BLOCKS_POLISHED_DEEPSLATE_FROM_COBBLED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_deepslate_from_cobbled_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_DEEPSLATE_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_deepslate_from_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_DEEPSLATE_SLAB = Kee[str](
    'recipes/building_blocks/polished_deepslate_slab')
  RECIPES_BUILDING_BLOCKS_POLISHED_DEEPSLATE_SLAB_FROM_COBBLED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_deepslate_slab_from_cobbled_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_DEEPSLATE_SLAB_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_deepslate_slab_from_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_DEEPSLATE_SLAB_FROM_POLISHED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_deepslate_slab_from_polished_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_DEEPSLATE_STAIRS = Kee[str](
    'recipes/building_blocks/polished_deepslate_stairs')
  RECIPES_BUILDING_BLOCKS_POLISHED_DEEPSLATE_STAIRS_FROM_COBBLED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_deepslate_stairs_from_cobbled_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_DEEPSLATE_STAIRS_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_deepslate_stairs_from_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_DEEPSLATE_STAIRS_FROM_POLISHED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_deepslate_stairs_from_polished_deepslate_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_DIORITE = Kee[str](
    'recipes/building_blocks/polished_diorite')
  RECIPES_BUILDING_BLOCKS_POLISHED_DIORITE_FROM_DIORITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_diorite_from_diorite_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_DIORITE_SLAB = Kee[str](
    'recipes/building_blocks/polished_diorite_slab')
  RECIPES_BUILDING_BLOCKS_POLISHED_DIORITE_SLAB_FROM_DIORITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_diorite_slab_from_diorite_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_DIORITE_SLAB_FROM_POLISHED_DIORITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_diorite_slab_from_polished_diorite_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_DIORITE_STAIRS = Kee[str](
    'recipes/building_blocks/polished_diorite_stairs')
  RECIPES_BUILDING_BLOCKS_POLISHED_DIORITE_STAIRS_FROM_DIORITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_diorite_stairs_from_diorite_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_DIORITE_STAIRS_FROM_POLISHED_DIORITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_diorite_stairs_from_polished_diorite_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_GRANITE = Kee[str](
    'recipes/building_blocks/polished_granite')
  RECIPES_BUILDING_BLOCKS_POLISHED_GRANITE_FROM_GRANITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_granite_from_granite_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_GRANITE_SLAB = Kee[str](
    'recipes/building_blocks/polished_granite_slab')
  RECIPES_BUILDING_BLOCKS_POLISHED_GRANITE_SLAB_FROM_GRANITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_granite_slab_from_granite_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_GRANITE_SLAB_FROM_POLISHED_GRANITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_granite_slab_from_polished_granite_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_GRANITE_STAIRS = Kee[str](
    'recipes/building_blocks/polished_granite_stairs')
  RECIPES_BUILDING_BLOCKS_POLISHED_GRANITE_STAIRS_FROM_GRANITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_granite_stairs_from_granite_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_GRANITE_STAIRS_FROM_POLISHED_GRANITE_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_granite_stairs_from_polished_granite_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_SULFUR = Kee[str](
    'recipes/building_blocks/polished_sulfur')
  RECIPES_BUILDING_BLOCKS_POLISHED_SULFUR_FROM_SULFUR_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_sulfur_from_sulfur_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_SULFUR_SLAB = Kee[str](
    'recipes/building_blocks/polished_sulfur_slab')
  RECIPES_BUILDING_BLOCKS_POLISHED_SULFUR_SLAB_FROM_POLISHED_SULFUR_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_sulfur_slab_from_polished_sulfur_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_SULFUR_SLAB_FROM_SULFUR_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_sulfur_slab_from_sulfur_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_SULFUR_STAIRS = Kee[str](
    'recipes/building_blocks/polished_sulfur_stairs')
  RECIPES_BUILDING_BLOCKS_POLISHED_SULFUR_STAIRS_FROM_POLISHED_SULFUR_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_sulfur_stairs_from_polished_sulfur_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_SULFUR_STAIRS_FROM_SULFUR_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_sulfur_stairs_from_sulfur_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_TUFF = Kee[str](
    'recipes/building_blocks/polished_tuff')
  RECIPES_BUILDING_BLOCKS_POLISHED_TUFF_FROM_TUFF_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_tuff_from_tuff_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_TUFF_SLAB = Kee[str](
    'recipes/building_blocks/polished_tuff_slab')
  RECIPES_BUILDING_BLOCKS_POLISHED_TUFF_SLAB_FROM_POLISHED_TUFF_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_tuff_slab_from_polished_tuff_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_TUFF_SLAB_FROM_TUFF_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_tuff_slab_from_tuff_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_TUFF_STAIRS = Kee[str](
    'recipes/building_blocks/polished_tuff_stairs')
  RECIPES_BUILDING_BLOCKS_POLISHED_TUFF_STAIRS_FROM_POLISHED_TUFF_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_tuff_stairs_from_polished_tuff_stonecutting')
  RECIPES_BUILDING_BLOCKS_POLISHED_TUFF_STAIRS_FROM_TUFF_STONECUTTING = Kee[str](
    'recipes/building_blocks/polished_tuff_stairs_from_tuff_stonecutting')
  RECIPES_BUILDING_BLOCKS_POPLAR_PLANKS = Kee[str](
    'recipes/building_blocks/poplar_planks')
  RECIPES_BUILDING_BLOCKS_POPLAR_SLAB = Kee[str](
    'recipes/building_blocks/poplar_slab')
  RECIPES_BUILDING_BLOCKS_POPLAR_STAIRS = Kee[str](
    'recipes/building_blocks/poplar_stairs')
  RECIPES_BUILDING_BLOCKS_POPLAR_WOOD = Kee[str](
    'recipes/building_blocks/poplar_wood')
  RECIPES_BUILDING_BLOCKS_POTENT_SULFUR = Kee[str](
    'recipes/building_blocks/potent_sulfur')
  RECIPES_BUILDING_BLOCKS_PRISMARINE = Kee[str](
    'recipes/building_blocks/prismarine')
  RECIPES_BUILDING_BLOCKS_PRISMARINE_BRICK_SLAB = Kee[str](
    'recipes/building_blocks/prismarine_brick_slab')
  RECIPES_BUILDING_BLOCKS_PRISMARINE_BRICK_SLAB_FROM_PRISMARINE_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/prismarine_brick_slab_from_prismarine_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_PRISMARINE_BRICK_STAIRS = Kee[str](
    'recipes/building_blocks/prismarine_brick_stairs')
  RECIPES_BUILDING_BLOCKS_PRISMARINE_BRICK_STAIRS_FROM_PRISMARINE_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/prismarine_brick_stairs_from_prismarine_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_PRISMARINE_BRICKS = Kee[str](
    'recipes/building_blocks/prismarine_bricks')
  RECIPES_BUILDING_BLOCKS_PRISMARINE_SLAB = Kee[str](
    'recipes/building_blocks/prismarine_slab')
  RECIPES_BUILDING_BLOCKS_PRISMARINE_SLAB_FROM_PRISMARINE_STONECUTTING = Kee[str](
    'recipes/building_blocks/prismarine_slab_from_prismarine_stonecutting')
  RECIPES_BUILDING_BLOCKS_PRISMARINE_STAIRS = Kee[str](
    'recipes/building_blocks/prismarine_stairs')
  RECIPES_BUILDING_BLOCKS_PRISMARINE_STAIRS_FROM_PRISMARINE_STONECUTTING = Kee[str](
    'recipes/building_blocks/prismarine_stairs_from_prismarine_stonecutting')
  RECIPES_BUILDING_BLOCKS_PURPLE_CONCRETE_POWDER = Kee[str](
    'recipes/building_blocks/purple_concrete_powder')
  RECIPES_BUILDING_BLOCKS_PURPLE_CONCRETE_SLAB = Kee[str](
    'recipes/building_blocks/purple_concrete_slab')
  RECIPES_BUILDING_BLOCKS_PURPLE_CONCRETE_SLAB_FROM_PURPLE_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/purple_concrete_slab_from_purple_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_PURPLE_CONCRETE_STAIRS = Kee[str](
    'recipes/building_blocks/purple_concrete_stairs')
  RECIPES_BUILDING_BLOCKS_PURPLE_CONCRETE_STAIRS_FROM_PURPLE_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/purple_concrete_stairs_from_purple_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_PURPLE_STAINED_GLASS = Kee[str](
    'recipes/building_blocks/purple_stained_glass')
  RECIPES_BUILDING_BLOCKS_PURPLE_TERRACOTTA = Kee[str](
    'recipes/building_blocks/purple_terracotta')
  RECIPES_BUILDING_BLOCKS_PURPLE_WOOL = Kee[str](
    'recipes/building_blocks/purple_wool')
  RECIPES_BUILDING_BLOCKS_PURPLE_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/purple_wool_slab')
  RECIPES_BUILDING_BLOCKS_PURPLE_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/purple_wool_stairs')
  RECIPES_BUILDING_BLOCKS_PURPUR_BLOCK = Kee[str](
    'recipes/building_blocks/purpur_block')
  RECIPES_BUILDING_BLOCKS_PURPUR_PILLAR = Kee[str](
    'recipes/building_blocks/purpur_pillar')
  RECIPES_BUILDING_BLOCKS_PURPUR_PILLAR_FROM_PURPUR_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/purpur_pillar_from_purpur_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_PURPUR_SLAB = Kee[str](
    'recipes/building_blocks/purpur_slab')
  RECIPES_BUILDING_BLOCKS_PURPUR_SLAB_FROM_PURPUR_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/purpur_slab_from_purpur_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_PURPUR_STAIRS = Kee[str](
    'recipes/building_blocks/purpur_stairs')
  RECIPES_BUILDING_BLOCKS_PURPUR_STAIRS_FROM_PURPUR_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/purpur_stairs_from_purpur_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_QUARTZ_BLOCK = Kee[str](
    'recipes/building_blocks/quartz_block')
  RECIPES_BUILDING_BLOCKS_QUARTZ_BRICKS = Kee[str](
    'recipes/building_blocks/quartz_bricks')
  RECIPES_BUILDING_BLOCKS_QUARTZ_BRICKS_FROM_QUARTZ_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/quartz_bricks_from_quartz_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_QUARTZ_PILLAR = Kee[str](
    'recipes/building_blocks/quartz_pillar')
  RECIPES_BUILDING_BLOCKS_QUARTZ_PILLAR_FROM_QUARTZ_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/quartz_pillar_from_quartz_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_QUARTZ_SLAB = Kee[str](
    'recipes/building_blocks/quartz_slab')
  RECIPES_BUILDING_BLOCKS_QUARTZ_SLAB_FROM_QUARTZ_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/quartz_slab_from_quartz_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_QUARTZ_STAIRS = Kee[str](
    'recipes/building_blocks/quartz_stairs')
  RECIPES_BUILDING_BLOCKS_QUARTZ_STAIRS_FROM_QUARTZ_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/quartz_stairs_from_quartz_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_RAW_COPPER_BLOCK = Kee[str](
    'recipes/building_blocks/raw_copper_block')
  RECIPES_BUILDING_BLOCKS_RAW_GOLD_BLOCK = Kee[str](
    'recipes/building_blocks/raw_gold_block')
  RECIPES_BUILDING_BLOCKS_RAW_IRON_BLOCK = Kee[str](
    'recipes/building_blocks/raw_iron_block')
  RECIPES_BUILDING_BLOCKS_RED_CONCRETE_POWDER = Kee[str](
    'recipes/building_blocks/red_concrete_powder')
  RECIPES_BUILDING_BLOCKS_RED_CONCRETE_SLAB = Kee[str](
    'recipes/building_blocks/red_concrete_slab')
  RECIPES_BUILDING_BLOCKS_RED_CONCRETE_SLAB_FROM_RED_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/red_concrete_slab_from_red_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_RED_CONCRETE_STAIRS = Kee[str](
    'recipes/building_blocks/red_concrete_stairs')
  RECIPES_BUILDING_BLOCKS_RED_CONCRETE_STAIRS_FROM_RED_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/red_concrete_stairs_from_red_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_RED_NETHER_BRICK_SLAB = Kee[str](
    'recipes/building_blocks/red_nether_brick_slab')
  RECIPES_BUILDING_BLOCKS_RED_NETHER_BRICK_SLAB_FROM_RED_NETHER_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/red_nether_brick_slab_from_red_nether_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_RED_NETHER_BRICK_STAIRS = Kee[str](
    'recipes/building_blocks/red_nether_brick_stairs')
  RECIPES_BUILDING_BLOCKS_RED_NETHER_BRICK_STAIRS_FROM_RED_NETHER_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/red_nether_brick_stairs_from_red_nether_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_RED_NETHER_BRICKS = Kee[str](
    'recipes/building_blocks/red_nether_bricks')
  RECIPES_BUILDING_BLOCKS_RED_SANDSTONE = Kee[str](
    'recipes/building_blocks/red_sandstone')
  RECIPES_BUILDING_BLOCKS_RED_SANDSTONE_SLAB = Kee[str](
    'recipes/building_blocks/red_sandstone_slab')
  RECIPES_BUILDING_BLOCKS_RED_SANDSTONE_SLAB_FROM_RED_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/red_sandstone_slab_from_red_sandstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_RED_SANDSTONE_STAIRS = Kee[str](
    'recipes/building_blocks/red_sandstone_stairs')
  RECIPES_BUILDING_BLOCKS_RED_SANDSTONE_STAIRS_FROM_RED_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/red_sandstone_stairs_from_red_sandstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_RED_STAINED_GLASS = Kee[str](
    'recipes/building_blocks/red_stained_glass')
  RECIPES_BUILDING_BLOCKS_RED_TERRACOTTA = Kee[str](
    'recipes/building_blocks/red_terracotta')
  RECIPES_BUILDING_BLOCKS_RED_WOOL = Kee[str](
    'recipes/building_blocks/red_wool')
  RECIPES_BUILDING_BLOCKS_RED_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/red_wool_slab')
  RECIPES_BUILDING_BLOCKS_RED_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/red_wool_stairs')
  RECIPES_BUILDING_BLOCKS_RESIN_BLOCK = Kee[str](
    'recipes/building_blocks/resin_block')
  RECIPES_BUILDING_BLOCKS_RESIN_BRICK_SLAB = Kee[str](
    'recipes/building_blocks/resin_brick_slab')
  RECIPES_BUILDING_BLOCKS_RESIN_BRICK_SLAB_FROM_RESIN_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/resin_brick_slab_from_resin_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_RESIN_BRICK_STAIRS = Kee[str](
    'recipes/building_blocks/resin_brick_stairs')
  RECIPES_BUILDING_BLOCKS_RESIN_BRICK_STAIRS_FROM_RESIN_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/resin_brick_stairs_from_resin_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_RESIN_BRICKS = Kee[str](
    'recipes/building_blocks/resin_bricks')
  RECIPES_BUILDING_BLOCKS_SANDSTONE = Kee[str](
    'recipes/building_blocks/sandstone')
  RECIPES_BUILDING_BLOCKS_SANDSTONE_SLAB = Kee[str](
    'recipes/building_blocks/sandstone_slab')
  RECIPES_BUILDING_BLOCKS_SANDSTONE_SLAB_FROM_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/sandstone_slab_from_sandstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_SANDSTONE_STAIRS = Kee[str](
    'recipes/building_blocks/sandstone_stairs')
  RECIPES_BUILDING_BLOCKS_SANDSTONE_STAIRS_FROM_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/sandstone_stairs_from_sandstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_SEA_LANTERN = Kee[str](
    'recipes/building_blocks/sea_lantern')
  RECIPES_BUILDING_BLOCKS_SMOOTH_BASALT = Kee[str](
    'recipes/building_blocks/smooth_basalt')
  RECIPES_BUILDING_BLOCKS_SMOOTH_QUARTZ = Kee[str](
    'recipes/building_blocks/smooth_quartz')
  RECIPES_BUILDING_BLOCKS_SMOOTH_QUARTZ_SLAB = Kee[str](
    'recipes/building_blocks/smooth_quartz_slab')
  RECIPES_BUILDING_BLOCKS_SMOOTH_QUARTZ_SLAB_FROM_SMOOTH_QUARTZ_STONECUTTING = Kee[str](
    'recipes/building_blocks/smooth_quartz_slab_from_smooth_quartz_stonecutting')
  RECIPES_BUILDING_BLOCKS_SMOOTH_QUARTZ_STAIRS = Kee[str](
    'recipes/building_blocks/smooth_quartz_stairs')
  RECIPES_BUILDING_BLOCKS_SMOOTH_QUARTZ_STAIRS_FROM_SMOOTH_QUARTZ_STONECUTTING = Kee[str](
    'recipes/building_blocks/smooth_quartz_stairs_from_smooth_quartz_stonecutting')
  RECIPES_BUILDING_BLOCKS_SMOOTH_RED_SANDSTONE = Kee[str](
    'recipes/building_blocks/smooth_red_sandstone')
  RECIPES_BUILDING_BLOCKS_SMOOTH_RED_SANDSTONE_SLAB = Kee[str](
    'recipes/building_blocks/smooth_red_sandstone_slab')
  RECIPES_BUILDING_BLOCKS_SMOOTH_RED_SANDSTONE_SLAB_FROM_SMOOTH_RED_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/smooth_red_sandstone_slab_from_smooth_red_sandstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_SMOOTH_RED_SANDSTONE_STAIRS = Kee[str](
    'recipes/building_blocks/smooth_red_sandstone_stairs')
  RECIPES_BUILDING_BLOCKS_SMOOTH_RED_SANDSTONE_STAIRS_FROM_SMOOTH_RED_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/smooth_red_sandstone_stairs_from_smooth_red_sandstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_SMOOTH_SANDSTONE = Kee[str](
    'recipes/building_blocks/smooth_sandstone')
  RECIPES_BUILDING_BLOCKS_SMOOTH_SANDSTONE_SLAB = Kee[str](
    'recipes/building_blocks/smooth_sandstone_slab')
  RECIPES_BUILDING_BLOCKS_SMOOTH_SANDSTONE_SLAB_FROM_SMOOTH_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/smooth_sandstone_slab_from_smooth_sandstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_SMOOTH_SANDSTONE_STAIRS = Kee[str](
    'recipes/building_blocks/smooth_sandstone_stairs')
  RECIPES_BUILDING_BLOCKS_SMOOTH_SANDSTONE_STAIRS_FROM_SMOOTH_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/smooth_sandstone_stairs_from_smooth_sandstone_stonecutting')
  RECIPES_BUILDING_BLOCKS_SMOOTH_STONE = Kee[str](
    'recipes/building_blocks/smooth_stone')
  RECIPES_BUILDING_BLOCKS_SMOOTH_STONE_SLAB = Kee[str](
    'recipes/building_blocks/smooth_stone_slab')
  RECIPES_BUILDING_BLOCKS_SMOOTH_STONE_SLAB_FROM_SMOOTH_STONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/smooth_stone_slab_from_smooth_stone_stonecutting')
  RECIPES_BUILDING_BLOCKS_SNOW_BLOCK = Kee[str](
    'recipes/building_blocks/snow_block')
  RECIPES_BUILDING_BLOCKS_SPONGE = Kee[str]('recipes/building_blocks/sponge')
  RECIPES_BUILDING_BLOCKS_SPRUCE_PLANKS = Kee[str](
    'recipes/building_blocks/spruce_planks')
  RECIPES_BUILDING_BLOCKS_SPRUCE_SLAB = Kee[str](
    'recipes/building_blocks/spruce_slab')
  RECIPES_BUILDING_BLOCKS_SPRUCE_STAIRS = Kee[str](
    'recipes/building_blocks/spruce_stairs')
  RECIPES_BUILDING_BLOCKS_SPRUCE_WOOD = Kee[str](
    'recipes/building_blocks/spruce_wood')
  RECIPES_BUILDING_BLOCKS_STONE = Kee[str]('recipes/building_blocks/stone')
  RECIPES_BUILDING_BLOCKS_STONE_BRICK_SLAB = Kee[str](
    'recipes/building_blocks/stone_brick_slab')
  RECIPES_BUILDING_BLOCKS_STONE_BRICK_SLAB_FROM_STONE_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/stone_brick_slab_from_stone_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_STONE_BRICK_SLAB_FROM_STONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/stone_brick_slab_from_stone_stonecutting')
  RECIPES_BUILDING_BLOCKS_STONE_BRICK_STAIRS = Kee[str](
    'recipes/building_blocks/stone_brick_stairs')
  RECIPES_BUILDING_BLOCKS_STONE_BRICK_STAIRS_FROM_STONE_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/stone_brick_stairs_from_stone_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_STONE_BRICK_STAIRS_FROM_STONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/stone_brick_stairs_from_stone_stonecutting')
  RECIPES_BUILDING_BLOCKS_STONE_BRICKS = Kee[str](
    'recipes/building_blocks/stone_bricks')
  RECIPES_BUILDING_BLOCKS_STONE_BRICKS_FROM_STONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/stone_bricks_from_stone_stonecutting')
  RECIPES_BUILDING_BLOCKS_STONE_SLAB = Kee[str](
    'recipes/building_blocks/stone_slab')
  RECIPES_BUILDING_BLOCKS_STONE_SLAB_FROM_STONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/stone_slab_from_stone_stonecutting')
  RECIPES_BUILDING_BLOCKS_STONE_STAIRS = Kee[str](
    'recipes/building_blocks/stone_stairs')
  RECIPES_BUILDING_BLOCKS_STONE_STAIRS_FROM_STONE_STONECUTTING = Kee[str](
    'recipes/building_blocks/stone_stairs_from_stone_stonecutting')
  RECIPES_BUILDING_BLOCKS_STRIPPED_ACACIA_WOOD = Kee[str](
    'recipes/building_blocks/stripped_acacia_wood')
  RECIPES_BUILDING_BLOCKS_STRIPPED_BIRCH_WOOD = Kee[str](
    'recipes/building_blocks/stripped_birch_wood')
  RECIPES_BUILDING_BLOCKS_STRIPPED_CHERRY_WOOD = Kee[str](
    'recipes/building_blocks/stripped_cherry_wood')
  RECIPES_BUILDING_BLOCKS_STRIPPED_CRIMSON_HYPHAE = Kee[str](
    'recipes/building_blocks/stripped_crimson_hyphae')
  RECIPES_BUILDING_BLOCKS_STRIPPED_DARK_OAK_WOOD = Kee[str](
    'recipes/building_blocks/stripped_dark_oak_wood')
  RECIPES_BUILDING_BLOCKS_STRIPPED_JUNGLE_WOOD = Kee[str](
    'recipes/building_blocks/stripped_jungle_wood')
  RECIPES_BUILDING_BLOCKS_STRIPPED_MANGROVE_WOOD = Kee[str](
    'recipes/building_blocks/stripped_mangrove_wood')
  RECIPES_BUILDING_BLOCKS_STRIPPED_OAK_WOOD = Kee[str](
    'recipes/building_blocks/stripped_oak_wood')
  RECIPES_BUILDING_BLOCKS_STRIPPED_PALE_OAK_WOOD = Kee[str](
    'recipes/building_blocks/stripped_pale_oak_wood')
  RECIPES_BUILDING_BLOCKS_STRIPPED_POPLAR_WOOD = Kee[str](
    'recipes/building_blocks/stripped_poplar_wood')
  RECIPES_BUILDING_BLOCKS_STRIPPED_SPRUCE_WOOD = Kee[str](
    'recipes/building_blocks/stripped_spruce_wood')
  RECIPES_BUILDING_BLOCKS_STRIPPED_WARPED_HYPHAE = Kee[str](
    'recipes/building_blocks/stripped_warped_hyphae')
  RECIPES_BUILDING_BLOCKS_SULFUR_BRICK_SLAB = Kee[str](
    'recipes/building_blocks/sulfur_brick_slab')
  RECIPES_BUILDING_BLOCKS_SULFUR_BRICK_SLAB_FROM_POLISHED_SULFUR_STONECUTTING = Kee[str](
    'recipes/building_blocks/sulfur_brick_slab_from_polished_sulfur_stonecutting')
  RECIPES_BUILDING_BLOCKS_SULFUR_BRICK_SLAB_FROM_SULFUR_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/sulfur_brick_slab_from_sulfur_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_SULFUR_BRICK_SLAB_FROM_SULFUR_STONECUTTING = Kee[str](
    'recipes/building_blocks/sulfur_brick_slab_from_sulfur_stonecutting')
  RECIPES_BUILDING_BLOCKS_SULFUR_BRICK_STAIRS = Kee[str](
    'recipes/building_blocks/sulfur_brick_stairs')
  RECIPES_BUILDING_BLOCKS_SULFUR_BRICK_STAIRS_FROM_POLISHED_SULFUR_STONECUTTING = Kee[str](
    'recipes/building_blocks/sulfur_brick_stairs_from_polished_sulfur_stonecutting')
  RECIPES_BUILDING_BLOCKS_SULFUR_BRICK_STAIRS_FROM_SULFUR_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/sulfur_brick_stairs_from_sulfur_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_SULFUR_BRICK_STAIRS_FROM_SULFUR_STONECUTTING = Kee[str](
    'recipes/building_blocks/sulfur_brick_stairs_from_sulfur_stonecutting')
  RECIPES_BUILDING_BLOCKS_SULFUR_BRICKS = Kee[str](
    'recipes/building_blocks/sulfur_bricks')
  RECIPES_BUILDING_BLOCKS_SULFUR_BRICKS_FROM_POLISHED_SULFUR_STONECUTTING = Kee[str](
    'recipes/building_blocks/sulfur_bricks_from_polished_sulfur_stonecutting')
  RECIPES_BUILDING_BLOCKS_SULFUR_BRICKS_FROM_SULFUR_STONECUTTING = Kee[str](
    'recipes/building_blocks/sulfur_bricks_from_sulfur_stonecutting')
  RECIPES_BUILDING_BLOCKS_SULFUR_FROM_SULFUR_SPIKES = Kee[str](
    'recipes/building_blocks/sulfur_from_sulfur_spikes')
  RECIPES_BUILDING_BLOCKS_SULFUR_SLAB = Kee[str](
    'recipes/building_blocks/sulfur_slab')
  RECIPES_BUILDING_BLOCKS_SULFUR_SLAB_FROM_SULFUR_STONECUTTING = Kee[str](
    'recipes/building_blocks/sulfur_slab_from_sulfur_stonecutting')
  RECIPES_BUILDING_BLOCKS_SULFUR_STAIRS = Kee[str](
    'recipes/building_blocks/sulfur_stairs')
  RECIPES_BUILDING_BLOCKS_SULFUR_STAIRS_FROM_SULFUR_STONECUTTING = Kee[str](
    'recipes/building_blocks/sulfur_stairs_from_sulfur_stonecutting')
  RECIPES_BUILDING_BLOCKS_TERRACOTTA = Kee[str](
    'recipes/building_blocks/terracotta')
  RECIPES_BUILDING_BLOCKS_TINTED_GLASS = Kee[str](
    'recipes/building_blocks/tinted_glass')
  RECIPES_BUILDING_BLOCKS_TUFF_BRICK_SLAB = Kee[str](
    'recipes/building_blocks/tuff_brick_slab')
  RECIPES_BUILDING_BLOCKS_TUFF_BRICK_SLAB_FROM_POLISHED_TUFF_STONECUTTING = Kee[str](
    'recipes/building_blocks/tuff_brick_slab_from_polished_tuff_stonecutting')
  RECIPES_BUILDING_BLOCKS_TUFF_BRICK_SLAB_FROM_TUFF_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/tuff_brick_slab_from_tuff_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_TUFF_BRICK_SLAB_FROM_TUFF_STONECUTTING = Kee[str](
    'recipes/building_blocks/tuff_brick_slab_from_tuff_stonecutting')
  RECIPES_BUILDING_BLOCKS_TUFF_BRICK_STAIRS = Kee[str](
    'recipes/building_blocks/tuff_brick_stairs')
  RECIPES_BUILDING_BLOCKS_TUFF_BRICK_STAIRS_FROM_POLISHED_TUFF_STONECUTTING = Kee[str](
    'recipes/building_blocks/tuff_brick_stairs_from_polished_tuff_stonecutting')
  RECIPES_BUILDING_BLOCKS_TUFF_BRICK_STAIRS_FROM_TUFF_BRICKS_STONECUTTING = Kee[str](
    'recipes/building_blocks/tuff_brick_stairs_from_tuff_bricks_stonecutting')
  RECIPES_BUILDING_BLOCKS_TUFF_BRICK_STAIRS_FROM_TUFF_STONECUTTING = Kee[str](
    'recipes/building_blocks/tuff_brick_stairs_from_tuff_stonecutting')
  RECIPES_BUILDING_BLOCKS_TUFF_BRICKS = Kee[str](
    'recipes/building_blocks/tuff_bricks')
  RECIPES_BUILDING_BLOCKS_TUFF_BRICKS_FROM_POLISHED_TUFF_STONECUTTING = Kee[str](
    'recipes/building_blocks/tuff_bricks_from_polished_tuff_stonecutting')
  RECIPES_BUILDING_BLOCKS_TUFF_BRICKS_FROM_TUFF_STONECUTTING = Kee[str](
    'recipes/building_blocks/tuff_bricks_from_tuff_stonecutting')
  RECIPES_BUILDING_BLOCKS_TUFF_SLAB = Kee[str](
    'recipes/building_blocks/tuff_slab')
  RECIPES_BUILDING_BLOCKS_TUFF_SLAB_FROM_TUFF_STONECUTTING = Kee[str](
    'recipes/building_blocks/tuff_slab_from_tuff_stonecutting')
  RECIPES_BUILDING_BLOCKS_TUFF_STAIRS = Kee[str](
    'recipes/building_blocks/tuff_stairs')
  RECIPES_BUILDING_BLOCKS_TUFF_STAIRS_FROM_TUFF_STONECUTTING = Kee[str](
    'recipes/building_blocks/tuff_stairs_from_tuff_stonecutting')
  RECIPES_BUILDING_BLOCKS_WARPED_HYPHAE = Kee[str](
    'recipes/building_blocks/warped_hyphae')
  RECIPES_BUILDING_BLOCKS_WARPED_PLANKS = Kee[str](
    'recipes/building_blocks/warped_planks')
  RECIPES_BUILDING_BLOCKS_WARPED_SLAB = Kee[str](
    'recipes/building_blocks/warped_slab')
  RECIPES_BUILDING_BLOCKS_WARPED_STAIRS = Kee[str](
    'recipes/building_blocks/warped_stairs')
  RECIPES_BUILDING_BLOCKS_WAXED_CHISELED_COPPER = Kee[str](
    'recipes/building_blocks/waxed_chiseled_copper')
  RECIPES_BUILDING_BLOCKS_WAXED_CHISELED_COPPER_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_chiseled_copper_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_CHISELED_COPPER_FROM_WAXED_COPPER_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_chiseled_copper_from_waxed_copper_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_CHISELED_COPPER_FROM_WAXED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_chiseled_copper_from_waxed_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_COPPER_BARS_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_copper_bars_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_COPPER_BLOCK_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_copper_block_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_COPPER_BULB_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_copper_bulb_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_COPPER_CHAIN_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_copper_chain_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_COPPER_CHEST_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_copper_chest_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_COPPER_DOOR_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_copper_door_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_COPPER_GOLEM_STATUE_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_copper_golem_statue_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_COPPER_GRATE = Kee[str](
    'recipes/building_blocks/waxed_copper_grate')
  RECIPES_BUILDING_BLOCKS_WAXED_COPPER_GRATE_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_copper_grate_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_COPPER_GRATE_FROM_WAXED_COPPER_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_copper_grate_from_waxed_copper_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_COPPER_LANTERN_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_copper_lantern_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_COPPER_TRAPDOOR_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_copper_trapdoor_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_CUT_COPPER = Kee[str](
    'recipes/building_blocks/waxed_cut_copper')
  RECIPES_BUILDING_BLOCKS_WAXED_CUT_COPPER_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_cut_copper_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_CUT_COPPER_FROM_WAXED_COPPER_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_cut_copper_from_waxed_copper_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_CUT_COPPER_SLAB = Kee[str](
    'recipes/building_blocks/waxed_cut_copper_slab')
  RECIPES_BUILDING_BLOCKS_WAXED_CUT_COPPER_SLAB_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_cut_copper_slab_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_CUT_COPPER_SLAB_FROM_WAXED_COPPER_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_cut_copper_slab_from_waxed_copper_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_CUT_COPPER_SLAB_FROM_WAXED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_cut_copper_slab_from_waxed_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_CUT_COPPER_STAIRS = Kee[str](
    'recipes/building_blocks/waxed_cut_copper_stairs')
  RECIPES_BUILDING_BLOCKS_WAXED_CUT_COPPER_STAIRS_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_cut_copper_stairs_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_CUT_COPPER_STAIRS_FROM_WAXED_COPPER_BLOCK_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_cut_copper_stairs_from_waxed_copper_block_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_CUT_COPPER_STAIRS_FROM_WAXED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_cut_copper_stairs_from_waxed_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_CHISELED_COPPER = Kee[str](
    'recipes/building_blocks/waxed_exposed_chiseled_copper')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_CHISELED_COPPER_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_exposed_chiseled_copper_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_CHISELED_COPPER_FROM_WAXED_EXPOSED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_exposed_chiseled_copper_from_waxed_exposed_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_CHISELED_COPPER_FROM_WAXED_EXPOSED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_exposed_chiseled_copper_from_waxed_exposed_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_COPPER_BARS_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_exposed_copper_bars_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_COPPER_BULB_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_exposed_copper_bulb_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_COPPER_CHAIN_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_exposed_copper_chain_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_COPPER_CHEST_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_exposed_copper_chest_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_COPPER_DOOR_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_exposed_copper_door_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_COPPER_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_exposed_copper_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_COPPER_GOLEM_STATUE_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_exposed_copper_golem_statue_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_COPPER_GRATE = Kee[str](
    'recipes/building_blocks/waxed_exposed_copper_grate')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_COPPER_GRATE_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_exposed_copper_grate_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_COPPER_GRATE_FROM_WAXED_EXPOSED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_exposed_copper_grate_from_waxed_exposed_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_COPPER_LANTERN_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_exposed_copper_lantern_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_COPPER_TRAPDOOR_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_exposed_copper_trapdoor_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_CUT_COPPER = Kee[str](
    'recipes/building_blocks/waxed_exposed_cut_copper')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_CUT_COPPER_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_exposed_cut_copper_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_CUT_COPPER_FROM_WAXED_EXPOSED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_exposed_cut_copper_from_waxed_exposed_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_CUT_COPPER_SLAB = Kee[str](
    'recipes/building_blocks/waxed_exposed_cut_copper_slab')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_CUT_COPPER_SLAB_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_exposed_cut_copper_slab_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_CUT_COPPER_SLAB_FROM_WAXED_EXPOSED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_exposed_cut_copper_slab_from_waxed_exposed_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_CUT_COPPER_SLAB_FROM_WAXED_EXPOSED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_exposed_cut_copper_slab_from_waxed_exposed_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_CUT_COPPER_STAIRS = Kee[str](
    'recipes/building_blocks/waxed_exposed_cut_copper_stairs')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_CUT_COPPER_STAIRS_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_exposed_cut_copper_stairs_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_CUT_COPPER_STAIRS_FROM_WAXED_EXPOSED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_exposed_cut_copper_stairs_from_waxed_exposed_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_CUT_COPPER_STAIRS_FROM_WAXED_EXPOSED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_exposed_cut_copper_stairs_from_waxed_exposed_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_EXPOSED_LIGHTNING_ROD_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_exposed_lightning_rod_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_LIGHTNING_ROD_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_lightning_rod_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_CHISELED_COPPER = Kee[str](
    'recipes/building_blocks/waxed_oxidized_chiseled_copper')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_CHISELED_COPPER_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_oxidized_chiseled_copper_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_CHISELED_COPPER_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_oxidized_chiseled_copper_from_waxed_oxidized_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_CHISELED_COPPER_FROM_WAXED_OXIDIZED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_oxidized_chiseled_copper_from_waxed_oxidized_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_COPPER_BARS_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_oxidized_copper_bars_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_COPPER_BULB_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_oxidized_copper_bulb_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_COPPER_CHAIN_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_oxidized_copper_chain_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_COPPER_CHEST_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_oxidized_copper_chest_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_COPPER_DOOR_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_oxidized_copper_door_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_COPPER_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_oxidized_copper_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_COPPER_GOLEM_STATUE_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_oxidized_copper_golem_statue_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_COPPER_GRATE = Kee[str](
    'recipes/building_blocks/waxed_oxidized_copper_grate')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_COPPER_GRATE_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_oxidized_copper_grate_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_COPPER_GRATE_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_oxidized_copper_grate_from_waxed_oxidized_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_COPPER_LANTERN_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_oxidized_copper_lantern_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_COPPER_TRAPDOOR_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_oxidized_copper_trapdoor_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_CUT_COPPER = Kee[str](
    'recipes/building_blocks/waxed_oxidized_cut_copper')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_CUT_COPPER_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_oxidized_cut_copper_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_CUT_COPPER_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_oxidized_cut_copper_from_waxed_oxidized_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_CUT_COPPER_SLAB = Kee[str](
    'recipes/building_blocks/waxed_oxidized_cut_copper_slab')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_CUT_COPPER_SLAB_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_oxidized_cut_copper_slab_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_CUT_COPPER_SLAB_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_oxidized_cut_copper_slab_from_waxed_oxidized_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_CUT_COPPER_SLAB_FROM_WAXED_OXIDIZED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_oxidized_cut_copper_slab_from_waxed_oxidized_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_CUT_COPPER_STAIRS = Kee[str](
    'recipes/building_blocks/waxed_oxidized_cut_copper_stairs')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_CUT_COPPER_STAIRS_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_oxidized_cut_copper_stairs_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_CUT_COPPER_STAIRS_FROM_WAXED_OXIDIZED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_CUT_COPPER_STAIRS_FROM_WAXED_OXIDIZED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_OXIDIZED_LIGHTNING_ROD_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_oxidized_lightning_rod_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_CHISELED_COPPER = Kee[str](
    'recipes/building_blocks/waxed_weathered_chiseled_copper')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_CHISELED_COPPER_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_weathered_chiseled_copper_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_CHISELED_COPPER_FROM_WAXED_WEATHERED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_weathered_chiseled_copper_from_waxed_weathered_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_CHISELED_COPPER_FROM_WAXED_WEATHERED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_weathered_chiseled_copper_from_waxed_weathered_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_COPPER_BARS_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_weathered_copper_bars_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_COPPER_BULB_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_weathered_copper_bulb_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_COPPER_CHAIN_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_weathered_copper_chain_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_COPPER_CHEST_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_weathered_copper_chest_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_COPPER_DOOR_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_weathered_copper_door_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_COPPER_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_weathered_copper_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_COPPER_GOLEM_STATUE_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_weathered_copper_golem_statue_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_COPPER_GRATE = Kee[str](
    'recipes/building_blocks/waxed_weathered_copper_grate')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_COPPER_GRATE_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_weathered_copper_grate_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_COPPER_GRATE_FROM_WAXED_WEATHERED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_weathered_copper_grate_from_waxed_weathered_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_COPPER_LANTERN_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_weathered_copper_lantern_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_COPPER_TRAPDOOR_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_weathered_copper_trapdoor_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_CUT_COPPER = Kee[str](
    'recipes/building_blocks/waxed_weathered_cut_copper')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_CUT_COPPER_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_weathered_cut_copper_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_CUT_COPPER_FROM_WAXED_WEATHERED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_weathered_cut_copper_from_waxed_weathered_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_CUT_COPPER_SLAB = Kee[str](
    'recipes/building_blocks/waxed_weathered_cut_copper_slab')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_CUT_COPPER_SLAB_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_weathered_cut_copper_slab_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_CUT_COPPER_SLAB_FROM_WAXED_WEATHERED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_weathered_cut_copper_slab_from_waxed_weathered_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_CUT_COPPER_SLAB_FROM_WAXED_WEATHERED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_weathered_cut_copper_slab_from_waxed_weathered_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_CUT_COPPER_STAIRS = Kee[str](
    'recipes/building_blocks/waxed_weathered_cut_copper_stairs')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_CUT_COPPER_STAIRS_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_weathered_cut_copper_stairs_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_CUT_COPPER_STAIRS_FROM_WAXED_WEATHERED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_weathered_cut_copper_stairs_from_waxed_weathered_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_CUT_COPPER_STAIRS_FROM_WAXED_WEATHERED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/waxed_weathered_cut_copper_stairs_from_waxed_weathered_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WAXED_WEATHERED_LIGHTNING_ROD_FROM_HONEYCOMB = Kee[str](
    'recipes/building_blocks/waxed_weathered_lightning_rod_from_honeycomb')
  RECIPES_BUILDING_BLOCKS_WEATHERED_CHISELED_COPPER = Kee[str](
    'recipes/building_blocks/weathered_chiseled_copper')
  RECIPES_BUILDING_BLOCKS_WEATHERED_CHISELED_COPPER_FROM_WEATHERED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/weathered_chiseled_copper_from_weathered_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WEATHERED_CHISELED_COPPER_FROM_WEATHERED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/weathered_chiseled_copper_from_weathered_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WEATHERED_COPPER_GRATE = Kee[str](
    'recipes/building_blocks/weathered_copper_grate')
  RECIPES_BUILDING_BLOCKS_WEATHERED_COPPER_GRATE_FROM_WEATHERED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/weathered_copper_grate_from_weathered_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WEATHERED_CUT_COPPER = Kee[str](
    'recipes/building_blocks/weathered_cut_copper')
  RECIPES_BUILDING_BLOCKS_WEATHERED_CUT_COPPER_FROM_WEATHERED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/weathered_cut_copper_from_weathered_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WEATHERED_CUT_COPPER_SLAB = Kee[str](
    'recipes/building_blocks/weathered_cut_copper_slab')
  RECIPES_BUILDING_BLOCKS_WEATHERED_CUT_COPPER_SLAB_FROM_WEATHERED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/weathered_cut_copper_slab_from_weathered_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WEATHERED_CUT_COPPER_SLAB_FROM_WEATHERED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/weathered_cut_copper_slab_from_weathered_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WEATHERED_CUT_COPPER_STAIRS = Kee[str](
    'recipes/building_blocks/weathered_cut_copper_stairs')
  RECIPES_BUILDING_BLOCKS_WEATHERED_CUT_COPPER_STAIRS_FROM_WEATHERED_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/weathered_cut_copper_stairs_from_weathered_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WEATHERED_CUT_COPPER_STAIRS_FROM_WEATHERED_CUT_COPPER_STONECUTTING = Kee[str](
    'recipes/building_blocks/weathered_cut_copper_stairs_from_weathered_cut_copper_stonecutting')
  RECIPES_BUILDING_BLOCKS_WHITE_CONCRETE_POWDER = Kee[str](
    'recipes/building_blocks/white_concrete_powder')
  RECIPES_BUILDING_BLOCKS_WHITE_CONCRETE_SLAB = Kee[str](
    'recipes/building_blocks/white_concrete_slab')
  RECIPES_BUILDING_BLOCKS_WHITE_CONCRETE_SLAB_FROM_WHITE_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/white_concrete_slab_from_white_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_WHITE_CONCRETE_STAIRS = Kee[str](
    'recipes/building_blocks/white_concrete_stairs')
  RECIPES_BUILDING_BLOCKS_WHITE_CONCRETE_STAIRS_FROM_WHITE_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/white_concrete_stairs_from_white_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_WHITE_STAINED_GLASS = Kee[str](
    'recipes/building_blocks/white_stained_glass')
  RECIPES_BUILDING_BLOCKS_WHITE_TERRACOTTA = Kee[str](
    'recipes/building_blocks/white_terracotta')
  RECIPES_BUILDING_BLOCKS_WHITE_WOOL_FROM_STRING = Kee[str](
    'recipes/building_blocks/white_wool_from_string')
  RECIPES_BUILDING_BLOCKS_WHITE_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/white_wool_slab')
  RECIPES_BUILDING_BLOCKS_WHITE_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/white_wool_stairs')
  RECIPES_BUILDING_BLOCKS_YELLOW_CONCRETE_POWDER = Kee[str](
    'recipes/building_blocks/yellow_concrete_powder')
  RECIPES_BUILDING_BLOCKS_YELLOW_CONCRETE_SLAB = Kee[str](
    'recipes/building_blocks/yellow_concrete_slab')
  RECIPES_BUILDING_BLOCKS_YELLOW_CONCRETE_SLAB_FROM_YELLOW_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/yellow_concrete_slab_from_yellow_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_YELLOW_CONCRETE_STAIRS = Kee[str](
    'recipes/building_blocks/yellow_concrete_stairs')
  RECIPES_BUILDING_BLOCKS_YELLOW_CONCRETE_STAIRS_FROM_YELLOW_CONCRETE_STONECUTTING = Kee[str](
    'recipes/building_blocks/yellow_concrete_stairs_from_yellow_concrete_stonecutting')
  RECIPES_BUILDING_BLOCKS_YELLOW_STAINED_GLASS = Kee[str](
    'recipes/building_blocks/yellow_stained_glass')
  RECIPES_BUILDING_BLOCKS_YELLOW_TERRACOTTA = Kee[str](
    'recipes/building_blocks/yellow_terracotta')
  RECIPES_BUILDING_BLOCKS_YELLOW_WOOL = Kee[str](
    'recipes/building_blocks/yellow_wool')
  RECIPES_BUILDING_BLOCKS_YELLOW_WOOL_SLAB = Kee[str](
    'recipes/building_blocks/yellow_wool_slab')
  RECIPES_BUILDING_BLOCKS_YELLOW_WOOL_STAIRS = Kee[str](
    'recipes/building_blocks/yellow_wool_stairs')
  RECIPES_COMBAT_ARROW = Kee[str]('recipes/combat/arrow')
  RECIPES_COMBAT_BLACK_HARNESS = Kee[str]('recipes/combat/black_harness')
  RECIPES_COMBAT_BLUE_HARNESS = Kee[str]('recipes/combat/blue_harness')
  RECIPES_COMBAT_BOW = Kee[str]('recipes/combat/bow')
  RECIPES_COMBAT_BROWN_HARNESS = Kee[str]('recipes/combat/brown_harness')
  RECIPES_COMBAT_COPPER_BOOTS = Kee[str]('recipes/combat/copper_boots')
  RECIPES_COMBAT_COPPER_CHESTPLATE = Kee[str](
    'recipes/combat/copper_chestplate')
  RECIPES_COMBAT_COPPER_HELMET = Kee[str]('recipes/combat/copper_helmet')
  RECIPES_COMBAT_COPPER_LEGGINGS = Kee[str]('recipes/combat/copper_leggings')
  RECIPES_COMBAT_COPPER_SPEAR = Kee[str]('recipes/combat/copper_spear')
  RECIPES_COMBAT_COPPER_SWORD = Kee[str]('recipes/combat/copper_sword')
  RECIPES_COMBAT_CROSSBOW = Kee[str]('recipes/combat/crossbow')
  RECIPES_COMBAT_CYAN_HARNESS = Kee[str]('recipes/combat/cyan_harness')
  RECIPES_COMBAT_DIAMOND_BOOTS = Kee[str]('recipes/combat/diamond_boots')
  RECIPES_COMBAT_DIAMOND_CHESTPLATE = Kee[str](
    'recipes/combat/diamond_chestplate')
  RECIPES_COMBAT_DIAMOND_HELMET = Kee[str]('recipes/combat/diamond_helmet')
  RECIPES_COMBAT_DIAMOND_LEGGINGS = Kee[str]('recipes/combat/diamond_leggings')
  RECIPES_COMBAT_DIAMOND_SPEAR = Kee[str]('recipes/combat/diamond_spear')
  RECIPES_COMBAT_DIAMOND_SWORD = Kee[str]('recipes/combat/diamond_sword')
  RECIPES_COMBAT_DYE_BLACK_HARNESS = Kee[str](
    'recipes/combat/dye_black_harness')
  RECIPES_COMBAT_DYE_BLUE_HARNESS = Kee[str]('recipes/combat/dye_blue_harness')
  RECIPES_COMBAT_DYE_BROWN_HARNESS = Kee[str](
    'recipes/combat/dye_brown_harness')
  RECIPES_COMBAT_DYE_CYAN_HARNESS = Kee[str]('recipes/combat/dye_cyan_harness')
  RECIPES_COMBAT_DYE_GRAY_HARNESS = Kee[str]('recipes/combat/dye_gray_harness')
  RECIPES_COMBAT_DYE_GREEN_HARNESS = Kee[str](
    'recipes/combat/dye_green_harness')
  RECIPES_COMBAT_DYE_LIGHT_BLUE_HARNESS = Kee[str](
    'recipes/combat/dye_light_blue_harness')
  RECIPES_COMBAT_DYE_LIGHT_GRAY_HARNESS = Kee[str](
    'recipes/combat/dye_light_gray_harness')
  RECIPES_COMBAT_DYE_LIME_HARNESS = Kee[str]('recipes/combat/dye_lime_harness')
  RECIPES_COMBAT_DYE_MAGENTA_HARNESS = Kee[str](
    'recipes/combat/dye_magenta_harness')
  RECIPES_COMBAT_DYE_ORANGE_HARNESS = Kee[str](
    'recipes/combat/dye_orange_harness')
  RECIPES_COMBAT_DYE_PINK_HARNESS = Kee[str]('recipes/combat/dye_pink_harness')
  RECIPES_COMBAT_DYE_PURPLE_HARNESS = Kee[str](
    'recipes/combat/dye_purple_harness')
  RECIPES_COMBAT_DYE_RED_HARNESS = Kee[str]('recipes/combat/dye_red_harness')
  RECIPES_COMBAT_DYE_WHITE_HARNESS = Kee[str](
    'recipes/combat/dye_white_harness')
  RECIPES_COMBAT_DYE_YELLOW_HARNESS = Kee[str](
    'recipes/combat/dye_yellow_harness')
  RECIPES_COMBAT_GOLDEN_BOOTS = Kee[str]('recipes/combat/golden_boots')
  RECIPES_COMBAT_GOLDEN_CHESTPLATE = Kee[str](
    'recipes/combat/golden_chestplate')
  RECIPES_COMBAT_GOLDEN_HELMET = Kee[str]('recipes/combat/golden_helmet')
  RECIPES_COMBAT_GOLDEN_LEGGINGS = Kee[str]('recipes/combat/golden_leggings')
  RECIPES_COMBAT_GOLDEN_SPEAR = Kee[str]('recipes/combat/golden_spear')
  RECIPES_COMBAT_GOLDEN_SWORD = Kee[str]('recipes/combat/golden_sword')
  RECIPES_COMBAT_GRAY_HARNESS = Kee[str]('recipes/combat/gray_harness')
  RECIPES_COMBAT_GREEN_HARNESS = Kee[str]('recipes/combat/green_harness')
  RECIPES_COMBAT_IRON_BOOTS = Kee[str]('recipes/combat/iron_boots')
  RECIPES_COMBAT_IRON_CHESTPLATE = Kee[str]('recipes/combat/iron_chestplate')
  RECIPES_COMBAT_IRON_HELMET = Kee[str]('recipes/combat/iron_helmet')
  RECIPES_COMBAT_IRON_LEGGINGS = Kee[str]('recipes/combat/iron_leggings')
  RECIPES_COMBAT_IRON_SPEAR = Kee[str]('recipes/combat/iron_spear')
  RECIPES_COMBAT_IRON_SWORD = Kee[str]('recipes/combat/iron_sword')
  RECIPES_COMBAT_LEATHER_BOOTS = Kee[str]('recipes/combat/leather_boots')
  RECIPES_COMBAT_LEATHER_CHESTPLATE = Kee[str](
    'recipes/combat/leather_chestplate')
  RECIPES_COMBAT_LEATHER_HELMET = Kee[str]('recipes/combat/leather_helmet')
  RECIPES_COMBAT_LEATHER_LEGGINGS = Kee[str]('recipes/combat/leather_leggings')
  RECIPES_COMBAT_LIGHT_BLUE_HARNESS = Kee[str](
    'recipes/combat/light_blue_harness')
  RECIPES_COMBAT_LIGHT_GRAY_HARNESS = Kee[str](
    'recipes/combat/light_gray_harness')
  RECIPES_COMBAT_LIME_HARNESS = Kee[str]('recipes/combat/lime_harness')
  RECIPES_COMBAT_MACE = Kee[str]('recipes/combat/mace')
  RECIPES_COMBAT_MAGENTA_HARNESS = Kee[str]('recipes/combat/magenta_harness')
  RECIPES_COMBAT_NETHERITE_BOOTS_SMITHING = Kee[str](
    'recipes/combat/netherite_boots_smithing')
  RECIPES_COMBAT_NETHERITE_CHESTPLATE_SMITHING = Kee[str](
    'recipes/combat/netherite_chestplate_smithing')
  RECIPES_COMBAT_NETHERITE_HELMET_SMITHING = Kee[str](
    'recipes/combat/netherite_helmet_smithing')
  RECIPES_COMBAT_NETHERITE_HORSE_ARMOR_SMITHING = Kee[str](
    'recipes/combat/netherite_horse_armor_smithing')
  RECIPES_COMBAT_NETHERITE_LEGGINGS_SMITHING = Kee[str](
    'recipes/combat/netherite_leggings_smithing')
  RECIPES_COMBAT_NETHERITE_NAUTILUS_ARMOR_SMITHING = Kee[str](
    'recipes/combat/netherite_nautilus_armor_smithing')
  RECIPES_COMBAT_NETHERITE_SPEAR_SMITHING = Kee[str](
    'recipes/combat/netherite_spear_smithing')
  RECIPES_COMBAT_NETHERITE_SWORD_SMITHING = Kee[str](
    'recipes/combat/netherite_sword_smithing')
  RECIPES_COMBAT_ORANGE_HARNESS = Kee[str]('recipes/combat/orange_harness')
  RECIPES_COMBAT_PINK_HARNESS = Kee[str]('recipes/combat/pink_harness')
  RECIPES_COMBAT_PURPLE_HARNESS = Kee[str]('recipes/combat/purple_harness')
  RECIPES_COMBAT_RED_HARNESS = Kee[str]('recipes/combat/red_harness')
  RECIPES_COMBAT_SADDLE = Kee[str]('recipes/combat/saddle')
  RECIPES_COMBAT_SHIELD = Kee[str]('recipes/combat/shield')
  RECIPES_COMBAT_SPECTRAL_ARROW = Kee[str]('recipes/combat/spectral_arrow')
  RECIPES_COMBAT_STONE_SPEAR = Kee[str]('recipes/combat/stone_spear')
  RECIPES_COMBAT_STONE_SWORD = Kee[str]('recipes/combat/stone_sword')
  RECIPES_COMBAT_TURTLE_HELMET = Kee[str]('recipes/combat/turtle_helmet')
  RECIPES_COMBAT_WHITE_HARNESS = Kee[str]('recipes/combat/white_harness')
  RECIPES_COMBAT_WOLF_ARMOR = Kee[str]('recipes/combat/wolf_armor')
  RECIPES_COMBAT_WOODEN_SPEAR = Kee[str]('recipes/combat/wooden_spear')
  RECIPES_COMBAT_WOODEN_SWORD = Kee[str]('recipes/combat/wooden_sword')
  RECIPES_COMBAT_YELLOW_HARNESS = Kee[str]('recipes/combat/yellow_harness')
  RECIPES_DECORATIONS_ACACIA_FENCE = Kee[str](
    'recipes/decorations/acacia_fence')
  RECIPES_DECORATIONS_ACACIA_HANGING_SIGN = Kee[str](
    'recipes/decorations/acacia_hanging_sign')
  RECIPES_DECORATIONS_ACACIA_SHELF = Kee[str](
    'recipes/decorations/acacia_shelf')
  RECIPES_DECORATIONS_ACACIA_SIGN = Kee[str]('recipes/decorations/acacia_sign')
  RECIPES_DECORATIONS_ANDESITE_WALL = Kee[str](
    'recipes/decorations/andesite_wall')
  RECIPES_DECORATIONS_ANDESITE_WALL_FROM_ANDESITE_STONECUTTING = Kee[str](
    'recipes/decorations/andesite_wall_from_andesite_stonecutting')
  RECIPES_DECORATIONS_ANVIL = Kee[str]('recipes/decorations/anvil')
  RECIPES_DECORATIONS_ARMOR_STAND = Kee[str]('recipes/decorations/armor_stand')
  RECIPES_DECORATIONS_BAMBOO_FENCE = Kee[str](
    'recipes/decorations/bamboo_fence')
  RECIPES_DECORATIONS_BAMBOO_HANGING_SIGN = Kee[str](
    'recipes/decorations/bamboo_hanging_sign')
  RECIPES_DECORATIONS_BAMBOO_MOSAIC = Kee[str](
    'recipes/decorations/bamboo_mosaic')
  RECIPES_DECORATIONS_BAMBOO_SHELF = Kee[str](
    'recipes/decorations/bamboo_shelf')
  RECIPES_DECORATIONS_BAMBOO_SIGN = Kee[str]('recipes/decorations/bamboo_sign')
  RECIPES_DECORATIONS_BARREL = Kee[str]('recipes/decorations/barrel')
  RECIPES_DECORATIONS_BEEHIVE = Kee[str]('recipes/decorations/beehive')
  RECIPES_DECORATIONS_BIRCH_FENCE = Kee[str]('recipes/decorations/birch_fence')
  RECIPES_DECORATIONS_BIRCH_HANGING_SIGN = Kee[str](
    'recipes/decorations/birch_hanging_sign')
  RECIPES_DECORATIONS_BIRCH_SHELF = Kee[str]('recipes/decorations/birch_shelf')
  RECIPES_DECORATIONS_BIRCH_SIGN = Kee[str]('recipes/decorations/birch_sign')
  RECIPES_DECORATIONS_BLACK_BANNER = Kee[str](
    'recipes/decorations/black_banner')
  RECIPES_DECORATIONS_BLACK_BED = Kee[str]('recipes/decorations/black_bed')
  RECIPES_DECORATIONS_BLACK_BED_FROM_WHITE_BED = Kee[str](
    'recipes/decorations/black_bed_from_white_bed')
  RECIPES_DECORATIONS_BLACK_CANDLE = Kee[str](
    'recipes/decorations/black_candle')
  RECIPES_DECORATIONS_BLACK_CARPET = Kee[str](
    'recipes/decorations/black_carpet')
  RECIPES_DECORATIONS_BLACK_CARPET_FROM_WHITE_CARPET = Kee[str](
    'recipes/decorations/black_carpet_from_white_carpet')
  RECIPES_DECORATIONS_BLACK_CUSHION = Kee[str](
    'recipes/decorations/black_cushion')
  RECIPES_DECORATIONS_BLACK_GLAZED_TERRACOTTA = Kee[str](
    'recipes/decorations/black_glazed_terracotta')
  RECIPES_DECORATIONS_BLACK_SHULKER_BOX = Kee[str](
    'recipes/decorations/black_shulker_box')
  RECIPES_DECORATIONS_BLACK_STAINED_GLASS_PANE = Kee[str](
    'recipes/decorations/black_stained_glass_pane')
  RECIPES_DECORATIONS_BLACK_STAINED_GLASS_PANE_FROM_GLASS_PANE = Kee[str](
    'recipes/decorations/black_stained_glass_pane_from_glass_pane')
  RECIPES_DECORATIONS_BLACKSTONE_WALL = Kee[str](
    'recipes/decorations/blackstone_wall')
  RECIPES_DECORATIONS_BLACKSTONE_WALL_FROM_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/decorations/blackstone_wall_from_blackstone_stonecutting')
  RECIPES_DECORATIONS_BLAST_FURNACE = Kee[str](
    'recipes/decorations/blast_furnace')
  RECIPES_DECORATIONS_BLUE_BANNER = Kee[str]('recipes/decorations/blue_banner')
  RECIPES_DECORATIONS_BLUE_BED = Kee[str]('recipes/decorations/blue_bed')
  RECIPES_DECORATIONS_BLUE_BED_FROM_WHITE_BED = Kee[str](
    'recipes/decorations/blue_bed_from_white_bed')
  RECIPES_DECORATIONS_BLUE_CANDLE = Kee[str]('recipes/decorations/blue_candle')
  RECIPES_DECORATIONS_BLUE_CARPET = Kee[str]('recipes/decorations/blue_carpet')
  RECIPES_DECORATIONS_BLUE_CARPET_FROM_WHITE_CARPET = Kee[str](
    'recipes/decorations/blue_carpet_from_white_carpet')
  RECIPES_DECORATIONS_BLUE_CUSHION = Kee[str](
    'recipes/decorations/blue_cushion')
  RECIPES_DECORATIONS_BLUE_GLAZED_TERRACOTTA = Kee[str](
    'recipes/decorations/blue_glazed_terracotta')
  RECIPES_DECORATIONS_BLUE_SHULKER_BOX = Kee[str](
    'recipes/decorations/blue_shulker_box')
  RECIPES_DECORATIONS_BLUE_STAINED_GLASS_PANE = Kee[str](
    'recipes/decorations/blue_stained_glass_pane')
  RECIPES_DECORATIONS_BLUE_STAINED_GLASS_PANE_FROM_GLASS_PANE = Kee[str](
    'recipes/decorations/blue_stained_glass_pane_from_glass_pane')
  RECIPES_DECORATIONS_BRICK_WALL = Kee[str]('recipes/decorations/brick_wall')
  RECIPES_DECORATIONS_BRICK_WALL_FROM_BRICKS_STONECUTTING = Kee[str](
    'recipes/decorations/brick_wall_from_bricks_stonecutting')
  RECIPES_DECORATIONS_BROWN_BANNER = Kee[str](
    'recipes/decorations/brown_banner')
  RECIPES_DECORATIONS_BROWN_BED = Kee[str]('recipes/decorations/brown_bed')
  RECIPES_DECORATIONS_BROWN_BED_FROM_WHITE_BED = Kee[str](
    'recipes/decorations/brown_bed_from_white_bed')
  RECIPES_DECORATIONS_BROWN_CANDLE = Kee[str](
    'recipes/decorations/brown_candle')
  RECIPES_DECORATIONS_BROWN_CARPET = Kee[str](
    'recipes/decorations/brown_carpet')
  RECIPES_DECORATIONS_BROWN_CARPET_FROM_WHITE_CARPET = Kee[str](
    'recipes/decorations/brown_carpet_from_white_carpet')
  RECIPES_DECORATIONS_BROWN_CUSHION = Kee[str](
    'recipes/decorations/brown_cushion')
  RECIPES_DECORATIONS_BROWN_GLAZED_TERRACOTTA = Kee[str](
    'recipes/decorations/brown_glazed_terracotta')
  RECIPES_DECORATIONS_BROWN_SHULKER_BOX = Kee[str](
    'recipes/decorations/brown_shulker_box')
  RECIPES_DECORATIONS_BROWN_STAINED_GLASS_PANE = Kee[str](
    'recipes/decorations/brown_stained_glass_pane')
  RECIPES_DECORATIONS_BROWN_STAINED_GLASS_PANE_FROM_GLASS_PANE = Kee[str](
    'recipes/decorations/brown_stained_glass_pane_from_glass_pane')
  RECIPES_DECORATIONS_CAMPFIRE = Kee[str]('recipes/decorations/campfire')
  RECIPES_DECORATIONS_CANDLE = Kee[str]('recipes/decorations/candle')
  RECIPES_DECORATIONS_CARTOGRAPHY_TABLE = Kee[str](
    'recipes/decorations/cartography_table')
  RECIPES_DECORATIONS_CHAIN = Kee[str]('recipes/decorations/chain')
  RECIPES_DECORATIONS_CHERRY_FENCE = Kee[str](
    'recipes/decorations/cherry_fence')
  RECIPES_DECORATIONS_CHERRY_HANGING_SIGN = Kee[str](
    'recipes/decorations/cherry_hanging_sign')
  RECIPES_DECORATIONS_CHERRY_SHELF = Kee[str](
    'recipes/decorations/cherry_shelf')
  RECIPES_DECORATIONS_CHERRY_SIGN = Kee[str]('recipes/decorations/cherry_sign')
  RECIPES_DECORATIONS_CHEST = Kee[str]('recipes/decorations/chest')
  RECIPES_DECORATIONS_CINNABAR_BRICK_WALL = Kee[str](
    'recipes/decorations/cinnabar_brick_wall')
  RECIPES_DECORATIONS_CINNABAR_BRICK_WALL_FROM_CINNABAR_BRICKS_STONECUTTING = Kee[str](
    'recipes/decorations/cinnabar_brick_wall_from_cinnabar_bricks_stonecutting')
  RECIPES_DECORATIONS_CINNABAR_BRICK_WALL_FROM_CINNABAR_STONECUTTING = Kee[str](
    'recipes/decorations/cinnabar_brick_wall_from_cinnabar_stonecutting')
  RECIPES_DECORATIONS_CINNABAR_BRICK_WALL_FROM_POLISHED_CINNABAR_STONECUTTING = Kee[str](
    'recipes/decorations/cinnabar_brick_wall_from_polished_cinnabar_stonecutting')
  RECIPES_DECORATIONS_CINNABAR_WALL = Kee[str](
    'recipes/decorations/cinnabar_wall')
  RECIPES_DECORATIONS_CINNABAR_WALL_FROM_CINNABAR_STONECUTTING = Kee[str](
    'recipes/decorations/cinnabar_wall_from_cinnabar_stonecutting')
  RECIPES_DECORATIONS_COBBLED_DEEPSLATE_WALL = Kee[str](
    'recipes/decorations/cobbled_deepslate_wall')
  RECIPES_DECORATIONS_COBBLED_DEEPSLATE_WALL_FROM_COBBLED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/decorations/cobbled_deepslate_wall_from_cobbled_deepslate_stonecutting')
  RECIPES_DECORATIONS_COBBLED_DEEPSLATE_WALL_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/decorations/cobbled_deepslate_wall_from_deepslate_stonecutting')
  RECIPES_DECORATIONS_COBBLESTONE_WALL = Kee[str](
    'recipes/decorations/cobblestone_wall')
  RECIPES_DECORATIONS_COBBLESTONE_WALL_FROM_COBBLESTONE_STONECUTTING = Kee[str](
    'recipes/decorations/cobblestone_wall_from_cobblestone_stonecutting')
  RECIPES_DECORATIONS_COBBLESTONE_WALL_FROM_STONE_STONECUTTING = Kee[str](
    'recipes/decorations/cobblestone_wall_from_stone_stonecutting')
  RECIPES_DECORATIONS_COMPOSTER = Kee[str]('recipes/decorations/composter')
  RECIPES_DECORATIONS_COPPER_BARS = Kee[str]('recipes/decorations/copper_bars')
  RECIPES_DECORATIONS_COPPER_CHAIN = Kee[str](
    'recipes/decorations/copper_chain')
  RECIPES_DECORATIONS_COPPER_CHEST = Kee[str](
    'recipes/decorations/copper_chest')
  RECIPES_DECORATIONS_COPPER_LANTERN = Kee[str](
    'recipes/decorations/copper_lantern')
  RECIPES_DECORATIONS_COPPER_TORCH = Kee[str](
    'recipes/decorations/copper_torch')
  RECIPES_DECORATIONS_CRAFTING_TABLE = Kee[str](
    'recipes/decorations/crafting_table')
  RECIPES_DECORATIONS_CRIMSON_FENCE = Kee[str](
    'recipes/decorations/crimson_fence')
  RECIPES_DECORATIONS_CRIMSON_HANGING_SIGN = Kee[str](
    'recipes/decorations/crimson_hanging_sign')
  RECIPES_DECORATIONS_CRIMSON_SHELF = Kee[str](
    'recipes/decorations/crimson_shelf')
  RECIPES_DECORATIONS_CRIMSON_SIGN = Kee[str](
    'recipes/decorations/crimson_sign')
  RECIPES_DECORATIONS_CYAN_BANNER = Kee[str]('recipes/decorations/cyan_banner')
  RECIPES_DECORATIONS_CYAN_BED = Kee[str]('recipes/decorations/cyan_bed')
  RECIPES_DECORATIONS_CYAN_BED_FROM_WHITE_BED = Kee[str](
    'recipes/decorations/cyan_bed_from_white_bed')
  RECIPES_DECORATIONS_CYAN_CANDLE = Kee[str]('recipes/decorations/cyan_candle')
  RECIPES_DECORATIONS_CYAN_CARPET = Kee[str]('recipes/decorations/cyan_carpet')
  RECIPES_DECORATIONS_CYAN_CARPET_FROM_WHITE_CARPET = Kee[str](
    'recipes/decorations/cyan_carpet_from_white_carpet')
  RECIPES_DECORATIONS_CYAN_CUSHION = Kee[str](
    'recipes/decorations/cyan_cushion')
  RECIPES_DECORATIONS_CYAN_GLAZED_TERRACOTTA = Kee[str](
    'recipes/decorations/cyan_glazed_terracotta')
  RECIPES_DECORATIONS_CYAN_SHULKER_BOX = Kee[str](
    'recipes/decorations/cyan_shulker_box')
  RECIPES_DECORATIONS_CYAN_STAINED_GLASS_PANE = Kee[str](
    'recipes/decorations/cyan_stained_glass_pane')
  RECIPES_DECORATIONS_CYAN_STAINED_GLASS_PANE_FROM_GLASS_PANE = Kee[str](
    'recipes/decorations/cyan_stained_glass_pane_from_glass_pane')
  RECIPES_DECORATIONS_DARK_OAK_FENCE = Kee[str](
    'recipes/decorations/dark_oak_fence')
  RECIPES_DECORATIONS_DARK_OAK_HANGING_SIGN = Kee[str](
    'recipes/decorations/dark_oak_hanging_sign')
  RECIPES_DECORATIONS_DARK_OAK_SHELF = Kee[str](
    'recipes/decorations/dark_oak_shelf')
  RECIPES_DECORATIONS_DARK_OAK_SIGN = Kee[str](
    'recipes/decorations/dark_oak_sign')
  RECIPES_DECORATIONS_DECORATED_POT_SIMPLE = Kee[str](
    'recipes/decorations/decorated_pot_simple')
  RECIPES_DECORATIONS_DEEPSLATE_BRICK_WALL = Kee[str](
    'recipes/decorations/deepslate_brick_wall')
  RECIPES_DECORATIONS_DEEPSLATE_BRICK_WALL_FROM_COBBLED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/decorations/deepslate_brick_wall_from_cobbled_deepslate_stonecutting')
  RECIPES_DECORATIONS_DEEPSLATE_BRICK_WALL_FROM_DEEPSLATE_BRICKS_STONECUTTING = Kee[str](
    'recipes/decorations/deepslate_brick_wall_from_deepslate_bricks_stonecutting')
  RECIPES_DECORATIONS_DEEPSLATE_BRICK_WALL_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/decorations/deepslate_brick_wall_from_deepslate_stonecutting')
  RECIPES_DECORATIONS_DEEPSLATE_BRICK_WALL_FROM_POLISHED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/decorations/deepslate_brick_wall_from_polished_deepslate_stonecutting')
  RECIPES_DECORATIONS_DEEPSLATE_TILE_WALL = Kee[str](
    'recipes/decorations/deepslate_tile_wall')
  RECIPES_DECORATIONS_DEEPSLATE_TILE_WALL_FROM_COBBLED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/decorations/deepslate_tile_wall_from_cobbled_deepslate_stonecutting')
  RECIPES_DECORATIONS_DEEPSLATE_TILE_WALL_FROM_DEEPSLATE_BRICKS_STONECUTTING = Kee[str](
    'recipes/decorations/deepslate_tile_wall_from_deepslate_bricks_stonecutting')
  RECIPES_DECORATIONS_DEEPSLATE_TILE_WALL_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/decorations/deepslate_tile_wall_from_deepslate_stonecutting')
  RECIPES_DECORATIONS_DEEPSLATE_TILE_WALL_FROM_DEEPSLATE_TILES_STONECUTTING = Kee[str](
    'recipes/decorations/deepslate_tile_wall_from_deepslate_tiles_stonecutting')
  RECIPES_DECORATIONS_DEEPSLATE_TILE_WALL_FROM_POLISHED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/decorations/deepslate_tile_wall_from_polished_deepslate_stonecutting')
  RECIPES_DECORATIONS_DIORITE_WALL = Kee[str](
    'recipes/decorations/diorite_wall')
  RECIPES_DECORATIONS_DIORITE_WALL_FROM_DIORITE_STONECUTTING = Kee[str](
    'recipes/decorations/diorite_wall_from_diorite_stonecutting')
  RECIPES_DECORATIONS_DYE_BLACK_BED = Kee[str](
    'recipes/decorations/dye_black_bed')
  RECIPES_DECORATIONS_DYE_BLACK_CARPET = Kee[str](
    'recipes/decorations/dye_black_carpet')
  RECIPES_DECORATIONS_DYE_BLACK_CUSHION = Kee[str](
    'recipes/decorations/dye_black_cushion')
  RECIPES_DECORATIONS_DYE_BLUE_BED = Kee[str](
    'recipes/decorations/dye_blue_bed')
  RECIPES_DECORATIONS_DYE_BLUE_CARPET = Kee[str](
    'recipes/decorations/dye_blue_carpet')
  RECIPES_DECORATIONS_DYE_BLUE_CUSHION = Kee[str](
    'recipes/decorations/dye_blue_cushion')
  RECIPES_DECORATIONS_DYE_BROWN_BED = Kee[str](
    'recipes/decorations/dye_brown_bed')
  RECIPES_DECORATIONS_DYE_BROWN_CARPET = Kee[str](
    'recipes/decorations/dye_brown_carpet')
  RECIPES_DECORATIONS_DYE_BROWN_CUSHION = Kee[str](
    'recipes/decorations/dye_brown_cushion')
  RECIPES_DECORATIONS_DYE_CYAN_BED = Kee[str](
    'recipes/decorations/dye_cyan_bed')
  RECIPES_DECORATIONS_DYE_CYAN_CARPET = Kee[str](
    'recipes/decorations/dye_cyan_carpet')
  RECIPES_DECORATIONS_DYE_CYAN_CUSHION = Kee[str](
    'recipes/decorations/dye_cyan_cushion')
  RECIPES_DECORATIONS_DYE_GRAY_BED = Kee[str](
    'recipes/decorations/dye_gray_bed')
  RECIPES_DECORATIONS_DYE_GRAY_CARPET = Kee[str](
    'recipes/decorations/dye_gray_carpet')
  RECIPES_DECORATIONS_DYE_GRAY_CUSHION = Kee[str](
    'recipes/decorations/dye_gray_cushion')
  RECIPES_DECORATIONS_DYE_GREEN_BED = Kee[str](
    'recipes/decorations/dye_green_bed')
  RECIPES_DECORATIONS_DYE_GREEN_CARPET = Kee[str](
    'recipes/decorations/dye_green_carpet')
  RECIPES_DECORATIONS_DYE_GREEN_CUSHION = Kee[str](
    'recipes/decorations/dye_green_cushion')
  RECIPES_DECORATIONS_DYE_LIGHT_BLUE_BED = Kee[str](
    'recipes/decorations/dye_light_blue_bed')
  RECIPES_DECORATIONS_DYE_LIGHT_BLUE_CARPET = Kee[str](
    'recipes/decorations/dye_light_blue_carpet')
  RECIPES_DECORATIONS_DYE_LIGHT_BLUE_CUSHION = Kee[str](
    'recipes/decorations/dye_light_blue_cushion')
  RECIPES_DECORATIONS_DYE_LIGHT_GRAY_BED = Kee[str](
    'recipes/decorations/dye_light_gray_bed')
  RECIPES_DECORATIONS_DYE_LIGHT_GRAY_CARPET = Kee[str](
    'recipes/decorations/dye_light_gray_carpet')
  RECIPES_DECORATIONS_DYE_LIGHT_GRAY_CUSHION = Kee[str](
    'recipes/decorations/dye_light_gray_cushion')
  RECIPES_DECORATIONS_DYE_LIME_BED = Kee[str](
    'recipes/decorations/dye_lime_bed')
  RECIPES_DECORATIONS_DYE_LIME_CARPET = Kee[str](
    'recipes/decorations/dye_lime_carpet')
  RECIPES_DECORATIONS_DYE_LIME_CUSHION = Kee[str](
    'recipes/decorations/dye_lime_cushion')
  RECIPES_DECORATIONS_DYE_MAGENTA_BED = Kee[str](
    'recipes/decorations/dye_magenta_bed')
  RECIPES_DECORATIONS_DYE_MAGENTA_CARPET = Kee[str](
    'recipes/decorations/dye_magenta_carpet')
  RECIPES_DECORATIONS_DYE_MAGENTA_CUSHION = Kee[str](
    'recipes/decorations/dye_magenta_cushion')
  RECIPES_DECORATIONS_DYE_ORANGE_BED = Kee[str](
    'recipes/decorations/dye_orange_bed')
  RECIPES_DECORATIONS_DYE_ORANGE_CARPET = Kee[str](
    'recipes/decorations/dye_orange_carpet')
  RECIPES_DECORATIONS_DYE_ORANGE_CUSHION = Kee[str](
    'recipes/decorations/dye_orange_cushion')
  RECIPES_DECORATIONS_DYE_PINK_BED = Kee[str](
    'recipes/decorations/dye_pink_bed')
  RECIPES_DECORATIONS_DYE_PINK_CARPET = Kee[str](
    'recipes/decorations/dye_pink_carpet')
  RECIPES_DECORATIONS_DYE_PINK_CUSHION = Kee[str](
    'recipes/decorations/dye_pink_cushion')
  RECIPES_DECORATIONS_DYE_PURPLE_BED = Kee[str](
    'recipes/decorations/dye_purple_bed')
  RECIPES_DECORATIONS_DYE_PURPLE_CARPET = Kee[str](
    'recipes/decorations/dye_purple_carpet')
  RECIPES_DECORATIONS_DYE_PURPLE_CUSHION = Kee[str](
    'recipes/decorations/dye_purple_cushion')
  RECIPES_DECORATIONS_DYE_RED_BED = Kee[str]('recipes/decorations/dye_red_bed')
  RECIPES_DECORATIONS_DYE_RED_CARPET = Kee[str](
    'recipes/decorations/dye_red_carpet')
  RECIPES_DECORATIONS_DYE_RED_CUSHION = Kee[str](
    'recipes/decorations/dye_red_cushion')
  RECIPES_DECORATIONS_DYE_WHITE_BED = Kee[str](
    'recipes/decorations/dye_white_bed')
  RECIPES_DECORATIONS_DYE_WHITE_CARPET = Kee[str](
    'recipes/decorations/dye_white_carpet')
  RECIPES_DECORATIONS_DYE_WHITE_CUSHION = Kee[str](
    'recipes/decorations/dye_white_cushion')
  RECIPES_DECORATIONS_DYE_YELLOW_BED = Kee[str](
    'recipes/decorations/dye_yellow_bed')
  RECIPES_DECORATIONS_DYE_YELLOW_CARPET = Kee[str](
    'recipes/decorations/dye_yellow_carpet')
  RECIPES_DECORATIONS_DYE_YELLOW_CUSHION = Kee[str](
    'recipes/decorations/dye_yellow_cushion')
  RECIPES_DECORATIONS_ENCHANTING_TABLE = Kee[str](
    'recipes/decorations/enchanting_table')
  RECIPES_DECORATIONS_END_CRYSTAL = Kee[str]('recipes/decorations/end_crystal')
  RECIPES_DECORATIONS_END_ROD = Kee[str]('recipes/decorations/end_rod')
  RECIPES_DECORATIONS_END_STONE_BRICK_WALL = Kee[str](
    'recipes/decorations/end_stone_brick_wall')
  RECIPES_DECORATIONS_END_STONE_BRICK_WALL_FROM_END_STONE_BRICKS_STONECUTTING = Kee[str](
    'recipes/decorations/end_stone_brick_wall_from_end_stone_bricks_stonecutting')
  RECIPES_DECORATIONS_END_STONE_BRICK_WALL_FROM_END_STONE_STONECUTTING = Kee[str](
    'recipes/decorations/end_stone_brick_wall_from_end_stone_stonecutting')
  RECIPES_DECORATIONS_ENDER_CHEST = Kee[str]('recipes/decorations/ender_chest')
  RECIPES_DECORATIONS_FLETCHING_TABLE = Kee[str](
    'recipes/decorations/fletching_table')
  RECIPES_DECORATIONS_FLOWER_POT = Kee[str]('recipes/decorations/flower_pot')
  RECIPES_DECORATIONS_FURNACE = Kee[str]('recipes/decorations/furnace')
  RECIPES_DECORATIONS_GLASS_PANE = Kee[str]('recipes/decorations/glass_pane')
  RECIPES_DECORATIONS_GLOW_ITEM_FRAME = Kee[str](
    'recipes/decorations/glow_item_frame')
  RECIPES_DECORATIONS_GOLDEN_DANDELION = Kee[str](
    'recipes/decorations/golden_dandelion')
  RECIPES_DECORATIONS_GRANITE_WALL = Kee[str](
    'recipes/decorations/granite_wall')
  RECIPES_DECORATIONS_GRANITE_WALL_FROM_GRANITE_STONECUTTING = Kee[str](
    'recipes/decorations/granite_wall_from_granite_stonecutting')
  RECIPES_DECORATIONS_GRAY_BANNER = Kee[str]('recipes/decorations/gray_banner')
  RECIPES_DECORATIONS_GRAY_BED = Kee[str]('recipes/decorations/gray_bed')
  RECIPES_DECORATIONS_GRAY_BED_FROM_WHITE_BED = Kee[str](
    'recipes/decorations/gray_bed_from_white_bed')
  RECIPES_DECORATIONS_GRAY_CANDLE = Kee[str]('recipes/decorations/gray_candle')
  RECIPES_DECORATIONS_GRAY_CARPET = Kee[str]('recipes/decorations/gray_carpet')
  RECIPES_DECORATIONS_GRAY_CARPET_FROM_WHITE_CARPET = Kee[str](
    'recipes/decorations/gray_carpet_from_white_carpet')
  RECIPES_DECORATIONS_GRAY_CUSHION = Kee[str](
    'recipes/decorations/gray_cushion')
  RECIPES_DECORATIONS_GRAY_GLAZED_TERRACOTTA = Kee[str](
    'recipes/decorations/gray_glazed_terracotta')
  RECIPES_DECORATIONS_GRAY_SHULKER_BOX = Kee[str](
    'recipes/decorations/gray_shulker_box')
  RECIPES_DECORATIONS_GRAY_STAINED_GLASS_PANE = Kee[str](
    'recipes/decorations/gray_stained_glass_pane')
  RECIPES_DECORATIONS_GRAY_STAINED_GLASS_PANE_FROM_GLASS_PANE = Kee[str](
    'recipes/decorations/gray_stained_glass_pane_from_glass_pane')
  RECIPES_DECORATIONS_GREEN_BANNER = Kee[str](
    'recipes/decorations/green_banner')
  RECIPES_DECORATIONS_GREEN_BED = Kee[str]('recipes/decorations/green_bed')
  RECIPES_DECORATIONS_GREEN_BED_FROM_WHITE_BED = Kee[str](
    'recipes/decorations/green_bed_from_white_bed')
  RECIPES_DECORATIONS_GREEN_CANDLE = Kee[str](
    'recipes/decorations/green_candle')
  RECIPES_DECORATIONS_GREEN_CARPET = Kee[str](
    'recipes/decorations/green_carpet')
  RECIPES_DECORATIONS_GREEN_CARPET_FROM_WHITE_CARPET = Kee[str](
    'recipes/decorations/green_carpet_from_white_carpet')
  RECIPES_DECORATIONS_GREEN_CUSHION = Kee[str](
    'recipes/decorations/green_cushion')
  RECIPES_DECORATIONS_GREEN_GLAZED_TERRACOTTA = Kee[str](
    'recipes/decorations/green_glazed_terracotta')
  RECIPES_DECORATIONS_GREEN_SHULKER_BOX = Kee[str](
    'recipes/decorations/green_shulker_box')
  RECIPES_DECORATIONS_GREEN_STAINED_GLASS_PANE = Kee[str](
    'recipes/decorations/green_stained_glass_pane')
  RECIPES_DECORATIONS_GREEN_STAINED_GLASS_PANE_FROM_GLASS_PANE = Kee[str](
    'recipes/decorations/green_stained_glass_pane_from_glass_pane')
  RECIPES_DECORATIONS_GRINDSTONE = Kee[str]('recipes/decorations/grindstone')
  RECIPES_DECORATIONS_HONEY_BLOCK = Kee[str]('recipes/decorations/honey_block')
  RECIPES_DECORATIONS_HONEYCOMB_BLOCK = Kee[str](
    'recipes/decorations/honeycomb_block')
  RECIPES_DECORATIONS_IRON_BARS = Kee[str]('recipes/decorations/iron_bars')
  RECIPES_DECORATIONS_IRON_CHAIN = Kee[str]('recipes/decorations/iron_chain')
  RECIPES_DECORATIONS_ITEM_FRAME = Kee[str]('recipes/decorations/item_frame')
  RECIPES_DECORATIONS_JUKEBOX = Kee[str]('recipes/decorations/jukebox')
  RECIPES_DECORATIONS_JUNGLE_FENCE = Kee[str](
    'recipes/decorations/jungle_fence')
  RECIPES_DECORATIONS_JUNGLE_HANGING_SIGN = Kee[str](
    'recipes/decorations/jungle_hanging_sign')
  RECIPES_DECORATIONS_JUNGLE_SHELF = Kee[str](
    'recipes/decorations/jungle_shelf')
  RECIPES_DECORATIONS_JUNGLE_SIGN = Kee[str]('recipes/decorations/jungle_sign')
  RECIPES_DECORATIONS_LADDER = Kee[str]('recipes/decorations/ladder')
  RECIPES_DECORATIONS_LANTERN = Kee[str]('recipes/decorations/lantern')
  RECIPES_DECORATIONS_LIGHT_BLUE_BANNER = Kee[str](
    'recipes/decorations/light_blue_banner')
  RECIPES_DECORATIONS_LIGHT_BLUE_BED = Kee[str](
    'recipes/decorations/light_blue_bed')
  RECIPES_DECORATIONS_LIGHT_BLUE_BED_FROM_WHITE_BED = Kee[str](
    'recipes/decorations/light_blue_bed_from_white_bed')
  RECIPES_DECORATIONS_LIGHT_BLUE_CANDLE = Kee[str](
    'recipes/decorations/light_blue_candle')
  RECIPES_DECORATIONS_LIGHT_BLUE_CARPET = Kee[str](
    'recipes/decorations/light_blue_carpet')
  RECIPES_DECORATIONS_LIGHT_BLUE_CARPET_FROM_WHITE_CARPET = Kee[str](
    'recipes/decorations/light_blue_carpet_from_white_carpet')
  RECIPES_DECORATIONS_LIGHT_BLUE_CUSHION = Kee[str](
    'recipes/decorations/light_blue_cushion')
  RECIPES_DECORATIONS_LIGHT_BLUE_GLAZED_TERRACOTTA = Kee[str](
    'recipes/decorations/light_blue_glazed_terracotta')
  RECIPES_DECORATIONS_LIGHT_BLUE_SHULKER_BOX = Kee[str](
    'recipes/decorations/light_blue_shulker_box')
  RECIPES_DECORATIONS_LIGHT_BLUE_STAINED_GLASS_PANE = Kee[str](
    'recipes/decorations/light_blue_stained_glass_pane')
  RECIPES_DECORATIONS_LIGHT_BLUE_STAINED_GLASS_PANE_FROM_GLASS_PANE = Kee[str](
    'recipes/decorations/light_blue_stained_glass_pane_from_glass_pane')
  RECIPES_DECORATIONS_LIGHT_GRAY_BANNER = Kee[str](
    'recipes/decorations/light_gray_banner')
  RECIPES_DECORATIONS_LIGHT_GRAY_BED = Kee[str](
    'recipes/decorations/light_gray_bed')
  RECIPES_DECORATIONS_LIGHT_GRAY_BED_FROM_WHITE_BED = Kee[str](
    'recipes/decorations/light_gray_bed_from_white_bed')
  RECIPES_DECORATIONS_LIGHT_GRAY_CANDLE = Kee[str](
    'recipes/decorations/light_gray_candle')
  RECIPES_DECORATIONS_LIGHT_GRAY_CARPET = Kee[str](
    'recipes/decorations/light_gray_carpet')
  RECIPES_DECORATIONS_LIGHT_GRAY_CARPET_FROM_WHITE_CARPET = Kee[str](
    'recipes/decorations/light_gray_carpet_from_white_carpet')
  RECIPES_DECORATIONS_LIGHT_GRAY_CUSHION = Kee[str](
    'recipes/decorations/light_gray_cushion')
  RECIPES_DECORATIONS_LIGHT_GRAY_GLAZED_TERRACOTTA = Kee[str](
    'recipes/decorations/light_gray_glazed_terracotta')
  RECIPES_DECORATIONS_LIGHT_GRAY_SHULKER_BOX = Kee[str](
    'recipes/decorations/light_gray_shulker_box')
  RECIPES_DECORATIONS_LIGHT_GRAY_STAINED_GLASS_PANE = Kee[str](
    'recipes/decorations/light_gray_stained_glass_pane')
  RECIPES_DECORATIONS_LIGHT_GRAY_STAINED_GLASS_PANE_FROM_GLASS_PANE = Kee[str](
    'recipes/decorations/light_gray_stained_glass_pane_from_glass_pane')
  RECIPES_DECORATIONS_LIME_BANNER = Kee[str]('recipes/decorations/lime_banner')
  RECIPES_DECORATIONS_LIME_BED = Kee[str]('recipes/decorations/lime_bed')
  RECIPES_DECORATIONS_LIME_BED_FROM_WHITE_BED = Kee[str](
    'recipes/decorations/lime_bed_from_white_bed')
  RECIPES_DECORATIONS_LIME_CANDLE = Kee[str]('recipes/decorations/lime_candle')
  RECIPES_DECORATIONS_LIME_CARPET = Kee[str]('recipes/decorations/lime_carpet')
  RECIPES_DECORATIONS_LIME_CARPET_FROM_WHITE_CARPET = Kee[str](
    'recipes/decorations/lime_carpet_from_white_carpet')
  RECIPES_DECORATIONS_LIME_CUSHION = Kee[str](
    'recipes/decorations/lime_cushion')
  RECIPES_DECORATIONS_LIME_GLAZED_TERRACOTTA = Kee[str](
    'recipes/decorations/lime_glazed_terracotta')
  RECIPES_DECORATIONS_LIME_SHULKER_BOX = Kee[str](
    'recipes/decorations/lime_shulker_box')
  RECIPES_DECORATIONS_LIME_STAINED_GLASS_PANE = Kee[str](
    'recipes/decorations/lime_stained_glass_pane')
  RECIPES_DECORATIONS_LIME_STAINED_GLASS_PANE_FROM_GLASS_PANE = Kee[str](
    'recipes/decorations/lime_stained_glass_pane_from_glass_pane')
  RECIPES_DECORATIONS_LODESTONE = Kee[str]('recipes/decorations/lodestone')
  RECIPES_DECORATIONS_LOOM = Kee[str]('recipes/decorations/loom')
  RECIPES_DECORATIONS_MAGENTA_BANNER = Kee[str](
    'recipes/decorations/magenta_banner')
  RECIPES_DECORATIONS_MAGENTA_BED = Kee[str]('recipes/decorations/magenta_bed')
  RECIPES_DECORATIONS_MAGENTA_BED_FROM_WHITE_BED = Kee[str](
    'recipes/decorations/magenta_bed_from_white_bed')
  RECIPES_DECORATIONS_MAGENTA_CANDLE = Kee[str](
    'recipes/decorations/magenta_candle')
  RECIPES_DECORATIONS_MAGENTA_CARPET = Kee[str](
    'recipes/decorations/magenta_carpet')
  RECIPES_DECORATIONS_MAGENTA_CARPET_FROM_WHITE_CARPET = Kee[str](
    'recipes/decorations/magenta_carpet_from_white_carpet')
  RECIPES_DECORATIONS_MAGENTA_CUSHION = Kee[str](
    'recipes/decorations/magenta_cushion')
  RECIPES_DECORATIONS_MAGENTA_GLAZED_TERRACOTTA = Kee[str](
    'recipes/decorations/magenta_glazed_terracotta')
  RECIPES_DECORATIONS_MAGENTA_SHULKER_BOX = Kee[str](
    'recipes/decorations/magenta_shulker_box')
  RECIPES_DECORATIONS_MAGENTA_STAINED_GLASS_PANE = Kee[str](
    'recipes/decorations/magenta_stained_glass_pane')
  RECIPES_DECORATIONS_MAGENTA_STAINED_GLASS_PANE_FROM_GLASS_PANE = Kee[str](
    'recipes/decorations/magenta_stained_glass_pane_from_glass_pane')
  RECIPES_DECORATIONS_MANGROVE_FENCE = Kee[str](
    'recipes/decorations/mangrove_fence')
  RECIPES_DECORATIONS_MANGROVE_HANGING_SIGN = Kee[str](
    'recipes/decorations/mangrove_hanging_sign')
  RECIPES_DECORATIONS_MANGROVE_SHELF = Kee[str](
    'recipes/decorations/mangrove_shelf')
  RECIPES_DECORATIONS_MANGROVE_SIGN = Kee[str](
    'recipes/decorations/mangrove_sign')
  RECIPES_DECORATIONS_MOSS_CARPET = Kee[str]('recipes/decorations/moss_carpet')
  RECIPES_DECORATIONS_MOSSY_COBBLESTONE_WALL = Kee[str](
    'recipes/decorations/mossy_cobblestone_wall')
  RECIPES_DECORATIONS_MOSSY_COBBLESTONE_WALL_FROM_MOSSY_COBBLESTONE_STONECUTTING = Kee[str](
    'recipes/decorations/mossy_cobblestone_wall_from_mossy_cobblestone_stonecutting')
  RECIPES_DECORATIONS_MOSSY_STONE_BRICK_WALL = Kee[str](
    'recipes/decorations/mossy_stone_brick_wall')
  RECIPES_DECORATIONS_MOSSY_STONE_BRICK_WALL_FROM_MOSSY_STONE_BRICK_STONECUTTING = Kee[str](
    'recipes/decorations/mossy_stone_brick_wall_from_mossy_stone_brick_stonecutting')
  RECIPES_DECORATIONS_MOSSY_STONE_BRICK_WALL_FROM_MOSSY_STONE_BRICKS_STONECUTTING = Kee[str](
    'recipes/decorations/mossy_stone_brick_wall_from_mossy_stone_bricks_stonecutting')
  RECIPES_DECORATIONS_MUD_BRICK_WALL = Kee[str](
    'recipes/decorations/mud_brick_wall')
  RECIPES_DECORATIONS_MUD_BRICK_WALL_FROM_MUD_BRICKS_STONECUTTING = Kee[str](
    'recipes/decorations/mud_brick_wall_from_mud_bricks_stonecutting')
  RECIPES_DECORATIONS_NETHER_BRICK_FENCE = Kee[str](
    'recipes/decorations/nether_brick_fence')
  RECIPES_DECORATIONS_NETHER_BRICK_WALL = Kee[str](
    'recipes/decorations/nether_brick_wall')
  RECIPES_DECORATIONS_NETHER_BRICK_WALL_FROM_NETHER_BRICKS_STONECUTTING = Kee[str](
    'recipes/decorations/nether_brick_wall_from_nether_bricks_stonecutting')
  RECIPES_DECORATIONS_OAK_FENCE = Kee[str]('recipes/decorations/oak_fence')
  RECIPES_DECORATIONS_OAK_HANGING_SIGN = Kee[str](
    'recipes/decorations/oak_hanging_sign')
  RECIPES_DECORATIONS_OAK_SHELF = Kee[str]('recipes/decorations/oak_shelf')
  RECIPES_DECORATIONS_OAK_SIGN = Kee[str]('recipes/decorations/oak_sign')
  RECIPES_DECORATIONS_ORANGE_BANNER = Kee[str](
    'recipes/decorations/orange_banner')
  RECIPES_DECORATIONS_ORANGE_BED = Kee[str]('recipes/decorations/orange_bed')
  RECIPES_DECORATIONS_ORANGE_BED_FROM_WHITE_BED = Kee[str](
    'recipes/decorations/orange_bed_from_white_bed')
  RECIPES_DECORATIONS_ORANGE_CANDLE = Kee[str](
    'recipes/decorations/orange_candle')
  RECIPES_DECORATIONS_ORANGE_CARPET = Kee[str](
    'recipes/decorations/orange_carpet')
  RECIPES_DECORATIONS_ORANGE_CARPET_FROM_WHITE_CARPET = Kee[str](
    'recipes/decorations/orange_carpet_from_white_carpet')
  RECIPES_DECORATIONS_ORANGE_CUSHION = Kee[str](
    'recipes/decorations/orange_cushion')
  RECIPES_DECORATIONS_ORANGE_GLAZED_TERRACOTTA = Kee[str](
    'recipes/decorations/orange_glazed_terracotta')
  RECIPES_DECORATIONS_ORANGE_SHULKER_BOX = Kee[str](
    'recipes/decorations/orange_shulker_box')
  RECIPES_DECORATIONS_ORANGE_STAINED_GLASS_PANE = Kee[str](
    'recipes/decorations/orange_stained_glass_pane')
  RECIPES_DECORATIONS_ORANGE_STAINED_GLASS_PANE_FROM_GLASS_PANE = Kee[str](
    'recipes/decorations/orange_stained_glass_pane_from_glass_pane')
  RECIPES_DECORATIONS_PAINTING = Kee[str]('recipes/decorations/painting')
  RECIPES_DECORATIONS_PALE_MOSS_CARPET = Kee[str](
    'recipes/decorations/pale_moss_carpet')
  RECIPES_DECORATIONS_PALE_OAK_FENCE = Kee[str](
    'recipes/decorations/pale_oak_fence')
  RECIPES_DECORATIONS_PALE_OAK_HANGING_SIGN = Kee[str](
    'recipes/decorations/pale_oak_hanging_sign')
  RECIPES_DECORATIONS_PALE_OAK_SHELF = Kee[str](
    'recipes/decorations/pale_oak_shelf')
  RECIPES_DECORATIONS_PALE_OAK_SIGN = Kee[str](
    'recipes/decorations/pale_oak_sign')
  RECIPES_DECORATIONS_PINK_BANNER = Kee[str]('recipes/decorations/pink_banner')
  RECIPES_DECORATIONS_PINK_BED = Kee[str]('recipes/decorations/pink_bed')
  RECIPES_DECORATIONS_PINK_BED_FROM_WHITE_BED = Kee[str](
    'recipes/decorations/pink_bed_from_white_bed')
  RECIPES_DECORATIONS_PINK_CANDLE = Kee[str]('recipes/decorations/pink_candle')
  RECIPES_DECORATIONS_PINK_CARPET = Kee[str]('recipes/decorations/pink_carpet')
  RECIPES_DECORATIONS_PINK_CARPET_FROM_WHITE_CARPET = Kee[str](
    'recipes/decorations/pink_carpet_from_white_carpet')
  RECIPES_DECORATIONS_PINK_CUSHION = Kee[str](
    'recipes/decorations/pink_cushion')
  RECIPES_DECORATIONS_PINK_GLAZED_TERRACOTTA = Kee[str](
    'recipes/decorations/pink_glazed_terracotta')
  RECIPES_DECORATIONS_PINK_SHULKER_BOX = Kee[str](
    'recipes/decorations/pink_shulker_box')
  RECIPES_DECORATIONS_PINK_STAINED_GLASS_PANE = Kee[str](
    'recipes/decorations/pink_stained_glass_pane')
  RECIPES_DECORATIONS_PINK_STAINED_GLASS_PANE_FROM_GLASS_PANE = Kee[str](
    'recipes/decorations/pink_stained_glass_pane_from_glass_pane')
  RECIPES_DECORATIONS_POLISHED_BLACKSTONE_BRICK_WALL = Kee[str](
    'recipes/decorations/polished_blackstone_brick_wall')
  RECIPES_DECORATIONS_POLISHED_BLACKSTONE_BRICK_WALL_FROM_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/decorations/polished_blackstone_brick_wall_from_blackstone_stonecutting')
  RECIPES_DECORATIONS_POLISHED_BLACKSTONE_BRICK_WALL_FROM_POLISHED_BLACKSTONE_BRICKS_STONECUTTING = Kee[str](
    'recipes/decorations/polished_blackstone_brick_wall_from_polished_blackstone_bricks_stonecutting')
  RECIPES_DECORATIONS_POLISHED_BLACKSTONE_BRICK_WALL_FROM_POLISHED_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/decorations/polished_blackstone_brick_wall_from_polished_blackstone_stonecutting')
  RECIPES_DECORATIONS_POLISHED_BLACKSTONE_WALL = Kee[str](
    'recipes/decorations/polished_blackstone_wall')
  RECIPES_DECORATIONS_POLISHED_BLACKSTONE_WALL_FROM_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/decorations/polished_blackstone_wall_from_blackstone_stonecutting')
  RECIPES_DECORATIONS_POLISHED_BLACKSTONE_WALL_FROM_POLISHED_BLACKSTONE_STONECUTTING = Kee[str](
    'recipes/decorations/polished_blackstone_wall_from_polished_blackstone_stonecutting')
  RECIPES_DECORATIONS_POLISHED_CINNABAR_WALL = Kee[str](
    'recipes/decorations/polished_cinnabar_wall')
  RECIPES_DECORATIONS_POLISHED_CINNABAR_WALL_FROM_CINNABAR_STONECUTTING = Kee[str](
    'recipes/decorations/polished_cinnabar_wall_from_cinnabar_stonecutting')
  RECIPES_DECORATIONS_POLISHED_CINNABAR_WALL_FROM_POLISHED_CINNABAR_STONECUTTING = Kee[str](
    'recipes/decorations/polished_cinnabar_wall_from_polished_cinnabar_stonecutting')
  RECIPES_DECORATIONS_POLISHED_DEEPSLATE_WALL = Kee[str](
    'recipes/decorations/polished_deepslate_wall')
  RECIPES_DECORATIONS_POLISHED_DEEPSLATE_WALL_FROM_COBBLED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/decorations/polished_deepslate_wall_from_cobbled_deepslate_stonecutting')
  RECIPES_DECORATIONS_POLISHED_DEEPSLATE_WALL_FROM_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/decorations/polished_deepslate_wall_from_deepslate_stonecutting')
  RECIPES_DECORATIONS_POLISHED_DEEPSLATE_WALL_FROM_POLISHED_DEEPSLATE_STONECUTTING = Kee[str](
    'recipes/decorations/polished_deepslate_wall_from_polished_deepslate_stonecutting')
  RECIPES_DECORATIONS_POLISHED_SULFUR_WALL = Kee[str](
    'recipes/decorations/polished_sulfur_wall')
  RECIPES_DECORATIONS_POLISHED_SULFUR_WALL_FROM_POLISHED_SULFUR_STONECUTTING = Kee[str](
    'recipes/decorations/polished_sulfur_wall_from_polished_sulfur_stonecutting')
  RECIPES_DECORATIONS_POLISHED_SULFUR_WALL_FROM_SULFUR_STONECUTTING = Kee[str](
    'recipes/decorations/polished_sulfur_wall_from_sulfur_stonecutting')
  RECIPES_DECORATIONS_POLISHED_TUFF_WALL = Kee[str](
    'recipes/decorations/polished_tuff_wall')
  RECIPES_DECORATIONS_POLISHED_TUFF_WALL_FROM_POLISHED_TUFF_STONECUTTING = Kee[str](
    'recipes/decorations/polished_tuff_wall_from_polished_tuff_stonecutting')
  RECIPES_DECORATIONS_POLISHED_TUFF_WALL_FROM_TUFF_STONECUTTING = Kee[str](
    'recipes/decorations/polished_tuff_wall_from_tuff_stonecutting')
  RECIPES_DECORATIONS_POPLAR_FENCE = Kee[str](
    'recipes/decorations/poplar_fence')
  RECIPES_DECORATIONS_POPLAR_HANGING_SIGN = Kee[str](
    'recipes/decorations/poplar_hanging_sign')
  RECIPES_DECORATIONS_POPLAR_SHELF = Kee[str](
    'recipes/decorations/poplar_shelf')
  RECIPES_DECORATIONS_POPLAR_SIGN = Kee[str]('recipes/decorations/poplar_sign')
  RECIPES_DECORATIONS_PRISMARINE_WALL = Kee[str](
    'recipes/decorations/prismarine_wall')
  RECIPES_DECORATIONS_PRISMARINE_WALL_FROM_PRISMARINE_STONECUTTING = Kee[str](
    'recipes/decorations/prismarine_wall_from_prismarine_stonecutting')
  RECIPES_DECORATIONS_PURPLE_BANNER = Kee[str](
    'recipes/decorations/purple_banner')
  RECIPES_DECORATIONS_PURPLE_BED = Kee[str]('recipes/decorations/purple_bed')
  RECIPES_DECORATIONS_PURPLE_BED_FROM_WHITE_BED = Kee[str](
    'recipes/decorations/purple_bed_from_white_bed')
  RECIPES_DECORATIONS_PURPLE_CANDLE = Kee[str](
    'recipes/decorations/purple_candle')
  RECIPES_DECORATIONS_PURPLE_CARPET = Kee[str](
    'recipes/decorations/purple_carpet')
  RECIPES_DECORATIONS_PURPLE_CARPET_FROM_WHITE_CARPET = Kee[str](
    'recipes/decorations/purple_carpet_from_white_carpet')
  RECIPES_DECORATIONS_PURPLE_CUSHION = Kee[str](
    'recipes/decorations/purple_cushion')
  RECIPES_DECORATIONS_PURPLE_GLAZED_TERRACOTTA = Kee[str](
    'recipes/decorations/purple_glazed_terracotta')
  RECIPES_DECORATIONS_PURPLE_SHULKER_BOX = Kee[str](
    'recipes/decorations/purple_shulker_box')
  RECIPES_DECORATIONS_PURPLE_STAINED_GLASS_PANE = Kee[str](
    'recipes/decorations/purple_stained_glass_pane')
  RECIPES_DECORATIONS_PURPLE_STAINED_GLASS_PANE_FROM_GLASS_PANE = Kee[str](
    'recipes/decorations/purple_stained_glass_pane_from_glass_pane')
  RECIPES_DECORATIONS_RED_BANNER = Kee[str]('recipes/decorations/red_banner')
  RECIPES_DECORATIONS_RED_BED = Kee[str]('recipes/decorations/red_bed')
  RECIPES_DECORATIONS_RED_BED_FROM_WHITE_BED = Kee[str](
    'recipes/decorations/red_bed_from_white_bed')
  RECIPES_DECORATIONS_RED_CANDLE = Kee[str]('recipes/decorations/red_candle')
  RECIPES_DECORATIONS_RED_CARPET = Kee[str]('recipes/decorations/red_carpet')
  RECIPES_DECORATIONS_RED_CARPET_FROM_WHITE_CARPET = Kee[str](
    'recipes/decorations/red_carpet_from_white_carpet')
  RECIPES_DECORATIONS_RED_CUSHION = Kee[str]('recipes/decorations/red_cushion')
  RECIPES_DECORATIONS_RED_GLAZED_TERRACOTTA = Kee[str](
    'recipes/decorations/red_glazed_terracotta')
  RECIPES_DECORATIONS_RED_NETHER_BRICK_WALL = Kee[str](
    'recipes/decorations/red_nether_brick_wall')
  RECIPES_DECORATIONS_RED_NETHER_BRICK_WALL_FROM_RED_NETHER_BRICKS_STONECUTTING = Kee[str](
    'recipes/decorations/red_nether_brick_wall_from_red_nether_bricks_stonecutting')
  RECIPES_DECORATIONS_RED_SANDSTONE_WALL = Kee[str](
    'recipes/decorations/red_sandstone_wall')
  RECIPES_DECORATIONS_RED_SANDSTONE_WALL_FROM_RED_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/decorations/red_sandstone_wall_from_red_sandstone_stonecutting')
  RECIPES_DECORATIONS_RED_SHULKER_BOX = Kee[str](
    'recipes/decorations/red_shulker_box')
  RECIPES_DECORATIONS_RED_STAINED_GLASS_PANE = Kee[str](
    'recipes/decorations/red_stained_glass_pane')
  RECIPES_DECORATIONS_RED_STAINED_GLASS_PANE_FROM_GLASS_PANE = Kee[str](
    'recipes/decorations/red_stained_glass_pane_from_glass_pane')
  RECIPES_DECORATIONS_RESIN_BRICK_WALL = Kee[str](
    'recipes/decorations/resin_brick_wall')
  RECIPES_DECORATIONS_RESIN_BRICK_WALL_FROM_RESIN_BRICKS_STONECUTTING = Kee[str](
    'recipes/decorations/resin_brick_wall_from_resin_bricks_stonecutting')
  RECIPES_DECORATIONS_RESPAWN_ANCHOR = Kee[str](
    'recipes/decorations/respawn_anchor')
  RECIPES_DECORATIONS_SANDSTONE_WALL = Kee[str](
    'recipes/decorations/sandstone_wall')
  RECIPES_DECORATIONS_SANDSTONE_WALL_FROM_SANDSTONE_STONECUTTING = Kee[str](
    'recipes/decorations/sandstone_wall_from_sandstone_stonecutting')
  RECIPES_DECORATIONS_SCAFFOLDING = Kee[str]('recipes/decorations/scaffolding')
  RECIPES_DECORATIONS_SHULKER_BOX = Kee[str]('recipes/decorations/shulker_box')
  RECIPES_DECORATIONS_SIGN = Kee[str]('recipes/decorations/sign')
  RECIPES_DECORATIONS_SLIME_BLOCK = Kee[str]('recipes/decorations/slime_block')
  RECIPES_DECORATIONS_SMITHING_TABLE = Kee[str](
    'recipes/decorations/smithing_table')
  RECIPES_DECORATIONS_SMOKER = Kee[str]('recipes/decorations/smoker')
  RECIPES_DECORATIONS_SNOW = Kee[str]('recipes/decorations/snow')
  RECIPES_DECORATIONS_SOUL_CAMPFIRE = Kee[str](
    'recipes/decorations/soul_campfire')
  RECIPES_DECORATIONS_SOUL_LANTERN = Kee[str](
    'recipes/decorations/soul_lantern')
  RECIPES_DECORATIONS_SOUL_TORCH = Kee[str]('recipes/decorations/soul_torch')
  RECIPES_DECORATIONS_SPRUCE_FENCE = Kee[str](
    'recipes/decorations/spruce_fence')
  RECIPES_DECORATIONS_SPRUCE_HANGING_SIGN = Kee[str](
    'recipes/decorations/spruce_hanging_sign')
  RECIPES_DECORATIONS_SPRUCE_SHELF = Kee[str](
    'recipes/decorations/spruce_shelf')
  RECIPES_DECORATIONS_SPRUCE_SIGN = Kee[str]('recipes/decorations/spruce_sign')
  RECIPES_DECORATIONS_STONE_BRICK_WALL = Kee[str](
    'recipes/decorations/stone_brick_wall')
  RECIPES_DECORATIONS_STONE_BRICK_WALL_FROM_STONE_BRICKS_STONECUTTING = Kee[str](
    'recipes/decorations/stone_brick_wall_from_stone_bricks_stonecutting')
  RECIPES_DECORATIONS_STONE_BRICK_WALL_FROM_STONE_STONECUTTING = Kee[str](
    'recipes/decorations/stone_brick_wall_from_stone_stonecutting')
  RECIPES_DECORATIONS_STONECUTTER = Kee[str]('recipes/decorations/stonecutter')
  RECIPES_DECORATIONS_STRAW_BED = Kee[str]('recipes/decorations/straw_bed')
  RECIPES_DECORATIONS_SULFUR_BRICK_WALL = Kee[str](
    'recipes/decorations/sulfur_brick_wall')
  RECIPES_DECORATIONS_SULFUR_BRICK_WALL_FROM_POLISHED_SULFUR_STONECUTTING = Kee[str](
    'recipes/decorations/sulfur_brick_wall_from_polished_sulfur_stonecutting')
  RECIPES_DECORATIONS_SULFUR_BRICK_WALL_FROM_SULFUR_BRICKS_STONECUTTING = Kee[str](
    'recipes/decorations/sulfur_brick_wall_from_sulfur_bricks_stonecutting')
  RECIPES_DECORATIONS_SULFUR_BRICK_WALL_FROM_SULFUR_STONECUTTING = Kee[str](
    'recipes/decorations/sulfur_brick_wall_from_sulfur_stonecutting')
  RECIPES_DECORATIONS_SULFUR_WALL = Kee[str]('recipes/decorations/sulfur_wall')
  RECIPES_DECORATIONS_SULFUR_WALL_FROM_SULFUR_STONECUTTING = Kee[str](
    'recipes/decorations/sulfur_wall_from_sulfur_stonecutting')
  RECIPES_DECORATIONS_TORCH = Kee[str]('recipes/decorations/torch')
  RECIPES_DECORATIONS_TUFF_BRICK_WALL = Kee[str](
    'recipes/decorations/tuff_brick_wall')
  RECIPES_DECORATIONS_TUFF_BRICK_WALL_FROM_POLISHED_TUFF_STONECUTTING = Kee[str](
    'recipes/decorations/tuff_brick_wall_from_polished_tuff_stonecutting')
  RECIPES_DECORATIONS_TUFF_BRICK_WALL_FROM_TUFF_BRICKS_STONECUTTING = Kee[str](
    'recipes/decorations/tuff_brick_wall_from_tuff_bricks_stonecutting')
  RECIPES_DECORATIONS_TUFF_BRICK_WALL_FROM_TUFF_STONECUTTING = Kee[str](
    'recipes/decorations/tuff_brick_wall_from_tuff_stonecutting')
  RECIPES_DECORATIONS_TUFF_WALL = Kee[str]('recipes/decorations/tuff_wall')
  RECIPES_DECORATIONS_TUFF_WALL_FROM_TUFF_STONECUTTING = Kee[str](
    'recipes/decorations/tuff_wall_from_tuff_stonecutting')
  RECIPES_DECORATIONS_WARPED_FENCE = Kee[str](
    'recipes/decorations/warped_fence')
  RECIPES_DECORATIONS_WARPED_HANGING_SIGN = Kee[str](
    'recipes/decorations/warped_hanging_sign')
  RECIPES_DECORATIONS_WARPED_SHELF = Kee[str](
    'recipes/decorations/warped_shelf')
  RECIPES_DECORATIONS_WARPED_SIGN = Kee[str]('recipes/decorations/warped_sign')
  RECIPES_DECORATIONS_WHITE_BANNER = Kee[str](
    'recipes/decorations/white_banner')
  RECIPES_DECORATIONS_WHITE_BED = Kee[str]('recipes/decorations/white_bed')
  RECIPES_DECORATIONS_WHITE_CANDLE = Kee[str](
    'recipes/decorations/white_candle')
  RECIPES_DECORATIONS_WHITE_CARPET = Kee[str](
    'recipes/decorations/white_carpet')
  RECIPES_DECORATIONS_WHITE_CUSHION = Kee[str](
    'recipes/decorations/white_cushion')
  RECIPES_DECORATIONS_WHITE_GLAZED_TERRACOTTA = Kee[str](
    'recipes/decorations/white_glazed_terracotta')
  RECIPES_DECORATIONS_WHITE_SHULKER_BOX = Kee[str](
    'recipes/decorations/white_shulker_box')
  RECIPES_DECORATIONS_WHITE_STAINED_GLASS_PANE = Kee[str](
    'recipes/decorations/white_stained_glass_pane')
  RECIPES_DECORATIONS_WHITE_STAINED_GLASS_PANE_FROM_GLASS_PANE = Kee[str](
    'recipes/decorations/white_stained_glass_pane_from_glass_pane')
  RECIPES_DECORATIONS_YELLOW_BANNER = Kee[str](
    'recipes/decorations/yellow_banner')
  RECIPES_DECORATIONS_YELLOW_BED = Kee[str]('recipes/decorations/yellow_bed')
  RECIPES_DECORATIONS_YELLOW_BED_FROM_WHITE_BED = Kee[str](
    'recipes/decorations/yellow_bed_from_white_bed')
  RECIPES_DECORATIONS_YELLOW_CANDLE = Kee[str](
    'recipes/decorations/yellow_candle')
  RECIPES_DECORATIONS_YELLOW_CARPET = Kee[str](
    'recipes/decorations/yellow_carpet')
  RECIPES_DECORATIONS_YELLOW_CARPET_FROM_WHITE_CARPET = Kee[str](
    'recipes/decorations/yellow_carpet_from_white_carpet')
  RECIPES_DECORATIONS_YELLOW_CUSHION = Kee[str](
    'recipes/decorations/yellow_cushion')
  RECIPES_DECORATIONS_YELLOW_GLAZED_TERRACOTTA = Kee[str](
    'recipes/decorations/yellow_glazed_terracotta')
  RECIPES_DECORATIONS_YELLOW_SHULKER_BOX = Kee[str](
    'recipes/decorations/yellow_shulker_box')
  RECIPES_DECORATIONS_YELLOW_STAINED_GLASS_PANE = Kee[str](
    'recipes/decorations/yellow_stained_glass_pane')
  RECIPES_DECORATIONS_YELLOW_STAINED_GLASS_PANE_FROM_GLASS_PANE = Kee[str](
    'recipes/decorations/yellow_stained_glass_pane_from_glass_pane')
  RECIPES_FOOD_BAKED_POTATO = Kee[str]('recipes/food/baked_potato')
  RECIPES_FOOD_BAKED_POTATO_FROM_CAMPFIRE_COOKING = Kee[str](
    'recipes/food/baked_potato_from_campfire_cooking')
  RECIPES_FOOD_BAKED_POTATO_FROM_SMOKING = Kee[str](
    'recipes/food/baked_potato_from_smoking')
  RECIPES_FOOD_BEETROOT_SOUP = Kee[str]('recipes/food/beetroot_soup')
  RECIPES_FOOD_BREAD = Kee[str]('recipes/food/bread')
  RECIPES_FOOD_CAKE = Kee[str]('recipes/food/cake')
  RECIPES_FOOD_COOKED_BEEF = Kee[str]('recipes/food/cooked_beef')
  RECIPES_FOOD_COOKED_BEEF_FROM_CAMPFIRE_COOKING = Kee[str](
    'recipes/food/cooked_beef_from_campfire_cooking')
  RECIPES_FOOD_COOKED_BEEF_FROM_SMOKING = Kee[str](
    'recipes/food/cooked_beef_from_smoking')
  RECIPES_FOOD_COOKED_CHICKEN = Kee[str]('recipes/food/cooked_chicken')
  RECIPES_FOOD_COOKED_CHICKEN_FROM_CAMPFIRE_COOKING = Kee[str](
    'recipes/food/cooked_chicken_from_campfire_cooking')
  RECIPES_FOOD_COOKED_CHICKEN_FROM_SMOKING = Kee[str](
    'recipes/food/cooked_chicken_from_smoking')
  RECIPES_FOOD_COOKED_COD = Kee[str]('recipes/food/cooked_cod')
  RECIPES_FOOD_COOKED_COD_FROM_CAMPFIRE_COOKING = Kee[str](
    'recipes/food/cooked_cod_from_campfire_cooking')
  RECIPES_FOOD_COOKED_COD_FROM_SMOKING = Kee[str](
    'recipes/food/cooked_cod_from_smoking')
  RECIPES_FOOD_COOKED_MUTTON = Kee[str]('recipes/food/cooked_mutton')
  RECIPES_FOOD_COOKED_MUTTON_FROM_CAMPFIRE_COOKING = Kee[str](
    'recipes/food/cooked_mutton_from_campfire_cooking')
  RECIPES_FOOD_COOKED_MUTTON_FROM_SMOKING = Kee[str](
    'recipes/food/cooked_mutton_from_smoking')
  RECIPES_FOOD_COOKED_PORKCHOP = Kee[str]('recipes/food/cooked_porkchop')
  RECIPES_FOOD_COOKED_PORKCHOP_FROM_CAMPFIRE_COOKING = Kee[str](
    'recipes/food/cooked_porkchop_from_campfire_cooking')
  RECIPES_FOOD_COOKED_PORKCHOP_FROM_SMOKING = Kee[str](
    'recipes/food/cooked_porkchop_from_smoking')
  RECIPES_FOOD_COOKED_RABBIT = Kee[str]('recipes/food/cooked_rabbit')
  RECIPES_FOOD_COOKED_RABBIT_FROM_CAMPFIRE_COOKING = Kee[str](
    'recipes/food/cooked_rabbit_from_campfire_cooking')
  RECIPES_FOOD_COOKED_RABBIT_FROM_SMOKING = Kee[str](
    'recipes/food/cooked_rabbit_from_smoking')
  RECIPES_FOOD_COOKED_SALMON = Kee[str]('recipes/food/cooked_salmon')
  RECIPES_FOOD_COOKED_SALMON_FROM_CAMPFIRE_COOKING = Kee[str](
    'recipes/food/cooked_salmon_from_campfire_cooking')
  RECIPES_FOOD_COOKED_SALMON_FROM_SMOKING = Kee[str](
    'recipes/food/cooked_salmon_from_smoking')
  RECIPES_FOOD_COOKIE = Kee[str]('recipes/food/cookie')
  RECIPES_FOOD_DRIED_KELP = Kee[str]('recipes/food/dried_kelp')
  RECIPES_FOOD_DRIED_KELP_FROM_CAMPFIRE_COOKING = Kee[str](
    'recipes/food/dried_kelp_from_campfire_cooking')
  RECIPES_FOOD_DRIED_KELP_FROM_SMELTING = Kee[str](
    'recipes/food/dried_kelp_from_smelting')
  RECIPES_FOOD_DRIED_KELP_FROM_SMOKING = Kee[str](
    'recipes/food/dried_kelp_from_smoking')
  RECIPES_FOOD_GOLDEN_APPLE = Kee[str]('recipes/food/golden_apple')
  RECIPES_FOOD_HONEY_BOTTLE = Kee[str]('recipes/food/honey_bottle')
  RECIPES_FOOD_MUSHROOM_STEW = Kee[str]('recipes/food/mushroom_stew')
  RECIPES_FOOD_PUMPKIN_PIE = Kee[str]('recipes/food/pumpkin_pie')
  RECIPES_FOOD_RABBIT_STEW_FROM_BROWN_MUSHROOM = Kee[str](
    'recipes/food/rabbit_stew_from_brown_mushroom')
  RECIPES_FOOD_RABBIT_STEW_FROM_RED_MUSHROOM = Kee[str](
    'recipes/food/rabbit_stew_from_red_mushroom')
  RECIPES_FOOD_RABBIT_STEW_FROM_SHELF_MUSHROOM = Kee[str](
    'recipes/food/rabbit_stew_from_shelf_mushroom')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_ALLIUM = Kee[str](
    'recipes/food/suspicious_stew_from_allium')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_AZURE_BLUET = Kee[str](
    'recipes/food/suspicious_stew_from_azure_bluet')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_BLUE_ORCHID = Kee[str](
    'recipes/food/suspicious_stew_from_blue_orchid')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_CLOSED_EYEBLOSSOM = Kee[str](
    'recipes/food/suspicious_stew_from_closed_eyeblossom')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_CORNFLOWER = Kee[str](
    'recipes/food/suspicious_stew_from_cornflower')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_DANDELION = Kee[str](
    'recipes/food/suspicious_stew_from_dandelion')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_GOLDEN_DANDELION = Kee[str](
    'recipes/food/suspicious_stew_from_golden_dandelion')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_LILY_OF_THE_VALLEY = Kee[str](
    'recipes/food/suspicious_stew_from_lily_of_the_valley')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_OPEN_EYEBLOSSOM = Kee[str](
    'recipes/food/suspicious_stew_from_open_eyeblossom')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_ORANGE_TULIP = Kee[str](
    'recipes/food/suspicious_stew_from_orange_tulip')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_OXEYE_DAISY = Kee[str](
    'recipes/food/suspicious_stew_from_oxeye_daisy')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_PINK_TULIP = Kee[str](
    'recipes/food/suspicious_stew_from_pink_tulip')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_POPPY = Kee[str](
    'recipes/food/suspicious_stew_from_poppy')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_RED_TULIP = Kee[str](
    'recipes/food/suspicious_stew_from_red_tulip')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_TORCHFLOWER = Kee[str](
    'recipes/food/suspicious_stew_from_torchflower')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_WHITE_TULIP = Kee[str](
    'recipes/food/suspicious_stew_from_white_tulip')
  RECIPES_FOOD_SUSPICIOUS_STEW_FROM_WITHER_ROSE = Kee[str](
    'recipes/food/suspicious_stew_from_wither_rose')
  RECIPES_MISC_BEACON = Kee[str]('recipes/misc/beacon')
  RECIPES_MISC_BLACK_DYE = Kee[str]('recipes/misc/black_dye')
  RECIPES_MISC_BLACK_DYE_FROM_WITHER_ROSE = Kee[str](
    'recipes/misc/black_dye_from_wither_rose')
  RECIPES_MISC_BLUE_DYE = Kee[str]('recipes/misc/blue_dye')
  RECIPES_MISC_BLUE_DYE_FROM_CORNFLOWER = Kee[str](
    'recipes/misc/blue_dye_from_cornflower')
  RECIPES_MISC_BOLT_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/bolt_armor_trim_smithing_template')
  RECIPES_MISC_BOLT_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/bolt_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_BONE_MEAL = Kee[str]('recipes/misc/bone_meal')
  RECIPES_MISC_BONE_MEAL_FROM_BONE_BLOCK = Kee[str](
    'recipes/misc/bone_meal_from_bone_block')
  RECIPES_MISC_BOOK = Kee[str]('recipes/misc/book')
  RECIPES_MISC_BORDURE_INDENTED_BANNER_PATTERN = Kee[str](
    'recipes/misc/bordure_indented_banner_pattern')
  RECIPES_MISC_BOWL = Kee[str]('recipes/misc/bowl')
  RECIPES_MISC_BRICK = Kee[str]('recipes/misc/brick')
  RECIPES_MISC_BROWN_DYE = Kee[str]('recipes/misc/brown_dye')
  RECIPES_MISC_BUCKET = Kee[str]('recipes/misc/bucket')
  RECIPES_MISC_CACTUS_GREEN = Kee[str]('recipes/misc/cactus_green')
  RECIPES_MISC_CHARCOAL = Kee[str]('recipes/misc/charcoal')
  RECIPES_MISC_COAL = Kee[str]('recipes/misc/coal')
  RECIPES_MISC_COAL_FROM_BLASTING = Kee[str]('recipes/misc/coal_from_blasting')
  RECIPES_MISC_COAL_FROM_BLASTING_COAL_ORE = Kee[str](
    'recipes/misc/coal_from_blasting_coal_ore')
  RECIPES_MISC_COAL_FROM_BLASTING_DEEPSLATE_COAL_ORE = Kee[str](
    'recipes/misc/coal_from_blasting_deepslate_coal_ore')
  RECIPES_MISC_COAL_FROM_SMELTING = Kee[str]('recipes/misc/coal_from_smelting')
  RECIPES_MISC_COAL_FROM_SMELTING_COAL_ORE = Kee[str](
    'recipes/misc/coal_from_smelting_coal_ore')
  RECIPES_MISC_COAL_FROM_SMELTING_DEEPSLATE_COAL_ORE = Kee[str](
    'recipes/misc/coal_from_smelting_deepslate_coal_ore')
  RECIPES_MISC_COAST_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/coast_armor_trim_smithing_template')
  RECIPES_MISC_COAST_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/coast_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_CONDUIT = Kee[str]('recipes/misc/conduit')
  RECIPES_MISC_COPPER_INGOT = Kee[str]('recipes/misc/copper_ingot')
  RECIPES_MISC_COPPER_INGOT_FROM_BLASTING_COPPER_ORE = Kee[str](
    'recipes/misc/copper_ingot_from_blasting_copper_ore')
  RECIPES_MISC_COPPER_INGOT_FROM_BLASTING_DEEPSLATE_COPPER_ORE = Kee[str](
    'recipes/misc/copper_ingot_from_blasting_deepslate_copper_ore')
  RECIPES_MISC_COPPER_INGOT_FROM_BLASTING_RAW_COPPER = Kee[str](
    'recipes/misc/copper_ingot_from_blasting_raw_copper')
  RECIPES_MISC_COPPER_INGOT_FROM_NUGGETS = Kee[str](
    'recipes/misc/copper_ingot_from_nuggets')
  RECIPES_MISC_COPPER_INGOT_FROM_SMELTING_COPPER_ORE = Kee[str](
    'recipes/misc/copper_ingot_from_smelting_copper_ore')
  RECIPES_MISC_COPPER_INGOT_FROM_SMELTING_DEEPSLATE_COPPER_ORE = Kee[str](
    'recipes/misc/copper_ingot_from_smelting_deepslate_copper_ore')
  RECIPES_MISC_COPPER_INGOT_FROM_SMELTING_RAW_COPPER = Kee[str](
    'recipes/misc/copper_ingot_from_smelting_raw_copper')
  RECIPES_MISC_COPPER_INGOT_FROM_WAXED_COPPER_BLOCK = Kee[str](
    'recipes/misc/copper_ingot_from_waxed_copper_block')
  RECIPES_MISC_COPPER_NUGGET = Kee[str]('recipes/misc/copper_nugget')
  RECIPES_MISC_COPPER_NUGGET_FROM_BLASTING = Kee[str](
    'recipes/misc/copper_nugget_from_blasting')
  RECIPES_MISC_COPPER_NUGGET_FROM_SMELTING = Kee[str](
    'recipes/misc/copper_nugget_from_smelting')
  RECIPES_MISC_CREAKING_HEART = Kee[str]('recipes/misc/creaking_heart')
  RECIPES_MISC_CREEPER_BANNER_PATTERN = Kee[str](
    'recipes/misc/creeper_banner_pattern')
  RECIPES_MISC_CYAN_DYE = Kee[str]('recipes/misc/cyan_dye')
  RECIPES_MISC_CYAN_DYE_FROM_PITCHER_PLANT = Kee[str](
    'recipes/misc/cyan_dye_from_pitcher_plant')
  RECIPES_MISC_DIAMOND = Kee[str]('recipes/misc/diamond')
  RECIPES_MISC_DIAMOND_FROM_BLASTING = Kee[str](
    'recipes/misc/diamond_from_blasting')
  RECIPES_MISC_DIAMOND_FROM_BLASTING_DEEPSLATE_DIAMOND_ORE = Kee[str](
    'recipes/misc/diamond_from_blasting_deepslate_diamond_ore')
  RECIPES_MISC_DIAMOND_FROM_BLASTING_DIAMOND_ORE = Kee[str](
    'recipes/misc/diamond_from_blasting_diamond_ore')
  RECIPES_MISC_DIAMOND_FROM_SMELTING = Kee[str](
    'recipes/misc/diamond_from_smelting')
  RECIPES_MISC_DIAMOND_FROM_SMELTING_DEEPSLATE_DIAMOND_ORE = Kee[str](
    'recipes/misc/diamond_from_smelting_deepslate_diamond_ore')
  RECIPES_MISC_DIAMOND_FROM_SMELTING_DIAMOND_ORE = Kee[str](
    'recipes/misc/diamond_from_smelting_diamond_ore')
  RECIPES_MISC_DUNE_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/dune_armor_trim_smithing_template')
  RECIPES_MISC_DUNE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/dune_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_EMERALD = Kee[str]('recipes/misc/emerald')
  RECIPES_MISC_EMERALD_FROM_BLASTING = Kee[str](
    'recipes/misc/emerald_from_blasting')
  RECIPES_MISC_EMERALD_FROM_BLASTING_DEEPSLATE_EMERALD_ORE = Kee[str](
    'recipes/misc/emerald_from_blasting_deepslate_emerald_ore')
  RECIPES_MISC_EMERALD_FROM_BLASTING_EMERALD_ORE = Kee[str](
    'recipes/misc/emerald_from_blasting_emerald_ore')
  RECIPES_MISC_EMERALD_FROM_SMELTING = Kee[str](
    'recipes/misc/emerald_from_smelting')
  RECIPES_MISC_EMERALD_FROM_SMELTING_DEEPSLATE_EMERALD_ORE = Kee[str](
    'recipes/misc/emerald_from_smelting_deepslate_emerald_ore')
  RECIPES_MISC_EMERALD_FROM_SMELTING_EMERALD_ORE = Kee[str](
    'recipes/misc/emerald_from_smelting_emerald_ore')
  RECIPES_MISC_ENDER_EYE = Kee[str]('recipes/misc/ender_eye')
  RECIPES_MISC_EYE_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/eye_armor_trim_smithing_template')
  RECIPES_MISC_EYE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/eye_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_FIELD_MASONED_BANNER_PATTERN = Kee[str](
    'recipes/misc/field_masoned_banner_pattern')
  RECIPES_MISC_FIRE_CHARGE = Kee[str]('recipes/misc/fire_charge')
  RECIPES_MISC_FIREWORK_ROCKET_SIMPLE = Kee[str](
    'recipes/misc/firework_rocket_simple')
  RECIPES_MISC_FLOW_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/flow_armor_trim_smithing_template')
  RECIPES_MISC_FLOW_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/flow_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_FLOWER_BANNER_PATTERN = Kee[str](
    'recipes/misc/flower_banner_pattern')
  RECIPES_MISC_GOLD_INGOT = Kee[str]('recipes/misc/gold_ingot')
  RECIPES_MISC_GOLD_INGOT_FROM_BLASTING = Kee[str](
    'recipes/misc/gold_ingot_from_blasting')
  RECIPES_MISC_GOLD_INGOT_FROM_BLASTING_DEEPSLATE_GOLD_ORE = Kee[str](
    'recipes/misc/gold_ingot_from_blasting_deepslate_gold_ore')
  RECIPES_MISC_GOLD_INGOT_FROM_BLASTING_GOLD_ORE = Kee[str](
    'recipes/misc/gold_ingot_from_blasting_gold_ore')
  RECIPES_MISC_GOLD_INGOT_FROM_BLASTING_NETHER_GOLD_ORE = Kee[str](
    'recipes/misc/gold_ingot_from_blasting_nether_gold_ore')
  RECIPES_MISC_GOLD_INGOT_FROM_BLASTING_RAW_GOLD = Kee[str](
    'recipes/misc/gold_ingot_from_blasting_raw_gold')
  RECIPES_MISC_GOLD_INGOT_FROM_GOLD_BLOCK = Kee[str](
    'recipes/misc/gold_ingot_from_gold_block')
  RECIPES_MISC_GOLD_INGOT_FROM_NUGGETS = Kee[str](
    'recipes/misc/gold_ingot_from_nuggets')
  RECIPES_MISC_GOLD_INGOT_FROM_SMELTING_DEEPSLATE_GOLD_ORE = Kee[str](
    'recipes/misc/gold_ingot_from_smelting_deepslate_gold_ore')
  RECIPES_MISC_GOLD_INGOT_FROM_SMELTING_GOLD_ORE = Kee[str](
    'recipes/misc/gold_ingot_from_smelting_gold_ore')
  RECIPES_MISC_GOLD_INGOT_FROM_SMELTING_NETHER_GOLD_ORE = Kee[str](
    'recipes/misc/gold_ingot_from_smelting_nether_gold_ore')
  RECIPES_MISC_GOLD_INGOT_FROM_SMELTING_RAW_GOLD = Kee[str](
    'recipes/misc/gold_ingot_from_smelting_raw_gold')
  RECIPES_MISC_GOLD_NUGGET = Kee[str]('recipes/misc/gold_nugget')
  RECIPES_MISC_GOLD_NUGGET_FROM_BLASTING = Kee[str](
    'recipes/misc/gold_nugget_from_blasting')
  RECIPES_MISC_GOLD_NUGGET_FROM_SMELTING = Kee[str](
    'recipes/misc/gold_nugget_from_smelting')
  RECIPES_MISC_GRAY_DYE = Kee[str]('recipes/misc/gray_dye')
  RECIPES_MISC_GRAY_DYE_FROM_CLOSED_EYEBLOSSOM = Kee[str](
    'recipes/misc/gray_dye_from_closed_eyeblossom')
  RECIPES_MISC_GREEN_DYE = Kee[str]('recipes/misc/green_dye')
  RECIPES_MISC_HOST_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/host_armor_trim_smithing_template')
  RECIPES_MISC_HOST_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/host_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_IRON_INGOT = Kee[str]('recipes/misc/iron_ingot')
  RECIPES_MISC_IRON_INGOT_FROM_BLASTING = Kee[str](
    'recipes/misc/iron_ingot_from_blasting')
  RECIPES_MISC_IRON_INGOT_FROM_BLASTING_DEEPSLATE_IRON_ORE = Kee[str](
    'recipes/misc/iron_ingot_from_blasting_deepslate_iron_ore')
  RECIPES_MISC_IRON_INGOT_FROM_BLASTING_IRON_ORE = Kee[str](
    'recipes/misc/iron_ingot_from_blasting_iron_ore')
  RECIPES_MISC_IRON_INGOT_FROM_BLASTING_RAW_IRON = Kee[str](
    'recipes/misc/iron_ingot_from_blasting_raw_iron')
  RECIPES_MISC_IRON_INGOT_FROM_IRON_BLOCK = Kee[str](
    'recipes/misc/iron_ingot_from_iron_block')
  RECIPES_MISC_IRON_INGOT_FROM_NUGGETS = Kee[str](
    'recipes/misc/iron_ingot_from_nuggets')
  RECIPES_MISC_IRON_INGOT_FROM_SMELTING_DEEPSLATE_IRON_ORE = Kee[str](
    'recipes/misc/iron_ingot_from_smelting_deepslate_iron_ore')
  RECIPES_MISC_IRON_INGOT_FROM_SMELTING_IRON_ORE = Kee[str](
    'recipes/misc/iron_ingot_from_smelting_iron_ore')
  RECIPES_MISC_IRON_INGOT_FROM_SMELTING_RAW_IRON = Kee[str](
    'recipes/misc/iron_ingot_from_smelting_raw_iron')
  RECIPES_MISC_IRON_NUGGET = Kee[str]('recipes/misc/iron_nugget')
  RECIPES_MISC_IRON_NUGGET_FROM_BLASTING = Kee[str](
    'recipes/misc/iron_nugget_from_blasting')
  RECIPES_MISC_IRON_NUGGET_FROM_SMELTING = Kee[str](
    'recipes/misc/iron_nugget_from_smelting')
  RECIPES_MISC_LAPIS_FROM_BLASTING = Kee[str](
    'recipes/misc/lapis_from_blasting')
  RECIPES_MISC_LAPIS_FROM_SMELTING = Kee[str](
    'recipes/misc/lapis_from_smelting')
  RECIPES_MISC_LAPIS_LAZULI = Kee[str]('recipes/misc/lapis_lazuli')
  RECIPES_MISC_LAPIS_LAZULI_FROM_BLASTING_DEEPSLATE_LAPIS_ORE = Kee[str](
    'recipes/misc/lapis_lazuli_from_blasting_deepslate_lapis_ore')
  RECIPES_MISC_LAPIS_LAZULI_FROM_BLASTING_LAPIS_ORE = Kee[str](
    'recipes/misc/lapis_lazuli_from_blasting_lapis_ore')
  RECIPES_MISC_LAPIS_LAZULI_FROM_SMELTING_DEEPSLATE_LAPIS_ORE = Kee[str](
    'recipes/misc/lapis_lazuli_from_smelting_deepslate_lapis_ore')
  RECIPES_MISC_LAPIS_LAZULI_FROM_SMELTING_LAPIS_ORE = Kee[str](
    'recipes/misc/lapis_lazuli_from_smelting_lapis_ore')
  RECIPES_MISC_LEAF_LITTER = Kee[str]('recipes/misc/leaf_litter')
  RECIPES_MISC_LEATHER = Kee[str]('recipes/misc/leather')
  RECIPES_MISC_LEATHER_BOOTS_DYED = Kee[str]('recipes/misc/leather_boots_dyed')
  RECIPES_MISC_LEATHER_CHESTPLATE_DYED = Kee[str](
    'recipes/misc/leather_chestplate_dyed')
  RECIPES_MISC_LEATHER_HELMET_DYED = Kee[str](
    'recipes/misc/leather_helmet_dyed')
  RECIPES_MISC_LEATHER_HORSE_ARMOR = Kee[str](
    'recipes/misc/leather_horse_armor')
  RECIPES_MISC_LEATHER_HORSE_ARMOR_DYED = Kee[str](
    'recipes/misc/leather_horse_armor_dyed')
  RECIPES_MISC_LEATHER_LEGGINGS_DYED = Kee[str](
    'recipes/misc/leather_leggings_dyed')
  RECIPES_MISC_LIGHT_BLUE_DYE_FROM_BLUE_ORCHID = Kee[str](
    'recipes/misc/light_blue_dye_from_blue_orchid')
  RECIPES_MISC_LIGHT_BLUE_DYE_FROM_BLUE_WHITE_DYE = Kee[str](
    'recipes/misc/light_blue_dye_from_blue_white_dye')
  RECIPES_MISC_LIGHT_BLUE_DYE_FROM_LAPIS_BONEMEAL = Kee[str](
    'recipes/misc/light_blue_dye_from_lapis_bonemeal')
  RECIPES_MISC_LIGHT_GRAY_DYE_FROM_AZURE_BLUET = Kee[str](
    'recipes/misc/light_gray_dye_from_azure_bluet')
  RECIPES_MISC_LIGHT_GRAY_DYE_FROM_BLACK_WHITE_DYE = Kee[str](
    'recipes/misc/light_gray_dye_from_black_white_dye')
  RECIPES_MISC_LIGHT_GRAY_DYE_FROM_GRAY_BONEMEAL = Kee[str](
    'recipes/misc/light_gray_dye_from_gray_bonemeal')
  RECIPES_MISC_LIGHT_GRAY_DYE_FROM_GRAY_WHITE_DYE = Kee[str](
    'recipes/misc/light_gray_dye_from_gray_white_dye')
  RECIPES_MISC_LIGHT_GRAY_DYE_FROM_INK_BONEMEAL = Kee[str](
    'recipes/misc/light_gray_dye_from_ink_bonemeal')
  RECIPES_MISC_LIGHT_GRAY_DYE_FROM_OXEYE_DAISY = Kee[str](
    'recipes/misc/light_gray_dye_from_oxeye_daisy')
  RECIPES_MISC_LIGHT_GRAY_DYE_FROM_WHITE_TULIP = Kee[str](
    'recipes/misc/light_gray_dye_from_white_tulip')
  RECIPES_MISC_LIME_DYE = Kee[str]('recipes/misc/lime_dye')
  RECIPES_MISC_LIME_DYE_FROM_SMELTING = Kee[str](
    'recipes/misc/lime_dye_from_smelting')
  RECIPES_MISC_MAGENTA_DYE_FROM_ALLIUM = Kee[str](
    'recipes/misc/magenta_dye_from_allium')
  RECIPES_MISC_MAGENTA_DYE_FROM_BLUE_RED_PINK = Kee[str](
    'recipes/misc/magenta_dye_from_blue_red_pink')
  RECIPES_MISC_MAGENTA_DYE_FROM_BLUE_RED_WHITE_DYE = Kee[str](
    'recipes/misc/magenta_dye_from_blue_red_white_dye')
  RECIPES_MISC_MAGENTA_DYE_FROM_LAPIS_INK_BONEMEAL = Kee[str](
    'recipes/misc/magenta_dye_from_lapis_ink_bonemeal')
  RECIPES_MISC_MAGENTA_DYE_FROM_LAPIS_RED_PINK = Kee[str](
    'recipes/misc/magenta_dye_from_lapis_red_pink')
  RECIPES_MISC_MAGENTA_DYE_FROM_LILAC = Kee[str](
    'recipes/misc/magenta_dye_from_lilac')
  RECIPES_MISC_MAGENTA_DYE_FROM_PURPLE_AND_PINK = Kee[str](
    'recipes/misc/magenta_dye_from_purple_and_pink')
  RECIPES_MISC_MAP = Kee[str]('recipes/misc/map')
  RECIPES_MISC_MAP_CLONING = Kee[str]('recipes/misc/map_cloning')
  RECIPES_MISC_MELON_SEEDS = Kee[str]('recipes/misc/melon_seeds')
  RECIPES_MISC_MOJANG_BANNER_PATTERN = Kee[str](
    'recipes/misc/mojang_banner_pattern')
  RECIPES_MISC_MUSIC_DISC_5 = Kee[str]('recipes/misc/music_disc_5')
  RECIPES_MISC_NETHER_BRICK = Kee[str]('recipes/misc/nether_brick')
  RECIPES_MISC_NETHERITE_INGOT = Kee[str]('recipes/misc/netherite_ingot')
  RECIPES_MISC_NETHERITE_INGOT_FROM_NETHERITE_BLOCK = Kee[str](
    'recipes/misc/netherite_ingot_from_netherite_block')
  RECIPES_MISC_NETHERITE_SCRAP = Kee[str]('recipes/misc/netherite_scrap')
  RECIPES_MISC_NETHERITE_SCRAP_FROM_BLASTING = Kee[str](
    'recipes/misc/netherite_scrap_from_blasting')
  RECIPES_MISC_NETHERITE_UPGRADE_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/netherite_upgrade_smithing_template')
  RECIPES_MISC_ORANGE_DYE_FROM_OPEN_EYEBLOSSOM = Kee[str](
    'recipes/misc/orange_dye_from_open_eyeblossom')
  RECIPES_MISC_ORANGE_DYE_FROM_ORANGE_TULIP = Kee[str](
    'recipes/misc/orange_dye_from_orange_tulip')
  RECIPES_MISC_ORANGE_DYE_FROM_RED_YELLOW = Kee[str](
    'recipes/misc/orange_dye_from_red_yellow')
  RECIPES_MISC_ORANGE_DYE_FROM_TORCHFLOWER = Kee[str](
    'recipes/misc/orange_dye_from_torchflower')
  RECIPES_MISC_PAPER = Kee[str]('recipes/misc/paper')
  RECIPES_MISC_PINK_DYE_FROM_CACTUS_FLOWER = Kee[str](
    'recipes/misc/pink_dye_from_cactus_flower')
  RECIPES_MISC_PINK_DYE_FROM_PEONY = Kee[str](
    'recipes/misc/pink_dye_from_peony')
  RECIPES_MISC_PINK_DYE_FROM_PINK_PETALS = Kee[str](
    'recipes/misc/pink_dye_from_pink_petals')
  RECIPES_MISC_PINK_DYE_FROM_PINK_TULIP = Kee[str](
    'recipes/misc/pink_dye_from_pink_tulip')
  RECIPES_MISC_PINK_DYE_FROM_RED_BONEMEAL = Kee[str](
    'recipes/misc/pink_dye_from_red_bonemeal')
  RECIPES_MISC_PINK_DYE_FROM_RED_WHITE_DYE = Kee[str](
    'recipes/misc/pink_dye_from_red_white_dye')
  RECIPES_MISC_POPPED_CHORUS_FRUIT = Kee[str](
    'recipes/misc/popped_chorus_fruit')
  RECIPES_MISC_PUMPKIN_SEEDS = Kee[str]('recipes/misc/pumpkin_seeds')
  RECIPES_MISC_PURPLE_DYE = Kee[str]('recipes/misc/purple_dye')
  RECIPES_MISC_QUARTZ = Kee[str]('recipes/misc/quartz')
  RECIPES_MISC_QUARTZ_FROM_BLASTING = Kee[str](
    'recipes/misc/quartz_from_blasting')
  RECIPES_MISC_RAISER_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/raiser_armor_trim_smithing_template')
  RECIPES_MISC_RAISER_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/raiser_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_RAW_COPPER = Kee[str]('recipes/misc/raw_copper')
  RECIPES_MISC_RAW_GOLD = Kee[str]('recipes/misc/raw_gold')
  RECIPES_MISC_RAW_IRON = Kee[str]('recipes/misc/raw_iron')
  RECIPES_MISC_RED_DYE_FROM_BEETROOT = Kee[str](
    'recipes/misc/red_dye_from_beetroot')
  RECIPES_MISC_RED_DYE_FROM_POPPY = Kee[str]('recipes/misc/red_dye_from_poppy')
  RECIPES_MISC_RED_DYE_FROM_ROSE_BUSH = Kee[str](
    'recipes/misc/red_dye_from_rose_bush')
  RECIPES_MISC_RED_DYE_FROM_TULIP = Kee[str]('recipes/misc/red_dye_from_tulip')
  RECIPES_MISC_RESIN_BRICK = Kee[str]('recipes/misc/resin_brick')
  RECIPES_MISC_RESIN_CLUMP = Kee[str]('recipes/misc/resin_clump')
  RECIPES_MISC_RIB_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/rib_armor_trim_smithing_template')
  RECIPES_MISC_RIB_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/rib_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_SENTRY_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/sentry_armor_trim_smithing_template')
  RECIPES_MISC_SENTRY_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/sentry_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_SHAPER_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/shaper_armor_trim_smithing_template')
  RECIPES_MISC_SHAPER_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/shaper_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_SILENCE_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/silence_armor_trim_smithing_template')
  RECIPES_MISC_SILENCE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/silence_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_SKULL_BANNER_PATTERN = Kee[str](
    'recipes/misc/skull_banner_pattern')
  RECIPES_MISC_SLIME_BALL = Kee[str]('recipes/misc/slime_ball')
  RECIPES_MISC_SNOUT_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/snout_armor_trim_smithing_template')
  RECIPES_MISC_SNOUT_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/snout_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_SPIRE_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/spire_armor_trim_smithing_template')
  RECIPES_MISC_SPIRE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/spire_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_STICK = Kee[str]('recipes/misc/stick')
  RECIPES_MISC_STICK_FROM_BAMBOO_ITEM = Kee[str](
    'recipes/misc/stick_from_bamboo_item')
  RECIPES_MISC_SUGAR_FROM_HONEY_BOTTLE = Kee[str](
    'recipes/misc/sugar_from_honey_bottle')
  RECIPES_MISC_SUGAR_FROM_SUGAR_CANE = Kee[str](
    'recipes/misc/sugar_from_sugar_cane')
  RECIPES_MISC_TIDE_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/tide_armor_trim_smithing_template')
  RECIPES_MISC_TIDE_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/tide_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_TIPPED_ARROW = Kee[str]('recipes/misc/tipped_arrow')
  RECIPES_MISC_VEX_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/vex_armor_trim_smithing_template')
  RECIPES_MISC_VEX_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/vex_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_WARD_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/ward_armor_trim_smithing_template')
  RECIPES_MISC_WARD_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/ward_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_WAYFINDER_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/wayfinder_armor_trim_smithing_template')
  RECIPES_MISC_WAYFINDER_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/wayfinder_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_WHEAT = Kee[str]('recipes/misc/wheat')
  RECIPES_MISC_WHITE_DYE = Kee[str]('recipes/misc/white_dye')
  RECIPES_MISC_WHITE_DYE_FROM_LILY_OF_THE_VALLEY = Kee[str](
    'recipes/misc/white_dye_from_lily_of_the_valley')
  RECIPES_MISC_WILD_ARMOR_TRIM_SMITHING_TEMPLATE = Kee[str](
    'recipes/misc/wild_armor_trim_smithing_template')
  RECIPES_MISC_WILD_ARMOR_TRIM_SMITHING_TEMPLATE_SMITHING_TRIM = Kee[str](
    'recipes/misc/wild_armor_trim_smithing_template_smithing_trim')
  RECIPES_MISC_WIND_CHARGE = Kee[str]('recipes/misc/wind_charge')
  RECIPES_MISC_WOLF_ARMOR_DYED = Kee[str]('recipes/misc/wolf_armor_dyed')
  RECIPES_MISC_WRITABLE_BOOK = Kee[str]('recipes/misc/writable_book')
  RECIPES_MISC_YELLOW_DYE_FROM_DANDELION = Kee[str](
    'recipes/misc/yellow_dye_from_dandelion')
  RECIPES_MISC_YELLOW_DYE_FROM_GOLDEN_DANDELION = Kee[str](
    'recipes/misc/yellow_dye_from_golden_dandelion')
  RECIPES_MISC_YELLOW_DYE_FROM_SUNFLOWER = Kee[str](
    'recipes/misc/yellow_dye_from_sunflower')
  RECIPES_MISC_YELLOW_DYE_FROM_WILDFLOWERS = Kee[str](
    'recipes/misc/yellow_dye_from_wildflowers')
  RECIPES_REDSTONE_ACACIA_BUTTON = Kee[str]('recipes/redstone/acacia_button')
  RECIPES_REDSTONE_ACACIA_DOOR = Kee[str]('recipes/redstone/acacia_door')
  RECIPES_REDSTONE_ACACIA_FENCE_GATE = Kee[str](
    'recipes/redstone/acacia_fence_gate')
  RECIPES_REDSTONE_ACACIA_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/acacia_pressure_plate')
  RECIPES_REDSTONE_ACACIA_TRAPDOOR = Kee[str](
    'recipes/redstone/acacia_trapdoor')
  RECIPES_REDSTONE_BAMBOO_BUTTON = Kee[str]('recipes/redstone/bamboo_button')
  RECIPES_REDSTONE_BAMBOO_DOOR = Kee[str]('recipes/redstone/bamboo_door')
  RECIPES_REDSTONE_BAMBOO_FENCE_GATE = Kee[str](
    'recipes/redstone/bamboo_fence_gate')
  RECIPES_REDSTONE_BAMBOO_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/bamboo_pressure_plate')
  RECIPES_REDSTONE_BAMBOO_TRAPDOOR = Kee[str](
    'recipes/redstone/bamboo_trapdoor')
  RECIPES_REDSTONE_BIRCH_BUTTON = Kee[str]('recipes/redstone/birch_button')
  RECIPES_REDSTONE_BIRCH_DOOR = Kee[str]('recipes/redstone/birch_door')
  RECIPES_REDSTONE_BIRCH_FENCE_GATE = Kee[str](
    'recipes/redstone/birch_fence_gate')
  RECIPES_REDSTONE_BIRCH_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/birch_pressure_plate')
  RECIPES_REDSTONE_BIRCH_TRAPDOOR = Kee[str]('recipes/redstone/birch_trapdoor')
  RECIPES_REDSTONE_CALIBRATED_SCULK_SENSOR = Kee[str](
    'recipes/redstone/calibrated_sculk_sensor')
  RECIPES_REDSTONE_CHERRY_BUTTON = Kee[str]('recipes/redstone/cherry_button')
  RECIPES_REDSTONE_CHERRY_DOOR = Kee[str]('recipes/redstone/cherry_door')
  RECIPES_REDSTONE_CHERRY_FENCE_GATE = Kee[str](
    'recipes/redstone/cherry_fence_gate')
  RECIPES_REDSTONE_CHERRY_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/cherry_pressure_plate')
  RECIPES_REDSTONE_CHERRY_TRAPDOOR = Kee[str](
    'recipes/redstone/cherry_trapdoor')
  RECIPES_REDSTONE_COMPARATOR = Kee[str]('recipes/redstone/comparator')
  RECIPES_REDSTONE_COPPER_BULB = Kee[str]('recipes/redstone/copper_bulb')
  RECIPES_REDSTONE_COPPER_DOOR = Kee[str]('recipes/redstone/copper_door')
  RECIPES_REDSTONE_COPPER_TRAPDOOR = Kee[str](
    'recipes/redstone/copper_trapdoor')
  RECIPES_REDSTONE_CRAFTER = Kee[str]('recipes/redstone/crafter')
  RECIPES_REDSTONE_CRIMSON_BUTTON = Kee[str]('recipes/redstone/crimson_button')
  RECIPES_REDSTONE_CRIMSON_DOOR = Kee[str]('recipes/redstone/crimson_door')
  RECIPES_REDSTONE_CRIMSON_FENCE_GATE = Kee[str](
    'recipes/redstone/crimson_fence_gate')
  RECIPES_REDSTONE_CRIMSON_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/crimson_pressure_plate')
  RECIPES_REDSTONE_CRIMSON_TRAPDOOR = Kee[str](
    'recipes/redstone/crimson_trapdoor')
  RECIPES_REDSTONE_DARK_OAK_BUTTON = Kee[str](
    'recipes/redstone/dark_oak_button')
  RECIPES_REDSTONE_DARK_OAK_DOOR = Kee[str]('recipes/redstone/dark_oak_door')
  RECIPES_REDSTONE_DARK_OAK_FENCE_GATE = Kee[str](
    'recipes/redstone/dark_oak_fence_gate')
  RECIPES_REDSTONE_DARK_OAK_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/dark_oak_pressure_plate')
  RECIPES_REDSTONE_DARK_OAK_TRAPDOOR = Kee[str](
    'recipes/redstone/dark_oak_trapdoor')
  RECIPES_REDSTONE_DAYLIGHT_DETECTOR = Kee[str](
    'recipes/redstone/daylight_detector')
  RECIPES_REDSTONE_DISPENSER = Kee[str]('recipes/redstone/dispenser')
  RECIPES_REDSTONE_DROPPER = Kee[str]('recipes/redstone/dropper')
  RECIPES_REDSTONE_EXPOSED_COPPER_BULB = Kee[str](
    'recipes/redstone/exposed_copper_bulb')
  RECIPES_REDSTONE_HEAVY_WEIGHTED_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/heavy_weighted_pressure_plate')
  RECIPES_REDSTONE_HONEY_BLOCK = Kee[str]('recipes/redstone/honey_block')
  RECIPES_REDSTONE_HOPPER = Kee[str]('recipes/redstone/hopper')
  RECIPES_REDSTONE_IRON_DOOR = Kee[str]('recipes/redstone/iron_door')
  RECIPES_REDSTONE_IRON_TRAPDOOR = Kee[str]('recipes/redstone/iron_trapdoor')
  RECIPES_REDSTONE_JUNGLE_BUTTON = Kee[str]('recipes/redstone/jungle_button')
  RECIPES_REDSTONE_JUNGLE_DOOR = Kee[str]('recipes/redstone/jungle_door')
  RECIPES_REDSTONE_JUNGLE_FENCE_GATE = Kee[str](
    'recipes/redstone/jungle_fence_gate')
  RECIPES_REDSTONE_JUNGLE_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/jungle_pressure_plate')
  RECIPES_REDSTONE_JUNGLE_TRAPDOOR = Kee[str](
    'recipes/redstone/jungle_trapdoor')
  RECIPES_REDSTONE_LECTERN = Kee[str]('recipes/redstone/lectern')
  RECIPES_REDSTONE_LEVER = Kee[str]('recipes/redstone/lever')
  RECIPES_REDSTONE_LIGHT_WEIGHTED_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/light_weighted_pressure_plate')
  RECIPES_REDSTONE_LIGHTNING_ROD = Kee[str]('recipes/redstone/lightning_rod')
  RECIPES_REDSTONE_MANGROVE_BUTTON = Kee[str](
    'recipes/redstone/mangrove_button')
  RECIPES_REDSTONE_MANGROVE_DOOR = Kee[str]('recipes/redstone/mangrove_door')
  RECIPES_REDSTONE_MANGROVE_FENCE_GATE = Kee[str](
    'recipes/redstone/mangrove_fence_gate')
  RECIPES_REDSTONE_MANGROVE_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/mangrove_pressure_plate')
  RECIPES_REDSTONE_MANGROVE_TRAPDOOR = Kee[str](
    'recipes/redstone/mangrove_trapdoor')
  RECIPES_REDSTONE_NOTE_BLOCK = Kee[str]('recipes/redstone/note_block')
  RECIPES_REDSTONE_OAK_BUTTON = Kee[str]('recipes/redstone/oak_button')
  RECIPES_REDSTONE_OAK_DOOR = Kee[str]('recipes/redstone/oak_door')
  RECIPES_REDSTONE_OAK_FENCE_GATE = Kee[str]('recipes/redstone/oak_fence_gate')
  RECIPES_REDSTONE_OAK_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/oak_pressure_plate')
  RECIPES_REDSTONE_OAK_TRAPDOOR = Kee[str]('recipes/redstone/oak_trapdoor')
  RECIPES_REDSTONE_OBSERVER = Kee[str]('recipes/redstone/observer')
  RECIPES_REDSTONE_OXIDIZED_COPPER_BULB = Kee[str](
    'recipes/redstone/oxidized_copper_bulb')
  RECIPES_REDSTONE_PALE_OAK_BUTTON = Kee[str](
    'recipes/redstone/pale_oak_button')
  RECIPES_REDSTONE_PALE_OAK_DOOR = Kee[str]('recipes/redstone/pale_oak_door')
  RECIPES_REDSTONE_PALE_OAK_FENCE_GATE = Kee[str](
    'recipes/redstone/pale_oak_fence_gate')
  RECIPES_REDSTONE_PALE_OAK_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/pale_oak_pressure_plate')
  RECIPES_REDSTONE_PALE_OAK_TRAPDOOR = Kee[str](
    'recipes/redstone/pale_oak_trapdoor')
  RECIPES_REDSTONE_PISTON = Kee[str]('recipes/redstone/piston')
  RECIPES_REDSTONE_POLISHED_BLACKSTONE_BUTTON = Kee[str](
    'recipes/redstone/polished_blackstone_button')
  RECIPES_REDSTONE_POLISHED_BLACKSTONE_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/polished_blackstone_pressure_plate')
  RECIPES_REDSTONE_POPLAR_BUTTON = Kee[str]('recipes/redstone/poplar_button')
  RECIPES_REDSTONE_POPLAR_DOOR = Kee[str]('recipes/redstone/poplar_door')
  RECIPES_REDSTONE_POPLAR_FENCE_GATE = Kee[str](
    'recipes/redstone/poplar_fence_gate')
  RECIPES_REDSTONE_POPLAR_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/poplar_pressure_plate')
  RECIPES_REDSTONE_POPLAR_TRAPDOOR = Kee[str](
    'recipes/redstone/poplar_trapdoor')
  RECIPES_REDSTONE_REDSTONE = Kee[str]('recipes/redstone/redstone')
  RECIPES_REDSTONE_REDSTONE_BLOCK = Kee[str]('recipes/redstone/redstone_block')
  RECIPES_REDSTONE_REDSTONE_FROM_BLASTING = Kee[str](
    'recipes/redstone/redstone_from_blasting')
  RECIPES_REDSTONE_REDSTONE_FROM_BLASTING_DEEPSLATE_REDSTONE_ORE = Kee[str](
    'recipes/redstone/redstone_from_blasting_deepslate_redstone_ore')
  RECIPES_REDSTONE_REDSTONE_FROM_BLASTING_REDSTONE_ORE = Kee[str](
    'recipes/redstone/redstone_from_blasting_redstone_ore')
  RECIPES_REDSTONE_REDSTONE_FROM_SMELTING = Kee[str](
    'recipes/redstone/redstone_from_smelting')
  RECIPES_REDSTONE_REDSTONE_FROM_SMELTING_DEEPSLATE_REDSTONE_ORE = Kee[str](
    'recipes/redstone/redstone_from_smelting_deepslate_redstone_ore')
  RECIPES_REDSTONE_REDSTONE_FROM_SMELTING_REDSTONE_ORE = Kee[str](
    'recipes/redstone/redstone_from_smelting_redstone_ore')
  RECIPES_REDSTONE_REDSTONE_LAMP = Kee[str]('recipes/redstone/redstone_lamp')
  RECIPES_REDSTONE_REDSTONE_TORCH = Kee[str]('recipes/redstone/redstone_torch')
  RECIPES_REDSTONE_REPEATER = Kee[str]('recipes/redstone/repeater')
  RECIPES_REDSTONE_SLIME_BLOCK = Kee[str]('recipes/redstone/slime_block')
  RECIPES_REDSTONE_SPRUCE_BUTTON = Kee[str]('recipes/redstone/spruce_button')
  RECIPES_REDSTONE_SPRUCE_DOOR = Kee[str]('recipes/redstone/spruce_door')
  RECIPES_REDSTONE_SPRUCE_FENCE_GATE = Kee[str](
    'recipes/redstone/spruce_fence_gate')
  RECIPES_REDSTONE_SPRUCE_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/spruce_pressure_plate')
  RECIPES_REDSTONE_SPRUCE_TRAPDOOR = Kee[str](
    'recipes/redstone/spruce_trapdoor')
  RECIPES_REDSTONE_STICKY_PISTON = Kee[str]('recipes/redstone/sticky_piston')
  RECIPES_REDSTONE_STONE_BUTTON = Kee[str]('recipes/redstone/stone_button')
  RECIPES_REDSTONE_STONE_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/stone_pressure_plate')
  RECIPES_REDSTONE_TARGET = Kee[str]('recipes/redstone/target')
  RECIPES_REDSTONE_TNT = Kee[str]('recipes/redstone/tnt')
  RECIPES_REDSTONE_TRAPPED_CHEST = Kee[str]('recipes/redstone/trapped_chest')
  RECIPES_REDSTONE_TRIPWIRE_HOOK = Kee[str]('recipes/redstone/tripwire_hook')
  RECIPES_REDSTONE_WARPED_BUTTON = Kee[str]('recipes/redstone/warped_button')
  RECIPES_REDSTONE_WARPED_DOOR = Kee[str]('recipes/redstone/warped_door')
  RECIPES_REDSTONE_WARPED_FENCE_GATE = Kee[str](
    'recipes/redstone/warped_fence_gate')
  RECIPES_REDSTONE_WARPED_PRESSURE_PLATE = Kee[str](
    'recipes/redstone/warped_pressure_plate')
  RECIPES_REDSTONE_WARPED_TRAPDOOR = Kee[str](
    'recipes/redstone/warped_trapdoor')
  RECIPES_REDSTONE_WAXED_COPPER_BULB = Kee[str](
    'recipes/redstone/waxed_copper_bulb')
  RECIPES_REDSTONE_WAXED_COPPER_BULB_FROM_HONEYCOMB = Kee[str](
    'recipes/redstone/waxed_copper_bulb_from_honeycomb')
  RECIPES_REDSTONE_WAXED_COPPER_DOOR_FROM_HONEYCOMB = Kee[str](
    'recipes/redstone/waxed_copper_door_from_honeycomb')
  RECIPES_REDSTONE_WAXED_COPPER_TRAPDOOR_FROM_HONEYCOMB = Kee[str](
    'recipes/redstone/waxed_copper_trapdoor_from_honeycomb')
  RECIPES_REDSTONE_WAXED_EXPOSED_COPPER_BULB = Kee[str](
    'recipes/redstone/waxed_exposed_copper_bulb')
  RECIPES_REDSTONE_WAXED_EXPOSED_COPPER_BULB_FROM_HONEYCOMB = Kee[str](
    'recipes/redstone/waxed_exposed_copper_bulb_from_honeycomb')
  RECIPES_REDSTONE_WAXED_EXPOSED_COPPER_DOOR_FROM_HONEYCOMB = Kee[str](
    'recipes/redstone/waxed_exposed_copper_door_from_honeycomb')
  RECIPES_REDSTONE_WAXED_EXPOSED_COPPER_TRAPDOOR_FROM_HONEYCOMB = Kee[str](
    'recipes/redstone/waxed_exposed_copper_trapdoor_from_honeycomb')
  RECIPES_REDSTONE_WAXED_OXIDIZED_COPPER_BULB = Kee[str](
    'recipes/redstone/waxed_oxidized_copper_bulb')
  RECIPES_REDSTONE_WAXED_OXIDIZED_COPPER_BULB_FROM_HONEYCOMB = Kee[str](
    'recipes/redstone/waxed_oxidized_copper_bulb_from_honeycomb')
  RECIPES_REDSTONE_WAXED_OXIDIZED_COPPER_DOOR_FROM_HONEYCOMB = Kee[str](
    'recipes/redstone/waxed_oxidized_copper_door_from_honeycomb')
  RECIPES_REDSTONE_WAXED_OXIDIZED_COPPER_TRAPDOOR_FROM_HONEYCOMB = Kee[str](
    'recipes/redstone/waxed_oxidized_copper_trapdoor_from_honeycomb')
  RECIPES_REDSTONE_WAXED_WEATHERED_COPPER_BULB = Kee[str](
    'recipes/redstone/waxed_weathered_copper_bulb')
  RECIPES_REDSTONE_WAXED_WEATHERED_COPPER_BULB_FROM_HONEYCOMB = Kee[str](
    'recipes/redstone/waxed_weathered_copper_bulb_from_honeycomb')
  RECIPES_REDSTONE_WAXED_WEATHERED_COPPER_DOOR_FROM_HONEYCOMB = Kee[str](
    'recipes/redstone/waxed_weathered_copper_door_from_honeycomb')
  RECIPES_REDSTONE_WAXED_WEATHERED_COPPER_TRAPDOOR_FROM_HONEYCOMB = Kee[str](
    'recipes/redstone/waxed_weathered_copper_trapdoor_from_honeycomb')
  RECIPES_REDSTONE_WEATHERED_COPPER_BULB = Kee[str](
    'recipes/redstone/weathered_copper_bulb')
  RECIPES_ROOT = Kee[str]('recipes/root')
  RECIPES_TOOLS_BLACK_BUNDLE = Kee[str]('recipes/tools/black_bundle')
  RECIPES_TOOLS_BLUE_BUNDLE = Kee[str]('recipes/tools/blue_bundle')
  RECIPES_TOOLS_BROWN_BUNDLE = Kee[str]('recipes/tools/brown_bundle')
  RECIPES_TOOLS_BRUSH = Kee[str]('recipes/tools/brush')
  RECIPES_TOOLS_BUNDLE = Kee[str]('recipes/tools/bundle')
  RECIPES_TOOLS_CLOCK = Kee[str]('recipes/tools/clock')
  RECIPES_TOOLS_COMPASS = Kee[str]('recipes/tools/compass')
  RECIPES_TOOLS_COPPER_AXE = Kee[str]('recipes/tools/copper_axe')
  RECIPES_TOOLS_COPPER_HOE = Kee[str]('recipes/tools/copper_hoe')
  RECIPES_TOOLS_COPPER_PICKAXE = Kee[str]('recipes/tools/copper_pickaxe')
  RECIPES_TOOLS_COPPER_SHOVEL = Kee[str]('recipes/tools/copper_shovel')
  RECIPES_TOOLS_CYAN_BUNDLE = Kee[str]('recipes/tools/cyan_bundle')
  RECIPES_TOOLS_DIAMOND_AXE = Kee[str]('recipes/tools/diamond_axe')
  RECIPES_TOOLS_DIAMOND_HOE = Kee[str]('recipes/tools/diamond_hoe')
  RECIPES_TOOLS_DIAMOND_PICKAXE = Kee[str]('recipes/tools/diamond_pickaxe')
  RECIPES_TOOLS_DIAMOND_SHOVEL = Kee[str]('recipes/tools/diamond_shovel')
  RECIPES_TOOLS_FISHING_ROD = Kee[str]('recipes/tools/fishing_rod')
  RECIPES_TOOLS_FLINT_AND_STEEL = Kee[str]('recipes/tools/flint_and_steel')
  RECIPES_TOOLS_GOLDEN_AXE = Kee[str]('recipes/tools/golden_axe')
  RECIPES_TOOLS_GOLDEN_HOE = Kee[str]('recipes/tools/golden_hoe')
  RECIPES_TOOLS_GOLDEN_PICKAXE = Kee[str]('recipes/tools/golden_pickaxe')
  RECIPES_TOOLS_GOLDEN_SHOVEL = Kee[str]('recipes/tools/golden_shovel')
  RECIPES_TOOLS_GRAY_BUNDLE = Kee[str]('recipes/tools/gray_bundle')
  RECIPES_TOOLS_GREEN_BUNDLE = Kee[str]('recipes/tools/green_bundle')
  RECIPES_TOOLS_IRON_AXE = Kee[str]('recipes/tools/iron_axe')
  RECIPES_TOOLS_IRON_HOE = Kee[str]('recipes/tools/iron_hoe')
  RECIPES_TOOLS_IRON_PICKAXE = Kee[str]('recipes/tools/iron_pickaxe')
  RECIPES_TOOLS_IRON_SHOVEL = Kee[str]('recipes/tools/iron_shovel')
  RECIPES_TOOLS_LEAD = Kee[str]('recipes/tools/lead')
  RECIPES_TOOLS_LIGHT_BLUE_BUNDLE = Kee[str]('recipes/tools/light_blue_bundle')
  RECIPES_TOOLS_LIGHT_GRAY_BUNDLE = Kee[str]('recipes/tools/light_gray_bundle')
  RECIPES_TOOLS_LIME_BUNDLE = Kee[str]('recipes/tools/lime_bundle')
  RECIPES_TOOLS_MAGENTA_BUNDLE = Kee[str]('recipes/tools/magenta_bundle')
  RECIPES_TOOLS_NAME_TAG = Kee[str]('recipes/tools/name_tag')
  RECIPES_TOOLS_NETHERITE_AXE_SMITHING = Kee[str](
    'recipes/tools/netherite_axe_smithing')
  RECIPES_TOOLS_NETHERITE_HOE_SMITHING = Kee[str](
    'recipes/tools/netherite_hoe_smithing')
  RECIPES_TOOLS_NETHERITE_PICKAXE_SMITHING = Kee[str](
    'recipes/tools/netherite_pickaxe_smithing')
  RECIPES_TOOLS_NETHERITE_SHOVEL_SMITHING = Kee[str](
    'recipes/tools/netherite_shovel_smithing')
  RECIPES_TOOLS_ORANGE_BUNDLE = Kee[str]('recipes/tools/orange_bundle')
  RECIPES_TOOLS_PINK_BUNDLE = Kee[str]('recipes/tools/pink_bundle')
  RECIPES_TOOLS_PURPLE_BUNDLE = Kee[str]('recipes/tools/purple_bundle')
  RECIPES_TOOLS_RECOVERY_COMPASS = Kee[str]('recipes/tools/recovery_compass')
  RECIPES_TOOLS_RED_BUNDLE = Kee[str]('recipes/tools/red_bundle')
  RECIPES_TOOLS_SHEARS = Kee[str]('recipes/tools/shears')
  RECIPES_TOOLS_SPYGLASS = Kee[str]('recipes/tools/spyglass')
  RECIPES_TOOLS_STONE_AXE = Kee[str]('recipes/tools/stone_axe')
  RECIPES_TOOLS_STONE_HOE = Kee[str]('recipes/tools/stone_hoe')
  RECIPES_TOOLS_STONE_PICKAXE = Kee[str]('recipes/tools/stone_pickaxe')
  RECIPES_TOOLS_STONE_SHOVEL = Kee[str]('recipes/tools/stone_shovel')
  RECIPES_TOOLS_WHITE_BUNDLE = Kee[str]('recipes/tools/white_bundle')
  RECIPES_TOOLS_WOODEN_AXE = Kee[str]('recipes/tools/wooden_axe')
  RECIPES_TOOLS_WOODEN_HOE = Kee[str]('recipes/tools/wooden_hoe')
  RECIPES_TOOLS_WOODEN_PICKAXE = Kee[str]('recipes/tools/wooden_pickaxe')
  RECIPES_TOOLS_WOODEN_SHOVEL = Kee[str]('recipes/tools/wooden_shovel')
  RECIPES_TOOLS_YELLOW_BUNDLE = Kee[str]('recipes/tools/yellow_bundle')
  RECIPES_TRANSPORTATION_ACACIA_BOAT = Kee[str](
    'recipes/transportation/acacia_boat')
  RECIPES_TRANSPORTATION_ACACIA_CHEST_BOAT = Kee[str](
    'recipes/transportation/acacia_chest_boat')
  RECIPES_TRANSPORTATION_ACTIVATOR_RAIL = Kee[str](
    'recipes/transportation/activator_rail')
  RECIPES_TRANSPORTATION_BAMBOO_CHEST_RAFT = Kee[str](
    'recipes/transportation/bamboo_chest_raft')
  RECIPES_TRANSPORTATION_BAMBOO_RAFT = Kee[str](
    'recipes/transportation/bamboo_raft')
  RECIPES_TRANSPORTATION_BIRCH_BOAT = Kee[str](
    'recipes/transportation/birch_boat')
  RECIPES_TRANSPORTATION_BIRCH_CHEST_BOAT = Kee[str](
    'recipes/transportation/birch_chest_boat')
  RECIPES_TRANSPORTATION_CARROT_ON_A_STICK = Kee[str](
    'recipes/transportation/carrot_on_a_stick')
  RECIPES_TRANSPORTATION_CHERRY_BOAT = Kee[str](
    'recipes/transportation/cherry_boat')
  RECIPES_TRANSPORTATION_CHERRY_CHEST_BOAT = Kee[str](
    'recipes/transportation/cherry_chest_boat')
  RECIPES_TRANSPORTATION_CHEST_MINECART = Kee[str](
    'recipes/transportation/chest_minecart')
  RECIPES_TRANSPORTATION_DARK_OAK_BOAT = Kee[str](
    'recipes/transportation/dark_oak_boat')
  RECIPES_TRANSPORTATION_DARK_OAK_CHEST_BOAT = Kee[str](
    'recipes/transportation/dark_oak_chest_boat')
  RECIPES_TRANSPORTATION_DETECTOR_RAIL = Kee[str](
    'recipes/transportation/detector_rail')
  RECIPES_TRANSPORTATION_FURNACE_MINECART = Kee[str](
    'recipes/transportation/furnace_minecart')
  RECIPES_TRANSPORTATION_HOPPER_MINECART = Kee[str](
    'recipes/transportation/hopper_minecart')
  RECIPES_TRANSPORTATION_JUNGLE_BOAT = Kee[str](
    'recipes/transportation/jungle_boat')
  RECIPES_TRANSPORTATION_JUNGLE_CHEST_BOAT = Kee[str](
    'recipes/transportation/jungle_chest_boat')
  RECIPES_TRANSPORTATION_MANGROVE_BOAT = Kee[str](
    'recipes/transportation/mangrove_boat')
  RECIPES_TRANSPORTATION_MANGROVE_CHEST_BOAT = Kee[str](
    'recipes/transportation/mangrove_chest_boat')
  RECIPES_TRANSPORTATION_MINECART = Kee[str]('recipes/transportation/minecart')
  RECIPES_TRANSPORTATION_OAK_BOAT = Kee[str]('recipes/transportation/oak_boat')
  RECIPES_TRANSPORTATION_OAK_CHEST_BOAT = Kee[str](
    'recipes/transportation/oak_chest_boat')
  RECIPES_TRANSPORTATION_PALE_OAK_BOAT = Kee[str](
    'recipes/transportation/pale_oak_boat')
  RECIPES_TRANSPORTATION_PALE_OAK_CHEST_BOAT = Kee[str](
    'recipes/transportation/pale_oak_chest_boat')
  RECIPES_TRANSPORTATION_POPLAR_BOAT = Kee[str](
    'recipes/transportation/poplar_boat')
  RECIPES_TRANSPORTATION_POPLAR_CHEST_BOAT = Kee[str](
    'recipes/transportation/poplar_chest_boat')
  RECIPES_TRANSPORTATION_POWERED_RAIL = Kee[str](
    'recipes/transportation/powered_rail')
  RECIPES_TRANSPORTATION_RAIL = Kee[str]('recipes/transportation/rail')
  RECIPES_TRANSPORTATION_SPRUCE_BOAT = Kee[str](
    'recipes/transportation/spruce_boat')
  RECIPES_TRANSPORTATION_SPRUCE_CHEST_BOAT = Kee[str](
    'recipes/transportation/spruce_chest_boat')
  RECIPES_TRANSPORTATION_TNT_MINECART = Kee[str](
    'recipes/transportation/tnt_minecart')
  RECIPES_TRANSPORTATION_WARPED_FUNGUS_ON_A_STICK = Kee[str](
    'recipes/transportation/warped_fungus_on_a_stick')
  STORY_CURE_ZOMBIE_VILLAGER = Kee[str]('story/cure_zombie_villager')
  STORY_DEFLECT_ARROW = Kee[str]('story/deflect_arrow')
  STORY_ENCHANT_ITEM = Kee[str]('story/enchant_item')
  STORY_ENTER_THE_END = Kee[str]('story/enter_the_end')
  STORY_ENTER_THE_NETHER = Kee[str]('story/enter_the_nether')
  STORY_FOLLOW_ENDER_EYE = Kee[str]('story/follow_ender_eye')
  STORY_FORM_OBSIDIAN = Kee[str]('story/form_obsidian')
  STORY_IRON_TOOLS = Kee[str]('story/iron_tools')
  STORY_LAVA_BUCKET = Kee[str]('story/lava_bucket')
  STORY_MINE_DIAMOND = Kee[str]('story/mine_diamond')
  STORY_MINE_STONE = Kee[str]('story/mine_stone')
  STORY_OBTAIN_ARMOR = Kee[str]('story/obtain_armor')
  STORY_ROOT = Kee[str]('story/root')
  STORY_SHINY_GEAR = Kee[str]('story/shiny_gear')
  STORY_SMELT_IRON = Kee[str]('story/smelt_iron')
  STORY_UPGRADE_TOOLS = Kee[str]('story/upgrade_tools')
