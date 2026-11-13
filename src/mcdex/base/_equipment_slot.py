"""
EquipmentSlot enumerates the slots an entity wears or holds an item in.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import KeeNum, Kee


class EquipmentSlot(KeeNum):
  """
  An item goes to one slot when an entity equips it: the elytra to the
  chest, a helmet to the head, a shield to the offhand, horse armor to a
  horse's body, a saddle to its saddle, and every other item to the main
  hand. EquipmentSlot enumerates those slots, in the order of the game's
  own enumeration as of 26.3, each holding the name the game serializes
  it by:

    EquipmentSlot('chest') is EquipmentSlot.CHEST

  The offhand arrived in 1.9, the body in 1.20.5 and the saddle in
  1.21.5; before each, an item that would go there went to the main
  hand.
  """

  MAINHAND = Kee[str]('mainhand')
  OFFHAND = Kee[str]('offhand')
  FEET = Kee[str]('feet')
  LEGS = Kee[str]('legs')
  CHEST = Kee[str]('chest')
  HEAD = Kee[str]('head')
  BODY = Kee[str]('body')
  SADDLE = Kee[str]('saddle')
