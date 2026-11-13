"""
TestMCThing tests 'MCThing', the base of every catalogue, and
'CatalogueMeta', its metaclass: a catalogue of test things, its members,
their records and the id each version knows them by.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee
from worktoy.waitaminute import TypeException, WorkToyException
from worktoy.waitaminute.keenum import KeeResolveError, KeeWriteOnceError
from worktoy.work_test import BaseTest

from mcdex import EntityId, MCThing, MCVersion, NotInVersion, Version

_RECORDS = {
  #  Renamed at 1.11, present in every version of the data.
  'blob': {'ids': {'1.11': 'test:blob', '1.7.2': 'Blob'}},
  #  Split off another thing: its old id carries that thing's data.
  'husk': {'ids': {'1.7.2': '', '1.10': 'Zombie{ZombieType:6}',
                   '1.11': 'test:husk'}},
  #  Removed before 26.3.
  'ghost': {'ids': {'1.7.2': '', '1.21.2': 'test:ghost', '1.21.4': ''}},
  #  A unique name no member's name can be.
  'creeper.primed': {'ids': {'1.7.2': 'test:creeper.primed'}},
  'lacking_none': {},
  'lacking_empty': {'ids': {}},
  'lacking_names': {'names': {'1.7.2': 'Blob'}},
  'phantom': {'ids': {'1.7.2': '', '1.9': ''}},
  'misdated_old': {'ids': {'1.2': 'Blob'}},
  'misdated_snapshot': {'ids': {'26.4-snapshot-7': 'Blob'}},
  'misdated_word': {'ids': {'creeper': 'Blob'}},
  'mislabeled_int': {'ids': {'1.7.2': 50}},
  'mislabeled_none': {'ids': {'1.7.2': None}},
  'mislabeled_id': {'ids': {'1.7.2': EntityId('x', 'X')}},
}


class Beasts(MCThing):
  """A catalogue of test things, its records given here."""

  __data_records__ = _RECORDS
  __id_class__ = EntityId
  __kind__ = 'beast'

  BLOB = Kee[str]('blob')
  HUSK = Kee[str]('husk')
  GHOST = Kee[str]('ghost')
  CREEPER_PRIMED = Kee[str]('creeper.primed')
  LACKING_NONE = Kee[str]('lacking_none')
  LACKING_EMPTY = Kee[str]('lacking_empty')
  LACKING_NAMES = Kee[str]('lacking_names')
  PHANTOM = Kee[str]('phantom')
  MISDATED_OLD = Kee[str]('misdated_old')
  MISDATED_SNAPSHOT = Kee[str]('misdated_snapshot')
  MISDATED_WORD = Kee[str]('misdated_word')
  MISLABELED_INT = Kee[str]('mislabeled_int')
  MISLABELED_NONE = Kee[str]('mislabeled_none')
  MISLABELED_ID = Kee[str]('mislabeled_id')
  NAMELESS = Kee[str]('')
  STRAY = Kee[str]('stray')


class TestMCThing(BaseTest):
  """
  TestMCThing tests 'MCThing' and 'CatalogueMeta'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE CATALOGUE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_members(self) -> None:
    blob = Beasts.BLOB
    self.assertIsInstance(blob, Beasts)
    self.assertIsInstance(blob, MCThing)
    self.assertEqual(len(Beasts), 16)
    self.assertIs(list(Beasts)[0], blob)

  def test_found_by_name(self) -> None:
    """By the member's name in any case, by its unique name, by position."""
    blob = Beasts.BLOB
    self.assertIs(Beasts['blob'], blob)
    self.assertIs(Beasts['BLOB'], blob)
    self.assertIs(Beasts.Blob, blob)
    self.assertIs(Beasts['creeper.primed'], Beasts.CREEPER_PRIMED)
    self.assertIs(Beasts[1], Beasts.HUSK)

  def test_unknown_name(self) -> None:
    with self.assertRaises(KeyError) as context:
      _ = Beasts['blop']
    self.assertIn("mcdex has no beast named 'blop'", str(context.exception))

  def test_not_a_name(self) -> None:
    for identifier in (Version.V1_9, ('blob',), 1.5):
      with self.subTest(identifier=identifier):
        with self.assertRaises(KeeResolveError):
          _ = Beasts[identifier]

  def test_contains(self) -> None:
    self.assertIn('blob', Beasts)
    self.assertIn('creeper.primed', Beasts)
    self.assertIn(Beasts.BLOB, Beasts)
    self.assertNotIn('blop', Beasts)
    self.assertNotIn(1, Beasts)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  A MEMBER   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_unique_name(self) -> None:
    self.assertEqual(Beasts.BLOB.uniqueName, 'blob')
    self.assertIs(type(Beasts.BLOB.uniqueName), str)
    self.assertEqual(Beasts.CREEPER_PRIMED.uniqueName, 'creeper.primed')

  def test_frozen(self) -> None:
    with self.assertRaises(KeeWriteOnceError):
      Beasts.BLOB.uniqueName = 'slime'

  def test_text(self) -> None:
    self.assertEqual(str(Beasts.BLOB), '<Beasts>.BLOB')
    self.assertEqual(repr(Beasts.BLOB), '<Beasts>.BLOB')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE RECORD   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_empty_name(self) -> None:
    with self.assertRaises(ValueError) as context:
      _ = Beasts.NAMELESS['1.7.2']
    self.assertIn("Beasts.NAMELESS has an empty 'uniqueName'",
                  str(context.exception))

  def test_no_record(self) -> None:
    with self.assertRaises(ValueError) as context:
      _ = Beasts.STRAY['1.7.2']
    self.assertIn("Beasts('stray') has no record in the data",
                  str(context.exception))

  def test_record_lacks_ids(self) -> None:
    for beast in (Beasts.LACKING_NONE, Beasts.LACKING_EMPTY,
                  Beasts.LACKING_NAMES):
      with self.subTest(beast=beast):
        with self.assertRaises(ValueError) as context:
          _ = beast.versionIds
        self.assertIn("Beasts('%s') received no 'ids'" % beast.uniqueName,
                      str(context.exception))

  def test_in_no_version(self) -> None:
    with self.assertRaises(ValueError) as context:
      _ = Beasts.PHANTOM['1.9']
    self.assertIn("Beasts('phantom') is in no version",
                  str(context.exception))

  def test_unknown_version(self) -> None:
    for beast in (Beasts.MISDATED_OLD, Beasts.MISDATED_SNAPSHOT,
                  Beasts.MISDATED_WORD):
      with self.subTest(beast=beast):
        with self.assertRaises(KeeResolveError):
          _ = beast['1.7.2']

  def test_id_not_str(self) -> None:
    for beast in (Beasts.MISLABELED_INT, Beasts.MISLABELED_NONE,
                  Beasts.MISLABELED_ID):
      with self.subTest(beast=beast):
        with self.assertRaises(TypeException):
          _ = beast['1.7.2']

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  VERSION IDS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_version_ids_every_version(self) -> None:
    """A key for every 'Version' from the first version of the data."""
    expected = [v for v in Version if v >= Version.V1_7_2]
    for beast in (Beasts.BLOB, Beasts.HUSK, Beasts.GHOST):
      with self.subTest(beast=beast):
        self.assertEqual(list(beast.versionIds), expected)

  def test_version_ids_values(self) -> None:
    ids = Beasts.BLOB.versionIds
    for version_ in ids:
      with self.subTest(version=version_.name):
        if version_ < Version.V1_11:
          self.assertEqual(ids[version_], 'Blob')
        else:
          self.assertEqual(ids[version_], 'test:blob')

  def test_version_ids_absent(self) -> None:
    self.assertEqual(Beasts.HUSK.versionIds[Version.V1_9_4], '')
    self.assertEqual(Beasts.HUSK.versionIds[Version.V1_10],
                     'Zombie{ZombieType:6}')
    self.assertEqual(Beasts.GHOST.versionIds[Version.V26_3], '')

  def test_version_ids_is_a_copy(self) -> None:
    ids = Beasts.BLOB.versionIds
    ids[Version.V26_3] = 'test:changed'
    self.assertEqual(Beasts.BLOB.versionIds[Version.V26_3], 'test:blob')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  ID IN A VERSION  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_getitem(self) -> None:
    cases = {
      Version.V1_7_2: 'Blob',
      Version.V1_10_2: 'Blob',
      Version.V1_11: 'test:blob',
      Version.V26_3: 'test:blob',
    }
    for version_, minecraftId in cases.items():
      with self.subTest(version=version_.name):
        self.assertEqual(Beasts.BLOB[version_],
                         EntityId('blob', minecraftId))

  def test_getitem_split(self) -> None:
    self.assertEqual(Beasts.HUSK['1.10.2'],
                     EntityId('husk', 'Zombie{ZombieType:6}'))
    self.assertEqual(Beasts.HUSK['1.11'].minecraftId, 'test:husk')

  def test_getitem_text_and_mc_version(self) -> None:
    blob = Beasts.BLOB
    self.assertEqual(blob['1.10.2'].minecraftId, 'Blob')
    self.assertEqual(blob[MCVersion(1, 11)].minecraftId, 'test:blob')
    self.assertEqual(blob['V1_12_2'].minecraftId, 'test:blob')

  def test_getitem_unknown_version(self) -> None:
    for version_ in ('26.4-snapshot-7', '1.2', MCVersion(26, 4), 7):
      with self.subTest(version=version_):
        with self.assertRaises(KeeResolveError):
          _ = Beasts.BLOB[version_]

  def test_not_in_version_before(self) -> None:
    husk = Beasts.HUSK
    with self.assertRaises(NotInVersion) as context:
      _ = husk['1.9.4']
    exception = context.exception
    self.assertIsInstance(exception, WorkToyException)
    self.assertIsInstance(exception, LookupError)
    self.assertIs(exception.item, husk)
    self.assertIs(exception.version, Version.V1_9_4)
    expected = "Vanilla 1.9.4 has no 'husk'; vanilla added it in 1.10!"
    self.assertEqual(str(exception), expected)
    self.assertEqual(repr(exception), expected)

  def test_not_in_version_after(self) -> None:
    with self.assertRaises(NotInVersion) as context:
      _ = Beasts.GHOST['26.3']
    self.assertEqual(
        str(context.exception),
        "Vanilla 26.3 has no 'ghost'; vanilla removed it in 1.21.4!",
    )

  def test_before_the_data(self) -> None:
    with self.assertRaises(ValueError) as context:
      _ = Beasts.BLOB['1.6.4']
    self.assertNotIsInstance(context.exception, NotInVersion)
    self.assertIn("no data on 'blob' before 1.7.2", str(context.exception))
