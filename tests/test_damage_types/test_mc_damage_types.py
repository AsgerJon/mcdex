"""
TestMCDamageTypes tests the damage types: the 'DamageTypeId' and 'MCDamageTypes'
classes, and the 'MCDamageTypes' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import BiomeId, DamageTypeId, GameId, MCDamageTypes, Version
from mcdex import MCThing, NotInVersion


class TestMCDamageTypes(BaseTest):
  """
  TestMCDamageTypes tests the damage types.
  """

  def test_damage_types(self) -> None:
    inFire = MCDamageTypes.IN_FIRE
    self.assertIsInstance(inFire, MCDamageTypes)
    self.assertIsInstance(inFire, MCThing)
    self.assertEqual(inFire[Version.V1_19_4],
                     DamageTypeId('in_fire', 'minecraft:in_fire'))
    self.assertIsInstance(inFire[Version.V26_3], GameId)
    self.assertEqual(repr(inFire), "<MCDamageTypes>.IN_FIRE")
    self.assertEqual(len(MCDamageTypes), 51)
    self.assertNotEqual(DamageTypeId('x', 'minecraft:x'),
                        BiomeId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = inFire[Version.V1_19_3]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.19.3 has no 'in_fire'; vanilla added it in 1.19.4!",
    )
    with self.assertRaises(KeyError):
      _ = MCDamageTypes['in_firex']

  def test_added_later(self) -> None:
    maceSmash = MCDamageTypes.MACE_SMASH
    self.assertEqual(maceSmash[Version.V1_21_2].minecraftId,
                     'minecraft:mace_smash')
    with self.assertRaises(NotInVersion):
      _ = maceSmash[Version.V1_21_1]
