"""
MCEntities is the catalogue of the game's entities: an enumeration with one
member for every entity of the data file that ships with mcdex, each the
same entity in every version, with the id each version knows it by:
what /summon takes.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import EntityId, MCThing


class MCEntities(MCThing, strictCase=False):
  """
  The catalogue of the game's entities, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    witherSkeleton = MCEntities.WitherSkeleton
    witherSkeleton is MCEntities['wither_skeleton']  # True
    witherSkeleton[Version.V1_10_2]
    # EntityId('wither_skeleton', 'Skeleton{SkeletonType:1}')
    len(MCEntities)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'entities.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'entities.json'
  __data_key__ = 'entities'
  __id_class__ = EntityId
  __kind__ = 'entity'

  #  Members, one for every thing of 'entities.json'
  AcaciaBoat = Kee[str]('acacia_boat')
  AcaciaChestBoat = Kee[str]('acacia_chest_boat')
  Allay = Kee[str]('allay')
  AreaEffectCloud = Kee[str]('area_effect_cloud')
  Armadillo = Kee[str]('armadillo')
  ArmorStand = Kee[str]('armor_stand')
  Arrow = Kee[str]('arrow')
  Axolotl = Kee[str]('axolotl')
  BambooChestRaft = Kee[str]('bamboo_chest_raft')
  BambooRaft = Kee[str]('bamboo_raft')
  Bat = Kee[str]('bat')
  Bee = Kee[str]('bee')
  BirchBoat = Kee[str]('birch_boat')
  BirchChestBoat = Kee[str]('birch_chest_boat')
  Blaze = Kee[str]('blaze')
  BlockDisplay = Kee[str]('block_display')
  Bogged = Kee[str]('bogged')
  Breeze = Kee[str]('breeze')
  BreezeWindCharge = Kee[str]('breeze_wind_charge')
  Camel = Kee[str]('camel')
  CamelHusk = Kee[str]('camel_husk')
  Cat = Kee[str]('cat')
  CaveSpider = Kee[str]('cave_spider')
  CherryBoat = Kee[str]('cherry_boat')
  CherryChestBoat = Kee[str]('cherry_chest_boat')
  ChestMinecart = Kee[str]('chest_minecart')
  Chicken = Kee[str]('chicken')
  Cod = Kee[str]('cod')
  CommandBlockMinecart = Kee[str]('command_block_minecart')
  CopperGolem = Kee[str]('copper_golem')
  Cow = Kee[str]('cow')
  Creaking = Kee[str]('creaking')
  CreakingTransient = Kee[str]('creaking_transient')
  Creeper = Kee[str]('creeper')
  Cushion = Kee[str]('cushion')
  DarkOakBoat = Kee[str]('dark_oak_boat')
  DarkOakChestBoat = Kee[str]('dark_oak_chest_boat')
  Dolphin = Kee[str]('dolphin')
  Donkey = Kee[str]('donkey')
  DragonFireball = Kee[str]('dragon_fireball')
  Drowned = Kee[str]('drowned')
  Egg = Kee[str]('egg')
  ElderGuardian = Kee[str]('elder_guardian')
  EndCrystal = Kee[str]('end_crystal')
  EnderDragon = Kee[str]('ender_dragon')
  EnderPearl = Kee[str]('ender_pearl')
  Enderman = Kee[str]('enderman')
  Endermite = Kee[str]('endermite')
  Evoker = Kee[str]('evoker')
  EvokerFangs = Kee[str]('evoker_fangs')
  ExperienceBottle = Kee[str]('experience_bottle')
  ExperienceOrb = Kee[str]('experience_orb')
  EyeOfEnder = Kee[str]('eye_of_ender')
  FallingBlock = Kee[str]('falling_block')
  Fireball = Kee[str]('fireball')
  FireworkRocket = Kee[str]('firework_rocket')
  FishingBobber = Kee[str]('fishing_bobber')
  Fox = Kee[str]('fox')
  Frog = Kee[str]('frog')
  FurnaceMinecart = Kee[str]('furnace_minecart')
  Ghast = Kee[str]('ghast')
  Giant = Kee[str]('giant')
  GlowItemFrame = Kee[str]('glow_item_frame')
  GlowSquid = Kee[str]('glow_squid')
  Goat = Kee[str]('goat')
  Guardian = Kee[str]('guardian')
  HappyGhast = Kee[str]('happy_ghast')
  Hoglin = Kee[str]('hoglin')
  HopperMinecart = Kee[str]('hopper_minecart')
  Horse = Kee[str]('horse')
  Husk = Kee[str]('husk')
  Illusioner = Kee[str]('illusioner')
  Interaction = Kee[str]('interaction')
  IronGolem = Kee[str]('iron_golem')
  Item = Kee[str]('item')
  ItemDisplay = Kee[str]('item_display')
  ItemFrame = Kee[str]('item_frame')
  JungleBoat = Kee[str]('jungle_boat')
  JungleChestBoat = Kee[str]('jungle_chest_boat')
  LeashKnot = Kee[str]('leash_knot')
  LightningBolt = Kee[str]('lightning_bolt')
  LingeringPotion = Kee[str]('lingering_potion')
  Llama = Kee[str]('llama')
  LlamaSpit = Kee[str]('llama_spit')
  MagmaCube = Kee[str]('magma_cube')
  MangroveBoat = Kee[str]('mangrove_boat')
  MangroveChestBoat = Kee[str]('mangrove_chest_boat')
  Mannequin = Kee[str]('mannequin')
  Marker = Kee[str]('marker')
  Minecart = Kee[str]('minecart')
  Mooshroom = Kee[str]('mooshroom')
  Mule = Kee[str]('mule')
  Nautilus = Kee[str]('nautilus')
  OakBoat = Kee[str]('oak_boat')
  OakChestBoat = Kee[str]('oak_chest_boat')
  Ocelot = Kee[str]('ocelot')
  OminousItemSpawner = Kee[str]('ominous_item_spawner')
  Painting = Kee[str]('painting')
  PaleOakBoat = Kee[str]('pale_oak_boat')
  PaleOakChestBoat = Kee[str]('pale_oak_chest_boat')
  Panda = Kee[str]('panda')
  Parched = Kee[str]('parched')
  Parrot = Kee[str]('parrot')
  Phantom = Kee[str]('phantom')
  Pig = Kee[str]('pig')
  Piglin = Kee[str]('piglin')
  PiglinBrute = Kee[str]('piglin_brute')
  Pillager = Kee[str]('pillager')
  Player = Kee[str]('player')
  PolarBear = Kee[str]('polar_bear')
  PoplarBoat = Kee[str]('poplar_boat')
  PoplarChestBoat = Kee[str]('poplar_chest_boat')
  PrimedTnt = Kee[str]('primed_tnt')
  Pufferfish = Kee[str]('pufferfish')
  Rabbit = Kee[str]('rabbit')
  Ravager = Kee[str]('ravager')
  Salmon = Kee[str]('salmon')
  Sheep = Kee[str]('sheep')
  Shulker = Kee[str]('shulker')
  ShulkerBullet = Kee[str]('shulker_bullet')
  Silverfish = Kee[str]('silverfish')
  Skeleton = Kee[str]('skeleton')
  SkeletonHorse = Kee[str]('skeleton_horse')
  Slime = Kee[str]('slime')
  SmallFireball = Kee[str]('small_fireball')
  Sniffer = Kee[str]('sniffer')
  SnowGolem = Kee[str]('snow_golem')
  Snowball = Kee[str]('snowball')
  SpawnerMinecart = Kee[str]('spawner_minecart')
  SpectralArrow = Kee[str]('spectral_arrow')
  Spider = Kee[str]('spider')
  SplashPotion = Kee[str]('splash_potion')
  SpruceBoat = Kee[str]('spruce_boat')
  SpruceChestBoat = Kee[str]('spruce_chest_boat')
  Squid = Kee[str]('squid')
  Stray = Kee[str]('stray')
  Strider = Kee[str]('strider')
  SulfurCube = Kee[str]('sulfur_cube')
  Tadpole = Kee[str]('tadpole')
  TextDisplay = Kee[str]('text_display')
  ThrownBottleOEnchanting = Kee[str]('thrown_bottle_o_enchanting')
  ThrownEgg = Kee[str]('thrown_egg')
  ThrownEnderPearl = Kee[str]('thrown_ender_pearl')
  Tnt = Kee[str]('tnt')
  TntMinecart = Kee[str]('tnt_minecart')
  TraderLlama = Kee[str]('trader_llama')
  Trident = Kee[str]('trident')
  TropicalFish = Kee[str]('tropical_fish')
  Turtle = Kee[str]('turtle')
  Vex = Kee[str]('vex')
  Villager = Kee[str]('villager')
  Vindicator = Kee[str]('vindicator')
  WanderingTrader = Kee[str]('wandering_trader')
  Warden = Kee[str]('warden')
  WindCharge = Kee[str]('wind_charge')
  Witch = Kee[str]('witch')
  Wither = Kee[str]('wither')
  WitherSkeleton = Kee[str]('wither_skeleton')
  WitherSkull = Kee[str]('wither_skull')
  Wolf = Kee[str]('wolf')
  Zoglin = Kee[str]('zoglin')
  Zombie = Kee[str]('zombie')
  ZombieHorse = Kee[str]('zombie_horse')
  ZombieNautilus = Kee[str]('zombie_nautilus')
  ZombieVillager = Kee[str]('zombie_villager')
  ZombifiedPiglin = Kee[str]('zombified_piglin')
