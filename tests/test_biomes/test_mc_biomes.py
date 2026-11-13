"""
TestMCBiomes tests the biomes: the 'BiomeId' and 'MCBiomes' classes, and
the 'MCBiomes' catalogue with the data it reads.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
from importlib.resources import files

from worktoy.work_test import BaseTest

from mcdex import BiomeId, BlockId, GameId, MCBiomes, MCThing
from mcdex import NotInVersion, Version


def _records() -> dict:
  text = files('mcdex.biomes').joinpath('biomes.json').read_text('utf-8')
  return json.loads(text)['biomes']


class TestMCBiomes(BaseTest):
  """
  TestMCBiomes tests the biomes.
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.records = _records()

  def test_kind(self) -> None:
    plains = MCBiomes['plains']
    self.assertIsInstance(plains, MCBiomes)
    self.assertIsInstance(plains, MCThing)
    self.assertIs(type(plains['26.3']), BiomeId)
    self.assertIsInstance(plains['26.3'], GameId)
    self.assertEqual(repr(plains), "<MCBiomes>.PLAINS")
    self.assertNotEqual(BiomeId('x', 'minecraft:x'), BlockId('x', 'minecraft:x'))

  def test_catalogue(self) -> None:
    self.assertEqual(len(MCBiomes), len(self.records))
    self.assertEqual([b.uniqueName for b in MCBiomes], list(self.records))
    with self.assertRaises(KeyError) as context:
      _ = MCBiomes['plain']
    self.assertIn("mcdex has no biome named 'plain'", str(context.exception))

  def test_ids_fit_their_era(self) -> None:
    """To 1.8.9 a number; from 1.9 a name."""
    for name, record in self.records.items():
      self.assertEqual(next(iter(record['ids'])), '1.7.2')
      for text, minecraftId in record['ids'].items():
        with self.subTest(name=name, version=text):
          if not minecraftId:
            continue
          if Version(text) < Version.V1_9:
            self.assertRegex(minecraftId, r'^[0-9]+$')
          else:
            self.assertRegex(minecraftId, r'^minecraft:[a-z_]+$')

  def test_latest_version(self) -> None:
    latest = [n for n, r in self.records.items()
              if list(r['ids'].values())[-1] == 'minecraft:' + n]
    self.assertEqual(len(latest), 67)

  def test_known_biomes(self) -> None:
    windsweptHills = MCBiomes['windswept_hills']
    self.assertEqual(windsweptHills['1.8.9'], BiomeId('windswept_hills', '3'))
    self.assertEqual(windsweptHills['1.12.2'].minecraftId,
                     'minecraft:extreme_hills')
    self.assertEqual(windsweptHills['1.17.1'].minecraftId,
                     'minecraft:mountains')
    self.assertEqual(windsweptHills['1.18'].minecraftId,
                     'minecraft:windswept_hills')
    self.assertEqual(MCBiomes['sunflower_plains']['1.7.10'].minecraftId, '129')
    self.assertEqual(MCBiomes['nether_wastes']['1.15.2'].minecraftId,
                     'minecraft:nether')
    self.assertEqual(MCBiomes['nether_wastes']['1.16'].minecraftId,
                     'minecraft:nether_wastes')
    self.assertEqual(MCBiomes['cherry_grove']['1.19.4'].minecraftId,
                     'minecraft:cherry_grove')

  def test_removed(self) -> None:
    """A biome 1.18 folded into another was removed; it keeps its name."""
    mountainEdge = MCBiomes['mountain_edge']
    self.assertEqual(mountainEdge['1.12.2'].minecraftId,
                     'minecraft:smaller_extreme_hills')
    self.assertEqual(mountainEdge['1.17.1'].minecraftId,
                     'minecraft:mountain_edge')
    with self.assertRaises(NotInVersion) as context:
      _ = mountainEdge['1.18']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.18 has no 'mountain_edge'; vanilla removed it in 1.18!",
    )
