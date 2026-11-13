"""
TestMCDimensions tests the dimensions: the 'DimensionId' and
'MCDimensions' classes, and the 'MCDimensions' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import BiomeId, DimensionId, GameId, MCDimensions
from mcdex import MCThing


class TestMCDimensions(BaseTest):
  """
  TestMCDimensions tests the dimensions.
  """

  def test_dimensions(self) -> None:
    theNether = MCDimensions['the_nether']
    self.assertIsInstance(theNether, MCDimensions)
    self.assertIsInstance(theNether, MCThing)
    self.assertIsInstance(theNether['26.3'], GameId)
    self.assertEqual(repr(theNether), "<MCDimensions>.THE_NETHER")
    self.assertEqual(len(MCDimensions), 3)
    self.assertNotEqual(DimensionId('x', 'minecraft:x'),
                        BiomeId('x', 'minecraft:x'))
    with self.assertRaises(KeyError):
      _ = MCDimensions['nether']

  def test_numbers_then_names(self) -> None:
    """Up to 1.12.2 a dimension is its number; from 1.13 its name."""
    theNether = MCDimensions['the_nether']
    self.assertEqual(theNether['1.7.2'], DimensionId('the_nether', '-1'))
    self.assertEqual(theNether['1.12.2'].minecraftId, '-1')
    self.assertEqual(theNether['1.13'].minecraftId, 'minecraft:the_nether')
    self.assertEqual(MCDimensions['overworld']['1.12.2'].minecraftId, '0')
    self.assertEqual(MCDimensions['the_end']['1.12.2'].minecraftId, '1')
    self.assertEqual(MCDimensions['the_end']['26.3'].minecraftId,
                     'minecraft:the_end')
