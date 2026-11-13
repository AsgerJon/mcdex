"""
TestMCTrimPatterns tests the trim patterns: the 'TrimPatternId' and
'MCTrimPatterns' classes, and the 'MCTrimPatterns' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import GameId, MCThing, MCTrimPatterns, NotInVersion
from mcdex import TrimMaterialId, TrimPatternId


class TestMCTrimPatterns(BaseTest):
  """
  TestMCTrimPatterns tests the trim patterns.
  """

  def test_trim_patterns(self) -> None:
    coast = MCTrimPatterns['coast']
    self.assertIsInstance(coast, MCTrimPatterns)
    self.assertIsInstance(coast, MCThing)
    self.assertEqual(coast['1.19.4'],
                     TrimPatternId('coast', 'minecraft:coast'))
    self.assertIsInstance(coast['26.3'], GameId)
    self.assertEqual(repr(coast), "<MCTrimPatterns>.COAST")
    self.assertEqual(len(MCTrimPatterns), 18)
    self.assertNotEqual(TrimPatternId('x', 'minecraft:x'),
                        TrimMaterialId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = coast['1.19.3']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.19.3 has no 'coast'; vanilla added it in 1.19.4!",
    )
    with self.assertRaises(KeyError):
      _ = MCTrimPatterns['coastx']

  def test_added_later(self) -> None:
    bolt = MCTrimPatterns['bolt']
    self.assertEqual(bolt['1.20.5'].minecraftId, 'minecraft:bolt')
    with self.assertRaises(NotInVersion):
      _ = bolt['1.20.4']
