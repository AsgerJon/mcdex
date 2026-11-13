"""
TestMCChickenVariants tests the chicken variants: the 'ChickenVariantId' and
'MCChickenVariants' classes, and the 'MCChickenVariants' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import ChickenVariantId, CowVariantId, GameId, MCChickenVariants
from mcdex import MCChickenVariants, MCThing, NotInVersion


class TestMCChickenVariants(BaseTest):
  """
  TestMCChickenVariants tests the chicken variants.
  """

  def test_chicken_variants(self) -> None:
    cold = MCChickenVariants['cold']
    self.assertIsInstance(cold, MCChickenVariants)
    self.assertIsInstance(cold, MCThing)
    self.assertEqual(cold['1.21.5'],
                     ChickenVariantId(
                         'cold', 'minecraft:chicken'
                                 '{variant:"minecraft:cold"}'))
    self.assertIsInstance(cold['26.3'], GameId)
    self.assertEqual(repr(cold), "<MCChickenVariants>.COLD")
    self.assertEqual(len(MCChickenVariants), 3)
    self.assertNotEqual(ChickenVariantId('x', 'minecraft:x'),
                        CowVariantId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = cold['1.21.4']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.21.4 has no 'cold'; vanilla added it in 1.21.5!",
    )
    with self.assertRaises(KeyError):
      _ = MCChickenVariants['coldx']
