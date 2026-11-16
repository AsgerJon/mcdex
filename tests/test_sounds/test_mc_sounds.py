"""
TestMCSounds tests the sound events: the 'SoundId' and 'MCSounds'
classes, and the 'MCSounds' catalogue with the data it reads.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
from importlib.resources import files

from worktoy.work_test import BaseTest

from mcdex import GameId, MCSounds, MCThing, NotInVersion
from mcdex import ParticleId, SoundId, Version


def _records() -> dict:
  text = files('mcdex.sounds').joinpath('sounds.json').read_text('utf-8')
  return json.loads(text)['sounds']


class TestMCSounds(BaseTest):
  """
  TestMCSounds tests the sound events.
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.records = _records()

  def test_kind(self) -> None:
    creeperHiss = MCSounds.CreeperHiss
    self.assertIsInstance(creeperHiss, MCSounds)
    self.assertIsInstance(creeperHiss, MCThing)
    self.assertIs(type(creeperHiss[Version.V26_3]), SoundId)
    self.assertIsInstance(creeperHiss[Version.V26_3], GameId)
    self.assertEqual(repr(creeperHiss), "<MCSounds>.CreeperHiss")
    self.assertNotEqual(SoundId('x', 'minecraft:x'), ParticleId('x', 'minecraft:x'))

  def test_catalogue(self) -> None:
    self.assertEqual(len(MCSounds), len(self.records))
    with self.assertRaises(KeyError) as context:
      _ = MCSounds['creeper_hisss']
    self.assertIn("mcdex has no sound named 'creeper_hisss'",
                  str(context.exception))

  def test_ids_fit_their_era(self) -> None:
    """
    The data begins at 1.7.2; each id 'minecraft:' and the game's name,
    which before 1.9 had capitals in a few, as 'item.fireCharge.use'.
    """
    for name, record in self.records.items():
      self.assertEqual(next(iter(record['ids'])), '1.7.2')
      self.assertRegex(name, r'^[a-z0-9_]+$')
      for text, minecraftId in record['ids'].items():
        with self.subTest(name=name, version=text):
          if minecraftId and Version(text) < Version.V1_9:
            self.assertRegex(minecraftId, r'^minecraft:[a-zA-Z0-9_.]+$')
          elif minecraftId:
            self.assertRegex(minecraftId, r'^minecraft:[a-z0-9_.]+$')

  def test_unique_names(self) -> None:
    """
    The game's newest name for the sound, without the 'entity.', 'block.'
    or 'item.' it begins with, the dots made '_', its glued words split.
    Only the first word goes: 'entity.item.break' is 'item_break'. A last
    word 'ambient' or 'primed' may be the verb of the sound's subtitle.
    """
    glued = {'flintandsteel': 'flint_and_steel', 'levelup': 'level_up',
             'nodamage': 'no_damage', 'basedrum': 'bass_drum',
             'deadbush': 'dead_bush', 'firecharge': 'fire_charge',
             'dragonbreath': 'dragon_breath', 'blastfurnace': 'blast_furnace'}
    for name, record in self.records.items():
      newest = [i for i in record['ids'].values() if i][-1]
      gameName = newest.split(':', 1)[1]
      for word in ('entity.', 'block.', 'item.'):
        if gameName.startswith(word):
          gameName = gameName[len(word):]
          break
      words = gameName.replace('.', '_').split('_')
      words = str.join('_', [glued.get(w, w) for w in words]).split('_')
      with self.subTest(name=name):
        if words[-1] in ('ambient', 'primed'):
          self.assertTrue(name.startswith(str.join('_', words[:-1]) + '_'))
        else:
          self.assertEqual(name, str.join('_', words))

  def test_human_names(self) -> None:
    """The verb of Mojang's subtitle where the game's word is code-speak."""
    for sound, gameName in (
        (MCSounds.CreeperHiss, 'entity.creeper.primed'),
        (MCSounds.TntFizz, 'entity.tnt.primed'),
        (MCSounds.ZombieGroan, 'entity.zombie.ambient'),
        (MCSounds.CowMoo, 'entity.cow.ambient'),
        (MCSounds.DonkeyHeeHaw, 'entity.donkey.ambient'),
        (MCSounds.BeaconHum, 'block.beacon.ambient'),
        (MCSounds.CodAmbient, 'entity.cod.ambient'),
        (MCSounds.FlintAndSteelUse, 'item.flintandsteel.use'),
        (MCSounds.PlayerLevelUp, 'entity.player.levelup'),
        (MCSounds.NoteBlockBassDrum, 'block.note_block.basedrum')):
      with self.subTest(sound=sound):
        self.assertEqual(sound[Version.V26_3].minecraftId,
                         'minecraft:' + gameName)

  def test_latest_version(self) -> None:
    latest = [n for n, r in self.records.items()
              if list(r['ids'].values())[-1]]
    self.assertEqual(len(latest), 1991)

  def test_known_sounds(self) -> None:
    creeperHiss = MCSounds.CreeperHiss
    self.assertEqual(creeperHiss[Version.V1_9], SoundId(
        'creeper_hiss', 'minecraft:entity.creeper.primed'))
    self.assertEqual(creeperHiss[Version.V1_8_9].minecraftId,
                     'minecraft:creeper.primed')
    self.assertEqual(creeperHiss[Version.V1_7_2].minecraftId,
                     'minecraft:creeper.primed')
    with self.assertRaises(ValueError) as context:
      _ = creeperHiss[Version.V1_6_4]
    self.assertEqual(str(context.exception),
                     "mcdex has no data on 'creeper_hiss' before 1.7.2")
    self.assertEqual(MCSounds.GoatHornSound7[Version.V1_19].minecraftId,
                     'minecraft:item.goat_horn.sound.7')
    self.assertEqual(MCSounds.CatRoyalPurr[Version.V26_3].minecraftId,
                     'minecraft:entity.cat_royal.purr')
    self.assertEqual(MCSounds.MusicGame[Version.V26_3].minecraftId,
                     'minecraft:music.game')

  def test_renamed_sounds(self) -> None:
    """A sound the game renamed is one sound, its old name in old versions."""
    versions = list(Version)
    for sound, old, new, renamed in (
        (MCSounds.EndermanVwoop, 'entity.endermen.ambient',
         'entity.enderman.ambient', Version.V1_13),
        (MCSounds.WoolBreak, 'block.cloth.break', 'block.wool.break',
         Version.V1_13),
        (MCSounds.SlimeHurtSmall, 'entity.small_slime.hurt',
         'entity.slime.hurt_small', Version.V1_13),
        (MCSounds.ParrotImitateEvoker,
         'entity.parrot.imitate.evocation_illager',
         'entity.parrot.imitate.evoker', Version.V1_13),
        (MCSounds.MusicDiscCat, 'record.cat', 'music_disc.cat',
         Version.V1_13),
        (MCSounds.ZombifiedPiglinGrunt, 'entity.zombie_pigman.ambient',
         'entity.zombified_piglin.ambient', Version.V1_16),
        (MCSounds.MusicNetherNetherWastes, 'music.nether',
         'music.nether.nether_wastes', Version.V1_16),
        (MCSounds.SweetBerryBushPickBerries,
         'item.sweet_berries.pick_from_bush',
         'block.sweet_berry_bush.pick_berries', Version.V1_17),
        (MCSounds.TrialSpawnerAmbientOminous,
         'block.trial_spawner.ambient_charged',
         'block.trial_spawner.ambient_ominous', Version.V1_21)):
      before = versions[versions.index(renamed) - 1]
      with self.subTest(sound=sound):
        self.assertEqual(sound[before].minecraftId, 'minecraft:' + old)
        self.assertEqual(sound[renamed].minecraftId, 'minecraft:' + new)

  def test_game_names(self) -> None:
    """
    The game's names find a sound too, as '/playsound' takes them, the
    old ones included: 1.12.2 called the enderman's 'entity.endermen.'.
    """
    self.assertIs(MCSounds['entity.creeper.primed'], MCSounds.CreeperHiss)
    self.assertIs(MCSounds['minecraft:entity.creeper.primed'],
                  MCSounds.CreeperHiss)
    self.assertIs(MCSounds['entity.endermen.ambient'],
                  MCSounds.EndermanVwoop)
    self.assertIs(MCSounds['entity.enderman.ambient'],
                  MCSounds.EndermanVwoop)
    with self.assertRaises(KeyError) as context:
      _ = MCSounds['entity.creeper.prime']
    self.assertIn("mcdex has no sound named 'entity.creeper.prime'",
                  str(context.exception))

  def test_before_1_9(self) -> None:
    """
    Before 1.9 a sound was a name of the client's sound list, linked to
    1.9's by the sound files each plays, and by the generator's list where
    several names play one set: TNT's and the creeper's fuse were two.
    """
    for sound, minecraftId in (
        (MCSounds.TntFizz, 'minecraft:game.tnt.primed'),
        (MCSounds.GenericHurt, 'minecraft:game.neutral.hurt'),
        (MCSounds.PlayerHurt, 'minecraft:game.player.hurt'),
        (MCSounds.AmbientCave, 'minecraft:ambient.cave.cave'),
        (MCSounds.EndermanVwoop, 'minecraft:mob.endermen.idle')):
      with self.subTest(sound=sound):
        self.assertEqual(sound[Version.V1_8_9].minecraftId, minecraftId)
    self.assertEqual(MCSounds.TntFizz[Version.V1_7_2].minecraftId,
                     'minecraft:game.tnt.primed')
    with self.assertRaises(NotInVersion) as context:
      _ = MCSounds.GuardianHurtLand[Version.V1_7_10]
    self.assertIn('vanilla added it in 1.8', str(context.exception))

  def test_split_in_1_9(self) -> None:
    """
    A sound 1.9 made several of is each of them before: 1.8.9 broke and
    placed wool with one sound, and shot an arrow and threw an egg with
    another. A game name of several sounds finds none of them.
    """
    for sound, minecraftId in (
        (MCSounds.WoolBreak, 'minecraft:dig.cloth'),
        (MCSounds.WoolPlace, 'minecraft:dig.cloth'),
        (MCSounds.ArrowShoot, 'minecraft:random.bow'),
        (MCSounds.EggThrow, 'minecraft:random.bow')):
      with self.subTest(sound=sound):
        self.assertEqual(sound[Version.V1_8_9].minecraftId, minecraftId)
    self.assertIs(MCSounds['creeper.primed'], MCSounds.CreeperHiss)
    with self.assertRaises(ValueError) as context:
      _ = MCSounds['dig.cloth']
    self.assertIn("the game's 'dig.cloth' names several members of "
                  "MCSounds", str(context.exception))

  def test_removed_sounds(self) -> None:
    """A sound the game dropped with no successor stays dropped."""
    parrotImitateWolf = MCSounds.ParrotImitateWolf
    self.assertEqual(parrotImitateWolf[Version.V1_14_4].minecraftId,
                     'minecraft:entity.parrot.imitate.wolf')
    with self.assertRaises(NotInVersion) as context:
      _ = parrotImitateWolf[Version.V1_15]
    self.assertIn('vanilla removed it in 1.15', str(context.exception))
