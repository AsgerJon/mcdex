"""
TestMCItems tests the 'MCItems' catalogue: the items it hands out, and
what every item of its data must satisfy, however many there are.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import re
from importlib.resources import files

from worktoy.waitaminute.keenum import KeeResolveError
from worktoy.work_test import BaseTest

from mcdex import EquipmentSlot, ItemId, MCItems, NotInVersion
from mcdex import Version


def _records() -> dict:
  """The data file, read directly, to compare the catalogue against."""
  text = files('mcdex.items').joinpath('items.json').read_text('utf-8')
  return json.loads(text)['items']


#  The game's names of the items that have one a person would use too,
#  each the same item: counted once, under the other name.
GAME_NAMES = (
  'short_grass', 'ender_eye', 'experience_bottle', 'beef', 'chicken', 'cod',
  'mutton', 'porkchop', 'rabbit', 'salmon', 'cooked_beef', 'leather_helmet',
  'leather_chestplate', 'leather_leggings', 'turtle_helmet', 'writable_book',
  'slime_ball', 'quartz', 'redstone', 'rabbit_foot', 'dragon_breath',
  'comparator', 'repeater', 'spawner', 'hay_block', 'map',
)


class TestMCItems(BaseTest):
  """
  TestMCItems tests the 'MCItems' catalogue.
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.records = _records()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  LOOKUP   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_getitem(self) -> None:
    grass = MCItems.GRASS
    self.assertIsInstance(grass, MCItems)
    self.assertEqual(grass.uniqueName, 'grass')

  def test_getitem_same_object(self) -> None:
    self.assertIs(MCItems['diamond'], MCItems['diamond'])

  def test_getitem_unknown(self) -> None:
    with self.assertRaises(KeyError) as context:
      _ = MCItems['grss']
    self.assertIn("mcdex has no item named 'grss'", str(context.exception))

  def test_getitem_by_position(self) -> None:
    """An 'int' is a position, as in any enumeration."""
    self.assertIs(MCItems[7], list(MCItems)[7])

  def test_getitem_not_a_name(self) -> None:
    for name in (Version.V1_9, ('grass',)):
      with self.subTest(name=name):
        with self.assertRaises(KeeResolveError):
          _ = MCItems[name]

  def test_len(self) -> None:
    self.assertEqual(len(MCItems), len(self.records))

  def test_iter(self) -> None:
    items = list(MCItems)
    self.assertEqual([item.uniqueName for item in items], list(self.records))
    for item in items:
      self.assertIs(item, MCItems[item.uniqueName])

  def test_iter_again(self) -> None:
    self.assertEqual(len(list(MCItems)), len(list(MCItems)))

  def test_contains(self) -> None:
    self.assertIn('grass', MCItems)
    self.assertIn(MCItems['grass'], MCItems)
    self.assertNotIn('grss', MCItems)
    self.assertNotIn(7, MCItems)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE DATA   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_names_are_lowercase_words(self) -> None:
    for name in self.records:
      with self.subTest(name=name):
        self.assertRegex(name, r'^[a-z0-9]+(_[a-z0-9]+)*$')

  def test_records_begin_together(self) -> None:
    """Every record's ids begin at the first version the data covers."""
    for name, record in self.records.items():
      with self.subTest(name=name):
        self.assertEqual(list(record), ['ids', 'maxStackSize',
                                        'equipmentSlot'])
        self.assertEqual(next(iter(record['ids'])), '1.7.2')

  def test_ids_fit_their_era(self) -> None:
    named = re.compile(r'minecraft:[a-z0-9_]+(:[0-9]+)?(\{.+\})?')
    flat = re.compile(r'minecraft:[a-z0-9_]+')
    for name, record in self.records.items():
      for text, minecraftId in record['ids'].items():
        with self.subTest(name=name, version=text):
          if not minecraftId:
            continue
          if Version(text) < Version.V1_13:
            self.assertIsNotNone(named.fullmatch(minecraftId))
          else:
            self.assertIsNotNone(flat.fullmatch(minecraftId))

  def test_latest_version(self) -> None:
    """26.3 has 1,658 items, one 26.3 id each, and some have two names."""
    latest = {}
    for name, record in self.records.items():
      id_ = list(record['ids'].values())[-1]
      if id_:
        latest.setdefault(id_, []).append(name)
    self.assertEqual(len(latest), 1658)
    self.assertEqual(latest['minecraft:short_grass'],
                     ['grass', 'short_grass'])

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  KNOWN ITEMS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_elytra(self) -> None:
    elytra = MCItems.ELYTRA
    self.assertEqual(elytra[Version.V1_9],
                     ItemId('elytra', 'minecraft:elytra'))
    self.assertEqual(elytra[Version.V26_3].minecraftId, 'minecraft:elytra')
    with self.assertRaises(NotInVersion) as context:
      _ = elytra[Version.V1_7_10]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.7.10 has no 'elytra'; vanilla added it in 1.9!",
    )

  def test_pink_wool(self) -> None:
    pinkWool = MCItems.PINK_WOOL
    self.assertEqual(pinkWool[Version.V1_7_10].minecraftId, 'minecraft:wool:6')
    self.assertEqual(pinkWool[Version.V1_12_2].minecraftId, 'minecraft:wool:6')
    self.assertEqual(pinkWool[Version.V1_13].minecraftId,
                     'minecraft:pink_wool')

  def test_grass(self) -> None:
    for name in ('grass', 'short_grass'):
      with self.subTest(name=name):
        grass = MCItems[name]
        self.assertEqual(grass[Version.V1_7_10].minecraftId,
                         'minecraft:tallgrass:1')
        self.assertEqual(grass[Version.V1_20_2].minecraftId, 'minecraft:grass')
        self.assertEqual(grass[Version.V26_3].minecraftId,
                         'minecraft:short_grass')
    self.assertEqual(MCItems.GRASS_BLOCK[Version.V1_12_2].minecraftId,
                     'minecraft:grass')
    self.assertEqual(MCItems.GRASS_BLOCK[Version.V1_13].minecraftId,
                     'minecraft:grass_block')

  def test_shulker_boxes(self) -> None:
    for name in ('shulker_box', 'purple_shulker_box'):
      with self.subTest(name=name):
        self.assertEqual(MCItems[name][Version.V1_11].minecraftId,
                         'minecraft:purple_shulker_box')
        self.assertEqual(MCItems[name][Version.V1_12_2].minecraftId,
                         'minecraft:purple_shulker_box')
    self.assertEqual(MCItems.SHULKER_BOX[Version.V26_3].minecraftId,
                     'minecraft:shulker_box')
    self.assertEqual(MCItems.PURPLE_SHULKER_BOX[Version.V26_3].minecraftId,
                     'minecraft:purple_shulker_box')

  def test_pumpkins(self) -> None:
    """Every pumpkin before 1.13 had a face: both items, as shulker boxes."""
    for name in ('pumpkin', 'carved_pumpkin'):
      with self.subTest(name=name):
        item = MCItems[name]
        self.assertEqual(item[Version.V1_7_10].minecraftId,
                         'minecraft:pumpkin')
        self.assertEqual(item[Version.V1_12_2].minecraftId,
                         'minecraft:pumpkin')
        self.assertIs(item.equipmentSlot[Version.V1_12_2],
                      EquipmentSlot.HEAD)
    self.assertEqual(MCItems.PUMPKIN[Version.V1_13].minecraftId,
                     'minecraft:pumpkin')
    self.assertIs(MCItems.PUMPKIN.equipmentSlot[Version.V1_13],
                  EquipmentSlot.MAINHAND)
    self.assertEqual(MCItems.CARVED_PUMPKIN[Version.V1_13].minecraftId,
                     'minecraft:carved_pumpkin')

  def test_stone_slabs(self) -> None:
    """Until 1.14 the stone slab was the smooth one: both items."""
    for name in ('stone_slab', 'smooth_stone_slab'):
      with self.subTest(name=name):
        item = MCItems[name]
        self.assertEqual(item[Version.V1_12_2].minecraftId,
                         'minecraft:stone_slab:0')
        self.assertEqual(item[Version.V1_13_2].minecraftId,
                         'minecraft:stone_slab')
    self.assertEqual(MCItems.STONE_SLAB[Version.V1_14].minecraftId,
                     'minecraft:stone_slab')
    self.assertEqual(MCItems.SMOOTH_STONE_SLAB[Version.V1_14].minecraftId,
                     'minecraft:smooth_stone_slab')

  def test_stone_stairs(self) -> None:
    """The old stone stairs were cobblestone stairs, and only those."""
    self.assertEqual(MCItems.COBBLESTONE_STAIRS[Version.V1_12_2].minecraftId,
                     'minecraft:stone_stairs')
    with self.assertRaises(NotInVersion):
      _ = MCItems.STONE_STAIRS[Version.V1_12_2]
    self.assertEqual(MCItems.STONE_STAIRS[Version.V1_14].minecraftId,
                     'minecraft:stone_stairs')

  def test_removed(self) -> None:
    with self.assertRaises(NotInVersion) as context:
      _ = MCItems.LIT_FURNACE[Version.V1_10]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.10 has no 'lit_furnace'; vanilla removed it in 1.9!",
    )

  def test_spawn_egg(self) -> None:
    creeperSpawnEgg = MCItems.CREEPER_SPAWN_EGG
    self.assertEqual(creeperSpawnEgg[Version.V1_8_9].minecraftId,
                     'minecraft:spawn_egg:50')
    self.assertEqual(creeperSpawnEgg[Version.V1_10_2].minecraftId,
                     'minecraft:spawn_egg{EntityTag:{id:"Creeper"}}')
    self.assertEqual(creeperSpawnEgg[Version.V1_12_2].minecraftId,
                     'minecraft:spawn_egg{EntityTag:{id:"minecraft:creeper"}}')
    self.assertEqual(creeperSpawnEgg[Version.V1_13].minecraftId,
                     'minecraft:creeper_spawn_egg')

  def test_splash_potion(self) -> None:
    splashPotion = MCItems.SPLASH_POTION
    self.assertEqual(splashPotion[Version.V1_8_9].minecraftId,
                     'minecraft:potion:16384')
    self.assertEqual(splashPotion[Version.V1_9].minecraftId,
                     'minecraft:splash_potion')

  def test_latest_stack_sizes_and_slots(self) -> None:
    """26.3's, as its own generator report gives them."""
    stacks, slots = {}, {}
    for name, record in self.records.items():
      if list(record['ids'].values())[-1] and name not in GAME_NAMES:
        stack = list(record['maxStackSize'].values())[-1]
        slot = list(record['equipmentSlot'].values())[-1]
        stacks[stack] = stacks.get(stack, 0) + 1
        slots[slot] = slots.get(slot, 0) + 1
    self.assertEqual(stacks, {64: 1342, 1: 248, 16: 68})
    self.assertEqual(slots, {'mainhand': 1574, 'body': 44, 'head': 16,
                             'chest': 8, 'legs': 7, 'feet': 7, 'offhand': 1,
                             'saddle': 1})

  def test_elytra_slot_and_stack(self) -> None:
    elytra = MCItems.ELYTRA
    self.assertIs(elytra.equipmentSlot[Version.V1_9], EquipmentSlot.CHEST)
    self.assertIs(elytra.equipmentSlot[Version.V26_3], EquipmentSlot.CHEST)
    self.assertEqual(elytra.maxStackSize[Version.V1_9], 1)
    self.assertNotIn(Version.V1_8_9, elytra.equipmentSlot)

  def test_slots_that_changed(self) -> None:
    shield = MCItems.SHIELD.equipmentSlot
    self.assertIs(shield[Version.V1_9], EquipmentSlot.MAINHAND)
    self.assertIs(shield[Version.V1_10], EquipmentSlot.OFFHAND)
    pumpkin = MCItems.CARVED_PUMPKIN.equipmentSlot
    self.assertIs(pumpkin[Version.V1_12_2], EquipmentSlot.HEAD)
    self.assertIs(pumpkin[Version.V1_13], EquipmentSlot.HEAD)
    saddle = MCItems.SADDLE.equipmentSlot
    self.assertIs(saddle[Version.V1_21_4], EquipmentSlot.MAINHAND)
    self.assertIs(saddle[Version.V1_21_5], EquipmentSlot.SADDLE)
    carpet = MCItems.WHITE_CARPET.equipmentSlot
    self.assertIs(carpet[Version.V1_20_4], EquipmentSlot.MAINHAND)
    self.assertIs(carpet[Version.V1_20_5], EquipmentSlot.BODY)
    helmet = MCItems.IRON_HELMET.equipmentSlot
    for version_ in (Version.V1_7_2, Version.V1_12_2, Version.V26_3):
      self.assertIs(helmet[version_], EquipmentSlot.HEAD)

  def test_stack_sizes_that_changed(self) -> None:
    door = MCItems.OAK_DOOR.maxStackSize
    self.assertEqual(door[Version.V1_7_10], 1)
    self.assertEqual(door[Version.V1_8], 64)
    pot = MCItems.DECORATED_POT.maxStackSize
    self.assertEqual(pot[Version.V1_20_2], 1)
    self.assertEqual(pot[Version.V1_20_3], 64)
    self.assertEqual(MCItems.ENDER_PEARL.maxStackSize[Version.V1_7_10], 16)
    self.assertEqual(MCItems.POTION.maxStackSize[Version.V1_12_2], 1)

  def test_diamond(self) -> None:
    diamond = MCItems.DIAMOND
    for text in ('1.7.2', '1.12.2', '1.13', '26.3'):
      with self.subTest(version=text):
        self.assertEqual(diamond[text].minecraftId, 'minecraft:diamond')
