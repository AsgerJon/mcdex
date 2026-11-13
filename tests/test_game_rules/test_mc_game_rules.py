"""
TestMCGameRules tests the game rules: the 'GameRuleId' and 'MCGameRules'
classes, and the 'MCGameRules' catalogue with the data it reads.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
from importlib.resources import files

from worktoy.work_test import BaseTest

from mcdex import GameId, GameRuleId, MCGameRules, MCThing
from mcdex import NotInVersion, StatisticId, Version


def _records() -> dict:
  text = files('mcdex.game_rules').joinpath('game_rules.json').read_text(
    'utf-8')
  return json.loads(text)['game_rules']


class TestMCGameRules(BaseTest):
  """
  TestMCGameRules tests the game rules.
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.records = _records()

  def test_kind(self) -> None:
    keepInventory = MCGameRules['keep_inventory']
    self.assertIsInstance(keepInventory, MCGameRules)
    self.assertIsInstance(keepInventory, MCThing)
    self.assertIs(type(keepInventory['26.3']), GameRuleId)
    self.assertIsInstance(keepInventory['26.3'], GameId)
    self.assertEqual(repr(keepInventory), "<MCGameRules>.KEEP_INVENTORY")
    self.assertNotEqual(GameRuleId('x', 'minecraft:x'),
                        StatisticId('x', 'minecraft:x'))

  def test_catalogue(self) -> None:
    self.assertEqual(len(MCGameRules), len(self.records))
    with self.assertRaises(KeyError) as context:
      _ = MCGameRules['keep_inventor']
    self.assertIn("mcdex has no game rule named 'keep_inventor'",
                  str(context.exception))

  def test_ids_fit_their_era(self) -> None:
    """Until 1.21.11 a camelCase name; since, a registry name."""
    for name, record in self.records.items():
      self.assertEqual(next(iter(record['ids'])), '1.7.2')
      self.assertRegex(name, r'^[a-z0-9]+(_[a-z0-9]+)*$')
      for text, minecraftId in record['ids'].items():
        with self.subTest(name=name, version=text):
          if not minecraftId:
            continue
          if Version(text) < Version.V1_21_11:
            self.assertRegex(minecraftId, r'^[a-z]+[a-zA-Z]*$')
          else:
            self.assertEqual(minecraftId, 'minecraft:' + name)

  def test_latest_version(self) -> None:
    latest = [n for n, r in self.records.items()
              if list(r['ids'].values())[-1] == 'minecraft:' + n]
    self.assertEqual(len(latest), 59)

  def test_known_rules(self) -> None:
    self.assertEqual(MCGameRules['keep_inventory']['1.7.10'],
                     GameRuleId('keep_inventory', 'keepInventory'))
    self.assertEqual(MCGameRules['advance_time']['1.21.10'].minecraftId,
                     'doDaylightCycle')
    self.assertEqual(MCGameRules['advance_time']['1.21.11'].minecraftId,
                     'minecraft:advance_time')
    fire = MCGameRules['fire_spread_radius_around_player']
    self.assertEqual(fire['1.7.2'].minecraftId, 'doFireTick')
    with self.assertRaises(NotInVersion) as context:
      _ = MCGameRules['allow_fire_ticks_away_from_player']['1.21.11']
    self.assertIn('removed it in 1.21.11', str(context.exception))
    with self.assertRaises(NotInVersion):
      _ = MCGameRules['random_tick_speed']['1.7.10']
