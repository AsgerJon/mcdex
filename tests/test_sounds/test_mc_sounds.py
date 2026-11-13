"""
TestMCSounds tests the sound events: the 'SoundId' and 'MCSounds'
classes, and the 'MCSounds' catalogue with the data it reads.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
from importlib.resources import files

from worktoy.work_test import BaseTest

from mcdex import GameId, MCSounds, MCThing, NotInVersion
from mcdex import ParticleId, SoundId, Version


def _records() -> dict:
  text = files('mcdex.sounds').joinpath('sounds.json').read_text('utf-8')
  return json.loads(text)['sounds']


class TestMCSounds(BaseTest):
  """
  TestMCSounds tests the sound events.
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.records = _records()

  def test_kind(self) -> None:
    primed = MCSounds['entity.creeper.primed']
    self.assertIsInstance(primed, MCSounds)
    self.assertIsInstance(primed, MCThing)
    self.assertIs(type(primed['26.3']), SoundId)
    self.assertIsInstance(primed['26.3'], GameId)
    self.assertEqual(repr(primed), "<MCSounds>.ENTITY_CREEPER_PRIMED")
    self.assertNotEqual(SoundId('x', 'minecraft:x'), ParticleId('x', 'minecraft:x'))

  def test_catalogue(self) -> None:
    self.assertEqual(len(MCSounds), len(self.records))
    with self.assertRaises(KeyError) as context:
      _ = MCSounds['entity.creeper.prime']
    self.assertIn("mcdex has no sound named 'entity.creeper.prime'",
                  str(context.exception))

  def test_ids_fit_their_era(self) -> None:
    """None listed before 1.9; from 1.9 'minecraft:' and the name."""
    for name, record in self.records.items():
      self.assertEqual(next(iter(record['ids'])), '1.7.2')
      self.assertRegex(name, r'^[a-z0-9_.]+$')
      for text, minecraftId in record['ids'].items():
        with self.subTest(name=name, version=text):
          if Version(text) < Version.V1_9:
            self.assertEqual(minecraftId, '')
          elif minecraftId:
            self.assertEqual(minecraftId, 'minecraft:' + name)

  def test_latest_version(self) -> None:
    latest = [n for n, r in self.records.items()
              if list(r['ids'].values())[-1]]
    self.assertEqual(len(latest), 1991)

  def test_known_sounds(self) -> None:
    primed = MCSounds['entity.creeper.primed']
    self.assertEqual(primed['1.9'], SoundId('entity.creeper.primed',
                                            'minecraft:entity.creeper.primed'))
    with self.assertRaises(NotInVersion) as context:
      _ = primed['1.8.9']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.8.9 has no 'entity.creeper.primed'; vanilla added it in 1.9!",
    )
    self.assertEqual(MCSounds['item.goat_horn.sound.7']['1.19'].minecraftId,
                     'minecraft:item.goat_horn.sound.7')
    self.assertEqual(MCSounds['entity.cat_royal.purr']['26.3'].minecraftId,
                     'minecraft:entity.cat_royal.purr')
