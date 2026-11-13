"""
NotInVersion is raised when an item or an entity is asked for in a
version of the game that vanilla does not have it in.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.utilities import textFmt
from worktoy.waitaminute import WorkToyException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import MCThing, Version


class NotInVersion(WorkToyException, LookupError):
  """
  NotInVersion subclasses 'LookupError' and is raised when an item or an
  entity is asked for in a version of the game that vanilla does not
  have it in: vanilla 1.7.10 has no elytra yet, vanilla 1.10 no lit
  furnace any more, and vanilla 1.9.4 no stray. A mod may bring the item
  to that version under an id of its own, so this says nothing of
  whether a given game has the item; it is what a test cites when the
  game lacks it:

    Vanilla 1.7.10 has no 'elytra'; vanilla added it in 1.9!
    Vanilla 1.10 has no 'lit_furnace'; vanilla removed it in 1.9!
    Vanilla 1.9.4 has no 'stray'; vanilla added it in 1.10!

  Attributes
  ----------
  item : MCThing
    The thing asked for, a member of its catalogue.
  version : Version
    The version that vanilla does not have it in.
  """

  __slots__ = ('item', 'version')

  def __init__(self, item: MCThing, version: Version) -> None:
    self.item = item
    self.version = version
    LookupError.__init__(self, )

  def __str__(self, ) -> str:
    """
    Names the first later version vanilla has it in; when there is none,
    the version that removed it, after the last one that had it.
    """
    ids = self.item.versionIds
    name_ = self.item.uniqueName
    modifier = getattr(self.item, 'modifier', '')
    if modifier:
      name_ = '%s %s' % (modifier.value, name_)
    later = [v for v, id_ in ids.items() if id_ and v > self.version]
    if later:
      infoSpec = """Vanilla %s has no '%s'; vanilla added it in %s!"""
      info = infoSpec % (self.version.value, name_, later[0].value)
      return textFmt(info)
    last = [v for v, id_ in ids.items() if id_ and v < self.version][-1]
    removed = [v for v, id_ in ids.items() if not id_ and v > last][0]
    infoSpec = """Vanilla %s has no '%s'; vanilla removed it in %s!"""
    info = infoSpec % (self.version.value, name_, removed.value)
    return textFmt(info)

  __repr__ = __str__
