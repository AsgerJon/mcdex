"""
Music is the catalogue of the game's songs: an enumeration with one
member for every song of the data file that ships with mcdex, each the
same song in every version, with the id each version knows it by:
the song a jukebox_playable component plays.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.keenum import Kee

from ..base import MCThing, MusicId


class Music(MCThing):
  """
  The catalogue of the game's songs, each a member, found by its name in
  capitals, in any case, or by its unique name:

    pigstep = Music.PIGSTEP
    pigstep is Music['pigstep']  # True
    pigstep[Version.V1_21]  # MusicId('pigstep', 'minecraft:pigstep')
    len(Music)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'music.json' beside this module.
  mcdex's tools write the members, one for every name of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'music.json'
  __data_key__ = 'music'
  __id_class__ = MusicId
  __kind__ = 'song'

  #  Members, one for every name of 'music.json'
  ELEVEN = Kee[str]('11')
  THIRTEEN = Kee[str]('13')
  FIVE = Kee[str]('5')
  BLOCKS = Kee[str]('blocks')
  BOUNCE = Kee[str]('bounce')
  CAT = Kee[str]('cat')
  CHIRP = Kee[str]('chirp')
  CREATOR = Kee[str]('creator')
  CREATOR_MUSIC_BOX = Kee[str]('creator_music_box')
  FAR = Kee[str]('far')
  LAVA_CHICKEN = Kee[str]('lava_chicken')
  MALL = Kee[str]('mall')
  MELLOHI = Kee[str]('mellohi')
  OTHERSIDE = Kee[str]('otherside')
  PIGSTEP = Kee[str]('pigstep')
  PRECIPICE = Kee[str]('precipice')
  RELIC = Kee[str]('relic')
  STAL = Kee[str]('stal')
  STRAD = Kee[str]('strad')
  TEARS = Kee[str]('tears')
  WAIT = Kee[str]('wait')
  WARD = Kee[str]('ward')
