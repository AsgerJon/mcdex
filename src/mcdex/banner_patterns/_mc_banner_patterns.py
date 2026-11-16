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


class MCBannerPatterns(MCThing, strictCase=False):
  """
  The catalogue of the game's banner patterns, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    squareBottomLeft = MCBannerPatterns.SquareBottomLeft
    squareBottomLeft is MCBannerPatterns['square_bottom_left']  # True
    squareBottomLeft[Version.V1_8]
    # BannerPatternId('square_bottom_left', 'bl')
    len(MCBannerPatterns)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'banner_patterns.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'banner_patterns.json'
  __data_key__ = 'banner_patterns'
  __id_class__ = BannerPatternId
  __kind__ = 'banner pattern'

  #  Members, one for every thing of 'banner_patterns.json'
  Base = Kee[str]('base')
  Border = Kee[str]('border')
  Bricks = Kee[str]('bricks')
  Circle = Kee[str]('circle')
  Creeper = Kee[str]('creeper')
  Cross = Kee[str]('cross')
  CurlyBorder = Kee[str]('curly_border')
  DiagonalLeft = Kee[str]('diagonal_left')
  DiagonalRight = Kee[str]('diagonal_right')
  DiagonalUpLeft = Kee[str]('diagonal_up_left')
  DiagonalUpRight = Kee[str]('diagonal_up_right')
  Flow = Kee[str]('flow')
  Flower = Kee[str]('flower')
  Globe = Kee[str]('globe')
  Gradient = Kee[str]('gradient')
  GradientUp = Kee[str]('gradient_up')
  Guster = Kee[str]('guster')
  HalfHorizontal = Kee[str]('half_horizontal')
  HalfHorizontalBottom = Kee[str]('half_horizontal_bottom')
  HalfVertical = Kee[str]('half_vertical')
  HalfVerticalRight = Kee[str]('half_vertical_right')
  Mojang = Kee[str]('mojang')
  Piglin = Kee[str]('piglin')
  Rhombus = Kee[str]('rhombus')
  Skull = Kee[str]('skull')
  SmallStripes = Kee[str]('small_stripes')
  SquareBottomLeft = Kee[str]('square_bottom_left')
  SquareBottomRight = Kee[str]('square_bottom_right')
  SquareTopLeft = Kee[str]('square_top_left')
  SquareTopRight = Kee[str]('square_top_right')
  StraightCross = Kee[str]('straight_cross')
  StripeBottom = Kee[str]('stripe_bottom')
  StripeCenter = Kee[str]('stripe_center')
  StripeDownLeft = Kee[str]('stripe_down_left')
  StripeDownRight = Kee[str]('stripe_down_right')
  StripeLeft = Kee[str]('stripe_left')
  StripeMiddle = Kee[str]('stripe_middle')
  StripeRight = Kee[str]('stripe_right')
  StripeTop = Kee[str]('stripe_top')
  TriangleBottom = Kee[str]('triangle_bottom')
  TriangleTop = Kee[str]('triangle_top')
  TrianglesBottom = Kee[str]('triangles_bottom')
  TrianglesTop = Kee[str]('triangles_top')
