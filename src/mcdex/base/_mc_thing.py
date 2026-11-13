"""
MCThing is the shared base of every catalogue of mcdex, as 'MCEntities'
and 'MCBlocks': an enumeration whose members are the things of one kind
of the game, each the same thing in every version, with the id each
version knows it by.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
from importlib.resources import files
from typing import TYPE_CHECKING

from worktoy.desc import Field
from worktoy.utilities import textFmt
from worktoy.waitaminute import TypeException

from . import CatalogueMeta, GameId, NotInVersion, Version

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, TypeAlias

  VersionIds: TypeAlias = dict[Version, str]
  Changes: TypeAlias = tuple[tuple[int, Any], ...]


class MCThing(CatalogueMeta.keeNum):
  """
  A thing of the game is one thing in every version, whatever each
  version calls it. A catalogue is an enumeration of the things of one
  kind, and each thing is a member of it, made once as the catalogue is:

    pinkWool = MCItems.PINK_WOOL
    pinkWool is MCItems['pink_wool']             # True
    pinkWool['1.12.2']
    # ItemId('pink_wool', 'minecraft:wool:6')
    for item in MCItems: ...                     # every item, in order
    len(MCItems)
    'pink_wool' in MCItems                       # True

  A member's value is its 'uniqueName', mcdex's name for it, the same in
  every version, and indexing the member by a version gives the id that
  version knows it by, an object of the kind's id class
  ('__id_class__').

  Implementation
  --------------

  'MCThing' is the root of 'CatalogueMeta', worktoy's enumeration
  metaclass with membership by unique name too, and has no members of its
  own: each catalogue is a subclass
  declaring one per name of its data file, 'PINK_WOOL = Kee[str](
  "pink_wool")', the member named by the unique name in capitals. A
  subclass names its data file, beside its module ('__data_file__'), the
  key the file keeps the records under ('__data_key__'), its id class
  and, for messages, the word for one ('__kind__'). A test may give the
  records itself instead ('__data_records__').

  The data file is read at the first use of the catalogue, not at
  import, and a member's record at the first use of the member, each
  kept by the catalogue: the members themselves are frozen. A record
  holds one table, 'ids', keyed by the first version each id applies
  from, as version texts or 'Version' members. The ids begin at the
  first version the data covers; an id is the 'minecraftId' of that
  version, or '' where vanilla has no such thing. 'versionIds' is the
  full table of ids, with a key for every 'Version' from the first
  version of the data, built at its first read and returned as a copy.

  A member is found by its name in any case, 'MCItems.Pink_Wool', by its
  unique name, as 'MCItems["pink_wool"]', or by its
  position. A unique name the catalogue lacks raises 'KeyError'. An
  empty unique name, a name the data lacks, a missing or empty table, or
  ids that leave the thing in no version raise 'ValueError' at the first
  use of the member; a version text that names no release raises
  'KeeResolveError'; an id other than a 'str' raises 'TypeException'.
  Versions are compared by their position in 'Version', as comparing the
  members themselves is slow.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __absent__ = ''
  __id_class__: type = GameId
  __kind__ = 'thing'
  __data_file__ = ''
  __data_key__ = ''
  __data_records__: dict = {}

  #  Private Variables
  __all_versions__: dict = {}
  __catalogue_records__: dict = {}
  __unique_names__: dict = {}
  __thing_tables__: dict = {}

  #  Public Variables
  uniqueName: Field[str] = Field()
  versionIds: Field[VersionIds] = Field()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @uniqueName.GET
  def _getUniqueName(self, ) -> str:
    """mcdex's name for the thing, the member's value: 'pink_wool'."""
    return self.value

  @versionIds.GET
  def _getVersionIds(self, ) -> VersionIds:
    """
    The id of the thing in every version from the first version of the
    data, as a new dict, '' where vanilla has no such thing.
    """
    return dict(self._table('ids'))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __getitem__(self, version: Any) -> GameId:
    """
    The id of the thing in the given version, of the kind's id class: its
    'uniqueName' and the 'minecraftId' that version knows it by. The
    version is a 'Version' member, its name, its text as the game reports
    it, or its 'MCVersion'; one 'Version' cannot resolve raises
    'KeeResolveError'.

    Raises
    ------
    NotInVersion
      Vanilla has no such thing in that version.
    ValueError
      The version is earlier than the data.
    """
    version_ = Version(version)
    position = self._position(version_)
    changes = self._changes('ids')
    first, _ = changes[0]
    if position < first:
      infoSpec = """mcdex has no data on '%s' before %s"""
      info = infoSpec % (self.uniqueName, self._versions()[first].value)
      raise ValueError(info)
    id_ = self._valueIn(changes, position)
    if id_ == self.__absent__:
      raise NotInVersion(self, version_)
    return self.__id_class__(self.uniqueName, id_)

  @classmethod
  def __class_resolve__(cls, identifier: Any) -> Any:
    """
    A member by its unique name, where its name in capitals does not
    find it, as '13' for 'THIRTEEN'. A
    unique name the catalogue lacks raises 'KeyError'; anything else
    goes on to the enumeration's other steps.
    """
    if not isinstance(identifier, str):
      return NotImplemented
    found = cls._byUniqueName().get(identifier)
    if found is None:
      infoSpec = """mcdex has no %s named '%s'"""
      raise KeyError(textFmt(infoSpec % (cls.__kind__, identifier)))
    return found

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _versions(cls, ) -> tuple[Version, ...]:
    """Every 'Version', by position, listed at the first call."""
    if not MCThing.__all_versions__:
      MCThing.__all_versions__['all'] = (*Version,)
    return MCThing.__all_versions__['all']

  @classmethod
  def _position(cls, version: Version) -> int:
    """
    The position of the 'Version' among them all, as '_versions' lists
    them; the positions are listed at the first call. The position is the
    enumeration's to give, not the member's: worktoy no longer promises
    the 'index' of a member.
    """
    if 'positions' not in MCThing.__all_versions__:
      versions = cls._versions()
      positions = {version_: i for i, version_ in enumerate(versions)}
      MCThing.__all_versions__['positions'] = positions
    return MCThing.__all_versions__['positions'][version]

  @classmethod
  def _records(cls, ) -> dict:
    """The records of the data file, read at the first call."""
    if cls.__data_records__:
      return cls.__data_records__
    if cls not in MCThing.__catalogue_records__:
      package = cls.__module__.rsplit('.', 1)[0]
      path = files(package).joinpath(cls.__data_file__)
      text = path.read_text('utf-8')
      records = json.loads(text)[cls.__data_key__]
      MCThing.__catalogue_records__[cls] = records
    return MCThing.__catalogue_records__[cls]

  @classmethod
  def _byUniqueName(cls, ) -> dict:
    """The members by their unique names, listed at the first call."""
    if cls not in MCThing.__unique_names__:
      named = {member.value: member for member in cls}
      MCThing.__unique_names__[cls] = named
    return MCThing.__unique_names__[cls]

  def _record(self, ) -> dict:
    """The member's record in the data, checked for its 'ids'."""
    clsName = type(self).__name__
    if not self.value:
      infoSpec = """%s.%s has an empty 'uniqueName'"""
      raise ValueError(infoSpec % (clsName, self.name))
    records = self._records()
    if self.value not in records:
      infoSpec = """%s('%s') has no record in the data"""
      raise ValueError(infoSpec % (clsName, self.value))
    record = records[self.value]
    if not record.get('ids'):
      infoSpec = """%s('%s') received no 'ids'"""
      raise ValueError(infoSpec % (clsName, self.value))
    return record

  def _changes(self, table: str) -> Changes:
    """
    The changes of one of the member's tables, as (position of the first
    version, value), in order, checked and kept at the first call. A
    subclass with tables besides 'ids' reads them in '_read'.
    """
    key = (type(self), self.name, table, 'changes')
    if key not in MCThing.__thing_tables__:
      MCThing.__thing_tables__[key] = self._read(table, self._record())
    return MCThing.__thing_tables__[key]

  def _read(self, table: str, record: dict) -> Changes:
    """
    The changes of the 'ids' table of a record: each id must be a 'str',
    and some version must have the thing.
    """
    return self._readIds(type(self).__name__, self.value, record[table])

  @classmethod
  def _readIds(cls, owner: str, uniqueName: str, ids: dict) -> Changes:
    """
    The changes of a table of ids, each a 'str', some version having the
    thing; 'owner' and 'uniqueName' name the thing in the error.
    """
    out = []
    for key, id_ in ids.items():
      if not isinstance(id_, str):
        raise TypeException('minecraftId', id_, str)
      out.append((cls._position(Version(key)), id_))
    if all(id_ == cls.__absent__ for _, id_ in out):
      infoSpec = """%s('%s') is in no version"""
      raise ValueError(infoSpec % (owner, uniqueName))
    return cls._sorted(out)

  def _table(self, table: str) -> dict:
    """
    A table of the member, a value for each version, built at the first
    call and kept: the ids from the first version of the data.
    """
    key = (type(self), self.name, table, 'table')
    if key not in MCThing.__thing_tables__:
      MCThing.__thing_tables__[key] = self._tableOf(self._changes(table))
    return MCThing.__thing_tables__[key]

  @classmethod
  def _tableOf(cls, changes: Changes) -> dict:
    """A value for each version from the first of the changes."""
    versions = cls._versions()
    first, _ = changes[0]
    return {versions[i]: cls._valueIn(changes, i)
            for i in range(first, len(versions))}

  @staticmethod
  def _sorted(pairs: list) -> Changes:
    return (*sorted(pairs, key=lambda pair: pair[0]),)

  @staticmethod
  def _valueIn(changes: Changes, index: int) -> Any:
    """The value of the last change at or before the position."""
    return [value for first, value in changes if first <= index][-1]
