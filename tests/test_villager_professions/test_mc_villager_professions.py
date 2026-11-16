"""
TestMCVillagerProfessions tests the villager professions: the
'VillagerProfessionId' and 'MCVillagerProfessions' classes, and the
'MCVillagerProfessions' catalogue with the data it reads.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
from importlib.resources import files

from worktoy.work_test import BaseTest

from mcdex import GameId, MCThing, MCVillagerProfessions
from mcdex import NotInVersion, Version, VillagerProfessionId


def _records() -> dict:
  text = files('mcdex.villager_professions').joinpath(
    'villager_professions.json').read_text('utf-8')
  return json.loads(text)['villager_professions']


class TestMCVillagerProfessions(BaseTest):
  """
  TestMCVillagerProfessions tests the villager professions.
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.records = _records()

  def test_kind(self) -> None:
    farmer = MCVillagerProfessions.Farmer
    self.assertIsInstance(farmer, MCVillagerProfessions)
    self.assertIsInstance(farmer, MCThing)
    self.assertIs(type(farmer[Version.V26_3]), VillagerProfessionId)
    self.assertIsInstance(farmer[Version.V26_3], GameId)
    self.assertEqual(repr(farmer), "<MCVillagerProfessions>.Farmer")
    #  Every name of the data, but 'none', which is 'Unemployed'.
    self.assertEqual(len(MCVillagerProfessions), len(self.records) - 1)
    with self.assertRaises(KeyError) as context:
      _ = MCVillagerProfessions['farmr']
    self.assertIn("mcdex has no villager profession named 'farmr'",
                  str(context.exception))

  def test_ids_fit_their_era(self) -> None:
    """mcdex's 'unemployed' is the game's 'none'."""
    for name, record in self.records.items():
      gameName = 'none' if name == 'unemployed' else name
      self.assertEqual(next(iter(record['ids'])), '1.7.2')
      for text, minecraftId in record['ids'].items():
        with self.subTest(name=name, version=text):
          if not minecraftId:
            continue
          if Version(text) < Version.V1_8:
            self.assertRegex(minecraftId, r'^Villager\{Profession:[0-9]\}$')
          elif Version(text) < Version.V1_14:
            self.assertRegex(
                minecraftId,
                r'^(Villager|minecraft:villager)'
                r'\{Profession:[0-9],Career:[0-9]\}$')
          else:
            self.assertEqual(minecraftId, 'minecraft:villager{VillagerData:'
                             '{profession:"minecraft:%s"}}' % gameName)

  def test_known_professions(self) -> None:
    self.assertEqual(MCVillagerProfessions.Farmer[Version.V1_7_10],
                     VillagerProfessionId('farmer', 'Villager{Profession:0}'))
    fisherman = MCVillagerProfessions.Fisherman
    self.assertEqual(fisherman[Version.V1_13_2].minecraftId,
                     'minecraft:villager{Profession:0,Career:2}')
    self.assertEqual(fisherman[Version.V1_14].minecraftId,
                     'minecraft:villager{VillagerData:'
                     '{profession:"minecraft:fisherman"}}')
    cartographer = MCVillagerProfessions.Cartographer
    self.assertEqual(cartographer[Version.V1_11].minecraftId,
                     'minecraft:villager{Profession:1,Career:2}')
    with self.assertRaises(NotInVersion) as context:
      _ = MCVillagerProfessions.Mason[Version.V1_13_2]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.13.2 has no 'mason'; vanilla added it in 1.14!",
    )
