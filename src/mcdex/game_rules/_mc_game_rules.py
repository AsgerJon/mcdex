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


class MCGameRules(MCThing):
  """
  The catalogue of the game's game rules, each a member, found by its name in
  capitals, in any case, or by its unique name:

    keepInventory = MCGameRules.KEEP_INVENTORY
    keepInventory is MCGameRules['keep_inventory']  # True
    keepInventory[Version.V1_12_2]
    # GameRuleId('keep_inventory', 'keepInventory')
    len(MCGameRules)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'game_rules.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'game_rules.json'
  __data_key__ = 'game_rules'
  __id_class__ = GameRuleId
  __kind__ = 'game rule'

  #  Members, one for every name of 'game_rules.json'
  ADVANCE_TIME = Kee[str]('advance_time')
  ADVANCE_WEATHER = Kee[str]('advance_weather')
  ALLOW_ENTERING_NETHER_USING_PORTALS = Kee[str](
    'allow_entering_nether_using_portals')
  ALLOW_FIRE_TICKS_AWAY_FROM_PLAYER = Kee[str](
    'allow_fire_ticks_away_from_player')
  BLOCK_DROPS = Kee[str]('block_drops')
  BLOCK_EXPLOSION_DROP_DECAY = Kee[str]('block_explosion_drop_decay')
  COMMAND_BLOCK_OUTPUT = Kee[str]('command_block_output')
  COMMAND_BLOCKS_WORK = Kee[str]('command_blocks_work')
  DROWNING_DAMAGE = Kee[str]('drowning_damage')
  ELYTRA_MOVEMENT_CHECK = Kee[str]('elytra_movement_check')
  ENDER_PEARLS_VANISH_ON_DEATH = Kee[str]('ender_pearls_vanish_on_death')
  ENTITY_DROPS = Kee[str]('entity_drops')
  FALL_DAMAGE = Kee[str]('fall_damage')
  FIRE_DAMAGE = Kee[str]('fire_damage')
  FIRE_SPREAD_RADIUS_AROUND_PLAYER = Kee[str](
    'fire_spread_radius_around_player')
  FORGIVE_DEAD_PLAYERS = Kee[str]('forgive_dead_players')
  FREEZE_DAMAGE = Kee[str]('freeze_damage')
  GAME_LOOP_FUNCTION = Kee[str]('game_loop_function')
  GLOBAL_SOUND_EVENTS = Kee[str]('global_sound_events')
  IMMEDIATE_RESPAWN = Kee[str]('immediate_respawn')
  KEEP_INVENTORY = Kee[str]('keep_inventory')
  LAVA_SOURCE_CONVERSION = Kee[str]('lava_source_conversion')
  LIMITED_CRAFTING = Kee[str]('limited_crafting')
  LOCATOR_BAR = Kee[str]('locator_bar')
  LOG_ADMIN_COMMANDS = Kee[str]('log_admin_commands')
  MAX_BLOCK_MODIFICATIONS = Kee[str]('max_block_modifications')
  MAX_COMMAND_FORKS = Kee[str]('max_command_forks')
  MAX_COMMAND_SEQUENCE_LENGTH = Kee[str]('max_command_sequence_length')
  MAX_ENTITY_CRAMMING = Kee[str]('max_entity_cramming')
  MAX_MINECART_SPEED = Kee[str]('max_minecart_speed')
  MAX_SNOW_ACCUMULATION_HEIGHT = Kee[str]('max_snow_accumulation_height')
  MOB_DROPS = Kee[str]('mob_drops')
  MOB_EXPLOSION_DROP_DECAY = Kee[str]('mob_explosion_drop_decay')
  MOB_GRIEFING = Kee[str]('mob_griefing')
  NATURAL_HEALTH_REGENERATION = Kee[str]('natural_health_regeneration')
  PLAYER_MOVEMENT_CHECK = Kee[str]('player_movement_check')
  PLAYERS_NETHER_PORTAL_CREATIVE_DELAY = Kee[str](
    'players_nether_portal_creative_delay')
  PLAYERS_NETHER_PORTAL_DEFAULT_DELAY = Kee[str](
    'players_nether_portal_default_delay')
  PLAYERS_SLEEPING_PERCENTAGE = Kee[str]('players_sleeping_percentage')
  PROJECTILES_CAN_BREAK_BLOCKS = Kee[str]('projectiles_can_break_blocks')
  PVP = Kee[str]('pvp')
  RAIDS = Kee[str]('raids')
  RANDOM_TICK_SPEED = Kee[str]('random_tick_speed')
  REDUCED_DEBUG_INFO = Kee[str]('reduced_debug_info')
  RESPAWN_RADIUS = Kee[str]('respawn_radius')
  SEND_COMMAND_FEEDBACK = Kee[str]('send_command_feedback')
  SHOW_ADVANCEMENT_MESSAGES = Kee[str]('show_advancement_messages')
  SHOW_DEATH_MESSAGES = Kee[str]('show_death_messages')
  SPAWN_CHUNK_RADIUS = Kee[str]('spawn_chunk_radius')
  SPAWN_MOBS = Kee[str]('spawn_mobs')
  SPAWN_MONSTERS = Kee[str]('spawn_monsters')
  SPAWN_PATROLS = Kee[str]('spawn_patrols')
  SPAWN_PHANTOMS = Kee[str]('spawn_phantoms')
  SPAWN_WANDERING_TRADERS = Kee[str]('spawn_wandering_traders')
  SPAWN_WARDENS = Kee[str]('spawn_wardens')
  SPAWNER_BLOCKS_WORK = Kee[str]('spawner_blocks_work')
  SPECTATORS_GENERATE_CHUNKS = Kee[str]('spectators_generate_chunks')
  SPREAD_VINES = Kee[str]('spread_vines')
  TNT_EXPLODES = Kee[str]('tnt_explodes')
  TNT_EXPLOSION_DROP_DECAY = Kee[str]('tnt_explosion_drop_decay')
  UNIVERSAL_ANGER = Kee[str]('universal_anger')
  WATER_SOURCE_CONVERSION = Kee[str]('water_source_conversion')
