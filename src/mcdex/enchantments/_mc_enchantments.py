"""
MCEnchantments is the catalogue of the game's enchantments: an enumeration with
one member for every enchantment of the data file that ships with mcdex, each
the same enchantment in every version, with the id each version knows it by:
what /enchant takes.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import EnchantmentId, MCThing


class MCEnchantments(MCThing):
  """
  The catalogue of the game's enchantments, each a member, found by its name in
  capitals, in any case, or by its unique name:

    protection = MCEnchantments.PROTECTION
    protection is MCEnchantments['protection']  # True
    protection[Version.V1_7_10]  # EnchantmentId('protection', '0')
    len(MCEnchantments)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'enchantments.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'enchantments.json'
  __data_key__ = 'enchantments'
  __id_class__ = EnchantmentId
  __kind__ = 'enchantment'

  #  Members, one for every name of 'enchantments.json'
  AQUA_AFFINITY = Kee[str]('aqua_affinity')
  BANE_OF_ARTHROPODS = Kee[str]('bane_of_arthropods')
  BINDING_CURSE = Kee[str]('binding_curse')
  BLAST_PROTECTION = Kee[str]('blast_protection')
  BREACH = Kee[str]('breach')
  CHANNELING = Kee[str]('channeling')
  CURSE_OF_BINDING = Kee[str]('curse_of_binding')
  CURSE_OF_VANISHING = Kee[str]('curse_of_vanishing')
  DENSITY = Kee[str]('density')
  DEPTH_STRIDER = Kee[str]('depth_strider')
  EFFICIENCY = Kee[str]('efficiency')
  FEATHER_FALLING = Kee[str]('feather_falling')
  FIRE_ASPECT = Kee[str]('fire_aspect')
  FIRE_PROTECTION = Kee[str]('fire_protection')
  FLAME = Kee[str]('flame')
  FORTUNE = Kee[str]('fortune')
  FROST_WALKER = Kee[str]('frost_walker')
  IMPALING = Kee[str]('impaling')
  INFINITY = Kee[str]('infinity')
  KNOCKBACK = Kee[str]('knockback')
  LOOTING = Kee[str]('looting')
  LOYALTY = Kee[str]('loyalty')
  LUCK_OF_THE_SEA = Kee[str]('luck_of_the_sea')
  LUNGE = Kee[str]('lunge')
  LURE = Kee[str]('lure')
  MENDING = Kee[str]('mending')
  MULTISHOT = Kee[str]('multishot')
  PIERCING = Kee[str]('piercing')
  POWER = Kee[str]('power')
  PROJECTILE_PROTECTION = Kee[str]('projectile_protection')
  PROTECTION = Kee[str]('protection')
  PUNCH = Kee[str]('punch')
  QUICK_CHARGE = Kee[str]('quick_charge')
  RESPIRATION = Kee[str]('respiration')
  RIPTIDE = Kee[str]('riptide')
  SHARPNESS = Kee[str]('sharpness')
  SILK_TOUCH = Kee[str]('silk_touch')
  SMITE = Kee[str]('smite')
  SOUL_SPEED = Kee[str]('soul_speed')
  SWEEPING_EDGE = Kee[str]('sweeping_edge')
  SWIFT_SNEAK = Kee[str]('swift_sneak')
  THORNS = Kee[str]('thorns')
  UNBREAKING = Kee[str]('unbreaking')
  VANISHING_CURSE = Kee[str]('vanishing_curse')
  WIND_BURST = Kee[str]('wind_burst')
