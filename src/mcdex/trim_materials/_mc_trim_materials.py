"""
MCTrimMaterials is the catalogue of the game's trim materials: an enumeration
with one member for every trim material of the data file that ships with mcdex,
each the same trim material in every version, with the id each version knows it
by: what an armor trim's material takes.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import MCThing, TrimMaterialId


class MCTrimMaterials(MCThing):
  """
  The catalogue of the game's trim materials, each a member, found by its name
  in capitals, in any case, or by its unique name:

    amethyst = MCTrimMaterials.AMETHYST
    amethyst is MCTrimMaterials['amethyst']  # True
    amethyst['1.20']  # TrimMaterialId('amethyst', 'minecraft:amethyst')
    len(MCTrimMaterials)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'trim_materials.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'trim_materials.json'
  __data_key__ = 'trim_materials'
  __id_class__ = TrimMaterialId
  __kind__ = 'trim material'

  #  Members, one for every name of 'trim_materials.json'
  AMETHYST = Kee[str]('amethyst')
  COPPER = Kee[str]('copper')
  DIAMOND = Kee[str]('diamond')
  EMERALD = Kee[str]('emerald')
  GOLD = Kee[str]('gold')
  IRON = Kee[str]('iron')
  LAPIS = Kee[str]('lapis')
  NETHERITE = Kee[str]('netherite')
  QUARTZ = Kee[str]('quartz')
  REDSTONE = Kee[str]('redstone')
  RESIN = Kee[str]('resin')
