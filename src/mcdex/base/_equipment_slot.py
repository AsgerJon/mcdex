"""
EquipmentSlot enumerates the slots an entity wears or holds an item in.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import KeeNum, Kee


class EquipmentSlot(KeeNum, strictCase=False):
  """
  An item goes to one slot when an entity equips it: the elytra to the
  chest, a helmet to the head, a shield to the offhand, horse armor to a
  horse's body, a saddle to its saddle, and every other item to the main
  hand. EquipmentSlot enumerates those slots, in the order of the game's
  own enumeration as of 26.3, each holding the name the game serializes
  it by:

    EquipmentSlot('chest') is EquipmentSlot.Chest

  The offhand arrived in 1.9, the body in 1.20.5 and the saddle in
  1.21.5; before each, an item that would go there went to the main
  hand.

  The members are named in PascalCase, the game's glued words split as a
  person writes them: 'MainHand' for 'mainhand'.
  """

  MainHand = Kee[str]('mainhand')
  OffHand = Kee[str]('offhand')
  Feet = Kee[str]('feet')
  Legs = Kee[str]('legs')
  Chest = Kee[str]('chest')
  Head = Kee[str]('head')
  Body = Kee[str]('body')
  Saddle = Kee[str]('saddle')
