"""
TestBlockId tests the 'BlockId' class: a block's unique name, and the id
a version of the game needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.waitaminute.desc import WriteOnceError
from worktoy.work_test import BaseTest

from mcdex import BlockId, EntityId, GameId, ItemId


class TestBlockId(BaseTest):
  """
  TestBlockId tests the 'BlockId' class.
  """

  def test_fields(self) -> None:
    for uniqueName, minecraftId in (
        ('pink_wool', 'minecraft:wool:6'),
        ('pink_wool', 'minecraft:pink_wool'),
        ('creeper_head', 'minecraft:skull:1{SkullType:4b}'),
        ('water_cauldron', 'minecraft:cauldron[level=1]')):
      with self.subTest(minecraftId=minecraftId):
        id_ = BlockId(uniqueName, minecraftId)
        self.assertIsInstance(id_, GameId)
        self.assertEqual(id_.uniqueName, uniqueName)
        self.assertEqual(id_.minecraftId, minecraftId)

  def test_empty(self) -> None:
    cases = {
      ('', 'minecraft:stone'): "BlockId() received an empty 'uniqueName'",
      ('stone', ''): "BlockId() received an empty 'minecraftId'",
    }
    for args, message in cases.items():
      with self.subTest(args=args):
        with self.assertRaises(ValueError) as context:
          BlockId(*args)
        self.assertIn(message, str(context.exception))

  def test_wrong_arguments(self) -> None:
    for args in (('stone',), (), ('a', 'b', 'c'), ('stone', 1)):
      with self.subTest(args=args):
        with self.assertRaises(TypeError):
          BlockId(*args)

  def test_write_once(self) -> None:
    id_ = BlockId('stone', 'minecraft:stone')
    with self.assertRaises(WriteOnceError):
      id_.minecraftId = 'minecraft:granite'

  def test_text(self) -> None:
    id_ = BlockId('pink_wool', 'minecraft:wool:6')
    self.assertEqual(str(id_), 'minecraft:wool:6')
    self.assertEqual(repr(id_), "BlockId('pink_wool', 'minecraft:wool:6')")
    self.assertEqual(eval(repr(id_)), id_)

  def test_equal_and_hash(self) -> None:
    id_ = BlockId('stone', 'minecraft:stone')
    self.assertEqual(id_, BlockId('stone', 'minecraft:stone'))
    self.assertNotEqual(id_, BlockId('stone', 'minecraft:granite'))
    self.assertEqual({id_: 1}[BlockId('stone', 'minecraft:stone')], 1)

  def test_not_another_kind(self) -> None:
    """A block's id is never an item's or an entity's, with the same text."""
    block = BlockId('tnt', 'minecraft:tnt')
    for other in (ItemId('tnt', 'minecraft:tnt'),
                  EntityId('tnt', 'minecraft:tnt'), 'minecraft:tnt', None):
      with self.subTest(other=other):
        self.assertFalse(block == other)
        self.assertIs(block.__eq__(other), NotImplemented)
    self.assertNotEqual(hash(block), hash(EntityId('tnt', 'minecraft:tnt')))
