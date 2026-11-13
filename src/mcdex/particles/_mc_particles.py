"""
MCParticles is the catalogue of the game's particles: an enumeration with one
member for every particle of the data file that ships with mcdex, each the
same particle in every version, with the id each version knows it by:
what /particle takes.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import MCThing, ParticleId


class MCParticles(MCThing):
  """
  The catalogue of the game's particles, each a member, found by its name in
  capitals, in any case, or by its unique name:

    poof = MCParticles.POOF
    poof is MCParticles['poof']  # True
    poof[Version.V1_12_2]  # ParticleId('poof', 'explode')
    len(MCParticles)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'particles.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'particles.json'
  __data_key__ = 'particles'
  __id_class__ = ParticleId
  __kind__ = 'particle'

  #  Members, one for every name of 'particles.json'
  AMBIENT_ENTITY_EFFECT = Kee[str]('ambient_entity_effect')
  ANGRY_VILLAGER = Kee[str]('angry_villager')
  ASH = Kee[str]('ash')
  BARRIER = Kee[str]('barrier')
  BLOCK = Kee[str]('block')
  BLOCK_CRUMBLE = Kee[str]('block_crumble')
  BLOCK_DUST = Kee[str]('block_dust')
  BLOCK_MARKER = Kee[str]('block_marker')
  BUBBLE = Kee[str]('bubble')
  BUBBLE_COLUMN_UP = Kee[str]('bubble_column_up')
  BUBBLE_POP = Kee[str]('bubble_pop')
  CAMPFIRE_COSY_SMOKE = Kee[str]('campfire_cosy_smoke')
  CAMPFIRE_SIGNAL_SMOKE = Kee[str]('campfire_signal_smoke')
  CHERRY_LEAVES = Kee[str]('cherry_leaves')
  CLOUD = Kee[str]('cloud')
  COMPOSTER = Kee[str]('composter')
  COPPER_FIRE_FLAME = Kee[str]('copper_fire_flame')
  CRIMSON_SPORE = Kee[str]('crimson_spore')
  CRIT = Kee[str]('crit')
  CURRENT_DOWN = Kee[str]('current_down')
  DAMAGE_INDICATOR = Kee[str]('damage_indicator')
  DOLPHIN = Kee[str]('dolphin')
  DRAGON_BREATH = Kee[str]('dragon_breath')
  DRIPPING_CHERRY_LEAVES = Kee[str]('dripping_cherry_leaves')
  DRIPPING_DRIPSTONE_LAVA = Kee[str]('dripping_dripstone_lava')
  DRIPPING_DRIPSTONE_WATER = Kee[str]('dripping_dripstone_water')
  DRIPPING_HONEY = Kee[str]('dripping_honey')
  DRIPPING_LAVA = Kee[str]('dripping_lava')
  DRIPPING_OBSIDIAN_TEAR = Kee[str]('dripping_obsidian_tear')
  DRIPPING_WATER = Kee[str]('dripping_water')
  DUST = Kee[str]('dust')
  DUST_COLOR_TRANSITION = Kee[str]('dust_color_transition')
  DUST_PILLAR = Kee[str]('dust_pillar')
  DUST_PLUME = Kee[str]('dust_plume')
  EFFECT = Kee[str]('effect')
  EGG_CRACK = Kee[str]('egg_crack')
  ELDER_GUARDIAN = Kee[str]('elder_guardian')
  ELECTRIC_SPARK = Kee[str]('electric_spark')
  ENCHANT = Kee[str]('enchant')
  ENCHANTED_HIT = Kee[str]('enchanted_hit')
  END_ROD = Kee[str]('end_rod')
  ENTITY_EFFECT = Kee[str]('entity_effect')
  EXPLOSION = Kee[str]('explosion')
  EXPLOSION_EMITTER = Kee[str]('explosion_emitter')
  FALLING_CHERRY_LEAVES = Kee[str]('falling_cherry_leaves')
  FALLING_DRIPSTONE_LAVA = Kee[str]('falling_dripstone_lava')
  FALLING_DRIPSTONE_WATER = Kee[str]('falling_dripstone_water')
  FALLING_DUST = Kee[str]('falling_dust')
  FALLING_HONEY = Kee[str]('falling_honey')
  FALLING_LAVA = Kee[str]('falling_lava')
  FALLING_NECTAR = Kee[str]('falling_nectar')
  FALLING_OBSIDIAN_TEAR = Kee[str]('falling_obsidian_tear')
  FALLING_SPORE_BLOSSOM = Kee[str]('falling_spore_blossom')
  FALLING_WATER = Kee[str]('falling_water')
  FIREFLY = Kee[str]('firefly')
  FIREWORK = Kee[str]('firework')
  FISHING = Kee[str]('fishing')
  FLAME = Kee[str]('flame')
  FLASH = Kee[str]('flash')
  FOOTSTEP = Kee[str]('footstep')
  GEYSER = Kee[str]('geyser')
  GEYSER_BASE = Kee[str]('geyser_base')
  GEYSER_PLUME = Kee[str]('geyser_plume')
  GEYSER_POOF = Kee[str]('geyser_poof')
  GLOW = Kee[str]('glow')
  GLOW_SQUID_INK = Kee[str]('glow_squid_ink')
  GUST = Kee[str]('gust')
  GUST_DUST = Kee[str]('gust_dust')
  GUST_EMITTER = Kee[str]('gust_emitter')
  GUST_EMITTER_LARGE = Kee[str]('gust_emitter_large')
  GUST_EMITTER_SMALL = Kee[str]('gust_emitter_small')
  HAPPY_VILLAGER = Kee[str]('happy_villager')
  HEART = Kee[str]('heart')
  INFESTED = Kee[str]('infested')
  INSTANT_EFFECT = Kee[str]('instant_effect')
  ITEM = Kee[str]('item')
  ITEM_COBWEB = Kee[str]('item_cobweb')
  ITEM_SLIME = Kee[str]('item_slime')
  ITEM_SNOWBALL = Kee[str]('item_snowball')
  ITEM_TAKE = Kee[str]('item_take')
  LANDING_CHERRY_LEAVES = Kee[str]('landing_cherry_leaves')
  LANDING_HONEY = Kee[str]('landing_honey')
  LANDING_LAVA = Kee[str]('landing_lava')
  LANDING_OBSIDIAN_TEAR = Kee[str]('landing_obsidian_tear')
  LARGE_SMOKE = Kee[str]('large_smoke')
  LAVA = Kee[str]('lava')
  LIGHT = Kee[str]('light')
  MYCELIUM = Kee[str]('mycelium')
  NAUTILUS = Kee[str]('nautilus')
  NOTE = Kee[str]('note')
  NOXIOUS_GAS = Kee[str]('noxious_gas')
  NOXIOUS_GAS_CLOUD = Kee[str]('noxious_gas_cloud')
  OMINOUS_SPAWNING = Kee[str]('ominous_spawning')
  ORANGE_POPLAR_LEAVES = Kee[str]('orange_poplar_leaves')
  PALE_OAK_LEAVES = Kee[str]('pale_oak_leaves')
  PAUSE_MOB_GROWTH = Kee[str]('pause_mob_growth')
  POOF = Kee[str]('poof')
  PORTAL = Kee[str]('portal')
  RAID_OMEN = Kee[str]('raid_omen')
  RAIN = Kee[str]('rain')
  RED_POPLAR_LEAVES = Kee[str]('red_poplar_leaves')
  RESET_MOB_GROWTH = Kee[str]('reset_mob_growth')
  REVERSE_PORTAL = Kee[str]('reverse_portal')
  SCRAPE = Kee[str]('scrape')
  SCULK_CHARGE = Kee[str]('sculk_charge')
  SCULK_CHARGE_POP = Kee[str]('sculk_charge_pop')
  SCULK_SOUL = Kee[str]('sculk_soul')
  SHRIEK = Kee[str]('shriek')
  SMALL_FLAME = Kee[str]('small_flame')
  SMALL_GUST = Kee[str]('small_gust')
  SMOKE = Kee[str]('smoke')
  SNEEZE = Kee[str]('sneeze')
  SNOW_SHOVEL = Kee[str]('snow_shovel')
  SNOWFLAKE = Kee[str]('snowflake')
  SONIC_BOOM = Kee[str]('sonic_boom')
  SOUL = Kee[str]('soul')
  SOUL_FIRE_FLAME = Kee[str]('soul_fire_flame')
  SPIT = Kee[str]('spit')
  SPLASH = Kee[str]('splash')
  SPORE_BLOSSOM_AIR = Kee[str]('spore_blossom_air')
  SQUID_INK = Kee[str]('squid_ink')
  SULFUR_BUBBLES = Kee[str]('sulfur_bubbles')
  SULFUR_CUBE_GOO = Kee[str]('sulfur_cube_goo')
  SUSPENDED_DEPTH = Kee[str]('suspended_depth')
  SWEEP_ATTACK = Kee[str]('sweep_attack')
  TINTED_LEAVES = Kee[str]('tinted_leaves')
  TOTEM_OF_UNDYING = Kee[str]('totem_of_undying')
  TRAIL = Kee[str]('trail')
  TRIAL_OMEN = Kee[str]('trial_omen')
  TRIAL_SPAWNER_DETECTION = Kee[str]('trial_spawner_detection')
  TRIAL_SPAWNER_DETECTION_OMINOUS = Kee[str]('trial_spawner_detection_ominous')
  UNDERWATER = Kee[str]('underwater')
  VAULT_CONNECTION = Kee[str]('vault_connection')
  VIBRATION = Kee[str]('vibration')
  WARPED_SPORE = Kee[str]('warped_spore')
  WAX_OFF = Kee[str]('wax_off')
  WAX_ON = Kee[str]('wax_on')
  WHITE_ASH = Kee[str]('white_ash')
  WHITE_SMOKE = Kee[str]('white_smoke')
  WITCH = Kee[str]('witch')
  YELLOW_POPLAR_LEAVES = Kee[str]('yellow_poplar_leaves')
