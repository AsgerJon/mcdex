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
  #  The same data under a name no member takes: no member of its own.
  'creeper_primed': {'ids': {'1.7.2': 'test:creeper.primed'}},
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


class Beasts(MCThing, strictCase=False):
  """A catalogue of test things, its records given here."""

  __data_records__ = _RECORDS
  __id_class__ = EntityId
  __kind__ = 'beast'

  Blob = Kee[str]('blob')
  Husk = Kee[str]('husk')
  Ghost = Kee[str]('ghost')
  CreeperPrimed = Kee[str]('creeper.primed')
  LackingNone = Kee[str]('lacking_none')
  LackingEmpty = Kee[str]('lacking_empty')
  LackingNames = Kee[str]('lacking_names')
  Phantom = Kee[str]('phantom')
  MisdatedOld = Kee[str]('misdated_old')
  MisdatedSnapshot = Kee[str]('misdated_snapshot')
  MisdatedWord = Kee[str]('misdated_word')
  MislabeledInt = Kee[str]('mislabeled_int')
  MislabeledNone = Kee[str]('mislabeled_none')
  MislabeledId = Kee[str]('mislabeled_id')
  Nameless = Kee[str]('')
  Stray = Kee[str]('stray')


class Strays(MCThing, strictCase=False):
  """A catalogue whose data names a thing it has no member for."""

  __data_records__ = {
    'kept': {'ids': {'1.7.2': 'test:kept'}},
    'lost': {'ids': {'1.7.2': 'test:lost'}},
  }
  __id_class__ = EntityId
  __kind__ = 'stray'

  Kept = Kee[str]('kept')


class TestMCThing(BaseTest):
  """
  TestMCThing tests 'MCThing' and 'CatalogueMeta'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE CATALOGUE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_members(self) -> None:
    blob = Beasts.Blob
    self.assertIsInstance(blob, Beasts)
    self.assertIsInstance(blob, MCThing)
    self.assertEqual(len(Beasts), 16)
    self.assertIs(list(Beasts)[0], blob)

  def test_found_by_name(self) -> None:
    """By the member's name in any case, by its unique name, by position."""
    blob = Beasts.Blob
    self.assertIs(Beasts['blob'], blob)
    self.assertIs(Beasts['BLOB'], blob)
    self.assertIs(Beasts.Blob, blob)
    self.assertIs(Beasts['creeper.primed'], Beasts.CreeperPrimed)
    self.assertIs(Beasts['creeper_primed'], Beasts.CreeperPrimed)
    self.assertIs(Beasts[1], Beasts.Husk)

  def test_names_are_pascal_case(self) -> None:
    self.assertEqual(Beasts.CreeperPrimed.name, 'CreeperPrimed')
    self.assertEqual(Beasts.MisdatedSnapshot.name, 'MisdatedSnapshot')

  def test_data_name_without_member(self) -> None:
    """
    A name of the data that no member has, nor any member's data, is a
    mistake of the data, raised at the first lookup by a name.
    """
    with self.assertRaises(ValueError) as context:
      _ = Strays['lost']
    self.assertIn("'lost' of the data is no stray's name, nor has the "
                  "data of one", str(context.exception))

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
    self.assertIn('creeper_primed', Beasts)
    self.assertIn(Beasts.Blob, Beasts)
    self.assertNotIn('blop', Beasts)
    self.assertNotIn(1, Beasts)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  A MEMBER   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_unique_name(self) -> None:
    self.assertEqual(Beasts.Blob.uniqueName, 'blob')
    self.assertIs(type(Beasts.Blob.uniqueName), str)
    self.assertEqual(Beasts.CreeperPrimed.uniqueName, 'creeper.primed')

  def test_frozen(self) -> None:
    with self.assertRaises(KeeWriteOnceError):
      Beasts.Blob.uniqueName = 'slime'

  def test_text(self) -> None:
    self.assertEqual(str(Beasts.Blob), '<Beasts>.Blob')
    self.assertEqual(repr(Beasts.Blob), '<Beasts>.Blob')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE RECORD   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_empty_name(self) -> None:
    with self.assertRaises(ValueError) as context:
      _ = Beasts.Nameless['1.7.2']
    self.assertIn("Beasts.Nameless has an empty 'uniqueName'",
                  str(context.exception))

  def test_no_record(self) -> None:
    with self.assertRaises(ValueError) as context:
      _ = Beasts.Stray['1.7.2']
    self.assertIn("Beasts('stray') has no record in the data",
                  str(context.exception))

  def test_record_lacks_ids(self) -> None:
    for beast in (Beasts.LackingNone, Beasts.LackingEmpty,
                  Beasts.LackingNames):
      with self.subTest(beast=beast):
        with self.assertRaises(ValueError) as context:
          _ = beast.versionIds
        self.assertIn("Beasts('%s') received no 'ids'" % beast.uniqueName,
                      str(context.exception))

  def test_in_no_version(self) -> None:
    with self.assertRaises(ValueError) as context:
      _ = Beasts.Phantom['1.9']
    self.assertIn("Beasts('phantom') is in no version",
                  str(context.exception))

  def test_unknown_version(self) -> None:
    for beast in (Beasts.MisdatedOld, Beasts.MisdatedSnapshot,
                  Beasts.MisdatedWord):
      with self.subTest(beast=beast):
        with self.assertRaises(KeeResolveError):
          _ = beast['1.7.2']

  def test_id_not_str(self) -> None:
    for beast in (Beasts.MislabeledInt, Beasts.MislabeledNone,
                  Beasts.MislabeledId):
      with self.subTest(beast=beast):
        with self.assertRaises(TypeException):
          _ = beast['1.7.2']

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  VERSION IDS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_version_ids_every_version(self) -> None:
    """A key for every 'Version' from the first version of the data."""
    expected = [v for v in Version if v >= Version.V1_7_2]
    for beast in (Beasts.Blob, Beasts.Husk, Beasts.Ghost):
      with self.subTest(beast=beast):
        self.assertEqual(list(beast.versionIds), expected)

  def test_version_ids_values(self) -> None:
    ids = Beasts.Blob.versionIds
    for version_ in ids:
      with self.subTest(version=version_.name):
        if version_ < Version.V1_11:
          self.assertEqual(ids[version_], 'Blob')
        else:
          self.assertEqual(ids[version_], 'test:blob')

  def test_version_ids_absent(self) -> None:
    self.assertEqual(Beasts.Husk.versionIds[Version.V1_9_4], '')
    self.assertEqual(Beasts.Husk.versionIds[Version.V1_10],
                     'Zombie{ZombieType:6}')
    self.assertEqual(Beasts.Ghost.versionIds[Version.V26_3], '')

  def test_version_ids_is_a_copy(self) -> None:
    ids = Beasts.Blob.versionIds
    ids[Version.V26_3] = 'test:changed'
    self.assertEqual(Beasts.Blob.versionIds[Version.V26_3], 'test:blob')

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
        self.assertEqual(Beasts.Blob[version_],
                         EntityId('blob', minecraftId))

  def test_getitem_split(self) -> None:
    self.assertEqual(Beasts.Husk['1.10.2'],
                     EntityId('husk', 'Zombie{ZombieType:6}'))
    self.assertEqual(Beasts.Husk['1.11'].minecraftId, 'test:husk')

  def test_getitem_text_and_mc_version(self) -> None:
    blob = Beasts.Blob
    self.assertEqual(blob['1.10.2'].minecraftId, 'Blob')
    self.assertEqual(blob[MCVersion(1, 11)].minecraftId, 'test:blob')
    self.assertEqual(blob['V1_12_2'].minecraftId, 'test:blob')

  def test_getitem_unknown_version(self) -> None:
    for version_ in ('26.4-snapshot-7', '1.2', MCVersion(26, 4), 7):
      with self.subTest(version=version_):
        with self.assertRaises(KeeResolveError):
          _ = Beasts.Blob[version_]

  def test_not_in_version_before(self) -> None:
    husk = Beasts.Husk
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
      _ = Beasts.Ghost['26.3']
    self.assertEqual(
        str(context.exception),
        "Vanilla 26.3 has no 'ghost'; vanilla removed it in 1.21.4!",
    )

  def test_before_the_data(self) -> None:
    with self.assertRaises(ValueError) as context:
      _ = Beasts.Blob['1.6.4']
    self.assertNotIsInstance(context.exception, NotInVersion)
    self.assertIn("no data on 'blob' before 1.7.2", str(context.exception))
