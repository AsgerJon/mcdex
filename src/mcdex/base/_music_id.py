"""
MusicId pairs a song's unique name with the id a version of the game needs to
identify it.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from . import GameId


class MusicId(GameId):
  """
  The id of a song, as a music disc plays it, in one version: its 'uniqueName',
  the same in every version, and its 'minecraftId', the song a jukebox_playable
  component plays in that version.

  A command takes it only inside an item's data, whose shape changed over
  the versions: see the README's 'Ids that go inside an item'.

  Implementation
  --------------

  All of it is 'GameId's: a 'MusicId' is equal only to a 'MusicId'.
  """
