"""
TestMCPigVariants tests the pig variants: the 'PigVariantId' and
'MCPigVariants' classes, and the 'MCPigVariants' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import FrogVariantId, GameId, MCPigVariants, MCThing, Version
from mcdex import NotInVersion, PigVariantId


class TestMCPigVariants(BaseTest):
  """
  TestMCPigVariants tests the pig variants.
  """

  def test_pig_variants(self) -> None:
    temperate = MCPigVariants.TEMPERATE
    self.assertIsInstance(temperate, MCPigVariants)
    self.assertIsInstance(temperate, MCThing)
    self.assertEqual(temperate[Version.V1_21_5],
                     PigVariantId(
                         'temperate', 'minecraft:pig'
                                      '{variant:"minecraft:temperate"}'))
    self.assertIsInstance(temperate[Version.V26_3], GameId)
    self.assertEqual(repr(temperate), "<MCPigVariants>.TEMPERATE")
    self.assertEqual(len(MCPigVariants), 3)
    self.assertNotEqual(PigVariantId('x', 'minecraft:x'),
                        FrogVariantId('x', 'minecraft:x'))
    self.assertEqual(temperate[Version.V1_21_4].minecraftId, 'minecraft:pig')
    self.assertEqual(temperate[Version.V1_7_10].minecraftId, 'Pig')
    with self.assertRaises(NotInVersion) as context:
      _ = MCPigVariants.WARM[Version.V1_21_4]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.21.4 has no 'warm'; vanilla added it in 1.21.5!",
    )
    with self.assertRaises(KeyError):
      _ = MCPigVariants['temperatex']
