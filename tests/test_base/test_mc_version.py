"""
TestMCVersion tests the 'MCVersion' class: its constructors, its text
form, its equality and hash, and its ordering.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.waitaminute.desc import WriteOnceError
from worktoy.work_test import BaseTest
from worktoy.work_test.samplers import IntSampler

from mcdex import MCVersion


class TestMCVersion(BaseTest):
  """
  TestMCVersion tests the 'MCVersion' class.
  """

  def setUp(self) -> None:
    self.randomInteger = IntSampler(0, 99, seed=26)

  def randomTriples(self, ) -> list[tuple[int, int, int]]:
    """Fifty triples of version components drawn from 0 to 99."""
    rand = self.randomInteger
    return [(rand(), rand(), rand()) for _ in range(50)]

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_three_ints(self) -> None:
    version_ = MCVersion(1, 7, 10)
    self.assertEqual(version_.major, 1)
    self.assertEqual(version_.minor, 7)
    self.assertEqual(version_.micro, 10)

  def test_two_ints(self) -> None:
    version_ = MCVersion(26, 3)
    self.assertEqual(version_.major, 26)
    self.assertEqual(version_.minor, 3)
    self.assertEqual(version_.micro, 0)

  def test_zeros(self) -> None:
    version_ = MCVersion(0, 0, 0)
    self.assertEqual((version_.major, version_.minor, version_.micro),
                     (0, 0, 0))

  def test_random_ints(self) -> None:
    for major, minor, micro in self.randomTriples():
      with self.subTest(major=major, minor=minor, micro=micro):
        version_ = MCVersion(major, minor, micro)
        self.assertEqual(version_.major, major)
        self.assertEqual(version_.minor, minor)
        self.assertEqual(version_.micro, micro)

  def test_negative(self) -> None:
    for args in ((-1, 0, 0), (0, -1, 0), (0, 0, -1), (-1, 0), (0, -1)):
      with self.subTest(args=args):
        with self.assertRaises(ValueError):
          MCVersion(*args)

  def test_text(self) -> None:
    cases = {
      '1.7.10': (1, 7, 10),
      '26.3': (26, 3, 0),
      '1.0': (1, 0, 0),
      '1.8.0': (1, 8, 0),
      '0.0.0': (0, 0, 0),
    }
    for text, expected in cases.items():
      with self.subTest(text=text):
        version_ = MCVersion(text)
        self.assertEqual(
            (version_.major, version_.minor, version_.micro), expected,
        )

  def test_bad_text(self) -> None:
    cases = (
      '', '1', '1.', '.1', '1..2', '1.2.3.4', 'a.b', '1.x', '1.2.x',
      '-1.2', '1.-2', ' 1.2', '1.2 ', '1.07', '01.7', '1.7.010',
      '26.4-snapshot-7', '1.21.11-rc1', '١.٢',
    )
    for text in cases:
      with self.subTest(text=text):
        with self.assertRaises(ValueError):
          MCVersion(text)

  def test_write_once(self) -> None:
    version_ = MCVersion(1, 7, 10)
    with self.assertRaises(WriteOnceError):
      version_.major = 2
    with self.assertRaises(WriteOnceError):
      version_.minor = 2
    with self.assertRaises(WriteOnceError):
      version_.micro = 2

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  TEXT   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_str(self) -> None:
    cases = {
      (1, 7, 10): '1.7.10',
      (26, 3, 0): '26.3',
      (1, 0, 0): '1.0',
      (1, 8, 0): '1.8',
      (1, 8, 9): '1.8.9',
      (0, 0, 0): '0.0',
    }
    for args, expected in cases.items():
      with self.subTest(args=args):
        self.assertEqual(str(MCVersion(*args)), expected)

  def test_str_round_trip(self) -> None:
    for args in self.randomTriples():
      with self.subTest(args=args):
        version_ = MCVersion(*args)
        self.assertEqual(MCVersion(str(version_)), version_)

  def test_repr(self) -> None:
    self.assertEqual(repr(MCVersion(1, 7, 10)), 'MCVersion(1, 7, 10)')
    self.assertEqual(repr(MCVersion(26, 3)), 'MCVersion(26, 3, 0)')

  def test_repr_round_trip(self) -> None:
    for args in self.randomTriples():
      with self.subTest(args=args):
        version_ = MCVersion(*args)
        self.assertEqual(eval(repr(version_)), version_)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  EQUALITY AND HASH  # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_equal(self) -> None:
    self.assertEqual(MCVersion(1, 7, 10), MCVersion(1, 7, 10))
    self.assertEqual(MCVersion(26, 3), MCVersion(26, 3, 0))
    self.assertEqual(MCVersion('1.8'), MCVersion(1, 8, 0))

  def test_not_equal(self) -> None:
    base = MCVersion(1, 7, 10)
    for other in (MCVersion(2, 7, 10), MCVersion(1, 8, 10),
                  MCVersion(1, 7, 11), MCVersion(0, 7, 10),
                  MCVersion(1, 6, 10), MCVersion(1, 7, 9)):
      with self.subTest(other=other):
        self.assertNotEqual(base, other)
        self.assertFalse(base == other)
        self.assertTrue(base != other)

  def test_equal_other_type(self) -> None:
    version_ = MCVersion(1, 7, 10)
    for other in ('1.7.10', (1, 7, 10), 1.7, None):
      with self.subTest(other=other):
        self.assertFalse(version_ == other)
        self.assertTrue(version_ != other)
        self.assertIs(version_.__eq__(other), NotImplemented)

  def test_hash(self) -> None:
    for args in self.randomTriples():
      with self.subTest(args=args):
        self.assertEqual(hash(MCVersion(*args)), hash(MCVersion(*args)))
    self.assertEqual(hash(MCVersion(26, 3)), hash(MCVersion(26, 3, 0)))

  def test_dict_key(self) -> None:
    table = {MCVersion(1, 7, 10): 'Robert', MCVersion(26, 3): 'Gary'}
    self.assertEqual(table[MCVersion('1.7.10')], 'Robert')
    self.assertEqual(table[MCVersion(26, 3, 0)], 'Gary')
    self.assertNotIn(MCVersion(1, 7, 2), table)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  ORDERING   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_order_by_component(self) -> None:
    ascending = (
      MCVersion(1, 7, 2),
      MCVersion(1, 7, 10),
      MCVersion(1, 8),
      MCVersion(1, 21, 11),
      MCVersion(2, 0, 0),
      MCVersion(26, 1),
      MCVersion(26, 1, 2),
      MCVersion(26, 3),
    )
    for low, high in zip(ascending, ascending[1:]):
      with self.subTest(low=low, high=high):
        self.assertTrue(low < high)
        self.assertTrue(low <= high)
        self.assertTrue(high > low)
        self.assertTrue(high >= low)
        self.assertFalse(high < low)
        self.assertFalse(high <= low)
        self.assertFalse(low > high)
        self.assertFalse(low >= high)

  def test_order_equal(self) -> None:
    low, high = MCVersion(26, 3), MCVersion(26, 3, 0)
    self.assertFalse(low < high)
    self.assertTrue(low <= high)
    self.assertFalse(low > high)
    self.assertTrue(low >= high)

  def test_order_numeric_not_textual(self) -> None:
    #  As text, '1.10' sorts before '1.9'.
    self.assertLess(MCVersion('1.9'), MCVersion('1.10'))
    self.assertLess(MCVersion('1.7.9'), MCVersion('1.7.10'))

  def test_sorted(self) -> None:
    triples = self.randomTriples()
    versions = [MCVersion(*args) for args in triples]
    expected = [MCVersion(*args) for args in sorted(triples)]
    self.assertEqual(sorted(versions), expected)

  def test_order_other_type(self) -> None:
    version_ = MCVersion(1, 7, 10)
    for other in ('1.7.10', (1, 7, 10), 1.7):
      with self.subTest(other=other):
        for op in ('__lt__', '__le__', '__gt__', '__ge__'):
          self.assertIs(getattr(version_, op)(other), NotImplemented)
        with self.assertRaises(TypeError):
          _ = version_ < other
        with self.assertRaises(TypeError):
          _ = version_ <= other
        with self.assertRaises(TypeError):
          _ = version_ > other
        with self.assertRaises(TypeError):
          _ = version_ >= other
