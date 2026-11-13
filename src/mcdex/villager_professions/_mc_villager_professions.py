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


class MCVillagerProfessions(MCThing):
  """
  The catalogue of the game's villager professions, each a member, found by its
  name in capitals, in any case, or by its unique name:

    fisherman = MCVillagerProfessions.FISHERMAN
    fisherman is MCVillagerProfessions['fisherman']  # True
    fisherman[Version.V1_13_2]
    # VillagerProfessionId('fisherman',
    #   'minecraft:villager{Profession:0,Career:2}')
    len(MCVillagerProfessions)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'villager_professions.json' beside this
  module. mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'villager_professions.json'
  __data_key__ = 'villager_professions'
  __id_class__ = VillagerProfessionId
  __kind__ = 'villager profession'

  #  Members, one for every name of 'villager_professions.json'
  ARMORER = Kee[str]('armorer')
  BUTCHER = Kee[str]('butcher')
  CARTOGRAPHER = Kee[str]('cartographer')
  CLERIC = Kee[str]('cleric')
  FARMER = Kee[str]('farmer')
  FISHERMAN = Kee[str]('fisherman')
  FLETCHER = Kee[str]('fletcher')
  LEATHERWORKER = Kee[str]('leatherworker')
  LIBRARIAN = Kee[str]('librarian')
  MASON = Kee[str]('mason')
  NITWIT = Kee[str]('nitwit')
  NONE = Kee[str]('none')
  SHEPHERD = Kee[str]('shepherd')
  TOOLSMITH = Kee[str]('toolsmith')
  WEAPONSMITH = Kee[str]('weaponsmith')
