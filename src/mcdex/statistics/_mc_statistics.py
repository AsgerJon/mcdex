"""
MCStatistics is the catalogue of the game's statistics: an enumeration with one
member for every statistic of the data file that ships with mcdex, each the
same statistic in every version, with the id each version knows it by:
the name the game keeps the count under, which /scoreboard objectives count.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import MCThing, StatisticId


class MCStatistics(MCThing):
  """
  The catalogue of the game's statistics, each a member, found by its name in
  capitals, in any case, or by its unique name:

    jump = MCStatistics.JUMP
    jump is MCStatistics['jump']  # True
    jump[Version.V1_12_2]  # StatisticId('jump', 'stat.jump')
    len(MCStatistics)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'statistics.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'statistics.json'
  __data_key__ = 'statistics'
  __id_class__ = StatisticId
  __kind__ = 'statistic'

  #  Members, one for every name of 'statistics.json'
  ANIMALS_BRED = Kee[str]('animals_bred')
  ARMOR_PIECES_CLEANED = Kee[str]('armor_pieces_cleaned')
  AVIATE_ONE_CM = Kee[str]('aviate_one_cm')
  BANNERS_CLEANED = Kee[str]('banners_cleaned')
  BARRELS_OPENED = Kee[str]('barrels_opened')
  BELL_RING = Kee[str]('bell_ring')
  BELLS_RUNG = Kee[str]('bells_rung')
  BOAT_ONE_CM = Kee[str]('boat_one_cm')
  CAKE_SLICES_EATEN = Kee[str]('cake_slices_eaten')
  CAULDRONS_FILLED = Kee[str]('cauldrons_filled')
  CHESTS_OPENED = Kee[str]('chests_opened')
  CLEAN_ARMOR = Kee[str]('clean_armor')
  CLEAN_BANNER = Kee[str]('clean_banner')
  CLEAN_SHULKER_BOX = Kee[str]('clean_shulker_box')
  CLIMB_ONE_CM = Kee[str]('climb_one_cm')
  CROUCH_ONE_CM = Kee[str]('crouch_one_cm')
  DAMAGE_ABSORBED = Kee[str]('damage_absorbed')
  DAMAGE_BLOCKED_BY_SHIELD = Kee[str]('damage_blocked_by_shield')
  DAMAGE_DEALT = Kee[str]('damage_dealt')
  DAMAGE_DEALT_ABSORBED = Kee[str]('damage_dealt_absorbed')
  DAMAGE_DEALT_RESISTED = Kee[str]('damage_dealt_resisted')
  DAMAGE_RESISTED = Kee[str]('damage_resisted')
  DAMAGE_TAKEN = Kee[str]('damage_taken')
  DEATHS = Kee[str]('deaths')
  DISPENSERS_SEARCHED = Kee[str]('dispensers_searched')
  DISTANCE_BY_BOAT = Kee[str]('distance_by_boat')
  DISTANCE_BY_ELYTRA = Kee[str]('distance_by_elytra')
  DISTANCE_BY_HAPPY_GHAST = Kee[str]('distance_by_happy_ghast')
  DISTANCE_BY_HORSE = Kee[str]('distance_by_horse')
  DISTANCE_BY_MINECART = Kee[str]('distance_by_minecart')
  DISTANCE_BY_NAUTILUS = Kee[str]('distance_by_nautilus')
  DISTANCE_BY_PIG = Kee[str]('distance_by_pig')
  DISTANCE_BY_STRIDER = Kee[str]('distance_by_strider')
  DISTANCE_CLIMBED = Kee[str]('distance_climbed')
  DISTANCE_CROUCHED = Kee[str]('distance_crouched')
  DISTANCE_FALLEN = Kee[str]('distance_fallen')
  DISTANCE_FLOWN = Kee[str]('distance_flown')
  DISTANCE_SPRINTED = Kee[str]('distance_sprinted')
  DISTANCE_SWUM = Kee[str]('distance_swum')
  DISTANCE_WALKED = Kee[str]('distance_walked')
  DISTANCE_WALKED_ON_WATER = Kee[str]('distance_walked_on_water')
  DISTANCE_WALKED_UNDER_WATER = Kee[str]('distance_walked_under_water')
  DROP = Kee[str]('drop')
  DROPPERS_SEARCHED = Kee[str]('droppers_searched')
  EAT_CAKE_SLICE = Kee[str]('eat_cake_slice')
  ENCHANT_ITEM = Kee[str]('enchant_item')
  ENDER_CHESTS_OPENED = Kee[str]('ender_chests_opened')
  FALL_ONE_CM = Kee[str]('fall_one_cm')
  FILL_CAULDRON = Kee[str]('fill_cauldron')
  FISH_CAUGHT = Kee[str]('fish_caught')
  FLY_ONE_CM = Kee[str]('fly_one_cm')
  GAMES_QUIT = Kee[str]('games_quit')
  HAPPY_GHAST_ONE_CM = Kee[str]('happy_ghast_one_cm')
  HOPPERS_SEARCHED = Kee[str]('hoppers_searched')
  HORSE_ONE_CM = Kee[str]('horse_one_cm')
  INSPECT_DISPENSER = Kee[str]('inspect_dispenser')
  INSPECT_DROPPER = Kee[str]('inspect_dropper')
  INSPECT_HOPPER = Kee[str]('inspect_hopper')
  INTERACT_WITH_ANVIL = Kee[str]('interact_with_anvil')
  INTERACT_WITH_BEACON = Kee[str]('interact_with_beacon')
  INTERACT_WITH_BLAST_FURNACE = Kee[str]('interact_with_blast_furnace')
  INTERACT_WITH_BREWINGSTAND = Kee[str]('interact_with_brewingstand')
  INTERACT_WITH_CAMPFIRE = Kee[str]('interact_with_campfire')
  INTERACT_WITH_CARTOGRAPHY_TABLE = Kee[str]('interact_with_cartography_table')
  INTERACT_WITH_CRAFTING_TABLE = Kee[str]('interact_with_crafting_table')
  INTERACT_WITH_FURNACE = Kee[str]('interact_with_furnace')
  INTERACT_WITH_GRINDSTONE = Kee[str]('interact_with_grindstone')
  INTERACT_WITH_LECTERN = Kee[str]('interact_with_lectern')
  INTERACT_WITH_LOOM = Kee[str]('interact_with_loom')
  INTERACT_WITH_SMITHING_TABLE = Kee[str]('interact_with_smithing_table')
  INTERACT_WITH_SMOKER = Kee[str]('interact_with_smoker')
  INTERACT_WITH_STONECUTTER = Kee[str]('interact_with_stonecutter')
  INTERACTIONS_WITH_ANVIL = Kee[str]('interactions_with_anvil')
  INTERACTIONS_WITH_BEACON = Kee[str]('interactions_with_beacon')
  INTERACTIONS_WITH_BLAST_FURNACE = Kee[str]('interactions_with_blast_furnace')
  INTERACTIONS_WITH_BREWING_STAND = Kee[str]('interactions_with_brewing_stand')
  INTERACTIONS_WITH_CAMPFIRE = Kee[str]('interactions_with_campfire')
  INTERACTIONS_WITH_CARTOGRAPHY_TABLE = Kee[str](
    'interactions_with_cartography_table')
  INTERACTIONS_WITH_CRAFTING_TABLE = Kee[str](
    'interactions_with_crafting_table')
  INTERACTIONS_WITH_FURNACE = Kee[str]('interactions_with_furnace')
  INTERACTIONS_WITH_GRINDSTONE = Kee[str]('interactions_with_grindstone')
  INTERACTIONS_WITH_LECTERN = Kee[str]('interactions_with_lectern')
  INTERACTIONS_WITH_LOOM = Kee[str]('interactions_with_loom')
  INTERACTIONS_WITH_SMITHING_TABLE = Kee[str](
    'interactions_with_smithing_table')
  INTERACTIONS_WITH_SMOKER = Kee[str]('interactions_with_smoker')
  INTERACTIONS_WITH_STONECUTTER = Kee[str]('interactions_with_stonecutter')
  ITEMS_DROPPED = Kee[str]('items_dropped')
  ITEMS_ENCHANTED = Kee[str]('items_enchanted')
  JUMP = Kee[str]('jump')
  JUMPS = Kee[str]('jumps')
  JUNK_FISHED = Kee[str]('junk_fished')
  LEAVE_GAME = Kee[str]('leave_game')
  MINECART_ONE_CM = Kee[str]('minecart_one_cm')
  MOB_KILLS = Kee[str]('mob_kills')
  MUSIC_DISCS_PLAYED = Kee[str]('music_discs_played')
  NAUTILUS_ONE_CM = Kee[str]('nautilus_one_cm')
  NOTE_BLOCKS_PLAYED = Kee[str]('note_blocks_played')
  NOTE_BLOCKS_TUNED = Kee[str]('note_blocks_tuned')
  NUMBER_OF_DEATHS = Kee[str]('number_of_deaths')
  OPEN_BARREL = Kee[str]('open_barrel')
  OPEN_CHEST = Kee[str]('open_chest')
  OPEN_ENDERCHEST = Kee[str]('open_enderchest')
  OPEN_SHULKER_BOX = Kee[str]('open_shulker_box')
  PIG_ONE_CM = Kee[str]('pig_one_cm')
  PLANTS_POTTED = Kee[str]('plants_potted')
  PLAY_NOTEBLOCK = Kee[str]('play_noteblock')
  PLAY_RECORD = Kee[str]('play_record')
  PLAY_TIME = Kee[str]('play_time')
  PLAYER_KILLS = Kee[str]('player_kills')
  POT_FLOWER = Kee[str]('pot_flower')
  RAID_TRIGGER = Kee[str]('raid_trigger')
  RAID_WIN = Kee[str]('raid_win')
  RAIDS_TRIGGERED = Kee[str]('raids_triggered')
  RAIDS_WON = Kee[str]('raids_won')
  SHULKER_BOXES_CLEANED = Kee[str]('shulker_boxes_cleaned')
  SHULKER_BOXES_OPENED = Kee[str]('shulker_boxes_opened')
  SLEEP_IN_BED = Kee[str]('sleep_in_bed')
  SLEEP_IN_STRAW_BED = Kee[str]('sleep_in_straw_bed')
  SNEAK_TIME = Kee[str]('sneak_time')
  SPRINT_ONE_CM = Kee[str]('sprint_one_cm')
  STRIDER_ONE_CM = Kee[str]('strider_one_cm')
  SWIM_ONE_CM = Kee[str]('swim_one_cm')
  TALKED_TO_VILLAGER = Kee[str]('talked_to_villager')
  TALKED_TO_VILLAGERS = Kee[str]('talked_to_villagers')
  TARGET_HIT = Kee[str]('target_hit')
  TARGETS_HIT = Kee[str]('targets_hit')
  TIME_PLAYED = Kee[str]('time_played')
  TIME_SINCE_DEATH = Kee[str]('time_since_death')
  TIME_SINCE_LAST_DEATH = Kee[str]('time_since_last_death')
  TIME_SINCE_LAST_REST = Kee[str]('time_since_last_rest')
  TIME_SINCE_REST = Kee[str]('time_since_rest')
  TIME_WITH_WORLD_OPEN = Kee[str]('time_with_world_open')
  TIMES_SLEPT_IN_A_BED = Kee[str]('times_slept_in_a_bed')
  TIMES_SLEPT_IN_A_STRAW_BED = Kee[str]('times_slept_in_a_straw_bed')
  TOTAL_WORLD_TIME = Kee[str]('total_world_time')
  TRADED_WITH_VILLAGER = Kee[str]('traded_with_villager')
  TRADED_WITH_VILLAGERS = Kee[str]('traded_with_villagers')
  TRAPPED_CHESTS_TRIGGERED = Kee[str]('trapped_chests_triggered')
  TREASURE_FISHED = Kee[str]('treasure_fished')
  TRIGGER_TRAPPED_CHEST = Kee[str]('trigger_trapped_chest')
  TUNE_NOTEBLOCK = Kee[str]('tune_noteblock')
  USE_CAULDRON = Kee[str]('use_cauldron')
  WALK_ON_WATER_ONE_CM = Kee[str]('walk_on_water_one_cm')
  WALK_ONE_CM = Kee[str]('walk_one_cm')
  WALK_UNDER_WATER_ONE_CM = Kee[str]('walk_under_water_one_cm')
  WATER_TAKEN_FROM_CAULDRON = Kee[str]('water_taken_from_cauldron')
