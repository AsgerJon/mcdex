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


class MCEffects(MCThing, strictCase=False):
  """
  The catalogue of the game's effects, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    speed = MCEffects.Speed
    speed is MCEffects['speed']  # True
    speed[Version.V1_7_10]  # EffectId('speed', '1')
    len(MCEffects)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'effects.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'effects.json'
  __data_key__ = 'effects'
  __id_class__ = EffectId
  __kind__ = 'effect'

  #  Members, one for every thing of 'effects.json'
  Absorption = Kee[str]('absorption')
  BadLuck = Kee[str]('bad_luck')
  BadOmen = Kee[str]('bad_omen')
  Blindness = Kee[str]('blindness')
  BreathOfTheNautilus = Kee[str]('breath_of_the_nautilus')
  ConduitPower = Kee[str]('conduit_power')
  Darkness = Kee[str]('darkness')
  DolphinsGrace = Kee[str]('dolphins_grace')
  FireResistance = Kee[str]('fire_resistance')
  Glowing = Kee[str]('glowing')
  Haste = Kee[str]('haste')
  HealthBoost = Kee[str]('health_boost')
  HeroOfTheVillage = Kee[str]('hero_of_the_village')
  Hunger = Kee[str]('hunger')
  Infested = Kee[str]('infested')
  InstantDamage = Kee[str]('instant_damage')
  InstantHealth = Kee[str]('instant_health')
  Invisibility = Kee[str]('invisibility')
  JumpBoost = Kee[str]('jump_boost')
  Levitation = Kee[str]('levitation')
  Luck = Kee[str]('luck')
  MiningFatigue = Kee[str]('mining_fatigue')
  Nausea = Kee[str]('nausea')
  NightVision = Kee[str]('night_vision')
  Oozing = Kee[str]('oozing')
  Poison = Kee[str]('poison')
  RaidOmen = Kee[str]('raid_omen')
  Regeneration = Kee[str]('regeneration')
  Resistance = Kee[str]('resistance')
  Saturation = Kee[str]('saturation')
  SlowFalling = Kee[str]('slow_falling')
  Slowness = Kee[str]('slowness')
  Speed = Kee[str]('speed')
  Strength = Kee[str]('strength')
  TrialOmen = Kee[str]('trial_omen')
  Unluck = Kee[str]('unluck')
  WaterBreathing = Kee[str]('water_breathing')
  Weakness = Kee[str]('weakness')
  Weaving = Kee[str]('weaving')
  WindCharged = Kee[str]('wind_charged')
  Wither = Kee[str]('wither')
