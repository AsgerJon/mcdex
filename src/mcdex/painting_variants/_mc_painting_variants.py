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


class MCPaintingVariants(MCThing, strictCase=False):
  """
  The catalogue of the game's painting variants, each a member. A member is
  named by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    donkeyKong = MCPaintingVariants.DonkeyKong
    donkeyKong is MCPaintingVariants['donkey_kong']  # True
    donkeyKong[Version.V1_12_2]
    # PaintingVariantId('donkey_kong',
    #   'minecraft:painting{Motive:"DonkeyKong"}')
    len(MCPaintingVariants)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'painting_variants.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'painting_variants.json'
  __data_key__ = 'painting_variants'
  __id_class__ = PaintingVariantId
  __kind__ = 'painting variant'

  #  Members, one for every thing of 'painting_variants.json'
  Alban = Kee[str]('alban')
  Aztec = Kee[str]('aztec')
  Aztec2 = Kee[str]('aztec2')
  Backyard = Kee[str]('backyard')
  Baroque = Kee[str]('baroque')
  Bomb = Kee[str]('bomb')
  Bouquet = Kee[str]('bouquet')
  BurningSkull = Kee[str]('burning_skull')
  Bust = Kee[str]('bust')
  Cavebird = Kee[str]('cavebird')
  Changing = Kee[str]('changing')
  Cotan = Kee[str]('cotan')
  Courbet = Kee[str]('courbet')
  Creebet = Kee[str]('creebet')
  Dennis = Kee[str]('dennis')
  DonkeyKong = Kee[str]('donkey_kong')
  Earth = Kee[str]('earth')
  Endboss = Kee[str]('endboss')
  Fern = Kee[str]('fern')
  Fighters = Kee[str]('fighters')
  Finding = Kee[str]('finding')
  Fire = Kee[str]('fire')
  Graham = Kee[str]('graham')
  Humble = Kee[str]('humble')
  Kebab = Kee[str]('kebab')
  Lowmist = Kee[str]('lowmist')
  Match = Kee[str]('match')
  Meditative = Kee[str]('meditative')
  Orb = Kee[str]('orb')
  Owlemons = Kee[str]('owlemons')
  Passage = Kee[str]('passage')
  Pigscene = Kee[str]('pigscene')
  Plant = Kee[str]('plant')
  Pointer = Kee[str]('pointer')
  Pond = Kee[str]('pond')
  Pool = Kee[str]('pool')
  PrairieRide = Kee[str]('prairie_ride')
  Sea = Kee[str]('sea')
  Skeleton = Kee[str]('skeleton')
  SkullAndRoses = Kee[str]('skull_and_roses')
  Stage = Kee[str]('stage')
  Sunflowers = Kee[str]('sunflowers')
  Sunset = Kee[str]('sunset')
  Tides = Kee[str]('tides')
  Unpacked = Kee[str]('unpacked')
  Void = Kee[str]('void')
  Wanderer = Kee[str]('wanderer')
  Wasteland = Kee[str]('wasteland')
  Water = Kee[str]('water')
  Wind = Kee[str]('wind')
  Wither = Kee[str]('wither')
