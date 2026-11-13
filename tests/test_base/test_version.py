"""
TestVersion tests the 'Version' enumeration: its members, their order,
and the resolution of a member from its name, its text or its
'MCVersion'.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.waitaminute.keenum import KeeResolveError
from worktoy.work_test import BaseTest

from mcdex import MCVersion, Version


class TestVersion(BaseTest):
  """
  TestVersion tests the 'Version' enumeration.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  MEMBERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_count(self) -> None:
    self.assertEqual(len(Version), 103)

  def test_first_and_last(self) -> None:
    members = list(Version)
    self.assertIs(members[0], Version.V1_0)
    self.assertIs(members[-1], Version.V26_3)
    self.assertEqual(Version.V1_0.value, MCVersion(1, 0, 0))
    self.assertEqual(Version.V26_3.value, MCVersion(26, 3, 0))

  def test_values_are_versions(self) -> None:
    for member in Version:
      with self.subTest(member=member.name):
        self.assertIsInstance(member.value, MCVersion)

  def test_names_match_values(self) -> None:
    for member in Version:
      with self.subTest(member=member.name):
        expected = 'V%s' % str(member.value).replace('.', '_')
        self.assertEqual(member.name, expected)

  def test_values_ascend(self) -> None:
    members = list(Version)
    for low, high in zip(members, members[1:]):
      with self.subTest(low=low.name, high=high.name):
        self.assertLess(low.value, high.value)

  def test_never_released(self) -> None:
    for text in ('1.2', '1.2.0', '1.5', '1.5.0', '1.4.3', '1.6.3', '1.7.1'):
      with self.subTest(text=text):
        with self.assertRaises(KeeResolveError):
          Version(text)

  def test_year_numbering(self) -> None:
    years = [m for m in Version if m.value.major == 26]
    self.assertEqual(
        [str(m.value) for m in years],
        ['26.1', '26.1.1', '26.1.2', '26.2', '26.3'],
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  RESOLUTION   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_from_name(self) -> None:
    self.assertIs(Version('V1_7_10'), Version.V1_7_10)
    self.assertIs(Version('v1_7_10'), Version.V1_7_10)

  def test_from_text(self) -> None:
    cases = {
      '1.7.10': Version.V1_7_10,
      '1.8': Version.V1_8,
      '1.8.0': Version.V1_8,
      '1.9': Version.V1_9,
      '1.0': Version.V1_0,
      '26.3': Version.V26_3,
      '26.3.0': Version.V26_3,
      '26.1.2': Version.V26_1_2,
    }
    for text, expected in cases.items():
      with self.subTest(text=text):
        self.assertIs(Version(text), expected)
        self.assertIs(Version[text], expected)

  def test_every_member_from_text(self) -> None:
    for member in Version:
      with self.subTest(member=member.name):
        self.assertIs(Version(str(member.value)), member)

  def test_from_mc_version(self) -> None:
    self.assertIs(Version(MCVersion(1, 7, 10)), Version.V1_7_10)
    self.assertIs(Version(MCVersion('26.3')), Version.V26_3)
    self.assertIs(Version.fromValue(MCVersion(1, 9)), Version.V1_9)

  def test_unresolvable(self) -> None:
    for identifier in ('', 'elytra', '26.4-snapshot-7', '1.7.10 ',
                       '99.0', MCVersion(26, 4), 3.5):
      with self.subTest(identifier=identifier):
        with self.assertRaises(KeeResolveError):
          Version(identifier)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  ORDERING   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_order(self) -> None:
    low, high = Version.V1_7_10, Version.V1_9
    self.assertTrue(low < high)
    self.assertTrue(low <= high)
    self.assertTrue(high > low)
    self.assertTrue(high >= low)
    self.assertFalse(high < low)
    self.assertFalse(high <= low)
    self.assertFalse(low > high)
    self.assertFalse(low >= high)

  def test_order_equal(self) -> None:
    member = Version.V26_3
    self.assertFalse(member < member)
    self.assertTrue(member <= member)
    self.assertFalse(member > member)
    self.assertTrue(member >= member)

  def test_order_numeric_not_textual(self) -> None:
    self.assertLess(Version.V1_9, Version.V1_10)
    self.assertLess(Version.V1_21_11, Version.V26_1)

  def test_sorted(self) -> None:
    members = list(Version)
    self.assertEqual(sorted(reversed(members)), members)

  def test_order_other_type(self) -> None:
    member = Version.V1_7_10
    for other in (MCVersion(1, 7, 10), '1.7.10', 7):
      with self.subTest(other=other):
        for op in ('__lt__', '__le__', '__gt__', '__ge__'):
          self.assertIs(getattr(member, op)(other), NotImplemented)
        with self.assertRaises(TypeError):
          _ = member < other
        with self.assertRaises(TypeError):
          _ = member <= other
        with self.assertRaises(TypeError):
          _ = member > other
        with self.assertRaises(TypeError):
          _ = member >= other

  def test_equality_is_identity(self) -> None:
    self.assertEqual(Version.V1_9, Version('1.9'))
    self.assertNotEqual(Version.V1_9, Version.V1_9_1)
    self.assertNotEqual(Version.V1_9, MCVersion(1, 9))
