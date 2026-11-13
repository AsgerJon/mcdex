"""
TestEntityId tests the 'EntityId' class: an entity's unique name, and the
id a version of the game needs to identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.waitaminute.desc import WriteOnceError
from worktoy.work_test import BaseTest

from mcdex import EntityId, ItemId


class TestEntityId(BaseTest):
  """
  TestEntityId tests the 'EntityId' class.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_fields(self) -> None:
    cases = (
      ('creeper', 'Creeper'),
      ('creeper', 'minecraft:creeper'),
      ('wither_skeleton', 'Skeleton{SkeletonType:1}'),
      ('spruce_boat', 'minecraft:boat{Type:"spruce"}'),
    )
    for uniqueName, minecraftId in cases:
      with self.subTest(minecraftId=minecraftId):
        id_ = EntityId(uniqueName, minecraftId)
        self.assertEqual(id_.uniqueName, uniqueName)
        self.assertEqual(id_.minecraftId, minecraftId)

  def test_empty(self) -> None:
    cases = {
      ('', 'Creeper'): "EntityId() received an empty 'uniqueName'",
      ('creeper', ''): "EntityId() received an empty 'minecraftId'",
    }
    for args, message in cases.items():
      with self.subTest(args=args):
        with self.assertRaises(ValueError) as context:
          EntityId(*args)
        self.assertIn(message, str(context.exception))

  def test_wrong_arguments(self) -> None:
    for args in (('creeper',), (), ('a', 'b', 'c'), ('creeper', 50)):
      with self.subTest(args=args):
        with self.assertRaises(TypeError):
          EntityId(*args)

  def test_write_once(self) -> None:
    id_ = EntityId('creeper', 'Creeper')
    with self.assertRaises(WriteOnceError):
      id_.uniqueName = 'skeleton'
    with self.assertRaises(WriteOnceError):
      id_.minecraftId = 'Skeleton'

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TEXT   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_str_is_minecraft_id(self) -> None:
    self.assertEqual(str(EntityId('creeper', 'Creeper')), 'Creeper')
    self.assertEqual(
        str(EntityId('wither_skeleton', 'Skeleton{SkeletonType:1}')),
        'Skeleton{SkeletonType:1}',
    )

  def test_repr(self) -> None:
    self.assertEqual(repr(EntityId('creeper', 'minecraft:creeper')),
                     "EntityId('creeper', 'minecraft:creeper')")

  def test_repr_round_trip(self) -> None:
    for id_ in (EntityId('creeper', 'Creeper'),
                EntityId('spruce_boat', 'minecraft:boat{Type:"spruce"}')):
      with self.subTest(id_=id_):
        self.assertEqual(eval(repr(id_)), id_)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  EQUALITY AND HASH  # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_equal(self) -> None:
    self.assertEqual(EntityId('creeper', 'Creeper'),
                     EntityId('creeper', 'Creeper'))

  def test_not_equal(self) -> None:
    base = EntityId('creeper', 'Creeper')
    for other in (EntityId('skeleton', 'Creeper'),
                  EntityId('creeper', 'minecraft:creeper')):
      with self.subTest(other=other):
        self.assertNotEqual(base, other)
        self.assertTrue(base != other)

  def test_not_an_item_id(self) -> None:
    """An entity's id is never an item's, even with the same text."""
    entity = EntityId('pig', 'minecraft:pig')
    item = ItemId('pig', 'minecraft:pig')
    self.assertFalse(entity == item)
    self.assertFalse(item == entity)
    self.assertIs(entity.__eq__(item), NotImplemented)

  def test_equal_other_type(self) -> None:
    id_ = EntityId('creeper', 'Creeper')
    for other in ('Creeper', ('creeper', 'Creeper'), None):
      with self.subTest(other=other):
        self.assertFalse(id_ == other)
        self.assertIs(id_.__eq__(other), NotImplemented)

  def test_hash(self) -> None:
    table = {EntityId('creeper', 'Creeper'): 'boom'}
    self.assertEqual(table[EntityId('creeper', 'Creeper')], 'boom')
    self.assertNotIn(EntityId('creeper', 'minecraft:creeper'), table)
