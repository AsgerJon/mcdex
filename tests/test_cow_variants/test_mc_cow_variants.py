"""
TestMCCowVariants tests the cow variants: the 'CowVariantId' and
'MCCowVariants' classes, and the 'MCCowVariants' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import CowVariantId, GameId, MCCowVariants, MCThing, Version
from mcdex import NotInVersion, PigVariantId


class TestMCCowVariants(BaseTest):
  """
  TestMCCowVariants tests the cow variants.
  """

  def test_cow_variants(self) -> None:
    warm = MCCowVariants.WARM
    self.assertIsInstance(warm, MCCowVariants)
    self.assertIsInstance(warm, MCThing)
    self.assertEqual(warm[Version.V1_21_5],
                     CowVariantId(
                         'warm', 'minecraft:cow{variant:"minecraft:warm"}'))
    self.assertIsInstance(warm[Version.V26_3], GameId)
    self.assertEqual(repr(warm), "<MCCowVariants>.WARM")
    self.assertEqual(len(MCCowVariants), 3)
    self.assertNotEqual(CowVariantId('x', 'minecraft:x'),
                        PigVariantId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = warm[Version.V1_21_4]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.21.4 has no 'warm'; vanilla added it in 1.21.5!",
    )
    with self.assertRaises(KeyError):
      _ = MCCowVariants['warmx']
