"""
TestMCZombieNautilusVariants tests the zombie nautilus variants: the
'ZombieNautilusVariantId' and 'MCZombieNautilusVariants' classes, and the
'MCZombieNautilusVariants' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import GameId, MCThing, MCZombieNautilusVariants, Version
from mcdex import MCZombieNautilusVariants, NotInVersion, PigVariantId
from mcdex import ZombieNautilusVariantId


class TestMCZombieNautilusVariants(BaseTest):
  """
  TestMCZombieNautilusVariants tests the zombie nautilus variants.
  """

  def test_zombie_nautilus_variants(self) -> None:
    warm = MCZombieNautilusVariants.WARM
    self.assertIsInstance(warm, MCZombieNautilusVariants)
    self.assertIsInstance(warm, MCThing)
    self.assertEqual(warm[Version.V1_21_11],
                     ZombieNautilusVariantId(
                         'warm', 'minecraft:zombie_nautilus'
                                 '{variant:"minecraft:warm"}'))
    self.assertIsInstance(warm[Version.V26_3], GameId)
    self.assertEqual(repr(warm), "<MCZombieNautilusVariants>.WARM")
    self.assertEqual(len(MCZombieNautilusVariants), 2)
    self.assertNotEqual(ZombieNautilusVariantId('x', 'minecraft:x'),
                        PigVariantId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = warm[Version.V1_21_10]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.21.10 has no 'warm'; vanilla added it in 1.21.11!",
    )
    with self.assertRaises(KeyError):
      _ = MCZombieNautilusVariants['warmx']
