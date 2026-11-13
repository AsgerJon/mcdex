"""
TestMCPigSoundVariants tests the pig sound variants: the 'PigSoundVariantId'
and 'MCPigSoundVariants' classes, and the 'MCPigSoundVariants' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import GameId, MCPigSoundVariants, MCThing, Version
from mcdex import NotInVersion, PigSoundVariantId, PigVariantId


class TestMCPigSoundVariants(BaseTest):
  """
  TestMCPigSoundVariants tests the pig sound variants.
  """

  def test_pig_sound_variants(self) -> None:
    mini = MCPigSoundVariants.MINI
    self.assertIsInstance(mini, MCPigSoundVariants)
    self.assertIsInstance(mini, MCThing)
    self.assertEqual(mini[Version.V26_1],
                     PigSoundVariantId(
                         'mini', 'minecraft:pig'
                                 '{sound_variant:"minecraft:mini"}'))
    self.assertIsInstance(mini[Version.V26_3], GameId)
    self.assertEqual(repr(mini), "<MCPigSoundVariants>.MINI")
    self.assertEqual(len(MCPigSoundVariants), 3)
    self.assertNotEqual(PigSoundVariantId('x', 'minecraft:x'),
                        PigVariantId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = mini[Version.V1_21_11]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.21.11 has no 'mini'; vanilla added it in 26.1!",
    )
    with self.assertRaises(KeyError):
      _ = MCPigSoundVariants['minix']
