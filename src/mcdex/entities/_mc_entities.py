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


class MCEntities(MCThing):
  """
  The catalogue of the game's entities, each a member, found by its name in
  capitals, in any case, or by its unique name:

    witherSkeleton = MCEntities.WITHER_SKELETON
    witherSkeleton is MCEntities['wither_skeleton']  # True
    witherSkeleton[Version.V1_10_2]
    # EntityId('wither_skeleton', 'Skeleton{SkeletonType:1}')
    len(MCEntities)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'entities.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'entities.json'
  __data_key__ = 'entities'
  __id_class__ = EntityId
  __kind__ = 'entity'

  #  Members, one for every name of 'entities.json'
  ACACIA_BOAT = Kee[str]('acacia_boat')
  ACACIA_CHEST_BOAT = Kee[str]('acacia_chest_boat')
  ALLAY = Kee[str]('allay')
  AREA_EFFECT_CLOUD = Kee[str]('area_effect_cloud')
  ARMADILLO = Kee[str]('armadillo')
  ARMOR_STAND = Kee[str]('armor_stand')
  ARROW = Kee[str]('arrow')
  AXOLOTL = Kee[str]('axolotl')
  BAMBOO_CHEST_RAFT = Kee[str]('bamboo_chest_raft')
  BAMBOO_RAFT = Kee[str]('bamboo_raft')
  BAT = Kee[str]('bat')
  BEE = Kee[str]('bee')
  BIRCH_BOAT = Kee[str]('birch_boat')
  BIRCH_CHEST_BOAT = Kee[str]('birch_chest_boat')
  BLAZE = Kee[str]('blaze')
  BLOCK_DISPLAY = Kee[str]('block_display')
  BOGGED = Kee[str]('bogged')
  BREEZE = Kee[str]('breeze')
  BREEZE_WIND_CHARGE = Kee[str]('breeze_wind_charge')
  CAMEL = Kee[str]('camel')
  CAMEL_HUSK = Kee[str]('camel_husk')
  CAT = Kee[str]('cat')
  CAVE_SPIDER = Kee[str]('cave_spider')
  CHERRY_BOAT = Kee[str]('cherry_boat')
  CHERRY_CHEST_BOAT = Kee[str]('cherry_chest_boat')
  CHEST_MINECART = Kee[str]('chest_minecart')
  CHICKEN = Kee[str]('chicken')
  COD = Kee[str]('cod')
  COMMAND_BLOCK_MINECART = Kee[str]('command_block_minecart')
  COPPER_GOLEM = Kee[str]('copper_golem')
  COW = Kee[str]('cow')
  CREAKING = Kee[str]('creaking')
  CREAKING_TRANSIENT = Kee[str]('creaking_transient')
  CREEPER = Kee[str]('creeper')
  CUSHION = Kee[str]('cushion')
  DARK_OAK_BOAT = Kee[str]('dark_oak_boat')
  DARK_OAK_CHEST_BOAT = Kee[str]('dark_oak_chest_boat')
  DOLPHIN = Kee[str]('dolphin')
  DONKEY = Kee[str]('donkey')
  DRAGON_FIREBALL = Kee[str]('dragon_fireball')
  DROWNED = Kee[str]('drowned')
  EGG = Kee[str]('egg')
  ELDER_GUARDIAN = Kee[str]('elder_guardian')
  END_CRYSTAL = Kee[str]('end_crystal')
  ENDER_DRAGON = Kee[str]('ender_dragon')
  ENDER_PEARL = Kee[str]('ender_pearl')
  ENDERMAN = Kee[str]('enderman')
  ENDERMITE = Kee[str]('endermite')
  EVOKER = Kee[str]('evoker')
  EVOKER_FANGS = Kee[str]('evoker_fangs')
  EXPERIENCE_BOTTLE = Kee[str]('experience_bottle')
  EXPERIENCE_ORB = Kee[str]('experience_orb')
  EYE_OF_ENDER = Kee[str]('eye_of_ender')
  FALLING_BLOCK = Kee[str]('falling_block')
  FIREBALL = Kee[str]('fireball')
  FIREWORK_ROCKET = Kee[str]('firework_rocket')
  FISHING_BOBBER = Kee[str]('fishing_bobber')
  FOX = Kee[str]('fox')
  FROG = Kee[str]('frog')
  FURNACE_MINECART = Kee[str]('furnace_minecart')
  GHAST = Kee[str]('ghast')
  GIANT = Kee[str]('giant')
  GLOW_ITEM_FRAME = Kee[str]('glow_item_frame')
  GLOW_SQUID = Kee[str]('glow_squid')
  GOAT = Kee[str]('goat')
  GUARDIAN = Kee[str]('guardian')
  HAPPY_GHAST = Kee[str]('happy_ghast')
  HOGLIN = Kee[str]('hoglin')
  HOPPER_MINECART = Kee[str]('hopper_minecart')
  HORSE = Kee[str]('horse')
  HUSK = Kee[str]('husk')
  ILLUSIONER = Kee[str]('illusioner')
  INTERACTION = Kee[str]('interaction')
  IRON_GOLEM = Kee[str]('iron_golem')
  ITEM = Kee[str]('item')
  ITEM_DISPLAY = Kee[str]('item_display')
  ITEM_FRAME = Kee[str]('item_frame')
  JUNGLE_BOAT = Kee[str]('jungle_boat')
  JUNGLE_CHEST_BOAT = Kee[str]('jungle_chest_boat')
  LEASH_KNOT = Kee[str]('leash_knot')
  LIGHTNING_BOLT = Kee[str]('lightning_bolt')
  LINGERING_POTION = Kee[str]('lingering_potion')
  LLAMA = Kee[str]('llama')
  LLAMA_SPIT = Kee[str]('llama_spit')
  MAGMA_CUBE = Kee[str]('magma_cube')
  MANGROVE_BOAT = Kee[str]('mangrove_boat')
  MANGROVE_CHEST_BOAT = Kee[str]('mangrove_chest_boat')
  MANNEQUIN = Kee[str]('mannequin')
  MARKER = Kee[str]('marker')
  MINECART = Kee[str]('minecart')
  MOOSHROOM = Kee[str]('mooshroom')
  MULE = Kee[str]('mule')
  NAUTILUS = Kee[str]('nautilus')
  OAK_BOAT = Kee[str]('oak_boat')
  OAK_CHEST_BOAT = Kee[str]('oak_chest_boat')
  OCELOT = Kee[str]('ocelot')
  OMINOUS_ITEM_SPAWNER = Kee[str]('ominous_item_spawner')
  PAINTING = Kee[str]('painting')
  PALE_OAK_BOAT = Kee[str]('pale_oak_boat')
  PALE_OAK_CHEST_BOAT = Kee[str]('pale_oak_chest_boat')
  PANDA = Kee[str]('panda')
  PARCHED = Kee[str]('parched')
  PARROT = Kee[str]('parrot')
  PHANTOM = Kee[str]('phantom')
  PIG = Kee[str]('pig')
  PIGLIN = Kee[str]('piglin')
  PIGLIN_BRUTE = Kee[str]('piglin_brute')
  PILLAGER = Kee[str]('pillager')
  PLAYER = Kee[str]('player')
  POLAR_BEAR = Kee[str]('polar_bear')
  POPLAR_BOAT = Kee[str]('poplar_boat')
  POPLAR_CHEST_BOAT = Kee[str]('poplar_chest_boat')
  PRIMED_TNT = Kee[str]('primed_tnt')
  PUFFERFISH = Kee[str]('pufferfish')
  RABBIT = Kee[str]('rabbit')
  RAVAGER = Kee[str]('ravager')
  SALMON = Kee[str]('salmon')
  SHEEP = Kee[str]('sheep')
  SHULKER = Kee[str]('shulker')
  SHULKER_BULLET = Kee[str]('shulker_bullet')
  SILVERFISH = Kee[str]('silverfish')
  SKELETON = Kee[str]('skeleton')
  SKELETON_HORSE = Kee[str]('skeleton_horse')
  SLIME = Kee[str]('slime')
  SMALL_FIREBALL = Kee[str]('small_fireball')
  SNIFFER = Kee[str]('sniffer')
  SNOW_GOLEM = Kee[str]('snow_golem')
  SNOWBALL = Kee[str]('snowball')
  SPAWNER_MINECART = Kee[str]('spawner_minecart')
  SPECTRAL_ARROW = Kee[str]('spectral_arrow')
  SPIDER = Kee[str]('spider')
  SPLASH_POTION = Kee[str]('splash_potion')
  SPRUCE_BOAT = Kee[str]('spruce_boat')
  SPRUCE_CHEST_BOAT = Kee[str]('spruce_chest_boat')
  SQUID = Kee[str]('squid')
  STRAY = Kee[str]('stray')
  STRIDER = Kee[str]('strider')
  SULFUR_CUBE = Kee[str]('sulfur_cube')
  TADPOLE = Kee[str]('tadpole')
  TEXT_DISPLAY = Kee[str]('text_display')
  THROWN_BOTTLE_O_ENCHANTING = Kee[str]('thrown_bottle_o_enchanting')
  THROWN_EGG = Kee[str]('thrown_egg')
  THROWN_ENDER_PEARL = Kee[str]('thrown_ender_pearl')
  TNT = Kee[str]('tnt')
  TNT_MINECART = Kee[str]('tnt_minecart')
  TRADER_LLAMA = Kee[str]('trader_llama')
  TRIDENT = Kee[str]('trident')
  TROPICAL_FISH = Kee[str]('tropical_fish')
  TURTLE = Kee[str]('turtle')
  VEX = Kee[str]('vex')
  VILLAGER = Kee[str]('villager')
  VINDICATOR = Kee[str]('vindicator')
  WANDERING_TRADER = Kee[str]('wandering_trader')
  WARDEN = Kee[str]('warden')
  WIND_CHARGE = Kee[str]('wind_charge')
  WITCH = Kee[str]('witch')
  WITHER = Kee[str]('wither')
  WITHER_SKELETON = Kee[str]('wither_skeleton')
  WITHER_SKULL = Kee[str]('wither_skull')
  WOLF = Kee[str]('wolf')
  ZOGLIN = Kee[str]('zoglin')
  ZOMBIE = Kee[str]('zombie')
  ZOMBIE_HORSE = Kee[str]('zombie_horse')
  ZOMBIE_NAUTILUS = Kee[str]('zombie_nautilus')
  ZOMBIE_VILLAGER = Kee[str]('zombie_villager')
  ZOMBIFIED_PIGLIN = Kee[str]('zombified_piglin')
