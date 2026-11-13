"""
TestGameNames tests that a catalogue whose things the game names by a
path ('entity.creeper.primed', 'story/mine_stone') finds a member by any
name the game gave it, in any version, with or without its namespace,
beside the member's own unique name. A name the game gave two things
finds the one that held it last, as the stone stairs' recipe of 1.14
took the name 1.12 gave the cobblestone stairs'.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee
from worktoy.work_test import BaseTest

from mcdex import EntityId, MCThing


class Chimes(MCThing):
  """A catalogue of test sounds, found by their game names too."""

  __data_records__ = {
    'tolling': {'ids': {'1.7.2': '', '1.14': 'minecraft:old.bell'}},
    'bell_ring': {'ids': {'1.7.2': 'minecraft:old.bell',
                          '1.9': 'minecraft:bell.ding',
                          '1.13': 'minecraft:block.bell.ring'}},
    'gong_hit': {'ids': {'1.7.2': 'minecraft:old.gong',
                         '1.13': 'minecraft:block.gong.hit'}},
    'clang': {'ids': {'1.7.2': '', '1.14': 'minecraft:old.gong'}},
  }
  __id_class__ = EntityId
  __kind__ = 'chime'
  __game_names__ = True

  #  Each name the game gave twice, once with the newer first, once after.
  TOLLING = Kee[str]('tolling')
  BELL_RING = Kee[str]('bell_ring')
  GONG_HIT = Kee[str]('gong_hit')
  CLANG = Kee[str]('clang')


class Echoes(MCThing):
  """A catalogue of test sounds, two of them with one game name."""

  __data_records__ = {
    'first_echo': {'ids': {'1.7.2': 'minecraft:echo'}},
    'second_echo': {'ids': {'1.7.2': '', '1.9': 'minecraft:echo'}},
  }
  __id_class__ = EntityId
  __kind__ = 'echo'
  __game_names__ = True

  FIRST_ECHO = Kee[str]('first_echo')
  SECOND_ECHO = Kee[str]('second_echo')


class Murmurs(MCThing):
  """A catalogue of test sounds, found by their unique names only."""

  __data_records__ = {'hum': {'ids': {'1.7.2': 'minecraft:block.hum'}}}
  __id_class__ = EntityId
  __kind__ = 'murmur'

  HUM = Kee[str]('hum')


class TestGameNames(BaseTest):
  """
  TestGameNames tests the lookup of a member by a game name.
  """

  def test_game_names(self) -> None:
    self.assertIs(Chimes['bell_ring'], Chimes.BELL_RING)
    self.assertIs(Chimes['block.bell.ring'], Chimes.BELL_RING)
    self.assertIs(Chimes['minecraft:block.bell.ring'], Chimes.BELL_RING)
    self.assertIs(Chimes['bell.ding'], Chimes.BELL_RING)
    self.assertIs(Chimes['block.gong.hit'], Chimes.GONG_HIT)

  def test_a_name_given_twice(self) -> None:
    """The thing that held the name last has it."""
    self.assertIs(Chimes['old.bell'], Chimes.TOLLING)
    self.assertIs(Chimes['old.gong'], Chimes.CLANG)
    with self.assertRaises(KeyError) as context:
      _ = Chimes['block.bell.rung']
    self.assertIn("mcdex has no chime named 'block.bell.rung'",
                  str(context.exception))

  def test_two_things_one_game_name(self) -> None:
    with self.assertRaises(ValueError) as context:
      _ = Echoes['echo']
    self.assertIn("two members of Echoes have the game name 'echo'",
                  str(context.exception))

  def test_only_where_asked(self) -> None:
    self.assertIs(Murmurs['hum'], Murmurs.HUM)
    with self.assertRaises(KeyError):
      _ = Murmurs['block.hum']
