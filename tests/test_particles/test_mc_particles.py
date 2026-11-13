"""
TestMCParticles tests the particles: the 'ParticleId' and 'MCParticles'
classes, and the 'MCParticles' catalogue with the data it reads.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
from importlib.resources import files

from worktoy.work_test import BaseTest

from mcdex import BlockId, GameId, MCParticles, MCThing
from mcdex import NotInVersion, ParticleId, Version


def _records() -> dict:
  text = files('mcdex.particles').joinpath('particles.json').read_text(
    'utf-8')
  return json.loads(text)['particles']


class TestMCParticles(BaseTest):
  """
  TestMCParticles tests the particles.
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.records = _records()

  def test_kind(self) -> None:
    flame = MCParticles.FLAME
    self.assertIsInstance(flame, MCParticles)
    self.assertIsInstance(flame, MCThing)
    self.assertIs(type(flame[Version.V26_3]), ParticleId)
    self.assertIsInstance(flame[Version.V26_3], GameId)
    self.assertEqual(repr(flame), "<MCParticles>.FLAME")
    self.assertNotEqual(ParticleId('x', 'minecraft:x'), BlockId('x', 'minecraft:x'))

  def test_catalogue(self) -> None:
    self.assertEqual(len(MCParticles), len(self.records))
    with self.assertRaises(KeyError) as context:
      _ = MCParticles['flam']
    self.assertIn("mcdex has no particle named 'flam'", str(context.exception))

  def test_ids_fit_their_era(self) -> None:
    """The data begins at 1.8, with '/particle'; old names to 1.12.2."""
    for name, record in self.records.items():
      self.assertEqual(next(iter(record['ids'])), '1.8')
      for text, minecraftId in record['ids'].items():
        with self.subTest(name=name, version=text):
          if minecraftId and Version(text) < Version.V1_13:
            self.assertRegex(minecraftId, r'^[a-zA-Z]+_?$')
          elif minecraftId:
            self.assertEqual(minecraftId, 'minecraft:' + name)

  def test_latest_version(self) -> None:
    latest = [n for n, r in self.records.items()
              if list(r['ids'].values())[-1] == 'minecraft:' + n]
    self.assertEqual(len(latest), 128)

  def test_known_particles(self) -> None:
    flame = MCParticles.FLAME
    self.assertEqual(flame[Version.V1_8], ParticleId('flame', 'flame'))
    self.assertEqual(flame[Version.V1_13].minecraftId, 'minecraft:flame')
    damageIndicator = MCParticles.DAMAGE_INDICATOR
    self.assertEqual(damageIndicator[Version.V1_12_2].minecraftId,
                     'damageIndicator')
    self.assertEqual(damageIndicator[Version.V1_13].minecraftId,
                     'minecraft:damage_indicator')
    item = MCParticles.ITEM
    self.assertEqual(item[Version.V1_8].minecraftId, 'iconcrack_')
    self.assertEqual(item[Version.V1_9].minecraftId, 'iconcrack')
    self.assertEqual(item[Version.V1_13].minecraftId, 'minecraft:item')
    with self.assertRaises(ValueError) as context:
      _ = MCParticles.FLAME[Version.V1_7_10]
    self.assertEqual(str(context.exception),
                     "mcdex has no data on 'flame' before 1.8")

  def test_linked_by_code(self) -> None:
    """The class that spawns 1.12's explode spawns 1.13's poof."""
    poof = MCParticles.POOF
    self.assertEqual(poof[Version.V1_12_2], ParticleId('poof', 'explode'))
    self.assertEqual(poof[Version.V1_13].minecraftId, 'minecraft:poof')
    self.assertEqual(MCParticles.ENTITY_EFFECT[Version.V1_12_2].minecraftId,
                     'mobSpell')
    self.assertEqual(MCParticles.ITEM_SLIME[Version.V1_12_2].minecraftId,
                     'slime')

  def test_linked_by_client_code(self) -> None:
    """The client's code draws and spawns the rest: witchMagic is witch."""
    witch = MCParticles.WITCH
    self.assertEqual(witch[Version.V1_12_2], ParticleId('witch', 'witchMagic'))
    self.assertEqual(witch[Version.V1_13].minecraftId, 'minecraft:witch')
    self.assertNotIn('spell_witch', MCParticles)
    self.assertEqual(MCParticles.FISHING[Version.V1_12_2].minecraftId, 'wake')
    self.assertEqual(MCParticles.DUST[Version.V1_12_2].minecraftId, 'reddust')
    self.assertEqual(MCParticles.MYCELIUM[Version.V1_12_2].minecraftId,
                     'townaura')
    self.assertEqual(MCParticles.DRIPPING_LAVA[Version.V1_12_2].minecraftId,
                     'dripLava')
    block = MCParticles.BLOCK
    self.assertEqual(block[Version.V1_8].minecraftId, 'blockcrack_')
    self.assertEqual(block[Version.V1_12_2].minecraftId, 'blockcrack')

  def test_removed_in_1_13(self) -> None:
    """Five of 1.12.2's particles are no 1.13 particle in the code."""
    removed = {p.uniqueName for p in MCParticles if self._has(p, '1.12.2')
               and not self._has(p, '1.13')}
    self.assertEqual(removed, {'block_dust', 'footstep', 'item_take',
                               'snow_shovel', 'suspended_depth'})
    footstep = MCParticles.FOOTSTEP
    self.assertEqual(footstep[Version.V1_12_2].minecraftId, 'footstep')
    with self.assertRaises(NotInVersion) as context:
      _ = footstep[Version.V1_13]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.13 has no 'footstep'; vanilla removed it in 1.13!",
    )

  @staticmethod
  def _has(particle: MCParticles, version: str) -> bool:
    try:
      _ = particle[version]
    except NotInVersion:
      return False
    return True
