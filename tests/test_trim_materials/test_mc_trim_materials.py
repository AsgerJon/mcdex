"""
TestMCTrimMaterials tests the trim materials: the 'TrimMaterialId' and
'MCTrimMaterials' classes, and the 'MCTrimMaterials' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import GameId, MCThing, MCTrimMaterials, Version
from mcdex import NotInVersion, TrimMaterialId, TrimPatternId


class TestMCTrimMaterials(BaseTest):
  """
  TestMCTrimMaterials tests the trim materials.
  """

  def test_trim_materials(self) -> None:
    amethyst = MCTrimMaterials.AMETHYST
    self.assertIsInstance(amethyst, MCTrimMaterials)
    self.assertIsInstance(amethyst, MCThing)
    self.assertEqual(amethyst[Version.V1_19_4],
                     TrimMaterialId('amethyst', 'minecraft:amethyst'))
    self.assertIsInstance(amethyst[Version.V26_3], GameId)
    self.assertEqual(repr(amethyst), "<MCTrimMaterials>.AMETHYST")
    self.assertEqual(len(MCTrimMaterials), 11)
    self.assertNotEqual(TrimMaterialId('x', 'minecraft:x'),
                        TrimPatternId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = amethyst[Version.V1_19_3]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.19.3 has no 'amethyst'; vanilla added it in 1.19.4!",
    )
    with self.assertRaises(KeyError):
      _ = MCTrimMaterials['amethystx']

  def test_added_later(self) -> None:
    resin = MCTrimMaterials.RESIN
    self.assertEqual(resin[Version.V1_21_4].minecraftId, 'minecraft:resin')
    with self.assertRaises(NotInVersion):
      _ = resin[Version.V1_21_3]
