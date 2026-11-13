"""
TestMCStatistics tests the custom statistics: the 'StatisticId' and
'MCStatistics' classes, and the 'MCStatistics' catalogue with its data.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
from importlib.resources import files

from worktoy.work_test import BaseTest

from mcdex import GameId, MCStatistics, MCThing, NotInVersion
from mcdex import SoundId, StatisticId, Version


def _records() -> dict:
  text = files('mcdex.statistics').joinpath('statistics.json').read_text(
    'utf-8')
  return json.loads(text)['statistics']


class TestMCStatistics(BaseTest):
  """
  TestMCStatistics tests the custom statistics.
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.records = _records()

  def test_kind(self) -> None:
    leaveGame = MCStatistics['leave_game']
    self.assertIsInstance(leaveGame, MCStatistics)
    self.assertIsInstance(leaveGame, MCThing)
    self.assertIs(type(leaveGame['26.3']), StatisticId)
    self.assertIsInstance(leaveGame['26.3'], GameId)
    self.assertEqual(repr(leaveGame), "<MCStatistics>.LEAVE_GAME")
    self.assertNotEqual(StatisticId('x', 'minecraft:x'), SoundId('x', 'minecraft:x'))

  def test_catalogue(self) -> None:
    self.assertEqual(len(MCStatistics), len(self.records))
    with self.assertRaises(KeyError) as context:
      _ = MCStatistics['leave_gam']
    self.assertIn("mcdex has no statistic named 'leave_gam'",
                  str(context.exception))

  def test_ids_fit_their_era(self) -> None:
    """To 1.12.2 a 'stat.' name; from 1.13 a registry name."""
    for name, record in self.records.items():
      self.assertEqual(next(iter(record['ids'])), '1.7.2')
      self.assertRegex(name, r'^[a-z0-9]+(_[a-z0-9]+)*$')
      for text, minecraftId in record['ids'].items():
        with self.subTest(name=name, version=text):
          if not minecraftId:
            continue
          if Version(text) < Version.V1_13:
            self.assertRegex(minecraftId, r'^stat\.[a-zA-Z]+$')
          else:
            self.assertRegex(minecraftId, r'^minecraft:[a-z0-9_]+$')

  def test_latest_version(self) -> None:
    latest = [n for n, r in self.records.items()
              if list(r['ids'].values())[-1] == 'minecraft:' + n]
    self.assertEqual(len(latest), 78)

  def test_known_statistics(self) -> None:
    self.assertEqual(MCStatistics['leave_game']['1.12.2'],
                     StatisticId('leave_game', 'stat.leaveGame'))
    playTime = MCStatistics['play_time']
    self.assertEqual(playTime['1.12.2'].minecraftId, 'stat.playOneMinute')
    self.assertEqual(playTime['1.16.5'].minecraftId,
                     'minecraft:play_one_minute')
    self.assertEqual(playTime['1.17'].minecraftId, 'minecraft:play_time')
    junkFished = MCStatistics['junk_fished']
    self.assertEqual(junkFished['1.11'].minecraftId, 'stat.junkFished')
    with self.assertRaises(NotInVersion) as context:
      _ = junkFished['1.12.2']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.12.2 has no 'junk_fished'; vanilla removed it in 1.11.1!",
    )
