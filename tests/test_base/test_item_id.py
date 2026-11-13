"""
TestItemId tests the 'ItemId' class: an item's unique name, and the id a
version of the game needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.waitaminute.desc import WriteOnceError
from worktoy.work_test import BaseTest

from mcdex import GameId, ItemId


class TestItemId(BaseTest):
  """
  TestItemId tests the 'ItemId' class.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_fields(self) -> None:
    cases = (
      ('pink_wool', '35:6'),
      ('pink_wool', 'minecraft:wool:6'),
      ('pink_wool', 'minecraft:pink_wool'),
      ('diamond', '264'),
    )
    for uniqueName, minecraftId in cases:
      with self.subTest(minecraftId=minecraftId):
        id_ = ItemId(uniqueName, minecraftId)
        self.assertIsInstance(id_, GameId)
        self.assertEqual(id_.uniqueName, uniqueName)
        self.assertEqual(id_.minecraftId, minecraftId)

  def test_empty(self) -> None:
    cases = {
      ('', 'minecraft:wool:6'): "ItemId() received an empty 'uniqueName'",
      ('pink_wool', ''): "ItemId() received an empty 'minecraftId'",
    }
    for args, message in cases.items():
      with self.subTest(args=args):
        with self.assertRaises(ValueError) as context:
          ItemId(*args)
        self.assertIn(message, str(context.exception))

  def test_wrong_arguments(self) -> None:
    for args in (('pink_wool',), (), ('a', 'b', 'c')):
      with self.subTest(args=args):
        with self.assertRaises(TypeError):
          ItemId(*args)

  def test_write_once(self) -> None:
    id_ = ItemId('pink_wool', 'minecraft:wool:6')
    with self.assertRaises(WriteOnceError):
      id_.uniqueName = 'red_wool'
    with self.assertRaises(WriteOnceError):
      id_.minecraftId = 'minecraft:wool:14'

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TEXT   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_str_is_minecraft_id(self) -> None:
    self.assertEqual(str(ItemId('pink_wool', 'minecraft:wool:6')),
                     'minecraft:wool:6')
    self.assertEqual(str(ItemId('diamond', '264')), '264')

  def test_repr(self) -> None:
    self.assertEqual(repr(ItemId('pink_wool', 'minecraft:wool:6')),
                     "ItemId('pink_wool', 'minecraft:wool:6')")

  def test_repr_round_trip(self) -> None:
    for id_ in (ItemId('pink_wool', '35:6'), ItemId('diamond', '264'),
                ItemId('elytra', 'minecraft:elytra')):
      with self.subTest(id_=id_):
        self.assertEqual(eval(repr(id_)), id_)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  EQUALITY AND HASH  # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_equal(self) -> None:
    self.assertEqual(ItemId('pink_wool', 'minecraft:wool:6'),
                     ItemId('pink_wool', 'minecraft:wool:6'))

  def test_not_equal(self) -> None:
    base = ItemId('pink_wool', 'minecraft:wool:6')
    for other in (ItemId('red_wool', 'minecraft:wool:6'),
                  ItemId('pink_wool', 'minecraft:wool:14'),
                  ItemId('pink_wool', 'minecraft:pink_wool')):
      with self.subTest(other=other):
        self.assertNotEqual(base, other)
        self.assertTrue(base != other)

  def test_equal_other_type(self) -> None:
    id_ = ItemId('pink_wool', 'minecraft:wool:6')
    for other in ('minecraft:wool:6', ('pink_wool', 'minecraft:wool:6'),
                  None):
      with self.subTest(other=other):
        self.assertFalse(id_ == other)
        self.assertIs(id_.__eq__(other), NotImplemented)

  def test_hash(self) -> None:
    table = {ItemId('pink_wool', 'minecraft:wool:6'): 'pink'}
    self.assertEqual(table[ItemId('pink_wool', 'minecraft:wool:6')], 'pink')
    self.assertNotIn(ItemId('pink_wool', 'minecraft:pink_wool'), table)
    self.assertNotIn(ItemId('red_wool', 'minecraft:wool:6'), table)
