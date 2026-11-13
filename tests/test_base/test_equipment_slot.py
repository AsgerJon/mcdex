"""
TestEquipmentSlot tests the 'EquipmentSlot' enumeration.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.waitaminute.keenum import KeeResolveError
from worktoy.work_test import BaseTest

from mcdex import EquipmentSlot


class TestEquipmentSlot(BaseTest):
  """
  TestEquipmentSlot tests the 'EquipmentSlot' enumeration.
  """

  def test_members(self) -> None:
    self.assertEqual(
        [member.name for member in EquipmentSlot],
        ['MAINHAND', 'OFFHAND', 'FEET', 'LEGS', 'CHEST', 'HEAD', 'BODY',
         'SADDLE'],
    )

  def test_values_are_game_names(self) -> None:
    for member in EquipmentSlot:
      with self.subTest(member=member.name):
        self.assertEqual(member.value, member.name.lower())

  def test_from_game_name(self) -> None:
    for text in ('mainhand', 'offhand', 'feet', 'legs', 'chest', 'head',
                 'body', 'saddle'):
      with self.subTest(text=text):
        self.assertEqual(EquipmentSlot(text).value, text)
    self.assertIs(EquipmentSlot('chest'), EquipmentSlot.CHEST)

  def test_unresolvable(self) -> None:
    for text in ('', 'hand', 'torso', 'helmet', 'armor'):
      with self.subTest(text=text):
        with self.assertRaises(KeeResolveError):
          EquipmentSlot(text)
