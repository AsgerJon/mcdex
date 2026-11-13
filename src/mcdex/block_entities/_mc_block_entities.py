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


class MCBlockEntities(MCThing):
  """
  The catalogue of the game's block entities, each a member, found by its name
  in capitals, in any case, or by its unique name:

    chest = MCBlockEntities.CHEST
    chest is MCBlockEntities['chest']  # True
    chest['1.10.2']  # BlockEntityId('chest', 'Chest')
    len(MCBlockEntities)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'block_entities.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'block_entities.json'
  __data_key__ = 'block_entities'
  __id_class__ = BlockEntityId
  __kind__ = 'block entity'

  #  Members, one for every name of 'block_entities.json'
  BANNER = Kee[str]('banner')
  BARREL = Kee[str]('barrel')
  BEACON = Kee[str]('beacon')
  BED = Kee[str]('bed')
  BEEHIVE = Kee[str]('beehive')
  BELL = Kee[str]('bell')
  BLAST_FURNACE = Kee[str]('blast_furnace')
  BREWING_STAND = Kee[str]('brewing_stand')
  BRUSHABLE_BLOCK = Kee[str]('brushable_block')
  CALIBRATED_SCULK_SENSOR = Kee[str]('calibrated_sculk_sensor')
  CAMPFIRE = Kee[str]('campfire')
  CHEST = Kee[str]('chest')
  CHISELED_BOOKSHELF = Kee[str]('chiseled_bookshelf')
  COMMAND_BLOCK = Kee[str]('command_block')
  COMPARATOR = Kee[str]('comparator')
  CONDUIT = Kee[str]('conduit')
  COPPER_GOLEM_STATUE = Kee[str]('copper_golem_statue')
  CRAFTER = Kee[str]('crafter')
  CREAKING_HEART = Kee[str]('creaking_heart')
  DAYLIGHT_DETECTOR = Kee[str]('daylight_detector')
  DECORATED_POT = Kee[str]('decorated_pot')
  DISPENSER = Kee[str]('dispenser')
  DROPPER = Kee[str]('dropper')
  ENCHANTING_TABLE = Kee[str]('enchanting_table')
  END_GATEWAY = Kee[str]('end_gateway')
  END_PORTAL = Kee[str]('end_portal')
  ENDER_CHEST = Kee[str]('ender_chest')
  FLOWER_POT = Kee[str]('flower_pot')
  FURNACE = Kee[str]('furnace')
  HANGING_SIGN = Kee[str]('hanging_sign')
  HOPPER = Kee[str]('hopper')
  JIGSAW = Kee[str]('jigsaw')
  JUKEBOX = Kee[str]('jukebox')
  LECTERN = Kee[str]('lectern')
  MOB_SPAWNER = Kee[str]('mob_spawner')
  NOTEBLOCK = Kee[str]('noteblock')
  PISTON = Kee[str]('piston')
  POTENT_SULFUR = Kee[str]('potent_sulfur')
  SCULK_CATALYST = Kee[str]('sculk_catalyst')
  SCULK_SENSOR = Kee[str]('sculk_sensor')
  SCULK_SHRIEKER = Kee[str]('sculk_shrieker')
  SHELF = Kee[str]('shelf')
  SHULKER_BOX = Kee[str]('shulker_box')
  SIGN = Kee[str]('sign')
  SKULL = Kee[str]('skull')
  SMOKER = Kee[str]('smoker')
  STRUCTURE_BLOCK = Kee[str]('structure_block')
  TEST_BLOCK = Kee[str]('test_block')
  TEST_INSTANCE_BLOCK = Kee[str]('test_instance_block')
  TRAPPED_CHEST = Kee[str]('trapped_chest')
  TRIAL_SPAWNER = Kee[str]('trial_spawner')
  VAULT = Kee[str]('vault')
