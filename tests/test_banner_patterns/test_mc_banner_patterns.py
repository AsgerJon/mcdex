"""
TestMCBannerPatterns tests the banner patterns: the 'BannerPatternId'
and 'MCBannerPatterns' classes, and the 'MCBannerPatterns' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import BannerPatternId, GameId, MCBannerPatterns, Version
from mcdex import MCThing, NotInVersion, PaintingVariantId


class TestMCBannerPatterns(BaseTest):
  """
  TestMCBannerPatterns tests the banner patterns.
  """

  def test_banner_patterns(self) -> None:
    base = MCBannerPatterns.BASE
    self.assertIsInstance(base, MCBannerPatterns)
    self.assertIsInstance(base, MCThing)
    self.assertIsInstance(base[Version.V26_3], GameId)
    self.assertEqual(repr(base), "<MCBannerPatterns>.BASE")
    #  43 patterns, two of them under a second name too.
    self.assertEqual(len(MCBannerPatterns), 45)
    self.assertNotEqual(BannerPatternId('x', 'minecraft:x'),
                        PaintingVariantId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = base[Version.V1_7_10]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.7.10 has no 'base'; vanilla added it in 1.8!",
    )
    with self.assertRaises(KeyError):
      _ = MCBannerPatterns['b']

  def test_codes_then_names(self) -> None:
    """To 1.20.4 a pattern is its code; from 1.20.5 its name."""
    squareBottomLeft = MCBannerPatterns.SQUARE_BOTTOM_LEFT
    self.assertEqual(squareBottomLeft[Version.V1_8],
                     BannerPatternId('square_bottom_left', 'bl'))
    self.assertEqual(squareBottomLeft[Version.V1_20_4].minecraftId, 'bl')
    self.assertEqual(squareBottomLeft[Version.V1_20_5].minecraftId,
                     'minecraft:square_bottom_left')
    self.assertEqual(MCBannerPatterns.GLOBE[Version.V1_14].minecraftId, 'glb')
    self.assertEqual(MCBannerPatterns.PIGLIN[Version.V1_16].minecraftId, 'pig')
