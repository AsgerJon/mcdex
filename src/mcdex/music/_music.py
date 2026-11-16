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


class Music(MCThing, strictCase=False):
  """
  The catalogue of the game's songs, each a member. A member is named
  by its unique name in PascalCase, and found by that name in any case or
  by the unique name itself:

    pigstep = Music.Pigstep
    pigstep is Music['pigstep']  # True
    pigstep[Version.V1_21]  # MusicId('pigstep', 'minecraft:pigstep')
    len(Music)

  Implementation
  --------------

  All of it is 'MCThing's, reading 'music.json' beside this module.
  mcdex's tools write the members, one for every thing of that file.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __data_file__ = 'music.json'
  __data_key__ = 'music'
  __id_class__ = MusicId
  __kind__ = 'song'

  #  Members, one for every thing of 'music.json'
  Eleven = Kee[str]('11')
  Thirteen = Kee[str]('13')
  Five = Kee[str]('5')
  Blocks = Kee[str]('blocks')
  Bounce = Kee[str]('bounce')
  Cat = Kee[str]('cat')
  Chirp = Kee[str]('chirp')
  Creator = Kee[str]('creator')
  CreatorMusicBox = Kee[str]('creator_music_box')
  Far = Kee[str]('far')
  LavaChicken = Kee[str]('lava_chicken')
  Mall = Kee[str]('mall')
  Mellohi = Kee[str]('mellohi')
  Otherside = Kee[str]('otherside')
  Pigstep = Kee[str]('pigstep')
  Precipice = Kee[str]('precipice')
  Relic = Kee[str]('relic')
  Stal = Kee[str]('stal')
  Strad = Kee[str]('strad')
  Tears = Kee[str]('tears')
  Wait = Kee[str]('wait')
  Ward = Kee[str]('ward')
