"""
MCBlockEntities is the catalogue of the game's block entities: an enumeration
with one member for every block entity of the data file that ships with mcdex,
each the same block entity in every version, with the id each version knows it
by: the name it is saved under, the 'id' in its data.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import BlockEntityId, MCThing


class MCBlockEntities(MCThing, strictCase=False):
  """
  The catalogue of the game's block entities, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    chest = MCBlockEntities.Chest
    chest is MCBlockEntities['chest']  # True
    chest[Version.V1_10_2]  # BlockEntityId('chest', 'Chest')
    len(MCBlockEntities)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'block_entities.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'block_entities.json'
  __data_key__ = 'block_entities'
  __id_class__ = BlockEntityId
  __kind__ = 'block entity'

  #  Members, one for every thing of 'block_entities.json'
  Banner = Kee[str]('banner')
  Barrel = Kee[str]('barrel')
  Beacon = Kee[str]('beacon')
  Bed = Kee[str]('bed')
  Beehive = Kee[str]('beehive')
  Bell = Kee[str]('bell')
  BlastFurnace = Kee[str]('blast_furnace')
  BrewingStand = Kee[str]('brewing_stand')
  BrushableBlock = Kee[str]('brushable_block')
  CalibratedSculkSensor = Kee[str]('calibrated_sculk_sensor')
  Campfire = Kee[str]('campfire')
  Chest = Kee[str]('chest')
  ChiseledBookshelf = Kee[str]('chiseled_bookshelf')
  CommandBlock = Kee[str]('command_block')
  Comparator = Kee[str]('comparator')
  Conduit = Kee[str]('conduit')
  CopperGolemStatue = Kee[str]('copper_golem_statue')
  Crafter = Kee[str]('crafter')
  CreakingHeart = Kee[str]('creaking_heart')
  DaylightDetector = Kee[str]('daylight_detector')
  DecoratedPot = Kee[str]('decorated_pot')
  Dispenser = Kee[str]('dispenser')
  Dropper = Kee[str]('dropper')
  EnchantingTable = Kee[str]('enchanting_table')
  EndGateway = Kee[str]('end_gateway')
  EndPortal = Kee[str]('end_portal')
  EnderChest = Kee[str]('ender_chest')
  FlowerPot = Kee[str]('flower_pot')
  Furnace = Kee[str]('furnace')
  HangingSign = Kee[str]('hanging_sign')
  Hopper = Kee[str]('hopper')
  Jigsaw = Kee[str]('jigsaw')
  Jukebox = Kee[str]('jukebox')
  Lectern = Kee[str]('lectern')
  MobSpawner = Kee[str]('mob_spawner')
  Noteblock = Kee[str]('noteblock')
  Piston = Kee[str]('piston')
  PotentSulfur = Kee[str]('potent_sulfur')
  SculkCatalyst = Kee[str]('sculk_catalyst')
  SculkSensor = Kee[str]('sculk_sensor')
  SculkShrieker = Kee[str]('sculk_shrieker')
  Shelf = Kee[str]('shelf')
  ShulkerBox = Kee[str]('shulker_box')
  Sign = Kee[str]('sign')
  Skull = Kee[str]('skull')
  Smoker = Kee[str]('smoker')
  StructureBlock = Kee[str]('structure_block')
  TestBlock = Kee[str]('test_block')
  TestInstanceBlock = Kee[str]('test_instance_block')
  TrappedChest = Kee[str]('trapped_chest')
  TrialSpawner = Kee[str]('trial_spawner')
  Vault = Kee[str]('vault')
