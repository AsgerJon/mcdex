"""
MCBannerPatterns is the catalogue of the game's banner patterns: an enumeration
with one member for every banner pattern of the data file that ships with
mcdex, each the same banner pattern in every version, with the id each version
knows it by: what a banner's pattern takes.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import BannerPatternId, MCThing


class MCBannerPatterns(MCThing):
  """
  The catalogue of the game's banner patterns, each a member, found by its name
  in capitals, in any case, or by its unique name:

    squareBottomLeft = MCBannerPatterns.SQUARE_BOTTOM_LEFT
    squareBottomLeft is MCBannerPatterns['square_bottom_left']  # True
    squareBottomLeft['1.8']  # BannerPatternId('square_bottom_left', 'bl')
    len(MCBannerPatterns)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'banner_patterns.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'banner_patterns.json'
  __data_key__ = 'banner_patterns'
  __id_class__ = BannerPatternId
  __kind__ = 'banner pattern'

  #  Members, one for every name of 'banner_patterns.json'
  BASE = Kee[str]('base')
  BORDER = Kee[str]('border')
  BRICKS = Kee[str]('bricks')
  CIRCLE = Kee[str]('circle')
  CREEPER = Kee[str]('creeper')
  CROSS = Kee[str]('cross')
  CURLY_BORDER = Kee[str]('curly_border')
  DIAGONAL_LEFT = Kee[str]('diagonal_left')
  DIAGONAL_RIGHT = Kee[str]('diagonal_right')
  DIAGONAL_UP_LEFT = Kee[str]('diagonal_up_left')
  DIAGONAL_UP_RIGHT = Kee[str]('diagonal_up_right')
  FLOW = Kee[str]('flow')
  FLOWER = Kee[str]('flower')
  GLOBE = Kee[str]('globe')
  GRADIENT = Kee[str]('gradient')
  GRADIENT_UP = Kee[str]('gradient_up')
  GUSTER = Kee[str]('guster')
  HALF_HORIZONTAL = Kee[str]('half_horizontal')
  HALF_HORIZONTAL_BOTTOM = Kee[str]('half_horizontal_bottom')
  HALF_VERTICAL = Kee[str]('half_vertical')
  HALF_VERTICAL_RIGHT = Kee[str]('half_vertical_right')
  MOJANG = Kee[str]('mojang')
  PIGLIN = Kee[str]('piglin')
  RHOMBUS = Kee[str]('rhombus')
  SKULL = Kee[str]('skull')
  SMALL_STRIPES = Kee[str]('small_stripes')
  SQUARE_BOTTOM_LEFT = Kee[str]('square_bottom_left')
  SQUARE_BOTTOM_RIGHT = Kee[str]('square_bottom_right')
  SQUARE_TOP_LEFT = Kee[str]('square_top_left')
  SQUARE_TOP_RIGHT = Kee[str]('square_top_right')
  STRAIGHT_CROSS = Kee[str]('straight_cross')
  STRIPE_BOTTOM = Kee[str]('stripe_bottom')
  STRIPE_CENTER = Kee[str]('stripe_center')
  STRIPE_DOWNLEFT = Kee[str]('stripe_downleft')
  STRIPE_DOWNRIGHT = Kee[str]('stripe_downright')
  STRIPE_LEFT = Kee[str]('stripe_left')
  STRIPE_MIDDLE = Kee[str]('stripe_middle')
  STRIPE_RIGHT = Kee[str]('stripe_right')
  STRIPE_TOP = Kee[str]('stripe_top')
  TRIANGLE_BOTTOM = Kee[str]('triangle_bottom')
  TRIANGLE_TOP = Kee[str]('triangle_top')
  TRIANGLES_BOTTOM = Kee[str]('triangles_bottom')
  TRIANGLES_TOP = Kee[str]('triangles_top')
