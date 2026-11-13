"""
TestMCTrimMaterials tests the trim materials: the 'TrimMaterialId' and
'MCTrimMaterials' classes, and the 'MCTrimMaterials' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import GameId, MCThing, MCTrimMaterials
from mcdex import NotInVersion, TrimMaterialId, TrimPatternId


class TestMCTrimMaterials(BaseTest):
  """
  TestMCTrimMaterials tests the trim materials.
  """

  def test_trim_materials(self) -> None:
    amethyst = MCTrimMaterials['amethyst']
    self.assertIsInstance(amethyst, MCTrimMaterials)
    self.assertIsInstance(amethyst, MCThing)
    self.assertEqual(amethyst['1.19.4'],
                     TrimMaterialId('amethyst', 'minecraft:amethyst'))
    self.assertIsInstance(amethyst['26.3'], GameId)
    self.assertEqual(repr(amethyst), "<MCTrimMaterials>.AMETHYST")
    self.assertEqual(len(MCTrimMaterials), 11)
    self.assertNotEqual(TrimMaterialId('x', 'minecraft:x'),
                        TrimPatternId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = amethyst['1.19.3']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.19.3 has no 'amethyst'; vanilla added it in 1.19.4!",
    )
    with self.assertRaises(KeyError):
      _ = MCTrimMaterials['amethystx']

  def test_added_later(self) -> None:
    resin = MCTrimMaterials['resin']
    self.assertEqual(resin['1.21.4'].minecraftId, 'minecraft:resin')
    with self.assertRaises(NotInVersion):
      _ = resin['1.21.3']
