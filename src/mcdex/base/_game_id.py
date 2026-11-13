"""
GameId pairs a thing's unique name with the id a version of the game
needs to identify it: the shared code of each kind's own id class.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.desc import FixBox
from worktoy.mcls import BaseObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, TypeAlias

  Key: TypeAlias = tuple[str, str]


class GameId(BaseObject):
  """
  The id of one thing of the game in one version: its 'uniqueName', the
  same in every version, and its 'minecraftId', all that version needs
  to identify it, as one string in the notation of its era. Each kind of
  thing has its own subclass, as 'EntityId' and 'BlockId', and an id of
  one kind is never equal to an id of another, even with the same text:
  the pig and its spawn egg are different things.

  Implementation
  --------------

  'uniqueName' and 'minecraftId' are 'FixBox[str]', written once by the
  constructor, which refuses an empty one with 'ValueError'. The text of
  an id is its 'minecraftId'. Equality and hash compare the class and
  both strings; anything but an id of the same class compares as
  'NotImplemented'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Public Variables
  uniqueName = FixBox[str]()
  minecraftId = FixBox[str]()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self, ) -> str:
    """The 'minecraftId', as 'minecraft:wool:6'."""
    return self.minecraftId

  def __repr__(self, ) -> str:
    """"BlockId('pink_wool', 'minecraft:wool:6')", which evaluates back."""
    return '%s(%r, %r)' % (type(self).__name__, *self._key())

  def __eq__(self, other: Any) -> bool:
    if type(other) is type(self):
      return self._key() == other._key()
    return NotImplemented

  def __hash__(self, ) -> int:
    return hash((type(self).__name__,) + self._key())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, str)
  def __init__(self, uniqueName: str, minecraftId: str) -> None:
    for name_, value_ in (('uniqueName', uniqueName),
                          ('minecraftId', minecraftId)):
      if not value_:
        infoSpec = """%s() received an empty '%s'"""
        raise ValueError(infoSpec % (type(self).__name__, name_))
    self.uniqueName = uniqueName
    self.minecraftId = minecraftId

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _key(self, ) -> Key:
    """The unique name and the minecraft id, for comparisons and hash."""
    return (self.uniqueName, self.minecraftId)
