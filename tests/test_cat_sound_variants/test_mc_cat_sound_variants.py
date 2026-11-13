"""
TestMCCatSoundVariants tests the cat sound variants: the 'CatSoundVariantId'
and 'MCCatSoundVariants' classes, and the 'MCCatSoundVariants' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import CatSoundVariantId, GameId, MCCatSoundVariants, Version
from mcdex import MCCatSoundVariants, MCThing, NotInVersion
from mcdex import WolfSoundVariantId


class TestMCCatSoundVariants(BaseTest):
  """
  TestMCCatSoundVariants tests the cat sound variants.
  """

  def test_cat_sound_variants(self) -> None:
    royal = MCCatSoundVariants.ROYAL
    self.assertIsInstance(royal, MCCatSoundVariants)
    self.assertIsInstance(royal, MCThing)
    self.assertEqual(royal[Version.V26_1],
                     CatSoundVariantId(
                         'royal', 'minecraft:cat'
                                  '{sound_variant:"minecraft:royal"}'))
    self.assertIsInstance(royal[Version.V26_3], GameId)
    self.assertEqual(repr(royal), "<MCCatSoundVariants>.ROYAL")
    self.assertEqual(len(MCCatSoundVariants), 2)
    self.assertNotEqual(CatSoundVariantId('x', 'minecraft:x'),
                        WolfSoundVariantId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = royal[Version.V1_21_11]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.21.11 has no 'royal'; vanilla added it in 26.1!",
    )
    classic = MCCatSoundVariants.CLASSIC
    self.assertEqual(classic[Version.V1_21_11].minecraftId, 'minecraft:cat')
    self.assertEqual(classic[Version.V26_1].minecraftId,
                     'minecraft:cat{sound_variant:"minecraft:classic"}')
    with self.assertRaises(KeyError):
      _ = MCCatSoundVariants['royalx']
