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
    flame = MCParticles['flame']
    self.assertIsInstance(flame, MCParticles)
    self.assertIsInstance(flame, MCThing)
    self.assertIs(type(flame['26.3']), ParticleId)
    self.assertIsInstance(flame['26.3'], GameId)
    self.assertEqual(repr(flame), "<MCParticles>.FLAME")
    self.assertNotEqual(ParticleId('x', 'minecraft:x'), BlockId('x', 'minecraft:x'))

  def test_catalogue(self) -> None:
    self.assertEqual(len(MCParticles), len(self.records))
    with self.assertRaises(KeyError) as context:
      _ = MCParticles['flam']
    self.assertIn("mcdex has no particle named 'flam'", str(context.exception))

  def test_ids_fit_their_era(self) -> None:
    """No '/particle' before 1.8; old names to 1.12.2; 'minecraft:' since."""
    for name, record in self.records.items():
      self.assertEqual(next(iter(record['ids'])), '1.7.2')
      for text, minecraftId in record['ids'].items():
        with self.subTest(name=name, version=text):
          if Version(text) < Version.V1_8:
            self.assertEqual(minecraftId, '')
          elif minecraftId and Version(text) < Version.V1_13:
            self.assertRegex(minecraftId, r'^[a-zA-Z]+_?$')
          elif minecraftId:
            self.assertEqual(minecraftId, 'minecraft:' + name)

  def test_latest_version(self) -> None:
    latest = [n for n, r in self.records.items()
              if list(r['ids'].values())[-1] == 'minecraft:' + n]
    self.assertEqual(len(latest), 128)

  def test_known_particles(self) -> None:
    flame = MCParticles['flame']
    self.assertEqual(flame['1.8'], ParticleId('flame', 'flame'))
    self.assertEqual(flame['1.13'].minecraftId, 'minecraft:flame')
    damageIndicator = MCParticles['damage_indicator']
    self.assertEqual(damageIndicator['1.12.2'].minecraftId, 'damageIndicator')
    self.assertEqual(damageIndicator['1.13'].minecraftId,
                     'minecraft:damage_indicator')
    item = MCParticles['item']
    self.assertEqual(item['1.8'].minecraftId, 'iconcrack_')
    self.assertEqual(item['1.9'].minecraftId, 'iconcrack')
    self.assertEqual(item['1.13'].minecraftId, 'minecraft:item')
    with self.assertRaises(NotInVersion) as context:
      _ = MCParticles['flame']['1.7.10']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.7.10 has no 'flame'; vanilla added it in 1.8!",
    )

  def test_linked_by_code(self) -> None:
    """The class that spawns 1.12's explode spawns 1.13's poof."""
    poof = MCParticles['poof']
    self.assertEqual(poof['1.12.2'], ParticleId('poof', 'explode'))
    self.assertEqual(poof['1.13'].minecraftId, 'minecraft:poof')
    self.assertEqual(MCParticles['entity_effect']['1.12.2'].minecraftId,
                     'mobSpell')
    self.assertEqual(MCParticles['item_slime']['1.12.2'].minecraftId, 'slime')

  def test_linked_by_client_code(self) -> None:
    """The client's code draws and spawns the rest: witchMagic is witch."""
    witch = MCParticles['witch']
    self.assertEqual(witch['1.12.2'], ParticleId('witch', 'witchMagic'))
    self.assertEqual(witch['1.13'].minecraftId, 'minecraft:witch')
    self.assertNotIn('spell_witch', MCParticles)
    self.assertEqual(MCParticles['fishing']['1.12.2'].minecraftId, 'wake')
    self.assertEqual(MCParticles['dust']['1.12.2'].minecraftId, 'reddust')
    self.assertEqual(MCParticles['mycelium']['1.12.2'].minecraftId,
                     'townaura')
    self.assertEqual(MCParticles['dripping_lava']['1.12.2'].minecraftId,
                     'dripLava')
    block = MCParticles['block']
    self.assertEqual(block['1.8'].minecraftId, 'blockcrack_')
    self.assertEqual(block['1.12.2'].minecraftId, 'blockcrack')

  def test_removed_in_1_13(self) -> None:
    """Five of 1.12.2's particles are no 1.13 particle in the code."""
    removed = {p.uniqueName for p in MCParticles if self._has(p, '1.12.2')
               and not self._has(p, '1.13')}
    self.assertEqual(removed, {'block_dust', 'footstep', 'item_take',
                               'snow_shovel', 'suspended_depth'})
    footstep = MCParticles['footstep']
    self.assertEqual(footstep['1.12.2'].minecraftId, 'footstep')
    with self.assertRaises(NotInVersion) as context:
      _ = footstep['1.13']
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
