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


class MCAttributes(MCThing):
  """
  The catalogue of the game's attributes, each a member, found by its name in
  capitals, in any case, or by its unique name:

    maxHealth = MCAttributes.MAX_HEALTH
    maxHealth is MCAttributes['max_health']  # True
    maxHealth[Version.V1_15_2]
    # AttributeId('max_health', 'generic.maxHealth')
    len(MCAttributes)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'attributes.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'attributes.json'
  __data_key__ = 'attributes'
  __id_class__ = AttributeId
  __kind__ = 'attribute'

  #  Members, one for every name of 'attributes.json'
  AIR_DRAG_MODIFIER = Kee[str]('air_drag_modifier')
  ARMOR = Kee[str]('armor')
  ARMOR_TOUGHNESS = Kee[str]('armor_toughness')
  ATTACK_DAMAGE = Kee[str]('attack_damage')
  ATTACK_KNOCKBACK = Kee[str]('attack_knockback')
  ATTACK_SPEED = Kee[str]('attack_speed')
  BELOW_NAME_DISTANCE = Kee[str]('below_name_distance')
  BLOCK_BREAK_SPEED = Kee[str]('block_break_speed')
  BLOCK_INTERACTION_RANGE = Kee[str]('block_interaction_range')
  BOUNCINESS = Kee[str]('bounciness')
  BURNING_TIME = Kee[str]('burning_time')
  CAMERA_DISTANCE = Kee[str]('camera_distance')
  ENTITY_INTERACTION_RANGE = Kee[str]('entity_interaction_range')
  EXPLOSION_KNOCKBACK_RESISTANCE = Kee[str]('explosion_knockback_resistance')
  FALL_DAMAGE_MULTIPLIER = Kee[str]('fall_damage_multiplier')
  FLYING_SPEED = Kee[str]('flying_speed')
  FOLLOW_RANGE = Kee[str]('follow_range')
  FRICTION_MODIFIER = Kee[str]('friction_modifier')
  GRAVITY = Kee[str]('gravity')
  JUMP_STRENGTH = Kee[str]('jump_strength')
  KNOCKBACK_RESISTANCE = Kee[str]('knockback_resistance')
  LUCK = Kee[str]('luck')
  MAX_ABSORPTION = Kee[str]('max_absorption')
  MAX_HEALTH = Kee[str]('max_health')
  MINING_EFFICIENCY = Kee[str]('mining_efficiency')
  MOVEMENT_EFFICIENCY = Kee[str]('movement_efficiency')
  MOVEMENT_SPEED = Kee[str]('movement_speed')
  NAME_TAG_DISTANCE = Kee[str]('name_tag_distance')
  OXYGEN_BONUS = Kee[str]('oxygen_bonus')
  SAFE_FALL_DISTANCE = Kee[str]('safe_fall_distance')
  SCALE = Kee[str]('scale')
  SNEAKING_SPEED = Kee[str]('sneaking_speed')
  SPAWN_REINFORCEMENTS = Kee[str]('spawn_reinforcements')
  STEP_HEIGHT = Kee[str]('step_height')
  SUBMERGED_MINING_SPEED = Kee[str]('submerged_mining_speed')
  SWEEPING_DAMAGE_RATIO = Kee[str]('sweeping_damage_ratio')
  TEMPT_RANGE = Kee[str]('tempt_range')
  WATER_MOVEMENT_EFFICIENCY = Kee[str]('water_movement_efficiency')
  WAYPOINT_RECEIVE_RANGE = Kee[str]('waypoint_receive_range')
  WAYPOINT_TRANSMIT_RANGE = Kee[str]('waypoint_transmit_range')
  ZOMBIE_REINFORCEMENTS = Kee[str]('zombie_reinforcements')
