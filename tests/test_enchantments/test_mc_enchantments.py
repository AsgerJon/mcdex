"""
TestMCEnchantments tests the enchantments: the 'EnchantmentId' and
'MCEnchantments' classes, and the 'MCEnchantments' catalogue with the
data it reads.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
from importlib.resources import files

from worktoy.work_test import BaseTest

from mcdex import EffectId, EnchantmentId, GameId, MCEnchantments
from mcdex import MCEnchantments, MCThing, NotInVersion, Version


def _records() -> dict:
  text = files('mcdex.enchantments').joinpath('enchantments.json').read_text(
    'utf-8')
  return json.loads(text)['enchantments']


class TestMCEnchantments(BaseTest):
  """
  TestMCEnchantments tests the enchantments.
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.records = _records()

  def test_kind(self) -> None:
    protection = MCEnchantments.PROTECTION
    self.assertIsInstance(protection, MCEnchantments)
    self.assertIsInstance(protection, MCThing)
    self.assertIs(type(protection[Version.V26_3]), EnchantmentId)
    self.assertIsInstance(protection[Version.V26_3], GameId)
    self.assertEqual(repr(protection), "<MCEnchantments>.PROTECTION")
    self.assertNotEqual(EnchantmentId('x', 'minecraft:x'),
                        EffectId('x', 'minecraft:x'))

  def test_catalogue(self) -> None:
    self.assertEqual(len(MCEnchantments), len(self.records))
    self.assertEqual([e.uniqueName for e in MCEnchantments], list(self.records))
    self.assertIn('sharpness', MCEnchantments)
    with self.assertRaises(KeyError) as context:
      _ = MCEnchantments['sharpnes']
    self.assertIn("mcdex has no enchantment named 'sharpnes'",
                  str(context.exception))

  def test_ids_fit_their_era(self) -> None:
    """1.7 numbers them for '/enchant'; from 1.8 it takes names."""
    for name, record in self.records.items():
      self.assertEqual(next(iter(record['ids'])), '1.7.2')
      for text, minecraftId in record['ids'].items():
        with self.subTest(name=name, version=text):
          if not minecraftId:
            continue
          if Version(text) < Version.V1_8:
            self.assertRegex(minecraftId, r'^[0-9]+$')
          else:
            self.assertRegex(minecraftId, r'^minecraft:[a-z_]+$')

  def test_latest_version(self) -> None:
    latest = [n for n, r in self.records.items()
              if list(r['ids'].values())[-1] == 'minecraft:' + n]
    self.assertEqual(len(latest), 43)

  def test_known_enchantments(self) -> None:
    protection = MCEnchantments.PROTECTION
    self.assertEqual(protection[Version.V1_7_10],
                     EnchantmentId('protection', '0'))
    self.assertEqual(protection[Version.V1_8].minecraftId,
                     'minecraft:protection')
    self.assertEqual(MCEnchantments.SHARPNESS[Version.V1_7_2].minecraftId,
                     '16')
    self.assertEqual(MCEnchantments.LURE[Version.V1_7_10].minecraftId, '62')
    sweepingEdge = MCEnchantments.SWEEPING_EDGE
    self.assertEqual(sweepingEdge[Version.V1_11_1].minecraftId,
                     'minecraft:sweeping')
    self.assertEqual(sweepingEdge[Version.V1_20_5].minecraftId,
                     'minecraft:sweeping_edge')
    with self.assertRaises(NotInVersion) as context:
      _ = MCEnchantments.MENDING[Version.V1_8_9]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.8.9 has no 'mending'; vanilla added it in 1.9!",
    )
