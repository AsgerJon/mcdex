"""
TestDataFiles tests every data file of mcdex at once, so a regenerated
file cannot break what the spot checks of each catalogue do not reach:
its names, the order of its versions, that it records changes only, the
form of its ids, that every member is named by its unique name in
PascalCase and found by it, and that every name of the data finds its
member, a name no member can take the member with the same data.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import re
from importlib.resources import files

from worktoy.work_test import BaseTest

import mcdex
from mcdex import MCThing, Version


#  A name of digits alone, as a jukebox song's '13', spelled out.
ONES = ('', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
        'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
        'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')

#  The names of the data no member can take: the game's names of the human
#  'slimeball' and of the diagonal stripes 'stripe_down_left' and
#  '_right', the same names in PascalCase, and the villager profession
#  'none', the keyword 'None' in PascalCase, mcdex's 'unemployed'.
NO_MEMBER = ('none', 'slime_ball', 'stripe_downleft', 'stripe_downright')


def _pascal(uniqueName: str) -> str:
  """A unique name in PascalCase: 'pink_wool' is 'PinkWool'."""
  if uniqueName.isdigit():
    return ONES[int(uniqueName)]
  words = str.split(uniqueName, '_')
  return str.join('', [word[:1].upper() + word[1:] for word in words])


def _catalogues() -> list:
  """Every catalogue of mcdex."""
  out = []
  for name in mcdex.__all__:
    value = getattr(mcdex, name)
    if isinstance(value, type) and issubclass(value, MCThing) \
        and value is not MCThing:
      out.append(value)
  return out


def _balanced(text: str) -> bool:
  """Whether the braces of an id close in order, its quotes in pairs."""
  stack, quoted = [], False
  pairs = {'}': '{', ']': '[', ')': '('}
  for char in text:
    if char == '"':
      quoted = not quoted
    elif not quoted and char in '{[(':
      stack.append(char)
    elif not quoted and char in '}])':
      if not stack or stack.pop() != pairs[char]:
        return False
  return not stack and not quoted


class TestDataFiles(BaseTest):
  """
  TestDataFiles tests the data file of every catalogue.
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.files = {}
    for catalogue in _catalogues():
      package = catalogue.__module__.rsplit('.', 1)[0]
      path = files(package).joinpath(catalogue.__data_file__)
      cls.files[catalogue] = json.loads(path.read_text('utf-8'))

  def test_every_catalogue(self) -> None:
    self.assertEqual(len(self.files), 36)

  def test_records(self) -> None:
    order = [str(version.value) for version in Version]
    for catalogue, data in self.files.items():
      first, last = data['covers']
      for name, record in data[catalogue.__data_key__].items():
        ids = record['ids']
        values = list(ids.values())
        with self.subTest(catalogue=catalogue.__name__, name=name):
          self.assertRegex(name, r'^[a-z0-9_]+$')
          self.assertEqual(next(iter(ids)), first)
          positions = [order.index(text) for text in ids]
          self.assertEqual(positions, sorted(positions))
          self.assertTrue(all(a != b for a, b in zip(values, values[1:])))
          self.assertTrue(any(values))
          for id_ in values:
            self.assertEqual(id_, id_.strip())
            self.assertNotIn('  ', id_)
            self.assertTrue(_balanced(id_), id_)
            self.assertNotIn('{}', id_)
            self.assertNotIn('[]', id_)
          if values[-1]:
            self.assertTrue(values[-1].startswith('minecraft:'), values[-1])
      self.assertEqual(last, order[-1])

  def test_member_names(self) -> None:
    for catalogue in _catalogues():
      for member in catalogue:
        with self.subTest(member=member):
          self.assertEqual(member.name, _pascal(member.uniqueName))

  def test_data_names_find_members(self) -> None:
    """
    Each name of the data finds the member of that name; one no member
    can take finds the member with the same data.
    """
    noMember = []
    for catalogue, data in self.files.items():
      records = data[catalogue.__data_key__]
      for name, record in records.items():
        member = catalogue[name]
        with self.subTest(catalogue=catalogue.__name__, name=name):
          self.assertIn(name, catalogue)
          if member.uniqueName != name:
            noMember.append(name)
            self.assertEqual(records[member.uniqueName], record)
    self.assertEqual(sorted(noMember), list(NO_MEMBER))

  def test_unique_names_find_members(self) -> None:
    for catalogue in _catalogues():
      for member in catalogue:
        with self.subTest(member=member):
          self.assertIs(catalogue[member.uniqueName], member)
