"""
MCPaintingVariants is the catalogue of the game's painting variants: an
enumeration with one member for every painting variant of the data file that
ships with mcdex, each the same painting variant in every version, with the id
each version knows it by: what /summon takes for a painting of that variant.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import MCThing, PaintingVariantId


class MCPaintingVariants(MCThing):
  """
  The catalogue of the game's painting variants, each a member, found by its
  name in capitals, in any case, or by its unique name:

    donkeyKong = MCPaintingVariants.DONKEY_KONG
    donkeyKong is MCPaintingVariants['donkey_kong']  # True
    donkeyKong['1.12.2']
    # PaintingVariantId('donkey_kong',
    #   'minecraft:painting{Motive:"DonkeyKong"}')
    len(MCPaintingVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'painting_variants.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'painting_variants.json'
  __data_key__ = 'painting_variants'
  __id_class__ = PaintingVariantId
  __kind__ = 'painting variant'

  #  Members, one for every name of 'painting_variants.json'
  ALBAN = Kee[str]('alban')
  AZTEC = Kee[str]('aztec')
  AZTEC2 = Kee[str]('aztec2')
  BACKYARD = Kee[str]('backyard')
  BAROQUE = Kee[str]('baroque')
  BOMB = Kee[str]('bomb')
  BOUQUET = Kee[str]('bouquet')
  BURNING_SKULL = Kee[str]('burning_skull')
  BUST = Kee[str]('bust')
  CAVEBIRD = Kee[str]('cavebird')
  CHANGING = Kee[str]('changing')
  COTAN = Kee[str]('cotan')
  COURBET = Kee[str]('courbet')
  CREEBET = Kee[str]('creebet')
  DENNIS = Kee[str]('dennis')
  DONKEY_KONG = Kee[str]('donkey_kong')
  EARTH = Kee[str]('earth')
  ENDBOSS = Kee[str]('endboss')
  FERN = Kee[str]('fern')
  FIGHTERS = Kee[str]('fighters')
  FINDING = Kee[str]('finding')
  FIRE = Kee[str]('fire')
  GRAHAM = Kee[str]('graham')
  HUMBLE = Kee[str]('humble')
  KEBAB = Kee[str]('kebab')
  LOWMIST = Kee[str]('lowmist')
  MATCH = Kee[str]('match')
  MEDITATIVE = Kee[str]('meditative')
  ORB = Kee[str]('orb')
  OWLEMONS = Kee[str]('owlemons')
  PASSAGE = Kee[str]('passage')
  PIGSCENE = Kee[str]('pigscene')
  PLANT = Kee[str]('plant')
  POINTER = Kee[str]('pointer')
  POND = Kee[str]('pond')
  POOL = Kee[str]('pool')
  PRAIRIE_RIDE = Kee[str]('prairie_ride')
  SEA = Kee[str]('sea')
  SKELETON = Kee[str]('skeleton')
  SKULL_AND_ROSES = Kee[str]('skull_and_roses')
  STAGE = Kee[str]('stage')
  SUNFLOWERS = Kee[str]('sunflowers')
  SUNSET = Kee[str]('sunset')
  TIDES = Kee[str]('tides')
  UNPACKED = Kee[str]('unpacked')
  VOID = Kee[str]('void')
  WANDERER = Kee[str]('wanderer')
  WASTELAND = Kee[str]('wasteland')
  WATER = Kee[str]('water')
  WIND = Kee[str]('wind')
  WITHER = Kee[str]('wither')
