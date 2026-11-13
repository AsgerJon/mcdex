"""
MCEffects is the catalogue of the game's effects: an enumeration with one
member for every effect of the data file that ships with mcdex, each the
same effect in every version, with the id each version knows it by:
what /effect takes.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import EffectId, MCThing


class MCEffects(MCThing):
  """
  The catalogue of the game's effects, each a member, found by its name in
  capitals, in any case, or by its unique name:

    speed = MCEffects.SPEED
    speed is MCEffects['speed']  # True
    speed['1.7.10']  # EffectId('speed', '1')
    len(MCEffects)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'effects.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'effects.json'
  __data_key__ = 'effects'
  __id_class__ = EffectId
  __kind__ = 'effect'

  #  Members, one for every name of 'effects.json'
  ABSORPTION = Kee[str]('absorption')
  BAD_OMEN = Kee[str]('bad_omen')
  BLINDNESS = Kee[str]('blindness')
  BREATH_OF_THE_NAUTILUS = Kee[str]('breath_of_the_nautilus')
  CONDUIT_POWER = Kee[str]('conduit_power')
  DARKNESS = Kee[str]('darkness')
  DOLPHINS_GRACE = Kee[str]('dolphins_grace')
  FIRE_RESISTANCE = Kee[str]('fire_resistance')
  GLOWING = Kee[str]('glowing')
  HASTE = Kee[str]('haste')
  HEALTH_BOOST = Kee[str]('health_boost')
  HERO_OF_THE_VILLAGE = Kee[str]('hero_of_the_village')
  HUNGER = Kee[str]('hunger')
  INFESTED = Kee[str]('infested')
  INSTANT_DAMAGE = Kee[str]('instant_damage')
  INSTANT_HEALTH = Kee[str]('instant_health')
  INVISIBILITY = Kee[str]('invisibility')
  JUMP_BOOST = Kee[str]('jump_boost')
  LEVITATION = Kee[str]('levitation')
  LUCK = Kee[str]('luck')
  MINING_FATIGUE = Kee[str]('mining_fatigue')
  NAUSEA = Kee[str]('nausea')
  NIGHT_VISION = Kee[str]('night_vision')
  OOZING = Kee[str]('oozing')
  POISON = Kee[str]('poison')
  RAID_OMEN = Kee[str]('raid_omen')
  REGENERATION = Kee[str]('regeneration')
  RESISTANCE = Kee[str]('resistance')
  SATURATION = Kee[str]('saturation')
  SLOW_FALLING = Kee[str]('slow_falling')
  SLOWNESS = Kee[str]('slowness')
  SPEED = Kee[str]('speed')
  STRENGTH = Kee[str]('strength')
  TRIAL_OMEN = Kee[str]('trial_omen')
  UNLUCK = Kee[str]('unluck')
  WATER_BREATHING = Kee[str]('water_breathing')
  WEAKNESS = Kee[str]('weakness')
  WEAVING = Kee[str]('weaving')
  WIND_CHARGED = Kee[str]('wind_charged')
  WITHER = Kee[str]('wither')
