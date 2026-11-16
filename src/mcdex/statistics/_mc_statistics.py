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


class MCStatistics(MCThing, strictCase=False):
  """
  The catalogue of the game's statistics, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    jump = MCStatistics.Jump
    jump is MCStatistics['jump']  # True
    jump[Version.V1_12_2]  # StatisticId('jump', 'stat.jump')
    len(MCStatistics)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'statistics.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'statistics.json'
  __data_key__ = 'statistics'
  __id_class__ = StatisticId
  __kind__ = 'statistic'

  #  Members, one for every thing of 'statistics.json'
  AnimalsBred = Kee[str]('animals_bred')
  ArmorPiecesCleaned = Kee[str]('armor_pieces_cleaned')
  AviateOneCm = Kee[str]('aviate_one_cm')
  BannersCleaned = Kee[str]('banners_cleaned')
  BarrelsOpened = Kee[str]('barrels_opened')
  BellRing = Kee[str]('bell_ring')
  BellsRung = Kee[str]('bells_rung')
  BoatOneCm = Kee[str]('boat_one_cm')
  CakeSlicesEaten = Kee[str]('cake_slices_eaten')
  CauldronsFilled = Kee[str]('cauldrons_filled')
  ChestsOpened = Kee[str]('chests_opened')
  CleanArmor = Kee[str]('clean_armor')
  CleanBanner = Kee[str]('clean_banner')
  CleanShulkerBox = Kee[str]('clean_shulker_box')
  ClimbOneCm = Kee[str]('climb_one_cm')
  CrouchOneCm = Kee[str]('crouch_one_cm')
  DamageAbsorbed = Kee[str]('damage_absorbed')
  DamageBlockedByShield = Kee[str]('damage_blocked_by_shield')
  DamageDealt = Kee[str]('damage_dealt')
  DamageDealtAbsorbed = Kee[str]('damage_dealt_absorbed')
  DamageDealtResisted = Kee[str]('damage_dealt_resisted')
  DamageResisted = Kee[str]('damage_resisted')
  DamageTaken = Kee[str]('damage_taken')
  Deaths = Kee[str]('deaths')
  DispensersSearched = Kee[str]('dispensers_searched')
  DistanceByBoat = Kee[str]('distance_by_boat')
  DistanceByElytra = Kee[str]('distance_by_elytra')
  DistanceByHappyGhast = Kee[str]('distance_by_happy_ghast')
  DistanceByHorse = Kee[str]('distance_by_horse')
  DistanceByMinecart = Kee[str]('distance_by_minecart')
  DistanceByNautilus = Kee[str]('distance_by_nautilus')
  DistanceByPig = Kee[str]('distance_by_pig')
  DistanceByStrider = Kee[str]('distance_by_strider')
  DistanceClimbed = Kee[str]('distance_climbed')
  DistanceCrouched = Kee[str]('distance_crouched')
  DistanceFallen = Kee[str]('distance_fallen')
  DistanceFlown = Kee[str]('distance_flown')
  DistanceSprinted = Kee[str]('distance_sprinted')
  DistanceSwum = Kee[str]('distance_swum')
  DistanceWalked = Kee[str]('distance_walked')
  DistanceWalkedOnWater = Kee[str]('distance_walked_on_water')
  DistanceWalkedUnderWater = Kee[str]('distance_walked_under_water')
  Drop = Kee[str]('drop')
  DroppersSearched = Kee[str]('droppers_searched')
  EatCakeSlice = Kee[str]('eat_cake_slice')
  EnchantItem = Kee[str]('enchant_item')
  EnderChestsOpened = Kee[str]('ender_chests_opened')
  FallOneCm = Kee[str]('fall_one_cm')
  FillCauldron = Kee[str]('fill_cauldron')
  FishCaught = Kee[str]('fish_caught')
  FlyOneCm = Kee[str]('fly_one_cm')
  GamesQuit = Kee[str]('games_quit')
  HappyGhastOneCm = Kee[str]('happy_ghast_one_cm')
  HoppersSearched = Kee[str]('hoppers_searched')
  HorseOneCm = Kee[str]('horse_one_cm')
  InspectDispenser = Kee[str]('inspect_dispenser')
  InspectDropper = Kee[str]('inspect_dropper')
  InspectHopper = Kee[str]('inspect_hopper')
  InteractWithAnvil = Kee[str]('interact_with_anvil')
  InteractWithBeacon = Kee[str]('interact_with_beacon')
  InteractWithBlastFurnace = Kee[str]('interact_with_blast_furnace')
  InteractWithBrewingstand = Kee[str]('interact_with_brewingstand')
  InteractWithCampfire = Kee[str]('interact_with_campfire')
  InteractWithCartographyTable = Kee[str]('interact_with_cartography_table')
  InteractWithCraftingTable = Kee[str]('interact_with_crafting_table')
  InteractWithFurnace = Kee[str]('interact_with_furnace')
  InteractWithGrindstone = Kee[str]('interact_with_grindstone')
  InteractWithLectern = Kee[str]('interact_with_lectern')
  InteractWithLoom = Kee[str]('interact_with_loom')
  InteractWithSmithingTable = Kee[str]('interact_with_smithing_table')
  InteractWithSmoker = Kee[str]('interact_with_smoker')
  InteractWithStonecutter = Kee[str]('interact_with_stonecutter')
  InteractionsWithAnvil = Kee[str]('interactions_with_anvil')
  InteractionsWithBeacon = Kee[str]('interactions_with_beacon')
  InteractionsWithBlastFurnace = Kee[str]('interactions_with_blast_furnace')
  InteractionsWithBrewingStand = Kee[str]('interactions_with_brewing_stand')
  InteractionsWithCampfire = Kee[str]('interactions_with_campfire')
  InteractionsWithCartographyTable = Kee[str](
    'interactions_with_cartography_table')
  InteractionsWithCraftingTable = Kee[str]('interactions_with_crafting_table')
  InteractionsWithFurnace = Kee[str]('interactions_with_furnace')
  InteractionsWithGrindstone = Kee[str]('interactions_with_grindstone')
  InteractionsWithLectern = Kee[str]('interactions_with_lectern')
  InteractionsWithLoom = Kee[str]('interactions_with_loom')
  InteractionsWithSmithingTable = Kee[str]('interactions_with_smithing_table')
  InteractionsWithSmoker = Kee[str]('interactions_with_smoker')
  InteractionsWithStonecutter = Kee[str]('interactions_with_stonecutter')
  ItemsDropped = Kee[str]('items_dropped')
  ItemsEnchanted = Kee[str]('items_enchanted')
  Jump = Kee[str]('jump')
  Jumps = Kee[str]('jumps')
  JunkFished = Kee[str]('junk_fished')
  LeaveGame = Kee[str]('leave_game')
  MinecartOneCm = Kee[str]('minecart_one_cm')
  MobKills = Kee[str]('mob_kills')
  MusicDiscsPlayed = Kee[str]('music_discs_played')
  NautilusOneCm = Kee[str]('nautilus_one_cm')
  NoteBlocksPlayed = Kee[str]('note_blocks_played')
  NoteBlocksTuned = Kee[str]('note_blocks_tuned')
  NumberOfDeaths = Kee[str]('number_of_deaths')
  OpenBarrel = Kee[str]('open_barrel')
  OpenChest = Kee[str]('open_chest')
  OpenEnderchest = Kee[str]('open_enderchest')
  OpenShulkerBox = Kee[str]('open_shulker_box')
  PigOneCm = Kee[str]('pig_one_cm')
  PlantsPotted = Kee[str]('plants_potted')
  PlayNoteblock = Kee[str]('play_noteblock')
  PlayRecord = Kee[str]('play_record')
  PlayTime = Kee[str]('play_time')
  PlayerKills = Kee[str]('player_kills')
  PotFlower = Kee[str]('pot_flower')
  RaidTrigger = Kee[str]('raid_trigger')
  RaidWin = Kee[str]('raid_win')
  RaidsTriggered = Kee[str]('raids_triggered')
  RaidsWon = Kee[str]('raids_won')
  ShulkerBoxesCleaned = Kee[str]('shulker_boxes_cleaned')
  ShulkerBoxesOpened = Kee[str]('shulker_boxes_opened')
  SleepInBed = Kee[str]('sleep_in_bed')
  SleepInStrawBed = Kee[str]('sleep_in_straw_bed')
  SneakTime = Kee[str]('sneak_time')
  SprintOneCm = Kee[str]('sprint_one_cm')
  StriderOneCm = Kee[str]('strider_one_cm')
  SwimOneCm = Kee[str]('swim_one_cm')
  TalkedToVillager = Kee[str]('talked_to_villager')
  TalkedToVillagers = Kee[str]('talked_to_villagers')
  TargetHit = Kee[str]('target_hit')
  TargetsHit = Kee[str]('targets_hit')
  TimePlayed = Kee[str]('time_played')
  TimeSinceDeath = Kee[str]('time_since_death')
  TimeSinceLastDeath = Kee[str]('time_since_last_death')
  TimeSinceLastRest = Kee[str]('time_since_last_rest')
  TimeSinceRest = Kee[str]('time_since_rest')
  TimeWithWorldOpen = Kee[str]('time_with_world_open')
  TimesSleptInABed = Kee[str]('times_slept_in_a_bed')
  TimesSleptInAStrawBed = Kee[str]('times_slept_in_a_straw_bed')
  TotalWorldTime = Kee[str]('total_world_time')
  TradedWithVillager = Kee[str]('traded_with_villager')
  TradedWithVillagers = Kee[str]('traded_with_villagers')
  TrappedChestsTriggered = Kee[str]('trapped_chests_triggered')
  TreasureFished = Kee[str]('treasure_fished')
  TriggerTrappedChest = Kee[str]('trigger_trapped_chest')
  TuneNoteblock = Kee[str]('tune_noteblock')
  UseCauldron = Kee[str]('use_cauldron')
  WalkOnWaterOneCm = Kee[str]('walk_on_water_one_cm')
  WalkOneCm = Kee[str]('walk_one_cm')
  WalkUnderWaterOneCm = Kee[str]('walk_under_water_one_cm')
  WaterTakenFromCauldron = Kee[str]('water_taken_from_cauldron')
