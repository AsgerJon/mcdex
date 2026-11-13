"""
MCPotions is the catalogue of the game's potions: an enumeration with one
member for every potion of the data file that ships with mcdex, each the same
potion in every version, with the id each version knows it by: the potion an
item is made with: from 1.9 its name, before it the potion item's damage value.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..base import MCThing, PotionId, PotionModifier
from ._modified_potion import ModifiedPotion

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any


class MCPotions(MCThing):
  """
  The catalogue of the game's potions, each a member, found by its name in
  capitals, in any case, or by its unique name:

    swiftness = MCPotions.SWIFTNESS
    swiftness is MCPotions['swiftness']  # True
    swiftness[Version.V1_8_9]  # PotionId('swiftness', '2')
    len(MCPotions)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'potions.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'potions.json'
  __data_key__ = 'potions'
  __id_class__ = PotionId
  __kind__ = 'potion'

  #  Private Variables
  __modified_potions__: dict = {}

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def __class_resolve__(cls, identifier: Any) -> Any:
    """
    A potion by its unique name, as in any catalogue; or a base potion
    with a modifier, 'MCPotions[MCPotions.NIGHT_VISION,
    PotionModifier.LONG]' or 'MCPotions["night_vision", "long"]': the
    long or strong potion, a 'ModifiedPotion', the same object every
    time. A base potion the game has no such potion of raises 'KeyError'.
    """
    if not isinstance(identifier, tuple) or len(identifier) != 2:
      return super().__class_resolve__(identifier)
    base, modifier = cls(identifier[0]), PotionModifier(identifier[1])
    key = (base, modifier)
    if key not in cls.__modified_potions__:
      if modifier.value not in base._record():
        infoSpec = """mcdex has no %s %s potion"""
        raise KeyError(infoSpec % (modifier.value, base.uniqueName))
      cls.__modified_potions__[key] = ModifiedPotion(base, modifier)
    return cls.__modified_potions__[key]

  #  Members, one for every name of 'potions.json'
  AWKWARD = Kee[str]('awkward')
  EMPTY = Kee[str]('empty')
  FIRE_RESISTANCE = Kee[str]('fire_resistance')
  HARMING = Kee[str]('harming')
  HEALING = Kee[str]('healing')
  INFESTED = Kee[str]('infested')
  INVISIBILITY = Kee[str]('invisibility')
  LEAPING = Kee[str]('leaping')
  LUCK = Kee[str]('luck')
  MUNDANE = Kee[str]('mundane')
  NIGHT_VISION = Kee[str]('night_vision')
  OOZING = Kee[str]('oozing')
  POISON = Kee[str]('poison')
  REGENERATION = Kee[str]('regeneration')
  SLOW_FALLING = Kee[str]('slow_falling')
  SLOWNESS = Kee[str]('slowness')
  STRENGTH = Kee[str]('strength')
  SWIFTNESS = Kee[str]('swiftness')
  THICK = Kee[str]('thick')
  TURTLE_MASTER = Kee[str]('turtle_master')
  WATER = Kee[str]('water')
  WATER_BREATHING = Kee[str]('water_breathing')
  WEAKNESS = Kee[str]('weakness')
  WEAVING = Kee[str]('weaving')
  WIND_CHARGED = Kee[str]('wind_charged')
