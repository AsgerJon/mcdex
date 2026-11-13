"""
TestItemTables tests what the 'MCItems' catalogue knows of an item
besides its ids: its max stack size and its equipment slot in each
version, on a catalogue of test items given their records here.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee
from worktoy.waitaminute import TypeException
from worktoy.waitaminute.keenum import KeeResolveError
from worktoy.work_test import BaseTest

from mcdex import EquipmentSlot, ItemId, MCItems, Version


def _record(ids: dict, stacks: dict = (), slots: dict = ()) -> dict:
  """A record as the data file holds one, stacking 64 in the main hand."""
  first = next(v for v, i in sorted(ids.items(), key=lambda p: Version(
    p[0])) if i)
  return {'ids': ids, 'maxStackSize': dict(stacks) or {first: 64},
          'equipmentSlot': dict(slots) or {first: 'mainhand'}}


_RECORDS = {
  #  Renamed twice, present in every version of the data.
  'test_tuft': _record({'1.20.3': 'test:short_tuft', '1.7.2': 'test:tallgrass:1',
                   '1.13': 'test:tuft'}),
  #  Added after the data begins; equipped and stacked like an elytra.
  'test_gadget': _record({'1.7.2': '', '1.9': 'test:gadget'}, {'1.9': 1},
                    {'1.9': 'mainhand', '1.10': 'chest'}),
  #  Removed before 26.3; stacked to 1 until 1.8.
  'test_relic': _record({'1.7.2': 'test:relic', '1.9': ''},
                   {'1.7.2': 1, '1.8': 64}),
  #  An id with NBT in some versions.
  'test_egg': _record({'1.7.2': 'test:egg:50',
                  '1.9': 'test:egg{EntityTag:{id:"Creeper"}}',
                  '1.13': 'test:egg'}),
  'test_lacking_stacks': {'ids': {'1.7.2': 'test:x'},
                     'equipmentSlot': {'1.7.2': 'mainhand'}},
  'test_lacking_slots': {'ids': {'1.7.2': 'test:x'},
                    'maxStackSize': {'1.7.2': 64}},
  'test_unsized_text': _record({'1.7.2': 'test:x'}, {'1.7.2': '64'}),
  'test_unsized_float': _record({'1.7.2': 'test:x'}, {'1.7.2': 64.0}),
  'test_oversized_zero': _record({'1.7.2': 'test:x'}, {'1.7.2': 0}),
  'test_oversized_hundred': _record({'1.7.2': 'test:x'}, {'1.7.2': 100}),
  'test_unslotted': _record({'1.7.2': 'test:x'}, (), {'1.7.2': 'torso'}),
  'test_patchy': _record({'1.7.2': 'test:x'}, {'1.8': 64}),
}


class TrialItems(MCItems):
  """A catalogue of test items, its records given here."""

  __data_records__ = _RECORDS

  TEST_TUFT = Kee[str]('test_tuft')
  TEST_GADGET = Kee[str]('test_gadget')
  TEST_RELIC = Kee[str]('test_relic')
  TEST_EGG = Kee[str]('test_egg')
  TEST_LACKING_STACKS = Kee[str]('test_lacking_stacks')
  TEST_LACKING_SLOTS = Kee[str]('test_lacking_slots')
  TEST_UNSIZED_TEXT = Kee[str]('test_unsized_text')
  TEST_UNSIZED_FLOAT = Kee[str]('test_unsized_float')
  TEST_OVERSIZED_ZERO = Kee[str]('test_oversized_zero')
  TEST_OVERSIZED_HUNDRED = Kee[str]('test_oversized_hundred')
  TEST_UNSLOTTED = Kee[str]('test_unslotted')
  TEST_PATCHY = Kee[str]('test_patchy')


class TestItemTables(BaseTest):
  """
  TestItemTables tests the stack sizes and slots of 'MCItems'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE RECORD   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_record_lacks_a_table(self) -> None:
    for item, table in ((TrialItems.TEST_LACKING_STACKS, 'maxStackSize'),
                        (TrialItems.TEST_LACKING_SLOTS, 'equipmentSlot')):
      with self.subTest(table=table):
        with self.assertRaises(ValueError) as context:
          _ = item[Version.V1_7_2]
        self.assertIn("TrialItems('%s') received no '%s'" % (
          item.uniqueName, table), str(context.exception))

  def test_stack_size_not_int(self) -> None:
    for item in (TrialItems.TEST_UNSIZED_TEXT, TrialItems.TEST_UNSIZED_FLOAT):
      with self.subTest(item=item):
        with self.assertRaises(TypeException):
          _ = item.maxStackSize

  def test_stack_size_out_of_bounds(self) -> None:
    for item in (TrialItems.TEST_OVERSIZED_ZERO, TrialItems.TEST_OVERSIZED_HUNDRED):
      with self.subTest(item=item):
        with self.assertRaises(ValueError) as context:
          _ = item.maxStackSize
        self.assertIn('must be from 1 to 99', str(context.exception))

  def test_unknown_slot(self) -> None:
    with self.assertRaises(KeeResolveError):
      _ = TrialItems.TEST_UNSLOTTED.equipmentSlot

  def test_stack_size_missing_for_a_version(self) -> None:
    with self.assertRaises(ValueError) as context:
      _ = TrialItems.TEST_PATCHY.maxStackSize
    self.assertIn("TrialItems('test_patchy') has no 'maxStackSize' for 1.7.2",
                  str(context.exception))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STACK SIZE AND SLOT  # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_max_stack_size_versions(self) -> None:
    """A key for every version vanilla has the item in."""
    present = [v for v in Version if Version.V1_9 <= v]
    self.assertEqual(list(TrialItems.TEST_GADGET.maxStackSize), present)
    gone = [v for v in Version if Version.V1_7_2 <= v < Version.V1_9]
    self.assertEqual(list(TrialItems.TEST_RELIC.maxStackSize), gone)

  def test_max_stack_size_values(self) -> None:
    sizes = TrialItems.TEST_RELIC.maxStackSize
    self.assertEqual(sizes[Version.V1_7_10], 1)
    self.assertEqual(sizes[Version.V1_8], 64)
    self.assertEqual(sizes[Version.V1_8_9], 64)
    self.assertEqual(set(TrialItems.TEST_TUFT.maxStackSize.values()), {64})

  def test_equipment_slot(self) -> None:
    slots = TrialItems.TEST_GADGET.equipmentSlot
    self.assertEqual(list(slots), [v for v in Version if Version.V1_9 <= v])
    self.assertIs(slots[Version.V1_9], EquipmentSlot.MAINHAND)
    self.assertIs(slots[Version.V1_10], EquipmentSlot.CHEST)
    self.assertIs(slots[Version.V26_3], EquipmentSlot.CHEST)

  def test_stack_and_slot_are_copies(self) -> None:
    gadget = TrialItems.TEST_GADGET
    sizes, slots = gadget.maxStackSize, gadget.equipmentSlot
    sizes[Version.V26_3] = 99
    slots[Version.V26_3] = EquipmentSlot.HEAD
    self.assertEqual(gadget.maxStackSize[Version.V26_3], 1)
    self.assertIs(gadget.equipmentSlot[Version.V26_3], EquipmentSlot.CHEST)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  IDS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_getitem(self) -> None:
    cases = {
      Version.V1_7_2: 'test:tallgrass:1',
      Version.V1_12_2: 'test:tallgrass:1',
      Version.V1_13: 'test:tuft',
      Version.V1_20_3: 'test:short_tuft',
    }
    for version_, minecraftId in cases.items():
      with self.subTest(version=version_.name):
        self.assertEqual(TrialItems.TEST_TUFT[version_],
                         ItemId('test_tuft', minecraftId))

  def test_version_ids(self) -> None:
    ids = TrialItems.TEST_GADGET.versionIds
    self.assertEqual(ids[Version.V1_8_9], '')
    self.assertEqual(ids[Version.V1_9], 'test:gadget')

  def test_nbt_id(self) -> None:
    egg = TrialItems.TEST_EGG
    self.assertEqual(egg[Version.V1_12_2].minecraftId,
                     'test:egg{EntityTag:{id:"Creeper"}}')
    self.assertEqual(egg[Version.V1_8_9].minecraftId, 'test:egg:50')
    self.assertEqual(egg[Version.V1_13].minecraftId, 'test:egg')
