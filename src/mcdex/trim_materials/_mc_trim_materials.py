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


class MCTrimMaterials(MCThing, strictCase=False):
  """
  The catalogue of the game's trim materials, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    amethyst = MCTrimMaterials.Amethyst
    amethyst is MCTrimMaterials['amethyst']  # True
    amethyst[Version.V1_20]  # TrimMaterialId('amethyst', 'minecraft:amethyst')
    len(MCTrimMaterials)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'trim_materials.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'trim_materials.json'
  __data_key__ = 'trim_materials'
  __id_class__ = TrimMaterialId
  __kind__ = 'trim material'

  #  Members, one for every thing of 'trim_materials.json'
  Amethyst = Kee[str]('amethyst')
  Copper = Kee[str]('copper')
  Diamond = Kee[str]('diamond')
  Emerald = Kee[str]('emerald')
  Gold = Kee[str]('gold')
  Iron = Kee[str]('iron')
  Lapis = Kee[str]('lapis')
  Netherite = Kee[str]('netherite')
  Quartz = Kee[str]('quartz')
  Redstone = Kee[str]('redstone')
  Resin = Kee[str]('resin')
