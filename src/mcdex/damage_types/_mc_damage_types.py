"""
MCDamageTypes is the catalogue of the game's damage types: an enumeration with
one member for every damage type of the data file that ships with mcdex, each
the same damage type in every version, with the id each version knows it by:
what /damage takes.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import DamageTypeId, MCThing


class MCDamageTypes(MCThing):
  """
  The catalogue of the game's damage types, each a member, found by its name in
  capitals, in any case, or by its unique name:

    inFire = MCDamageTypes.IN_FIRE
    inFire is MCDamageTypes['in_fire']  # True
    inFire[Version.V1_19_4]  # DamageTypeId('in_fire', 'minecraft:in_fire')
    len(MCDamageTypes)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'damage_types.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'damage_types.json'
  __data_key__ = 'damage_types'
  __id_class__ = DamageTypeId
  __kind__ = 'damage type'

  #  Members, one for every name of 'damage_types.json'
  ARROW = Kee[str]('arrow')
  BAD_RESPAWN_POINT = Kee[str]('bad_respawn_point')
  CACTUS = Kee[str]('cactus')
  CAMPFIRE = Kee[str]('campfire')
  CRAMMING = Kee[str]('cramming')
  DRAGON_BREATH = Kee[str]('dragon_breath')
  DROWN = Kee[str]('drown')
  DRY_OUT = Kee[str]('dry_out')
  ENDER_PEARL = Kee[str]('ender_pearl')
  EXPLOSION = Kee[str]('explosion')
  FALL = Kee[str]('fall')
  FALLING_ANVIL = Kee[str]('falling_anvil')
  FALLING_BLOCK = Kee[str]('falling_block')
  FALLING_STALACTITE = Kee[str]('falling_stalactite')
  FIREBALL = Kee[str]('fireball')
  FIREWORKS = Kee[str]('fireworks')
  FLY_INTO_WALL = Kee[str]('fly_into_wall')
  FREEZE = Kee[str]('freeze')
  GENERIC = Kee[str]('generic')
  GENERIC_KILL = Kee[str]('generic_kill')
  HOT_FLOOR = Kee[str]('hot_floor')
  IN_FIRE = Kee[str]('in_fire')
  IN_WALL = Kee[str]('in_wall')
  INDIRECT_MAGIC = Kee[str]('indirect_magic')
  LAVA = Kee[str]('lava')
  LIGHTNING_BOLT = Kee[str]('lightning_bolt')
  MACE_SMASH = Kee[str]('mace_smash')
  MAGIC = Kee[str]('magic')
  MOB_ATTACK = Kee[str]('mob_attack')
  MOB_ATTACK_NO_AGGRO = Kee[str]('mob_attack_no_aggro')
  MOB_PROJECTILE = Kee[str]('mob_projectile')
  ON_FIRE = Kee[str]('on_fire')
  OUT_OF_WORLD = Kee[str]('out_of_world')
  OUTSIDE_BORDER = Kee[str]('outside_border')
  PLAYER_ATTACK = Kee[str]('player_attack')
  PLAYER_EXPLOSION = Kee[str]('player_explosion')
  SONIC_BOOM = Kee[str]('sonic_boom')
  SPEAR = Kee[str]('spear')
  SPIT = Kee[str]('spit')
  STALAGMITE = Kee[str]('stalagmite')
  STARVE = Kee[str]('starve')
  STING = Kee[str]('sting')
  SULFUR_CUBE_HOT = Kee[str]('sulfur_cube_hot')
  SWEET_BERRY_BUSH = Kee[str]('sweet_berry_bush')
  THORNS = Kee[str]('thorns')
  THROWN = Kee[str]('thrown')
  TRIDENT = Kee[str]('trident')
  UNATTRIBUTED_FIREBALL = Kee[str]('unattributed_fireball')
  WIND_CHARGE = Kee[str]('wind_charge')
  WITHER = Kee[str]('wither')
  WITHER_SKULL = Kee[str]('wither_skull')
