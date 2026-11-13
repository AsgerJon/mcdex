"""
TestMCChickenSoundVariants tests the chicken sound variants: the
'ChickenSoundVariantId' and 'MCChickenSoundVariants' classes, and the
'MCChickenSoundVariants' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import ChickenSoundVariantId, ChickenVariantId, GameId, Version
from mcdex import MCChickenSoundVariants, MCThing
from mcdex import NotInVersion


class TestMCChickenSoundVariants(BaseTest):
  """
  TestMCChickenSoundVariants tests the chicken sound variants.
  """

  def test_chicken_sound_variants(self) -> None:
    picky = MCChickenSoundVariants.PICKY
    self.assertIsInstance(picky, MCChickenSoundVariants)
    self.assertIsInstance(picky, MCThing)
    self.assertEqual(picky[Version.V26_1],
                     ChickenSoundVariantId(
                         'picky', 'minecraft:chicken'
                                  '{sound_variant:"minecraft:picky"}'))
    self.assertIsInstance(picky[Version.V26_3], GameId)
    self.assertEqual(repr(picky), "<MCChickenSoundVariants>.PICKY")
    self.assertEqual(len(MCChickenSoundVariants), 2)
    self.assertNotEqual(ChickenSoundVariantId('x', 'minecraft:x'),
                        ChickenVariantId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = picky[Version.V1_21_11]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.21.11 has no 'picky'; vanilla added it in 26.1!",
    )
    with self.assertRaises(KeyError):
      _ = MCChickenSoundVariants['pickyx']
