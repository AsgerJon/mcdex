"""
TestMCCowSoundVariants tests the cow sound variants: the 'CowSoundVariantId'
and 'MCCowSoundVariants' classes, and the 'MCCowSoundVariants' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import CowSoundVariantId, CowVariantId, GameId, MCCowSoundVariants
from mcdex import MCCowSoundVariants, MCThing, NotInVersion, Version


class TestMCCowSoundVariants(BaseTest):
  """
  TestMCCowSoundVariants tests the cow sound variants.
  """

  def test_cow_sound_variants(self) -> None:
    moody = MCCowSoundVariants.MOODY
    self.assertIsInstance(moody, MCCowSoundVariants)
    self.assertIsInstance(moody, MCThing)
    self.assertEqual(moody[Version.V26_1],
                     CowSoundVariantId(
                         'moody', 'minecraft:cow'
                                  '{sound_variant:"minecraft:moody"}'))
    self.assertIsInstance(moody[Version.V26_3], GameId)
    self.assertEqual(repr(moody), "<MCCowSoundVariants>.MOODY")
    self.assertEqual(len(MCCowSoundVariants), 2)
    self.assertNotEqual(CowSoundVariantId('x', 'minecraft:x'),
                        CowVariantId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = moody[Version.V1_21_11]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.21.11 has no 'moody'; vanilla added it in 26.1!",
    )
    with self.assertRaises(KeyError):
      _ = MCCowSoundVariants['moodyx']
