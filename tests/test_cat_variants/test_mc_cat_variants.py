"""
TestMCCatVariants tests the cat variants: the 'CatVariantId' and
'MCCatVariants' classes, and the 'MCCatVariants' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import CatVariantId, GameId, MCCatVariants, MCThing
from mcdex import NotInVersion, WolfVariantId


class TestMCCatVariants(BaseTest):
  """
  TestMCCatVariants tests the cat variants.
  """

  def test_cat_variants(self) -> None:
    black = MCCatVariants['black']
    self.assertIsInstance(black, MCCatVariants)
    self.assertIsInstance(black, MCThing)
    self.assertIsInstance(black['26.3'], GameId)
    self.assertEqual(repr(black), "<MCCatVariants>.BLACK")
    self.assertEqual(len(MCCatVariants), 11)
    self.assertNotEqual(CatVariantId('x', 'minecraft:x'),
                        WolfVariantId('x', 'minecraft:x'))
    with self.assertRaises(KeyError):
      _ = MCCatVariants['tuxedo']

  def test_numbers_then_names(self) -> None:
    """A tamed ocelot's number to 1.13.2, a cat's to 1.18.2, then names."""
    black = MCCatVariants['black']
    self.assertEqual(black['1.7.2'],
                     CatVariantId('black', 'Ozelot{CatType:1}'))
    self.assertEqual(black['1.12.2'].minecraftId,
                     'minecraft:ocelot{CatType:1}')
    self.assertEqual(black['1.18.2'].minecraftId, 'minecraft:cat{CatType:1}')
    self.assertEqual(black['1.19'].minecraftId,
                     'minecraft:cat{variant:"minecraft:black"}')
    britishShorthair = MCCatVariants['british_shorthair']
    self.assertEqual(britishShorthair['1.14'].minecraftId,
                     'minecraft:cat{CatType:4}')
    self.assertEqual(britishShorthair['1.19'].minecraftId,
                     'minecraft:cat{variant:"minecraft:british_shorthair"}')
    with self.assertRaises(NotInVersion) as context:
      _ = MCCatVariants['tabby']['1.13.2']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.13.2 has no 'tabby'; vanilla added it in 1.14!",
    )
