"""
TestMCFrogVariants tests the frog variants: the 'FrogVariantId' and
'MCFrogVariants' classes, and the 'MCFrogVariants' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import CatVariantId, FrogVariantId, GameId, MCFrogVariants
from mcdex import MCFrogVariants, MCThing, NotInVersion


class TestMCFrogVariants(BaseTest):
  """
  TestMCFrogVariants tests the frog variants.
  """

  def test_frog_variants(self) -> None:
    temperate = MCFrogVariants['temperate']
    self.assertIsInstance(temperate, MCFrogVariants)
    self.assertIsInstance(temperate, MCThing)
    self.assertEqual(temperate['1.19'],
                     FrogVariantId(
                         'temperate', 'minecraft:frog'
                                      '{variant:"minecraft:temperate"}'))
    self.assertIsInstance(temperate['26.3'], GameId)
    self.assertEqual(repr(temperate), "<MCFrogVariants>.TEMPERATE")
    self.assertEqual(len(MCFrogVariants), 3)
    self.assertNotEqual(FrogVariantId('x', 'minecraft:x'),
                        CatVariantId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = temperate['1.18.2']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.18.2 has no 'temperate'; vanilla added it in 1.19!",
    )
    with self.assertRaises(KeyError):
      _ = MCFrogVariants['temperatex']
