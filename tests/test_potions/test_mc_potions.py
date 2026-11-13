"""
TestMCPotions tests the potions: the 'PotionId' and 'MCPotions' classes,
and the 'MCPotions' catalogue with the data it reads.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
from importlib.resources import files

from worktoy.waitaminute.desc import WriteOnceError
from worktoy.waitaminute.keenum import KeeResolveError
from worktoy.work_test import BaseTest

from mcdex import EffectId, GameId, MCPotions, MCThing, ModifiedPotion
from mcdex import NotInVersion, PotionId, PotionModifier, Version


def _records() -> dict:
  text = files('mcdex.potions').joinpath('potions.json').read_text('utf-8')
  return json.loads(text)['potions']


class TestMCPotions(BaseTest):
  """
  TestMCPotions tests the potions.
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.records = _records()

  def test_kind(self) -> None:
    swiftness = MCPotions.SWIFTNESS
    self.assertIsInstance(swiftness, MCPotions)
    self.assertIsInstance(swiftness, MCThing)
    self.assertIs(type(swiftness[Version.V26_3]), PotionId)
    self.assertIsInstance(swiftness[Version.V26_3], GameId)
    self.assertEqual(repr(swiftness), "<MCPotions>.SWIFTNESS")
    self.assertNotEqual(PotionId('x', 'minecraft:x'), EffectId('x', 'minecraft:x'))

  def test_catalogue(self) -> None:
    self.assertEqual(len(MCPotions), len(self.records))
    self.assertEqual([p.uniqueName for p in MCPotions], list(self.records))
    with self.assertRaises(KeyError) as context:
      _ = MCPotions['swifness']
    self.assertIn("mcdex has no potion named 'swifness'",
                  str(context.exception))

  def test_ids_fit_their_era(self) -> None:
    """Before 1.9 a damage value from 0 to 127; from 1.9 a name."""
    for name, record in self.records.items():
      tables = {'': record['ids']}
      tables.update({k: record[k]['ids'] for k in ('long', 'strong')
                     if k in record})
      for modifier, ids in tables.items():
        self.assertEqual(next(iter(ids)), '1.7.2')
        expected = 'minecraft:%s%s' % (modifier + '_' if modifier else '',
                                       name)
        for text, minecraftId in ids.items():
          with self.subTest(name=name, modifier=modifier, version=text):
            if not minecraftId:
              continue
            if Version(text) < Version.V1_9:
              self.assertLess(int(minecraftId), 128)
            else:
              self.assertEqual(minecraftId, expected)

  def test_latest_version(self) -> None:
    """26.3's 46 potions: 24 base potions, 13 long and 9 strong ones."""
    latest = [n for n, r in self.records.items()
              if list(r['ids'].values())[-1]]
    self.assertEqual(len(latest), 24)
    self.assertEqual(sum('long' in r for r in self.records.values()), 13)
    self.assertEqual(sum('strong' in r for r in self.records.values()), 9)

  def test_known_potions(self) -> None:
    regeneration = MCPotions.REGENERATION
    self.assertEqual(regeneration[Version.V1_8_9],
                     PotionId('regeneration', '1'))
    self.assertEqual(regeneration[Version.V1_9].minecraftId,
                     'minecraft:regeneration')
    self.assertEqual(MCPotions.WATER[Version.V1_7_10].minecraftId, '0')
    self.assertEqual(MCPotions.LEAPING[Version.V1_8].minecraftId, '11')
    with self.assertRaises(NotInVersion) as context:
      _ = MCPotions.LEAPING[Version.V1_7_10]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.7.10 has no 'leaping'; vanilla added it in 1.8!",
    )
    with self.assertRaises(NotInVersion) as context:
      _ = MCPotions.EMPTY[Version.V26_3]
    self.assertIn("removed it in 1.20.5", str(context.exception))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  LONG AND STRONG POTIONS  # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_modifiers(self) -> None:
    self.assertEqual(list(PotionModifier), [PotionModifier.LONG,
                                            PotionModifier.STRONG])
    self.assertEqual(PotionModifier.LONG.value, 'long')
    self.assertIs(PotionModifier('strong'), PotionModifier.STRONG)

  def test_modified_potion(self) -> None:
    """A base potion with a modifier, the same object every time."""
    nightVision = MCPotions.NIGHT_VISION
    longNightVision = MCPotions[nightVision, PotionModifier.LONG]
    self.assertIsInstance(longNightVision, ModifiedPotion)
    self.assertIs(MCPotions['night_vision', 'long'], longNightVision)
    self.assertIs(longNightVision.base, nightVision)
    self.assertIs(longNightVision.modifier, PotionModifier.LONG)
    self.assertEqual(longNightVision.uniqueName, 'night_vision')
    self.assertEqual(
        repr(longNightVision),
        'MCPotions[<MCPotions>.NIGHT_VISION, <PotionModifier>.LONG]')
    with self.assertRaises(WriteOnceError):
      longNightVision.modifier = PotionModifier.STRONG

  def test_modified_potion_ids(self) -> None:
    """The night vision's 6 with the bit for long, before 1.9: 70."""
    longNightVision = MCPotions[MCPotions.NIGHT_VISION, PotionModifier.LONG]
    self.assertEqual(longNightVision[Version.V1_8_9],
                     PotionId('night_vision', '70'))
    self.assertEqual(longNightVision[Version.V1_12_2],
                     PotionId('night_vision', 'minecraft:long_night_vision'))
    strongRegeneration = MCPotions[
        MCPotions.REGENERATION, PotionModifier.STRONG]
    self.assertEqual(strongRegeneration[Version.V1_7_2].minecraftId, '33')
    ids = longNightVision.versionIds
    self.assertEqual(ids[Version.V1_8_9], '70')
    ids[Version.V26_3] = 'test:changed'
    self.assertEqual(longNightVision.versionIds[Version.V26_3],
                     'minecraft:long_night_vision')

  def test_modified_potion_not_in_version(self) -> None:
    strongLeaping = MCPotions[MCPotions.LEAPING, PotionModifier.STRONG]
    with self.assertRaises(NotInVersion) as context:
      _ = strongLeaping[Version.V1_7_10]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.7.10 has no 'strong leaping'; vanilla added it in 1.8!",
    )
    with self.assertRaises(ValueError) as context:
      _ = strongLeaping[Version.V1_6_4]
    self.assertIn('no data on MCPotions[<MCPotions>.LEAPING, '
                  '<PotionModifier>.STRONG] before 1.7.2',
                  str(context.exception))

  def test_no_such_modified_potion(self) -> None:
    with self.assertRaises(KeyError) as context:
      _ = MCPotions[MCPotions.NIGHT_VISION, PotionModifier.STRONG]
    self.assertIn('mcdex has no strong night_vision potion',
                  str(context.exception))
    for identifier in (('night_vision', 'lasting'),
                       ('night_vision', 'long', 'strong')):
      with self.subTest(identifier=identifier):
        with self.assertRaises(KeeResolveError):
          _ = MCPotions[identifier]
