"""
TestMCStructures tests the structures: the 'StructureId' and
'MCStructures' classes, and the 'MCStructures' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import BiomeId, GameId, MCStructures, MCThing
from mcdex import NotInVersion, StructureId


class TestMCStructures(BaseTest):
  """
  TestMCStructures tests the structures.
  """

  def test_structures(self) -> None:
    villagePlains = MCStructures['village_plains']
    self.assertIsInstance(villagePlains, MCStructures)
    self.assertIsInstance(villagePlains, MCThing)
    self.assertEqual(villagePlains['1.19'],
                     StructureId('village_plains', 'minecraft:village_plains'))
    self.assertIsInstance(villagePlains['26.3'], GameId)
    self.assertEqual(repr(villagePlains), "<MCStructures>.VILLAGE_PLAINS")
    self.assertEqual(len(MCStructures), 52)
    self.assertNotEqual(StructureId('x', 'minecraft:x'),
                        BiomeId('x', 'minecraft:x'))
    with self.assertRaises(KeyError):
      _ = MCStructures['village']

  def test_kinds_of_one_old_structure(self) -> None:
    """An old village is each kind of village by what makes it that kind."""
    villagePlains = MCStructures['village_plains']
    self.assertEqual(villagePlains['1.7.10'].minecraftId,
                     'Village{Children:[{Desert:0b}]}')
    self.assertEqual(villagePlains['1.12.2'].minecraftId,
                     'Village{Children:[{Type:0b}]}')
    self.assertEqual(villagePlains['1.14'].minecraftId,
                     'Village{start_pool:"village/plains/town_centers"}')
    self.assertEqual(
        villagePlains['1.18.2'].minecraftId,
        'minecraft:village'
        '{start_pool:"minecraft:village/plains/town_centers"}')
    self.assertEqual(MCStructures['village_desert']['1.7.10'].minecraftId,
                     'Village{Children:[{Desert:1b}]}')
    self.assertEqual(MCStructures['desert_pyramid']['1.12.2'].minecraftId,
                     'Temple{Children:[{id:"TeDP"}]}')
    self.assertEqual(MCStructures['desert_pyramid']['1.13'].minecraftId,
                     'Desert_Pyramid')
    self.assertEqual(MCStructures['mineshaft_mesa']['1.18.2'].minecraftId,
                     'minecraft:mineshaft{Children:[{MST:1}]}')
    self.assertEqual(MCStructures['end_city']['1.16'].minecraftId,
                     'minecraft:endcity')

  def test_kind_not_made(self) -> None:
    """A kind the version's code does not make is not in it."""
    with self.assertRaises(NotInVersion) as context:
      _ = MCStructures['village_snowy']['1.13.2']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.13.2 has no 'village_snowy'; vanilla added it in 1.14!",
    )
