"""
TestMusic tests the music: the 'MusicId' and
'Music' classes, and the 'Music' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import GameId, MusicId, Music, MCThing
from mcdex import NotInVersion, SoundId


class TestMusic(BaseTest):
  """
  TestMusic tests the music.
  """

  def test_jukebox_songs(self) -> None:
    pigstep = Music['pigstep']
    self.assertIsInstance(pigstep, Music)
    self.assertIsInstance(pigstep, MCThing)
    self.assertEqual(pigstep['1.21'],
                     MusicId('pigstep', 'minecraft:pigstep'))
    self.assertIsInstance(pigstep['26.3'], GameId)
    self.assertEqual(repr(pigstep), "<Music>.PIGSTEP")
    self.assertEqual(len(Music), 22)
    self.assertNotEqual(MusicId('x', 'minecraft:x'),
                        SoundId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = pigstep['1.20.6']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.20.6 has no 'pigstep'; vanilla added it in 1.21!",
    )
    with self.assertRaises(KeyError):
      _ = Music['pigstepx']

  def test_added_later(self) -> None:
    tears = Music['tears']
    self.assertEqual(tears['1.21.6'].minecraftId, 'minecraft:tears')
    with self.assertRaises(NotInVersion):
      _ = tears['1.21.5']
