"""
TestMCWolfSoundVariants tests the wolf sound variants: the 'WolfSoundVariantId'
and 'MCWolfSoundVariants' classes, and the 'MCWolfSoundVariants' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import GameId, MCThing, MCWolfSoundVariants
from mcdex import NotInVersion, WolfSoundVariantId, WolfVariantId


class TestMCWolfSoundVariants(BaseTest):
  """
  TestMCWolfSoundVariants tests the wolf sound variants.
  """

  def test_wolf_sound_variants(self) -> None:
    puglin = MCWolfSoundVariants['puglin']
    self.assertIsInstance(puglin, MCWolfSoundVariants)
    self.assertIsInstance(puglin, MCThing)
    self.assertEqual(puglin['1.21.5'],
                     WolfSoundVariantId(
                         'puglin', 'minecraft:wolf'
                                   '{sound_variant:"minecraft:puglin"}'))
    self.assertIsInstance(puglin['26.3'], GameId)
    self.assertEqual(repr(puglin), "<MCWolfSoundVariants>.PUGLIN")
    self.assertEqual(len(MCWolfSoundVariants), 7)
    self.assertNotEqual(WolfSoundVariantId('x', 'minecraft:x'),
                        WolfVariantId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = puglin['1.21.4']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.21.4 has no 'puglin'; vanilla added it in 1.21.5!",
    )
    self.assertEqual(MCWolfSoundVariants['classic']['1.21.4'].minecraftId,
                     'minecraft:wolf')
    with self.assertRaises(KeyError):
      _ = MCWolfSoundVariants['puglinx']
