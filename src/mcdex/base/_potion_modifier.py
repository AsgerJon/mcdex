"""
PotionModifier is the enumeration of what makes a potion more than its
base potion: the game's long and strong potions.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee, KeeNum


class PotionModifier(KeeNum):
  """
  A long potion lasts longer than its base potion, a strong one is
  stronger, as the game makes each of them: the long night vision is the
  night vision potion for 9600 ticks, not 3600. With a base potion, a
  modifier is the potion:

    MCPotions[MCPotions.NIGHT_VISION, PotionModifier.LONG]
    MCPotions['swiftness', 'strong']

  Implementation
  --------------

  A member's value is the word the game names such a potion with, as in
  'minecraft:long_night_vision'.
  """

  LONG = Kee[str]('long')
  STRONG = Kee[str]('strong')
