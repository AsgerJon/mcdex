"""
MCVersion encapsulates Minecraft versions. The releases are enumerated by
the 'Version' class, whose member values are instances of 'MCVersion'.
This allows for versions missing from the enumeration, such as
particular snapshots.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import re
from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.desc import FixBox
from worktoy.mcls import BaseObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, TypeAlias

  Key: TypeAlias = tuple[int, int, int]


class MCVersion(BaseObject):
  """
  A Minecraft version is three numbers, as 1.7.10, written with the last
  left out when it is zero, as 26.3 or 1.8. Versions must compare as
  numbers, so that 1.9 comes before 1.10, be equal by their numbers, key
  a dictionary, and be read from the text the game reports:

    MCVersion(1, 7, 10)
    MCVersion(26, 3)          # 26.3.0
    MCVersion('1.7.10')
    str(MCVersion(26, 3, 0))  # '26.3'

  Implementation
  --------------

  'major', 'minor' and 'micro' are 'FixBox[int]', written once by the
  constructor, so a version never changes and hashes the same for life.
  The constructor takes three components, two with 'micro' zero, or
  their text, and refuses a negative component or text other than two
  or three dot separated decimals without leading zeros with
  'ValueError'. Equality, hash and ordering compare the tuple of the
  three components, so 26.3 and 26.3.0 are one version. A comparison
  with anything but an 'MCVersion' returns 'NotImplemented'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __text_pattern__ = re.compile(
      r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:\.(0|[1-9][0-9]*))?'
  )

  #  Public Variables
  major = FixBox[int]()
  minor = FixBox[int]()
  micro = FixBox[int]()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self, ) -> str:
    """'1.7.10', or '26.3' when 'micro' is zero."""
    if self.micro:
      return '%d.%d.%d' % self._key()
    return '%d.%d' % (self.major, self.minor)

  def __repr__(self, ) -> str:
    """'MCVersion(1, 7, 10)', which evaluates to an equal version."""
    return '%s(%d, %d, %d)' % (type(self).__name__, *self._key())

  def __eq__(self, other: Any) -> bool:
    if isinstance(other, MCVersion):
      return self._key() == other._key()
    return NotImplemented

  def __hash__(self, ) -> int:
    return hash(self._key())

  def __lt__(self, other: Any) -> bool:
    if isinstance(other, MCVersion):
      return self._key() < other._key()
    return NotImplemented

  def __le__(self, other: Any) -> bool:
    if isinstance(other, MCVersion):
      return self._key() <= other._key()
    return NotImplemented

  def __gt__(self, other: Any) -> bool:
    if isinstance(other, MCVersion):
      return self._key() > other._key()
    return NotImplemented

  def __ge__(self, other: Any) -> bool:
    if isinstance(other, MCVersion):
      return self._key() >= other._key()
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int, int)
  def __init__(self, major: int, minor: int, micro: int) -> None:
    for name_, value_ in (('major', major), ('minor', minor),
                          ('micro', micro)):
      if value_ < 0:
        infoSpec = """%s() received a negative '%s': %d"""
        info = infoSpec % (type(self).__name__, name_, value_)
        raise ValueError(info)
    self.major = major
    self.minor = minor
    self.micro = micro

  @overload(int, int)
  def __init__(self, major: int, minor: int) -> None:
    self.__init__(major, minor, 0)

  @overload(str)
  def __init__(self, text: str) -> None:
    if (match_ := self.__text_pattern__.fullmatch(text)) is None:
      infoSpec = """%s() cannot read a version from: '%s'"""
      info = infoSpec % (type(self).__name__, text)
      raise ValueError(info)
    major, minor, micro = match_.groups(default='0')
    self.__init__(int(major), int(minor), int(micro))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _key(self, ) -> Key:
    """The three components as one tuple, for comparisons and hashing."""
    return (self.major, self.minor, self.micro)
