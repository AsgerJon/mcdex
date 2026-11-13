"""
TestMCBlocks tests the 'MCBlocks' catalogue: the blocks it hands out,
and what every block of its data must satisfy, however many there are.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import re
from importlib.resources import files

from worktoy.waitaminute.keenum import KeeResolveError
from worktoy.work_test import BaseTest

from mcdex import BlockId, MCBlocks, MCEntities, MCItems
from mcdex import NotInVersion, Version


def _records() -> dict:
  """The data file, read directly, to compare the catalogue against."""
  text = files('mcdex.blocks').joinpath('blocks.json').read_text('utf-8')
  return json.loads(text)['blocks']


class TestMCBlocks(BaseTest):
  """
  TestMCBlocks tests the 'MCBlocks' catalogue.
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.records = _records()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  LOOKUP   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_getitem(self) -> None:
    pinkWool = MCBlocks['pink_wool']
    self.assertIsInstance(pinkWool, MCBlocks)
    self.assertIs(MCBlocks['pink_wool'], pinkWool)

  def test_getitem_unknown(self) -> None:
    with self.assertRaises(KeyError) as context:
      _ = MCBlocks['pink_wol']
    self.assertIn("mcdex has no block named 'pink_wol'",
                  str(context.exception))

  def test_getitem_by_position(self) -> None:
    """An 'int' is a position, as in any enumeration."""
    self.assertIs(MCBlocks[35], list(MCBlocks)[35])

  def test_getitem_not_a_name(self) -> None:
    for name in (Version.V1_9, ('stone',)):
      with self.subTest(name=name):
        with self.assertRaises(KeeResolveError):
          _ = MCBlocks[name]

  def test_len_iter_contains(self) -> None:
    self.assertEqual(len(MCBlocks), len(self.records))
    blocks = list(MCBlocks)
    self.assertEqual([b.uniqueName for b in blocks], list(self.records))
    self.assertIn('stone', MCBlocks)
    self.assertIn(MCBlocks['stone'], MCBlocks)
    self.assertNotIn('ston', MCBlocks)
    self.assertNotIn(1, MCBlocks)

  def test_kinds_are_apart(self) -> None:
    """A block, an item and an entity of one name are three things."""
    self.assertNotIn(MCItems['tnt'], MCBlocks)
    self.assertNotIn(MCEntities['tnt'], MCBlocks)
    self.assertNotIn(MCBlocks['tnt'], MCEntities)
    self.assertNotEqual(MCBlocks['tnt']['26.3'], MCEntities['tnt']['26.3'])

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE DATA   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_names_are_lowercase_words(self) -> None:
    for name in self.records:
      with self.subTest(name=name):
        self.assertRegex(name, r'^[a-z0-9]+(_[a-z0-9]+)*$')

  def test_records_begin_together(self) -> None:
    for name, record in self.records.items():
      with self.subTest(name=name):
        self.assertEqual(list(record), ['ids'])
        self.assertEqual(next(iter(record['ids'])), '1.7.2')

  def test_ids_fit_their_era(self) -> None:
    """
    Before 1.13 a name, its meta where it tells blocks apart, and the
    block entity data where that did; from 1.13 a name, until 1.17 with
    the cauldron's level where that made the water cauldron.
    """
    old = re.compile(r'minecraft:[a-z0-9_]+(:[0-9]+)?(\{.+\})?')
    state = re.compile(r'minecraft:[a-z0-9_]+(\[[a-z_]+=[a-z0-9_]+\])?')
    flat = re.compile(r'minecraft:[a-z0-9_]+')
    for name, record in self.records.items():
      for text, minecraftId in record['ids'].items():
        with self.subTest(name=name, version=text):
          if not minecraftId:
            continue
          if Version(text) < Version.V1_13:
            self.assertIsNotNone(old.fullmatch(minecraftId))
          elif Version(text) < Version.V1_17:
            self.assertIsNotNone(state.fullmatch(minecraftId))
          else:
            self.assertIsNotNone(flat.fullmatch(minecraftId))

  def test_latest_version(self) -> None:
    """26.3 has 1,286 blocks; the short grass has two names."""
    latest = {}
    for name, record in self.records.items():
      id_ = list(record['ids'].values())[-1]
      if id_:
        latest.setdefault(id_, []).append(name)
    self.assertEqual(len(latest), 1286)
    self.assertEqual(latest['minecraft:short_grass'], ['grass', 'short_grass'])
    for id_, names in latest.items():
      with self.subTest(id_=id_):
        self.assertIn(id_.split(':', 1)[1], names)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  KNOWN BLOCKS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _ids(self, cases: dict) -> None:
    for (name, text), minecraftId in cases.items():
      with self.subTest(name=name, version=text):
        self.assertEqual(MCBlocks[name][text], BlockId(name, minecraftId))

  def test_flattened(self) -> None:
    self._ids({
      ('pink_wool', '1.12.2'): 'minecraft:wool:6',
      ('pink_wool', '1.13'): 'minecraft:pink_wool',
      ('oak_log', '1.12.2'): 'minecraft:log:0',
      ('oak_wood', '1.12.2'): 'minecraft:log:12',
      ('oak_stairs', '1.12.2'): 'minecraft:oak_stairs',
      ('torch', '1.12.2'): 'minecraft:torch:5',
      ('wall_torch', '1.12.2'): 'minecraft:torch:1',
      ('nether_portal', '1.12.2'): 'minecraft:portal',
      ('grass_block', '1.12.2'): 'minecraft:grass',
      ('dead_bush', '1.12.2'): 'minecraft:deadbush',
      ('furnace', '1.12.2'): 'minecraft:furnace',
      ('water', '1.12.2'): 'minecraft:water',
    })

  def test_variants_by_version(self) -> None:
    self.assertEqual(MCBlocks['stone']['1.7.10'].minecraftId,
                     'minecraft:stone')
    self.assertEqual(MCBlocks['stone']['1.8'].minecraftId, 'minecraft:stone:0')
    self.assertEqual(MCBlocks['granite']['1.8'].minecraftId,
                     'minecraft:stone:1')
    with self.assertRaises(NotInVersion) as context:
      _ = MCBlocks['granite']['1.7.10']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.7.10 has no 'granite'; vanilla added it in 1.8!",
    )

  def test_block_entity_variants(self) -> None:
    self._ids({
      ('creeper_head', '1.12.2'): 'minecraft:skull:1{SkullType:4b}',
      ('creeper_wall_head', '1.12.2'): 'minecraft:skull:2{SkullType:4b}',
      ('skeleton_skull', '1.12.2'): 'minecraft:skull:1{SkullType:0b}',
      ('dragon_head', '1.9'): 'minecraft:skull:1{SkullType:5b}',
      ('red_bed', '1.11.2'): 'minecraft:bed',
      ('red_bed', '1.12'): 'minecraft:bed{color:14}',
      ('white_bed', '1.12'): 'minecraft:bed{color:0}',
      ('white_banner', '1.8'): 'minecraft:standing_banner{Base:15}',
      ('black_banner', '1.12.2'): 'minecraft:standing_banner{Base:0}',
      ('orange_wall_banner', '1.12.2'): 'minecraft:wall_banner{Base:14}',
      ('flower_pot', '1.12.2'): 'minecraft:flower_pot',
      ('potted_poppy', '1.7.10'): 'minecraft:flower_pot{Item:38,Data:0}',
      ('potted_poppy', '1.8'):
        'minecraft:flower_pot{Item:"minecraft:red_flower",Data:0}',
    })
    with self.assertRaises(NotInVersion):
      _ = MCBlocks['dragon_head']['1.8.9']
    with self.assertRaises(NotInVersion):
      _ = MCBlocks['white_bed']['1.11.2']

  def test_renamed_and_split(self) -> None:
    self._ids({
      ('water_cauldron', '1.12.2'): 'minecraft:cauldron:1',
      ('water_cauldron', '1.16.5'): 'minecraft:cauldron[level=1]',
      ('water_cauldron', '1.17'): 'minecraft:water_cauldron',
      ('cauldron', '1.16.5'): 'minecraft:cauldron',
      ('dirt_path', '1.16.5'): 'minecraft:grass_path',
      ('dirt_path', '1.17'): 'minecraft:dirt_path',
      ('oak_sign', '1.13'): 'minecraft:sign',
      ('oak_sign', '1.14'): 'minecraft:oak_sign',
      ('iron_chain', '1.21.8'): 'minecraft:chain',
      ('grass', '1.12.2'): 'minecraft:tallgrass:1',
      ('grass', '1.20.2'): 'minecraft:grass',
      ('short_grass', '1.20.3'): 'minecraft:short_grass',
    })

  def test_old_id_of_two_blocks(self) -> None:
    """The old block was both, as for the items."""
    self._ids({
      ('pumpkin', '1.12.2'): 'minecraft:pumpkin',
      ('carved_pumpkin', '1.12.2'): 'minecraft:pumpkin',
      ('shulker_box', '1.12.2'): 'minecraft:purple_shulker_box',
      ('purple_shulker_box', '1.12.2'): 'minecraft:purple_shulker_box',
      ('smooth_stone_slab', '1.13'): 'minecraft:stone_slab',
      ('stone_slab', '1.13'): 'minecraft:stone_slab',
    })
