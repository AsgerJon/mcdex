"""
TestWorktoyWarnings guarantees that mcdex builds only on what worktoy
promises. worktoy gives a warning, a 'WorkToyWarning', where a project
uses what it no longer promises, as the 'DeprecatedPromise' of the
'index' of a member since worktoy 1.2.0. Here every such warning is an
error, and each test reads catalogues of its own, so no table another
test has read and kept hides a read.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import warnings

from worktoy.keenum import Kee
from worktoy.waitaminute import WorkToyWarning
from worktoy.work_test import BaseTest

from mcdex import EntityId, EquipmentSlot, MCItems, MCPotions, MCThing
from mcdex import NotInVersion, PotionModifier, Version


class Wisps(MCThing):
  """A catalogue of test things, its records given here."""

  __data_records__ = {
    'wisp': {'ids': {'1.7.2': 'Wisp', '1.11': 'test:wisp'}},
  }
  __id_class__ = EntityId
  __kind__ = 'wisp'

  WISP = Kee[str]('wisp')


class Trinkets(MCItems):
  """A catalogue of test items, its records given here."""

  __data_records__ = {
    'test_trinket': {
      'ids': {'1.7.2': '', '1.9': 'test:trinket'},
      'maxStackSize': {'1.9': 1},
      'equipmentSlot': {'1.9': 'mainhand', '1.10': 'chest'},
    },
  }

  TEST_TRINKET = Kee[str]('test_trinket')


class TestWorktoyWarnings(BaseTest):
  """
  Reading a thing, the tables of an item and a potion with a modifier
  gives no warning of worktoy's.
  """

  def test_thing(self) -> None:
    """The ids of a thing, read and looked up, and a version before them."""
    with warnings.catch_warnings():
      warnings.simplefilter('error', WorkToyWarning)
      wisp = Wisps.WISP
      self.assertEqual(wisp[Version.V1_10_2].minecraftId, 'Wisp')
      self.assertEqual(wisp[Version.V26_3].minecraftId, 'test:wisp')
      self.assertEqual(wisp.versionIds[Version.V1_11], 'test:wisp')
      with self.assertRaises(ValueError):
        _ = wisp[Version.V1_6_4]

  def test_item_tables(self) -> None:
    """The stack sizes and slots of an item, read and looked up."""
    with warnings.catch_warnings():
      warnings.simplefilter('error', WorkToyWarning)
      testTrinket = Trinkets.TEST_TRINKET
      self.assertEqual(testTrinket[Version.V1_9].minecraftId, 'test:trinket')
      self.assertEqual(testTrinket.maxStackSize[Version.V1_9], 1)
      self.assertIs(testTrinket.equipmentSlot[Version.V1_10],
                    EquipmentSlot.CHEST)
      with self.assertRaises(NotInVersion):
        _ = testTrinket[Version.V1_8_9]

  def test_modified_potion(self) -> None:
    """A potion with a modifier, looked up, and a version before it."""
    with warnings.catch_warnings():
      warnings.simplefilter('error', WorkToyWarning)
      longNightVision = MCPotions[
          MCPotions.NIGHT_VISION, PotionModifier.LONG]
      self.assertEqual(longNightVision[Version.V1_8_9].minecraftId, '70')
      with self.assertRaises(ValueError):
        _ = longNightVision[Version.V1_6_4]
