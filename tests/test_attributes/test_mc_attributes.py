"""
TestMCAttributes tests the attributes: the 'AttributeId' and
'MCAttributes' classes, and the 'MCAttributes' catalogue with its data.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
from importlib.resources import files

from worktoy.work_test import BaseTest

from mcdex import AttributeId, EffectId, GameId, MCAttributes
from mcdex import MCThing, NotInVersion, Version


def _records() -> dict:
  text = files('mcdex.attributes').joinpath('attributes.json').read_text(
    'utf-8')
  return json.loads(text)['attributes']


class TestMCAttributes(BaseTest):
  """
  TestMCAttributes tests the attributes.
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.records = _records()

  def test_kind(self) -> None:
    maxHealth = MCAttributes['max_health']
    self.assertIsInstance(maxHealth, MCAttributes)
    self.assertIsInstance(maxHealth, MCThing)
    self.assertIs(type(maxHealth['26.3']), AttributeId)
    self.assertIsInstance(maxHealth['26.3'], GameId)
    self.assertEqual(repr(maxHealth), "<MCAttributes>.MAX_HEALTH")
    self.assertNotEqual(AttributeId('x', 'minecraft:x'), EffectId('x', 'minecraft:x'))

  def test_catalogue(self) -> None:
    self.assertEqual(len(MCAttributes), len(self.records))
    with self.assertRaises(KeyError) as context:
      _ = MCAttributes['max_healt']
    self.assertIn("mcdex has no attribute named 'max_healt'",
                  str(context.exception))

  def test_ids_fit_their_era(self) -> None:
    """To 1.15.2 the name in an entity's data; from 1.16 a registry name."""
    for name, record in self.records.items():
      self.assertEqual(next(iter(record['ids'])), '1.7.2')
      for text, minecraftId in record['ids'].items():
        with self.subTest(name=name, version=text):
          if not minecraftId:
            continue
          if Version(text) < Version.V1_16:
            self.assertRegex(minecraftId, r'^[a-z]+\.[a-zA-Z]+$')
          elif Version(text) < Version.V1_21_2:
            self.assertRegex(minecraftId, r'^minecraft:[a-z]+\.[a-z_]+$')
          else:
            self.assertEqual(minecraftId, 'minecraft:' + name)

  def test_latest_version(self) -> None:
    latest = [n for n, r in self.records.items()
              if list(r['ids'].values())[-1] == 'minecraft:' + n]
    self.assertEqual(len(latest), 40)

  def test_known_attributes(self) -> None:
    maxHealth = MCAttributes['max_health']
    self.assertEqual(maxHealth['1.15.2'],
                     AttributeId('max_health', 'generic.maxHealth'))
    self.assertEqual(maxHealth['1.16'].minecraftId,
                     'minecraft:generic.max_health')
    self.assertEqual(maxHealth['1.21.2'].minecraftId, 'minecraft:max_health')
    jumpStrength = MCAttributes['jump_strength']
    self.assertEqual(jumpStrength['1.7.10'].minecraftId, 'horse.jumpStrength')
    self.assertEqual(jumpStrength['1.20.5'].minecraftId,
                     'minecraft:generic.jump_strength')
    with self.assertRaises(NotInVersion) as context:
      _ = MCAttributes['attack_speed']['1.8.9']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.8.9 has no 'attack_speed'; vanilla added it in 1.9!",
    )
