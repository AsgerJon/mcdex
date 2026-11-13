"""
ItemId pairs an item's unique name with the id a version of the game
needs to identify it.
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


class ItemId(BaseObject):
  """
  A user of mcdex names an item once, by its unique name, as
  'pink_wool', and each version of the game needs its own id for it.
  'ItemId' holds the two: 'uniqueName', the same in every version, and
  'minecraftId', all that one version needs to identify the item, as
  one string in the notation of its era:

    ItemId('pink_wool', '35:6')                 # before 1.7.2
    ItemId('pink_wool', 'minecraft:wool:6')     # 1.7.2 to 1.12.2
    ItemId('pink_wool', 'minecraft:pink_wool')  # since 1.13

  Before 1.7.2 the game had only numbers, the id and the meta value;
  then names, with the meta where it told items apart; and since 1.13
  the name alone. A meta that is only damage, as the elytra's was, is no
  part of the id. A registry name has no ':' in its path, so a trailing
  ':6' is always the meta. An item the game told apart by NBT carries it
  after the name, as the /give command takes it: a creeper spawn egg of
  1.12.2 is 'minecraft:spawn_egg{EntityTag:{id:"minecraft:creeper"}}'.

  Implementation
  --------------

  'uniqueName' and 'minecraftId' are 'FixBox[str]', written once by the
  constructor, which refuses an empty one with 'ValueError'. The text of
  an id is its 'minecraftId'. Equality and hash compare both strings;
  anything but an 'ItemId' compares as 'NotImplemented'.
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
    """"ItemId('pink_wool', 'minecraft:wool:6')", which evaluates back."""
    return '%s(%r, %r)' % (type(self).__name__, *self._key())

  def __eq__(self, other: Any) -> bool:
    if isinstance(other, ItemId):
      return self._key() == other._key()
    return NotImplemented

  def __hash__(self, ) -> int:
    return hash(self._key())

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
