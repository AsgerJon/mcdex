"""
Version enumerates every release of Minecraft, in the order Mojang
released them.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import KeeNum, Kee
from worktoy.waitaminute.keenum import KeeResolveError

from . import MCVersion

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any


class Version(KeeNum):
  """
  Version enumerates every release of Minecraft, in the order Mojang
  released them, from 1.0 to 26.3: 103 members, each holding its
  'MCVersion'. Only real releases are members; there was never a '1.2'
  (the first was 1.2.1) nor a '1.5' (1.5.1). Since 26.1, Mojang numbers
  its releases by year.

  The list is Mojang's own version manifest, as it read on 2026-11-07:
  piston-meta.mojang.com/mc/game/version_manifest_v2.json

  A member resolves from its name, from its 'MCVersion', or from the text
  the game reports, and members order by their versions:

    Version('1.7.10') is Version.V1_7_10
    Version(MCVersion(26, 3)) is Version.V26_3
    Version.V1_7_10 < Version.V1_9

  Implementation
  --------------

  '__class_resolve__' reads a 'str' that names no member as an
  'MCVersion' and resolves that by value; text that reads as no version,
  or as a version that was never released, defers to the enumeration,
  which raises 'KeeResolveError'. Equality is the identity of
  'KeeNum'; the ordering compares the values, and returns
  'NotImplemented' for anything but a member.
  """

  V1_0 = Kee[MCVersion](MCVersion(1, 0, 0))
  V1_1 = Kee[MCVersion](MCVersion(1, 1, 0))
  V1_2_1 = Kee[MCVersion](MCVersion(1, 2, 1))
  V1_2_2 = Kee[MCVersion](MCVersion(1, 2, 2))
  V1_2_3 = Kee[MCVersion](MCVersion(1, 2, 3))
  V1_2_4 = Kee[MCVersion](MCVersion(1, 2, 4))
  V1_2_5 = Kee[MCVersion](MCVersion(1, 2, 5))
  V1_3_1 = Kee[MCVersion](MCVersion(1, 3, 1))
  V1_3_2 = Kee[MCVersion](MCVersion(1, 3, 2))
  V1_4_2 = Kee[MCVersion](MCVersion(1, 4, 2))
  V1_4_4 = Kee[MCVersion](MCVersion(1, 4, 4))
  V1_4_5 = Kee[MCVersion](MCVersion(1, 4, 5))
  V1_4_6 = Kee[MCVersion](MCVersion(1, 4, 6))
  V1_4_7 = Kee[MCVersion](MCVersion(1, 4, 7))
  V1_5_1 = Kee[MCVersion](MCVersion(1, 5, 1))
  V1_5_2 = Kee[MCVersion](MCVersion(1, 5, 2))
  V1_6_1 = Kee[MCVersion](MCVersion(1, 6, 1))
  V1_6_2 = Kee[MCVersion](MCVersion(1, 6, 2))
  V1_6_4 = Kee[MCVersion](MCVersion(1, 6, 4))
  V1_7_2 = Kee[MCVersion](MCVersion(1, 7, 2))
  V1_7_3 = Kee[MCVersion](MCVersion(1, 7, 3))
  V1_7_4 = Kee[MCVersion](MCVersion(1, 7, 4))
  V1_7_5 = Kee[MCVersion](MCVersion(1, 7, 5))
  V1_7_6 = Kee[MCVersion](MCVersion(1, 7, 6))
  V1_7_7 = Kee[MCVersion](MCVersion(1, 7, 7))
  V1_7_8 = Kee[MCVersion](MCVersion(1, 7, 8))
  V1_7_9 = Kee[MCVersion](MCVersion(1, 7, 9))
  V1_7_10 = Kee[MCVersion](MCVersion(1, 7, 10))
  V1_8 = Kee[MCVersion](MCVersion(1, 8, 0))
  V1_8_1 = Kee[MCVersion](MCVersion(1, 8, 1))
  V1_8_2 = Kee[MCVersion](MCVersion(1, 8, 2))
  V1_8_3 = Kee[MCVersion](MCVersion(1, 8, 3))
  V1_8_4 = Kee[MCVersion](MCVersion(1, 8, 4))
  V1_8_5 = Kee[MCVersion](MCVersion(1, 8, 5))
  V1_8_6 = Kee[MCVersion](MCVersion(1, 8, 6))
  V1_8_7 = Kee[MCVersion](MCVersion(1, 8, 7))
  V1_8_8 = Kee[MCVersion](MCVersion(1, 8, 8))
  V1_8_9 = Kee[MCVersion](MCVersion(1, 8, 9))
  V1_9 = Kee[MCVersion](MCVersion(1, 9, 0))
  V1_9_1 = Kee[MCVersion](MCVersion(1, 9, 1))
  V1_9_2 = Kee[MCVersion](MCVersion(1, 9, 2))
  V1_9_3 = Kee[MCVersion](MCVersion(1, 9, 3))
  V1_9_4 = Kee[MCVersion](MCVersion(1, 9, 4))
  V1_10 = Kee[MCVersion](MCVersion(1, 10, 0))
  V1_10_1 = Kee[MCVersion](MCVersion(1, 10, 1))
  V1_10_2 = Kee[MCVersion](MCVersion(1, 10, 2))
  V1_11 = Kee[MCVersion](MCVersion(1, 11, 0))
  V1_11_1 = Kee[MCVersion](MCVersion(1, 11, 1))
  V1_11_2 = Kee[MCVersion](MCVersion(1, 11, 2))
  V1_12 = Kee[MCVersion](MCVersion(1, 12, 0))
  V1_12_1 = Kee[MCVersion](MCVersion(1, 12, 1))
  V1_12_2 = Kee[MCVersion](MCVersion(1, 12, 2))
  V1_13 = Kee[MCVersion](MCVersion(1, 13, 0))
  V1_13_1 = Kee[MCVersion](MCVersion(1, 13, 1))
  V1_13_2 = Kee[MCVersion](MCVersion(1, 13, 2))
  V1_14 = Kee[MCVersion](MCVersion(1, 14, 0))
  V1_14_1 = Kee[MCVersion](MCVersion(1, 14, 1))
  V1_14_2 = Kee[MCVersion](MCVersion(1, 14, 2))
  V1_14_3 = Kee[MCVersion](MCVersion(1, 14, 3))
  V1_14_4 = Kee[MCVersion](MCVersion(1, 14, 4))
  V1_15 = Kee[MCVersion](MCVersion(1, 15, 0))
  V1_15_1 = Kee[MCVersion](MCVersion(1, 15, 1))
  V1_15_2 = Kee[MCVersion](MCVersion(1, 15, 2))
  V1_16 = Kee[MCVersion](MCVersion(1, 16, 0))
  V1_16_1 = Kee[MCVersion](MCVersion(1, 16, 1))
  V1_16_2 = Kee[MCVersion](MCVersion(1, 16, 2))
  V1_16_3 = Kee[MCVersion](MCVersion(1, 16, 3))
  V1_16_4 = Kee[MCVersion](MCVersion(1, 16, 4))
  V1_16_5 = Kee[MCVersion](MCVersion(1, 16, 5))
  V1_17 = Kee[MCVersion](MCVersion(1, 17, 0))
  V1_17_1 = Kee[MCVersion](MCVersion(1, 17, 1))
  V1_18 = Kee[MCVersion](MCVersion(1, 18, 0))
  V1_18_1 = Kee[MCVersion](MCVersion(1, 18, 1))
  V1_18_2 = Kee[MCVersion](MCVersion(1, 18, 2))
  V1_19 = Kee[MCVersion](MCVersion(1, 19, 0))
  V1_19_1 = Kee[MCVersion](MCVersion(1, 19, 1))
  V1_19_2 = Kee[MCVersion](MCVersion(1, 19, 2))
  V1_19_3 = Kee[MCVersion](MCVersion(1, 19, 3))
  V1_19_4 = Kee[MCVersion](MCVersion(1, 19, 4))
  V1_20 = Kee[MCVersion](MCVersion(1, 20, 0))
  V1_20_1 = Kee[MCVersion](MCVersion(1, 20, 1))
  V1_20_2 = Kee[MCVersion](MCVersion(1, 20, 2))
  V1_20_3 = Kee[MCVersion](MCVersion(1, 20, 3))
  V1_20_4 = Kee[MCVersion](MCVersion(1, 20, 4))
  V1_20_5 = Kee[MCVersion](MCVersion(1, 20, 5))
  V1_20_6 = Kee[MCVersion](MCVersion(1, 20, 6))
  V1_21 = Kee[MCVersion](MCVersion(1, 21, 0))
  V1_21_1 = Kee[MCVersion](MCVersion(1, 21, 1))
  V1_21_2 = Kee[MCVersion](MCVersion(1, 21, 2))
  V1_21_3 = Kee[MCVersion](MCVersion(1, 21, 3))
  V1_21_4 = Kee[MCVersion](MCVersion(1, 21, 4))
  V1_21_5 = Kee[MCVersion](MCVersion(1, 21, 5))
  V1_21_6 = Kee[MCVersion](MCVersion(1, 21, 6))
  V1_21_7 = Kee[MCVersion](MCVersion(1, 21, 7))
  V1_21_8 = Kee[MCVersion](MCVersion(1, 21, 8))
  V1_21_9 = Kee[MCVersion](MCVersion(1, 21, 9))
  V1_21_10 = Kee[MCVersion](MCVersion(1, 21, 10))
  V1_21_11 = Kee[MCVersion](MCVersion(1, 21, 11))
  V26_1 = Kee[MCVersion](MCVersion(26, 1, 0))
  V26_1_1 = Kee[MCVersion](MCVersion(26, 1, 1))
  V26_1_2 = Kee[MCVersion](MCVersion(26, 1, 2))
  V26_2 = Kee[MCVersion](MCVersion(26, 2, 0))
  V26_3 = Kee[MCVersion](MCVersion(26, 3, 0))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def __class_resolve__(cls, identifier: Any) -> Any:
    """
    Resolves the text the game reports, as '1.7.10', to its member, or
    returns 'NotImplemented'.
    """
    if not isinstance(identifier, str):
      return NotImplemented
    try:
      return cls.fromValue(MCVersion(identifier))
    except (ValueError, KeeResolveError):
      return NotImplemented

  def __lt__(self, other: Any) -> bool:
    if isinstance(other, Version):
      return self.value < other.value
    return NotImplemented

  def __le__(self, other: Any) -> bool:
    if isinstance(other, Version):
      return self.value <= other.value
    return NotImplemented

  def __gt__(self, other: Any) -> bool:
    if isinstance(other, Version):
      return self.value > other.value
    return NotImplemented

  def __ge__(self, other: Any) -> bool:
    if isinstance(other, Version):
      return self.value >= other.value
    return NotImplemented
