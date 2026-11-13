"""
ModifiedPotion is a long or a strong potion: a base potion of
'MCPotions' with a 'PotionModifier', and the id each version knows it by.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.desc import Field, FixBox
from worktoy.mcls import BaseObject

from ..base import MCThing, NotInVersion, PotionId, PotionModifier, Version

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, TypeAlias

  VersionIds: TypeAlias = dict[Version, str]
  Changes: TypeAlias = tuple[tuple[int, str], ...]


class ModifiedPotion(BaseObject):
  """
  A long or a strong potion is its base potion with a modifier, as the
  game makes it, and has an id of its own in each version: the long
  night vision is 'minecraft:long_night_vision' in 1.12.2 and '70' in
  1.8.9, the night vision's 6 with the bit for long. 'MCPotions' gives
  it, the same object every time:

    longNightVision = MCPotions[MCPotions.NIGHT_VISION, PotionModifier.LONG]
    longNightVision['1.12.2']
    # PotionId('night_vision', 'minecraft:long_night_vision')
    longNightVision.base        # <MCPotions>.NIGHT_VISION
    longNightVision.modifier    # <PotionModifier>.LONG

  Implementation
  --------------

  Its 'uniqueName' is its base potion's, and its ids are the table the
  data file keeps under the modifier in the base potion's record, read
  at the first use and checked as any thing's ids. Indexing it by a
  version, and 'versionIds', are as for a member of a catalogue.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Private Variables
  __potion_changes__: Changes = ()

  #  Public Variables
  base = FixBox[MCThing]()
  modifier = FixBox[PotionModifier]()
  uniqueName: Field[str] = Field()
  versionIds: Field[VersionIds] = Field()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @uniqueName.GET
  def _getUniqueName(self, ) -> str:
    """The base potion's unique name, as 'night_vision'."""
    return self.base.uniqueName

  @versionIds.GET
  def _getVersionIds(self, ) -> VersionIds:
    """
    The id of the potion in every version from the first version of the
    data, as a new dict, '' where vanilla has no such potion.
    """
    return self.base._tableOf(self._changes())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self, ) -> str:
    """"MCPotions[<MCPotions>.NIGHT_VISION, <PotionModifier>.LONG]"."""
    clsName = type(self.base).__name__
    return '%s[%s, %s]' % (clsName, self.base, self.modifier)

  __repr__ = __str__

  def __getitem__(self, version: Any) -> PotionId:
    """
    The 'PotionId' of the potion in the given version.

    Raises
    ------
    NotInVersion
      Vanilla has no such potion in that version.
    ValueError
      The version is earlier than the data.
    """
    version_ = Version(version)
    position = self.base._position(version_)
    changes = self._changes()
    first, _ = changes[0]
    if position < first:
      infoSpec = """mcdex has no data on %s before %s"""
      info = infoSpec % (self, self.base._versions()[first].value)
      raise ValueError(info)
    id_ = self.base._valueIn(changes, position)
    if not id_:
      raise NotInVersion(self, version_)
    return PotionId(self.uniqueName, id_)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __init__(self, base: MCThing, modifier: PotionModifier) -> None:
    self.base = base
    self.modifier = modifier

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _changes(self, ) -> Changes:
    """The changes of the potion's ids, read and checked at the first call."""
    if not self.__potion_changes__:
      record = self.base._record()[self.modifier.value]
      self.__potion_changes__ = self.base._readIds(
        str(self), self.uniqueName, record.get('ids', {}))
    return self.__potion_changes__
