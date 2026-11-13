"""
TestMCVillagerTypes tests the villager types: the 'VillagerTypeId' and
'MCVillagerTypes' classes, and the 'MCVillagerTypes' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import GameId, MCThing, MCVillagerTypes
from mcdex import NotInVersion, VillagerProfessionId, VillagerTypeId


class TestMCVillagerTypes(BaseTest):
  """
  TestMCVillagerTypes tests the villager types.
  """

  def test_types(self) -> None:
    desert = MCVillagerTypes['desert']
    self.assertIsInstance(desert, MCVillagerTypes)
    self.assertIsInstance(desert, MCThing)
    self.assertEqual(
        desert['1.14'],
        VillagerTypeId('desert', 'minecraft:villager{VillagerData:'
                                 '{type:"minecraft:desert"}}'))
    self.assertIsInstance(desert['26.3'], GameId)
    self.assertEqual(repr(desert), "<MCVillagerTypes>.DESERT")
    self.assertEqual(len(MCVillagerTypes), 7)
    self.assertNotEqual(VillagerTypeId('x', 'minecraft:x'),
                        VillagerProfessionId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = desert['1.13.2']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.13.2 has no 'desert'; vanilla added it in 1.14!",
    )
    with self.assertRaises(KeyError):
      _ = MCVillagerTypes['dessert']

  def test_plains_before_types(self) -> None:
    """Every villager before 1.14 is of the type Mojang gives it: plains."""
    plains = MCVillagerTypes['plains']
    self.assertEqual(plains['1.7.10'], VillagerTypeId('plains', 'Villager'))
    self.assertEqual(plains['1.13.2'].minecraftId, 'minecraft:villager')
    self.assertEqual(plains['1.14'].minecraftId,
                     'minecraft:villager'
                     '{VillagerData:{type:"minecraft:plains"}}')
