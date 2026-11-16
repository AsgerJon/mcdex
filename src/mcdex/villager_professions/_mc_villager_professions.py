"""
MCVillagerProfessions is the catalogue of the game's villager professions: an
enumeration with one member for every villager profession of the data file that
ships with mcdex, each the same villager profession in every version, with the
id each version knows it by: what /summon takes for a villager of that
profession.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import MCThing, VillagerProfessionId


class MCVillagerProfessions(MCThing, strictCase=False):
  """
  The catalogue of the game's villager professions, each a member. A member is
  named by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    fisherman = MCVillagerProfessions.Fisherman
    fisherman is MCVillagerProfessions['fisherman']  # True
    fisherman[Version.V1_13_2]
    # VillagerProfessionId('fisherman',
    #   'minecraft:villager{Profession:0,Career:2}')
    len(MCVillagerProfessions)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'villager_professions.json' beside this
  module. mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'villager_professions.json'
  __data_key__ = 'villager_professions'
  __id_class__ = VillagerProfessionId
  __kind__ = 'villager profession'

  #  Members, one for every thing of 'villager_professions.json'
  Armorer = Kee[str]('armorer')
  Butcher = Kee[str]('butcher')
  Cartographer = Kee[str]('cartographer')
  Cleric = Kee[str]('cleric')
  Farmer = Kee[str]('farmer')
  Fisherman = Kee[str]('fisherman')
  Fletcher = Kee[str]('fletcher')
  Leatherworker = Kee[str]('leatherworker')
  Librarian = Kee[str]('librarian')
  Mason = Kee[str]('mason')
  Nitwit = Kee[str]('nitwit')
  Shepherd = Kee[str]('shepherd')
  Toolsmith = Kee[str]('toolsmith')
  Unemployed = Kee[str]('unemployed')
  Weaponsmith = Kee[str]('weaponsmith')
