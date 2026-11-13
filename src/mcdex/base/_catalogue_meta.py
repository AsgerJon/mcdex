"""
CatalogueMeta is the metaclass of mcdex's catalogues: worktoy's
enumeration metaclass, with membership that takes a unique name too.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import KeeMeta

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any


class CatalogueMeta(KeeMeta):
  """
  A catalogue answers whether it has a thing of a name, as well as
  whether a thing is its own:

    'pink_wool' in MCItems          # True
    MCItems.PINK_WOOL in MCItems    # True
    MCBlocks.PINK_WOOL in MCItems   # False

  Implementation
  --------------

  All of it is 'KeeMeta's, but for a 'str', which is in the catalogue
  when it is the unique name of one of its members. The catalogues are
  built on 'CatalogueMeta.keeNum', the root this metaclass gives its
  enumerations.
  """

  def __contains__(cls, identifier: Any) -> bool:
    if isinstance(identifier, str):
      return identifier in cls._byUniqueName()
    return KeeMeta.__contains__(cls, identifier)
