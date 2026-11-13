"""
TestMCBlockEntities tests the block entities: the 'BlockEntityId' and
'MCBlockEntities' classes, and the 'MCBlockEntities' catalogue with the
data it reads.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
from importlib.resources import files

from worktoy.work_test import BaseTest

from mcdex import BlockEntityId, BlockId, GameId, MCBlockEntities
from mcdex import MCBlockEntities, MCThing, NotInVersion, Version


def _records() -> dict:
  text = files('mcdex.block_entities').joinpath(
    'block_entities.json').read_text('utf-8')
  return json.loads(text)['block_entities']


class TestMCBlockEntities(BaseTest):
  """
  TestMCBlockEntities tests the block entities.
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.records = _records()

  def test_kind(self) -> None:
    chest = MCBlockEntities['chest']
    self.assertIsInstance(chest, MCBlockEntities)
    self.assertIsInstance(chest, MCThing)
    self.assertIs(type(chest['26.3']), BlockEntityId)
    self.assertIsInstance(chest['26.3'], GameId)
    self.assertEqual(repr(chest), "<MCBlockEntities>.CHEST")
    self.assertNotEqual(BlockEntityId('chest', 'minecraft:chest'),
                        BlockId('chest', 'minecraft:chest'))

  def test_catalogue(self) -> None:
    self.assertEqual(len(MCBlockEntities), len(self.records))
    with self.assertRaises(KeyError) as context:
      _ = MCBlockEntities['chst']
    self.assertIn("mcdex has no block entity named 'chst'",
                  str(context.exception))

  def test_ids_fit_their_era(self) -> None:
    """To 1.10.2 the old names, as 'Chest'; from 1.11 'minecraft:chest'."""
    for name, record in self.records.items():
      self.assertEqual(next(iter(record['ids'])), '1.7.2')
      for text, minecraftId in record['ids'].items():
        with self.subTest(name=name, version=text):
          if not minecraftId:
            continue
          if Version(text) < Version.V1_11:
            self.assertRegex(minecraftId, r'^[A-Z][A-Za-z]+$')
          else:
            self.assertRegex(minecraftId, r'^minecraft:[a-z_]+$')

  def test_latest_version(self) -> None:
    latest = [n for n, r in self.records.items()
              if list(r['ids'].values())[-1] == 'minecraft:' + n]
    self.assertEqual(len(latest), 49)

  def test_known_block_entities(self) -> None:
    self.assertEqual(MCBlockEntities['dispenser']['1.10.2'],
                     BlockEntityId('dispenser', 'Trap'))
    self.assertEqual(MCBlockEntities['dispenser']['1.11'].minecraftId,
                     'minecraft:dispenser')
    self.assertEqual(MCBlockEntities['brewing_stand']['1.7.10'].minecraftId,
                     'Cauldron')
    self.assertEqual(MCBlockEntities['brushable_block']['1.19.4'].minecraftId,
                     'minecraft:suspicious_sand')
    self.assertEqual(MCBlockEntities['brushable_block']['1.20'].minecraftId,
                     'minecraft:brushable_block')

  def test_shared_and_removed(self) -> None:
    trappedChest = MCBlockEntities['trapped_chest']
    self.assertEqual(trappedChest['1.12.2'].minecraftId, 'minecraft:chest')
    self.assertEqual(trappedChest['1.13'].minecraftId, 'minecraft:trapped_chest')
    with self.assertRaises(NotInVersion) as context:
      _ = MCBlockEntities['flower_pot']['1.13']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.13 has no 'flower_pot'; vanilla removed it in 1.13!",
    )
    with self.assertRaises(NotInVersion):
      _ = MCBlockEntities['bed']['26.2']
