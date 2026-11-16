"""
MCAttributes is the catalogue of the game's attributes: an enumeration with one
member for every attribute of the data file that ships with mcdex, each the
same attribute in every version, with the id each version knows it by:
the name an entity's data gives it, and from 1.16 what /attribute takes.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import AttributeId, MCThing


class MCAttributes(MCThing, strictCase=False):
  """
  The catalogue of the game's attributes, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    maxHealth = MCAttributes.MaxHealth
    maxHealth is MCAttributes['max_health']  # True
    maxHealth[Version.V1_15_2]
    # AttributeId('max_health', 'generic.maxHealth')
    len(MCAttributes)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'attributes.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'attributes.json'
  __data_key__ = 'attributes'
  __id_class__ = AttributeId
  __kind__ = 'attribute'

  #  Members, one for every thing of 'attributes.json'
  AirDragModifier = Kee[str]('air_drag_modifier')
  Armor = Kee[str]('armor')
  ArmorToughness = Kee[str]('armor_toughness')
  AttackDamage = Kee[str]('attack_damage')
  AttackKnockback = Kee[str]('attack_knockback')
  AttackSpeed = Kee[str]('attack_speed')
  BelowNameDistance = Kee[str]('below_name_distance')
  BlockBreakSpeed = Kee[str]('block_break_speed')
  BlockInteractionRange = Kee[str]('block_interaction_range')
  Bounciness = Kee[str]('bounciness')
  BurningTime = Kee[str]('burning_time')
  CameraDistance = Kee[str]('camera_distance')
  EntityInteractionRange = Kee[str]('entity_interaction_range')
  ExplosionKnockbackResistance = Kee[str]('explosion_knockback_resistance')
  FallDamageMultiplier = Kee[str]('fall_damage_multiplier')
  FlyingSpeed = Kee[str]('flying_speed')
  FollowRange = Kee[str]('follow_range')
  FrictionModifier = Kee[str]('friction_modifier')
  Gravity = Kee[str]('gravity')
  JumpStrength = Kee[str]('jump_strength')
  KnockbackResistance = Kee[str]('knockback_resistance')
  Luck = Kee[str]('luck')
  MaxAbsorption = Kee[str]('max_absorption')
  MaxHealth = Kee[str]('max_health')
  MiningEfficiency = Kee[str]('mining_efficiency')
  MovementEfficiency = Kee[str]('movement_efficiency')
  MovementSpeed = Kee[str]('movement_speed')
  NameTagDistance = Kee[str]('name_tag_distance')
  OxygenBonus = Kee[str]('oxygen_bonus')
  SafeFallDistance = Kee[str]('safe_fall_distance')
  Scale = Kee[str]('scale')
  SneakingSpeed = Kee[str]('sneaking_speed')
  SpawnReinforcements = Kee[str]('spawn_reinforcements')
  StepHeight = Kee[str]('step_height')
  SubmergedMiningSpeed = Kee[str]('submerged_mining_speed')
  SweepingDamageRatio = Kee[str]('sweeping_damage_ratio')
  TemptRange = Kee[str]('tempt_range')
  WaterMovementEfficiency = Kee[str]('water_movement_efficiency')
  WaypointReceiveRange = Kee[str]('waypoint_receive_range')
  WaypointTransmitRange = Kee[str]('waypoint_transmit_range')
  ZombieReinforcements = Kee[str]('zombie_reinforcements')
