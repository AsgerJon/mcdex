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


class MCEnchantments(MCThing, strictCase=False):
  """
  The catalogue of the game's enchantments, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    protection = MCEnchantments.Protection
    protection is MCEnchantments['protection']  # True
    protection[Version.V1_7_10]  # EnchantmentId('protection', '0')
    len(MCEnchantments)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'enchantments.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'enchantments.json'
  __data_key__ = 'enchantments'
  __id_class__ = EnchantmentId
  __kind__ = 'enchantment'

  #  Members, one for every thing of 'enchantments.json'
  AquaAffinity = Kee[str]('aqua_affinity')
  BaneOfArthropods = Kee[str]('bane_of_arthropods')
  BindingCurse = Kee[str]('binding_curse')
  BlastProtection = Kee[str]('blast_protection')
  Breach = Kee[str]('breach')
  Channeling = Kee[str]('channeling')
  CurseOfBinding = Kee[str]('curse_of_binding')
  CurseOfVanishing = Kee[str]('curse_of_vanishing')
  Density = Kee[str]('density')
  DepthStrider = Kee[str]('depth_strider')
  Efficiency = Kee[str]('efficiency')
  FeatherFalling = Kee[str]('feather_falling')
  FireAspect = Kee[str]('fire_aspect')
  FireProtection = Kee[str]('fire_protection')
  Flame = Kee[str]('flame')
  Fortune = Kee[str]('fortune')
  FrostWalker = Kee[str]('frost_walker')
  Impaling = Kee[str]('impaling')
  Infinity = Kee[str]('infinity')
  Knockback = Kee[str]('knockback')
  Looting = Kee[str]('looting')
  Loyalty = Kee[str]('loyalty')
  LuckOfTheSea = Kee[str]('luck_of_the_sea')
  Lunge = Kee[str]('lunge')
  Lure = Kee[str]('lure')
  Mending = Kee[str]('mending')
  Multishot = Kee[str]('multishot')
  Piercing = Kee[str]('piercing')
  Power = Kee[str]('power')
  ProjectileProtection = Kee[str]('projectile_protection')
  Protection = Kee[str]('protection')
  Punch = Kee[str]('punch')
  QuickCharge = Kee[str]('quick_charge')
  Respiration = Kee[str]('respiration')
  Riptide = Kee[str]('riptide')
  Sharpness = Kee[str]('sharpness')
  SilkTouch = Kee[str]('silk_touch')
  Smite = Kee[str]('smite')
  SoulSpeed = Kee[str]('soul_speed')
  SweepingEdge = Kee[str]('sweeping_edge')
  SwiftSneak = Kee[str]('swift_sneak')
  Thorns = Kee[str]('thorns')
  Unbreaking = Kee[str]('unbreaking')
  VanishingCurse = Kee[str]('vanishing_curse')
  WindBurst = Kee[str]('wind_burst')
