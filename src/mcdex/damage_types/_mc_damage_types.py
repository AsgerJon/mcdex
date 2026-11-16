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


class MCDamageTypes(MCThing, strictCase=False):
  """
  The catalogue of the game's damage types, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    inFire = MCDamageTypes.InFire
    inFire is MCDamageTypes['in_fire']  # True
    inFire[Version.V1_19_4]  # DamageTypeId('in_fire', 'minecraft:in_fire')
    len(MCDamageTypes)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'damage_types.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'damage_types.json'
  __data_key__ = 'damage_types'
  __id_class__ = DamageTypeId
  __kind__ = 'damage type'

  #  Members, one for every thing of 'damage_types.json'
  Arrow = Kee[str]('arrow')
  BadRespawnPoint = Kee[str]('bad_respawn_point')
  Cactus = Kee[str]('cactus')
  Campfire = Kee[str]('campfire')
  Cramming = Kee[str]('cramming')
  DragonBreath = Kee[str]('dragon_breath')
  Drown = Kee[str]('drown')
  DryOut = Kee[str]('dry_out')
  EnderPearl = Kee[str]('ender_pearl')
  Explosion = Kee[str]('explosion')
  Fall = Kee[str]('fall')
  FallingAnvil = Kee[str]('falling_anvil')
  FallingBlock = Kee[str]('falling_block')
  FallingStalactite = Kee[str]('falling_stalactite')
  Fireball = Kee[str]('fireball')
  Fireworks = Kee[str]('fireworks')
  FlyIntoWall = Kee[str]('fly_into_wall')
  Freeze = Kee[str]('freeze')
  Generic = Kee[str]('generic')
  GenericKill = Kee[str]('generic_kill')
  HotFloor = Kee[str]('hot_floor')
  InFire = Kee[str]('in_fire')
  InWall = Kee[str]('in_wall')
  IndirectMagic = Kee[str]('indirect_magic')
  Lava = Kee[str]('lava')
  LightningBolt = Kee[str]('lightning_bolt')
  MaceSmash = Kee[str]('mace_smash')
  Magic = Kee[str]('magic')
  MobAttack = Kee[str]('mob_attack')
  MobAttackNoAggro = Kee[str]('mob_attack_no_aggro')
  MobProjectile = Kee[str]('mob_projectile')
  OnFire = Kee[str]('on_fire')
  OutOfWorld = Kee[str]('out_of_world')
  OutsideBorder = Kee[str]('outside_border')
  PlayerAttack = Kee[str]('player_attack')
  PlayerExplosion = Kee[str]('player_explosion')
  SonicBoom = Kee[str]('sonic_boom')
  Spear = Kee[str]('spear')
  Spit = Kee[str]('spit')
  Stalagmite = Kee[str]('stalagmite')
  Starve = Kee[str]('starve')
  Sting = Kee[str]('sting')
  SulfurCubeHot = Kee[str]('sulfur_cube_hot')
  SweetBerryBush = Kee[str]('sweet_berry_bush')
  Thorns = Kee[str]('thorns')
  Thrown = Kee[str]('thrown')
  Trident = Kee[str]('trident')
  UnattributedFireball = Kee[str]('unattributed_fireball')
  WindCharge = Kee[str]('wind_charge')
  Wither = Kee[str]('wither')
  WitherSkull = Kee[str]('wither_skull')
