"""
MCGameRules is the catalogue of the game's game rules: an enumeration with one
member for every game rule of the data file that ships with mcdex, each the
same game rule in every version, with the id each version knows it by:
what /gamerule takes.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import GameRuleId, MCThing


class MCGameRules(MCThing, strictCase=False):
  """
  The catalogue of the game's game rules, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    keepInventory = MCGameRules.KeepInventory
    keepInventory is MCGameRules['keep_inventory']  # True
    keepInventory[Version.V1_12_2]
    # GameRuleId('keep_inventory', 'keepInventory')
    len(MCGameRules)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'game_rules.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'game_rules.json'
  __data_key__ = 'game_rules'
  __id_class__ = GameRuleId
  __kind__ = 'game rule'

  #  Members, one for every thing of 'game_rules.json'
  AdvanceTime = Kee[str]('advance_time')
  AdvanceWeather = Kee[str]('advance_weather')
  AllowEnteringNetherUsingPortals = Kee[str](
    'allow_entering_nether_using_portals')
  AllowFireTicksAwayFromPlayer = Kee[str]('allow_fire_ticks_away_from_player')
  BlockDrops = Kee[str]('block_drops')
  BlockExplosionDropDecay = Kee[str]('block_explosion_drop_decay')
  CommandBlockOutput = Kee[str]('command_block_output')
  CommandBlocksWork = Kee[str]('command_blocks_work')
  DrowningDamage = Kee[str]('drowning_damage')
  ElytraMovementCheck = Kee[str]('elytra_movement_check')
  EnderPearlsVanishOnDeath = Kee[str]('ender_pearls_vanish_on_death')
  EntityDrops = Kee[str]('entity_drops')
  FallDamage = Kee[str]('fall_damage')
  FireDamage = Kee[str]('fire_damage')
  FireSpreadRadiusAroundPlayer = Kee[str]('fire_spread_radius_around_player')
  ForgiveDeadPlayers = Kee[str]('forgive_dead_players')
  FreezeDamage = Kee[str]('freeze_damage')
  GameLoopFunction = Kee[str]('game_loop_function')
  GlobalSoundEvents = Kee[str]('global_sound_events')
  ImmediateRespawn = Kee[str]('immediate_respawn')
  KeepInventory = Kee[str]('keep_inventory')
  LavaSourceConversion = Kee[str]('lava_source_conversion')
  LimitedCrafting = Kee[str]('limited_crafting')
  LocatorBar = Kee[str]('locator_bar')
  LogAdminCommands = Kee[str]('log_admin_commands')
  MaxBlockModifications = Kee[str]('max_block_modifications')
  MaxCommandForks = Kee[str]('max_command_forks')
  MaxCommandSequenceLength = Kee[str]('max_command_sequence_length')
  MaxEntityCramming = Kee[str]('max_entity_cramming')
  MaxMinecartSpeed = Kee[str]('max_minecart_speed')
  MaxSnowAccumulationHeight = Kee[str]('max_snow_accumulation_height')
  MobDrops = Kee[str]('mob_drops')
  MobExplosionDropDecay = Kee[str]('mob_explosion_drop_decay')
  MobGriefing = Kee[str]('mob_griefing')
  NaturalHealthRegeneration = Kee[str]('natural_health_regeneration')
  PlayerMovementCheck = Kee[str]('player_movement_check')
  PlayersNetherPortalCreativeDelay = Kee[str](
    'players_nether_portal_creative_delay')
  PlayersNetherPortalDefaultDelay = Kee[str](
    'players_nether_portal_default_delay')
  PlayersSleepingPercentage = Kee[str]('players_sleeping_percentage')
  ProjectilesCanBreakBlocks = Kee[str]('projectiles_can_break_blocks')
  Pvp = Kee[str]('pvp')
  Raids = Kee[str]('raids')
  RandomTickSpeed = Kee[str]('random_tick_speed')
  ReducedDebugInfo = Kee[str]('reduced_debug_info')
  RespawnRadius = Kee[str]('respawn_radius')
  SendCommandFeedback = Kee[str]('send_command_feedback')
  ShowAdvancementMessages = Kee[str]('show_advancement_messages')
  ShowDeathMessages = Kee[str]('show_death_messages')
  SpawnChunkRadius = Kee[str]('spawn_chunk_radius')
  SpawnMobs = Kee[str]('spawn_mobs')
  SpawnMonsters = Kee[str]('spawn_monsters')
  SpawnPatrols = Kee[str]('spawn_patrols')
  SpawnPhantoms = Kee[str]('spawn_phantoms')
  SpawnWanderingTraders = Kee[str]('spawn_wandering_traders')
  SpawnWardens = Kee[str]('spawn_wardens')
  SpawnerBlocksWork = Kee[str]('spawner_blocks_work')
  SpectatorsGenerateChunks = Kee[str]('spectators_generate_chunks')
  SpreadVines = Kee[str]('spread_vines')
  TntExplodes = Kee[str]('tnt_explodes')
  TntExplosionDropDecay = Kee[str]('tnt_explosion_drop_decay')
  UniversalAnger = Kee[str]('universal_anger')
  WaterSourceConversion = Kee[str]('water_source_conversion')
