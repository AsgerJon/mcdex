"""
TestMCDamageTypes tests the damage types: the 'DamageTypeId' and 'MCDamageTypes'
classes, and the 'MCDamageTypes' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import BiomeId, DamageTypeId, GameId, MCDamageTypes
from mcdex import MCThing, NotInVersion


class TestMCDamageTypes(BaseTest):
  """
  TestMCDamageTypes tests the damage types.
  """

  def test_damage_types(self) -> None:
    inFire = MCDamageTypes['in_fire']
    self.assertIsInstance(inFire, MCDamageTypes)
    self.assertIsInstance(inFire, MCThing)
    self.assertEqual(inFire['1.19.4'],
                     DamageTypeId('in_fire', 'minecraft:in_fire'))
    self.assertIsInstance(inFire['26.3'], GameId)
    self.assertEqual(repr(inFire), "<MCDamageTypes>.IN_FIRE")
    self.assertEqual(len(MCDamageTypes), 51)
    self.assertNotEqual(DamageTypeId('x', 'minecraft:x'),
                        BiomeId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = inFire['1.19.3']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.19.3 has no 'in_fire'; vanilla added it in 1.19.4!",
    )
    with self.assertRaises(KeyError):
      _ = MCDamageTypes['in_firex']

  def test_added_later(self) -> None:
    maceSmash = MCDamageTypes['mace_smash']
    self.assertEqual(maceSmash['1.21.2'].minecraftId, 'minecraft:mace_smash')
    with self.assertRaises(NotInVersion):
      _ = maceSmash['1.21.1']
