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


class MCParticles(MCThing, strictCase=False):
  """
  The catalogue of the game's particles, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    poof = MCParticles.Poof
    poof is MCParticles['poof']  # True
    poof[Version.V1_12_2]  # ParticleId('poof', 'explode')
    len(MCParticles)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'particles.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'particles.json'
  __data_key__ = 'particles'
  __id_class__ = ParticleId
  __kind__ = 'particle'

  #  Members, one for every thing of 'particles.json'
  AmbientEntityEffect = Kee[str]('ambient_entity_effect')
  AngryVillager = Kee[str]('angry_villager')
  Ash = Kee[str]('ash')
  Barrier = Kee[str]('barrier')
  Block = Kee[str]('block')
  BlockCrumble = Kee[str]('block_crumble')
  BlockDust = Kee[str]('block_dust')
  BlockMarker = Kee[str]('block_marker')
  Bubble = Kee[str]('bubble')
  BubbleColumnUp = Kee[str]('bubble_column_up')
  BubblePop = Kee[str]('bubble_pop')
  CampfireCosySmoke = Kee[str]('campfire_cosy_smoke')
  CampfireSignalSmoke = Kee[str]('campfire_signal_smoke')
  CherryLeaves = Kee[str]('cherry_leaves')
  Cloud = Kee[str]('cloud')
  Composter = Kee[str]('composter')
  CopperFireFlame = Kee[str]('copper_fire_flame')
  CrimsonSpore = Kee[str]('crimson_spore')
  Crit = Kee[str]('crit')
  CurrentDown = Kee[str]('current_down')
  DamageIndicator = Kee[str]('damage_indicator')
  Dolphin = Kee[str]('dolphin')
  DragonBreath = Kee[str]('dragon_breath')
  DrippingCherryLeaves = Kee[str]('dripping_cherry_leaves')
  DrippingDripstoneLava = Kee[str]('dripping_dripstone_lava')
  DrippingDripstoneWater = Kee[str]('dripping_dripstone_water')
  DrippingHoney = Kee[str]('dripping_honey')
  DrippingLava = Kee[str]('dripping_lava')
  DrippingObsidianTear = Kee[str]('dripping_obsidian_tear')
  DrippingWater = Kee[str]('dripping_water')
  Dust = Kee[str]('dust')
  DustColorTransition = Kee[str]('dust_color_transition')
  DustPillar = Kee[str]('dust_pillar')
  DustPlume = Kee[str]('dust_plume')
  Effect = Kee[str]('effect')
  EggCrack = Kee[str]('egg_crack')
  ElderGuardian = Kee[str]('elder_guardian')
  ElectricSpark = Kee[str]('electric_spark')
  Enchant = Kee[str]('enchant')
  EnchantedHit = Kee[str]('enchanted_hit')
  EndRod = Kee[str]('end_rod')
  EntityEffect = Kee[str]('entity_effect')
  Explosion = Kee[str]('explosion')
  ExplosionEmitter = Kee[str]('explosion_emitter')
  FallingCherryLeaves = Kee[str]('falling_cherry_leaves')
  FallingDripstoneLava = Kee[str]('falling_dripstone_lava')
  FallingDripstoneWater = Kee[str]('falling_dripstone_water')
  FallingDust = Kee[str]('falling_dust')
  FallingHoney = Kee[str]('falling_honey')
  FallingLava = Kee[str]('falling_lava')
  FallingNectar = Kee[str]('falling_nectar')
  FallingObsidianTear = Kee[str]('falling_obsidian_tear')
  FallingSporeBlossom = Kee[str]('falling_spore_blossom')
  FallingWater = Kee[str]('falling_water')
  Firefly = Kee[str]('firefly')
  Firework = Kee[str]('firework')
  Fishing = Kee[str]('fishing')
  Flame = Kee[str]('flame')
  Flash = Kee[str]('flash')
  Footstep = Kee[str]('footstep')
  Geyser = Kee[str]('geyser')
  GeyserBase = Kee[str]('geyser_base')
  GeyserPlume = Kee[str]('geyser_plume')
  GeyserPoof = Kee[str]('geyser_poof')
  Glow = Kee[str]('glow')
  GlowSquidInk = Kee[str]('glow_squid_ink')
  Gust = Kee[str]('gust')
  GustDust = Kee[str]('gust_dust')
  GustEmitter = Kee[str]('gust_emitter')
  GustEmitterLarge = Kee[str]('gust_emitter_large')
  GustEmitterSmall = Kee[str]('gust_emitter_small')
  HappyVillager = Kee[str]('happy_villager')
  Heart = Kee[str]('heart')
  Infested = Kee[str]('infested')
  InstantEffect = Kee[str]('instant_effect')
  Item = Kee[str]('item')
  ItemCobweb = Kee[str]('item_cobweb')
  ItemSlime = Kee[str]('item_slime')
  ItemSnowball = Kee[str]('item_snowball')
  ItemTake = Kee[str]('item_take')
  LandingCherryLeaves = Kee[str]('landing_cherry_leaves')
  LandingHoney = Kee[str]('landing_honey')
  LandingLava = Kee[str]('landing_lava')
  LandingObsidianTear = Kee[str]('landing_obsidian_tear')
  LargeSmoke = Kee[str]('large_smoke')
  Lava = Kee[str]('lava')
  Light = Kee[str]('light')
  Mycelium = Kee[str]('mycelium')
  Nautilus = Kee[str]('nautilus')
  Note = Kee[str]('note')
  NoxiousGas = Kee[str]('noxious_gas')
  NoxiousGasCloud = Kee[str]('noxious_gas_cloud')
  OminousSpawning = Kee[str]('ominous_spawning')
  OrangePoplarLeaves = Kee[str]('orange_poplar_leaves')
  PaleOakLeaves = Kee[str]('pale_oak_leaves')
  PauseMobGrowth = Kee[str]('pause_mob_growth')
  Poof = Kee[str]('poof')
  Portal = Kee[str]('portal')
  RaidOmen = Kee[str]('raid_omen')
  Rain = Kee[str]('rain')
  RedPoplarLeaves = Kee[str]('red_poplar_leaves')
  ResetMobGrowth = Kee[str]('reset_mob_growth')
  ReversePortal = Kee[str]('reverse_portal')
  Scrape = Kee[str]('scrape')
  SculkCharge = Kee[str]('sculk_charge')
  SculkChargePop = Kee[str]('sculk_charge_pop')
  SculkSoul = Kee[str]('sculk_soul')
  Shriek = Kee[str]('shriek')
  SmallFlame = Kee[str]('small_flame')
  SmallGust = Kee[str]('small_gust')
  Smoke = Kee[str]('smoke')
  Sneeze = Kee[str]('sneeze')
  SnowShovel = Kee[str]('snow_shovel')
  Snowflake = Kee[str]('snowflake')
  SonicBoom = Kee[str]('sonic_boom')
  Soul = Kee[str]('soul')
  SoulFireFlame = Kee[str]('soul_fire_flame')
  Spit = Kee[str]('spit')
  Splash = Kee[str]('splash')
  SporeBlossomAir = Kee[str]('spore_blossom_air')
  SquidInk = Kee[str]('squid_ink')
  SulfurBubbles = Kee[str]('sulfur_bubbles')
  SulfurCubeGoo = Kee[str]('sulfur_cube_goo')
  SuspendedDepth = Kee[str]('suspended_depth')
  SweepAttack = Kee[str]('sweep_attack')
  TintedLeaves = Kee[str]('tinted_leaves')
  TotemOfUndying = Kee[str]('totem_of_undying')
  Trail = Kee[str]('trail')
  TrialOmen = Kee[str]('trial_omen')
  TrialSpawnerDetection = Kee[str]('trial_spawner_detection')
  TrialSpawnerDetectionOminous = Kee[str]('trial_spawner_detection_ominous')
  Underwater = Kee[str]('underwater')
  VaultConnection = Kee[str]('vault_connection')
  Vibration = Kee[str]('vibration')
  WarpedSpore = Kee[str]('warped_spore')
  WaxOff = Kee[str]('wax_off')
  WaxOn = Kee[str]('wax_on')
  WhiteAsh = Kee[str]('white_ash')
  WhiteSmoke = Kee[str]('white_smoke')
  Witch = Kee[str]('witch')
  YellowPoplarLeaves = Kee[str]('yellow_poplar_leaves')
