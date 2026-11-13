"""
MCDimensions is the catalogue of the game's dimensions: an enumeration with one
member for every dimension of the data file that ships with mcdex, each the
same dimension in every version, with the id each version knows it by:
what /execute in takes.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import DimensionId, MCThing


class MCDimensions(MCThing):
  """
  The catalogue of the game's dimensions, each a member, found by its name in
  capitals, in any case, or by its unique name:

    theNether = MCDimensions.THE_NETHER
    theNether is MCDimensions['the_nether']  # True
    theNether[Version.V1_12_2]  # DimensionId('the_nether', '-1')
    len(MCDimensions)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'dimensions.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'dimensions.json'
  __data_key__ = 'dimensions'
  __id_class__ = DimensionId
  __kind__ = 'dimension'

  #  Members, one for every name of 'dimensions.json'
  OVERWORLD = Kee[str]('overworld')
  THE_END = Kee[str]('the_end')
  THE_NETHER = Kee[str]('the_nether')
