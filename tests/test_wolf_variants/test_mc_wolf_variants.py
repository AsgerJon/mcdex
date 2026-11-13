"""
TestMCWolfVariants tests the wolf variants: the 'WolfVariantId' and
'MCWolfVariants' classes, and the 'MCWolfVariants' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import EntityId, GameId, MCThing, MCWolfVariants
from mcdex import NotInVersion, WolfVariantId


class TestMCWolfVariants(BaseTest):
  """
  TestMCWolfVariants tests the wolf variants.
  """

  def test_wolf_variants(self) -> None:
    pale = MCWolfVariants['pale']
    self.assertIsInstance(pale, MCWolfVariants)
    self.assertIsInstance(pale, MCThing)
    self.assertEqual(pale['1.20.5'],
                     WolfVariantId(
                         'pale', 'minecraft:wolf{variant:"minecraft:pale"}'))
    self.assertIsInstance(pale['26.3'], GameId)
    self.assertEqual(repr(pale), "<MCWolfVariants>.PALE")
    self.assertEqual(len(MCWolfVariants), 9)
    self.assertNotEqual(WolfVariantId('x', 'minecraft:x'),
                        EntityId('x', 'minecraft:x'))
    self.assertEqual(pale['1.20.4'].minecraftId, 'minecraft:wolf')
    self.assertEqual(pale['1.7.10'].minecraftId, 'Wolf')
    with self.assertRaises(NotInVersion) as context:
      _ = MCWolfVariants['ashen']['1.20.4']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.20.4 has no 'ashen'; vanilla added it in 1.20.5!",
    )
    with self.assertRaises(KeyError):
      _ = MCWolfVariants['palex']

  def test_added_later(self) -> None:
    ashen = MCWolfVariants['ashen']
    self.assertEqual(ashen['26.3'].minecraftId,
                     'minecraft:wolf{variant:"minecraft:ashen"}')
