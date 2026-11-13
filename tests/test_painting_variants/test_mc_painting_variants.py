"""
TestMCPaintingVariants tests the paintings: the 'PaintingVariantId' and
'MCPaintingVariants' classes, and the 'MCPaintingVariants' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import CatVariantId, GameId, MCPaintingVariants
from mcdex import MCThing, NotInVersion, PaintingVariantId


class TestMCPaintingVariants(BaseTest):
  """
  TestMCPaintingVariants tests the paintings.
  """

  def test_painting_variants(self) -> None:
    kebab = MCPaintingVariants['kebab']
    self.assertIsInstance(kebab, MCPaintingVariants)
    self.assertIsInstance(kebab, MCThing)
    self.assertIsInstance(kebab['26.3'], GameId)
    self.assertEqual(repr(kebab), "<MCPaintingVariants>.KEBAB")
    self.assertEqual(len(MCPaintingVariants), 51)
    self.assertNotEqual(PaintingVariantId('x', 'minecraft:x'),
                        CatVariantId('x', 'minecraft:x'))
    with self.assertRaises(KeyError):
      _ = MCPaintingVariants['kebabs']

  def test_titles_then_names(self) -> None:
    """
    What /summon takes: the painting with its picture, to 1.12.2 its
    title, from 1.13 its name, from 1.19 under 'variant'.
    """
    donkeyKong = MCPaintingVariants['donkey_kong']
    self.assertEqual(donkeyKong['1.7.2'],
                     PaintingVariantId('donkey_kong',
                                       'Painting{Motive:"DonkeyKong"}'))
    self.assertEqual(donkeyKong['1.12.2'].minecraftId,
                     'minecraft:painting{Motive:"DonkeyKong"}')
    self.assertEqual(donkeyKong['1.13'].minecraftId,
                     'minecraft:painting{Motive:"minecraft:donkey_kong"}')
    self.assertEqual(donkeyKong['1.19'].minecraftId,
                     'minecraft:painting{variant:"minecraft:donkey_kong"}')
    earth = MCPaintingVariants['earth']
    self.assertEqual(earth['1.19'].minecraftId,
                     'minecraft:painting{variant:"minecraft:earth"}')
    with self.assertRaises(NotInVersion) as context:
      _ = earth['1.18.2']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.18.2 has no 'earth'; vanilla added it in 1.19!",
    )
