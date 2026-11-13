"""
TestMCEffects tests the mob effects: the 'EffectId' and 'MCEffects'
classes, and the 'MCEffects' catalogue with the data it reads.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import re
from importlib.resources import files

from worktoy.work_test import BaseTest

from mcdex import BlockId, EffectId, GameId, MCEffects, MCThing
from mcdex import NotInVersion, Version


def _records() -> dict:
  text = files('mcdex.effects').joinpath('effects.json').read_text('utf-8')
  return json.loads(text)['effects']


class TestMCEffects(BaseTest):
  """
  TestMCEffects tests the mob effects.
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.records = _records()

  def test_kind(self) -> None:
    speed = MCEffects.SPEED
    self.assertIsInstance(speed, MCEffects)
    self.assertIsInstance(speed, MCThing)
    self.assertIs(type(speed[Version.V26_3]), EffectId)
    self.assertIsInstance(speed[Version.V26_3], GameId)
    self.assertEqual(repr(speed), "<MCEffects>.SPEED")
    self.assertNotEqual(EffectId('x', 'minecraft:x'), BlockId('x', 'minecraft:x'))

  def test_catalogue(self) -> None:
    self.assertEqual(len(MCEffects), len(self.records))
    self.assertEqual([e.uniqueName for e in MCEffects], list(self.records))
    self.assertIs(MCEffects['speed'], MCEffects['speed'])
    self.assertIn('speed', MCEffects)
    with self.assertRaises(KeyError) as context:
      _ = MCEffects['sped']
    self.assertIn("mcdex has no effect named 'sped'", str(context.exception))

  def test_ids_fit_their_era(self) -> None:
    """1.7 numbers its effects for '/effect'; from 1.8 it takes names."""
    for name, record in self.records.items():
      self.assertEqual(next(iter(record['ids'])), '1.7.2')
      for text, minecraftId in record['ids'].items():
        with self.subTest(name=name, version=text):
          if not minecraftId:
            continue
          if Version(text) < Version.V1_8:
            self.assertRegex(minecraftId, r'^[1-9][0-9]*$')
          else:
            #  A name a person would use beside the game's, its own data.
            gameName = {'bad_luck': 'unluck'}.get(name, name)
            self.assertEqual(minecraftId, 'minecraft:' + gameName)

  def test_latest_version(self) -> None:
    latest = [r['ids'] for n, r in self.records.items()
              if list(r['ids'].values())[-1] and n != 'bad_luck']
    self.assertEqual(len(latest), 40)

  def test_known_effects(self) -> None:
    speed = MCEffects.SPEED
    self.assertEqual(speed[Version.V1_7_10], EffectId('speed', '1'))
    self.assertEqual(speed[Version.V1_8].minecraftId, 'minecraft:speed')
    self.assertEqual(MCEffects.INSTANT_HEALTH[Version.V1_7_2].minecraftId, '6')
    self.assertEqual(MCEffects.SATURATION[Version.V1_7_10].minecraftId, '23')
    self.assertEqual(MCEffects.DARKNESS[Version.V1_19].minecraftId,
                     'minecraft:darkness')
    with self.assertRaises(NotInVersion) as context:
      _ = MCEffects.GLOWING[Version.V1_8_9]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.8.9 has no 'glowing'; vanilla added it in 1.9!",
    )
