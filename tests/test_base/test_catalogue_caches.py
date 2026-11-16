"""
TestCatalogueCaches tests that the tables mcdex reads and keeps belong to
the one catalogue they were read for. Two catalogue classes may share a
name, as two test catalogues built by one function do; each must still
read its own records, find its own members by their unique names and
give its own potions with a modifier.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
import sys

from worktoy.keenum import Kee
from worktoy.work_test import BaseTest

from mcdex import EntityId, MCThing, Version


def _things(minecraftId: str) -> type:
  """A catalogue named 'Things', its one thing known by 'minecraftId'."""

  class Things(MCThing, strictCase=False):
    """A catalogue of one test thing, its record given here."""

    __data_records__ = {'a.b': {'ids': {'1.7.2': minecraftId}}}
    __id_class__ = EntityId
    __kind__ = 'thing'

    AB = Kee[str]('a.b')

  return Things


#  Two catalogues named 'Tonics', each with a long tonic of its own id,
#  printing whether each long tonic is of its own catalogue, and its id.
_TONICS = """
from worktoy.keenum import Kee
from mcdex import MCPotions, Version


def tonics(longId):
  class Tonics(MCPotions, strictCase=False):
    __data_records__ = {
      'test_tonic': {'ids': {'1.7.2': '1'}, 'long': {'ids': {'1.7.2': longId}}},
    }
    TestTonic = Kee[str]('test_tonic')
  return Tonics


first, second = tonics('65'), tonics('66')
firstLongTestTonic = first['test_tonic', 'long']
secondLongTestTonic = second['test_tonic', 'long']
print(firstLongTestTonic.base is first.TestTonic,
      secondLongTestTonic.base is second.TestTonic)
print(firstLongTestTonic[Version.V1_8_9].minecraftId,
      secondLongTestTonic[Version.V1_8_9].minecraftId)
"""


class TestCatalogueCaches(BaseTest):
  """
  Each of two catalogues of the same name reads its own data.
  """

  def test_ids(self) -> None:
    first, second = _things('test:first'), _things('test:second')
    self.assertEqual(first.AB[Version.V1_12_2].minecraftId, 'test:first')
    self.assertEqual(second.AB[Version.V1_12_2].minecraftId, 'test:second')
    self.assertEqual(second.AB.versionIds, {
      version_: 'test:second' for version_ in second.AB.versionIds})

  def test_unique_names(self) -> None:
    first, second = _things('test:first'), _things('test:second')
    self.assertIs(first['a.b'], first.AB)
    self.assertIs(second['a.b'], second.AB)

  def test_modified_potions(self) -> None:
    """
    In a process of its own: a subclass of 'MCPotions' shares the
    potions of 'MCPotions', and worktoy then names each of them by the
    root of their family, '<CatalogueMetaNum>.Swiftness', for the rest
    of the process.
    """
    env = dict(os.environ, PYTHONPATH=str.join(os.pathsep, sys.path))
    result = subprocess.run(
        [sys.executable, '-c', _TONICS], capture_output=True, text=True,
        env=env, )
    self.assertEqual(result.stderr, '')
    self.assertEqual(result.stdout, 'True True\n65 66\n')
