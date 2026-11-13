"""
TestMCEntities tests the 'MCEntities' catalogue: the entities it hands
out, and what every entity of its data must satisfy, however many there
are.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import json
import re
from importlib.resources import files

from worktoy.waitaminute.keenum import KeeResolveError
from worktoy.work_test import BaseTest

from mcdex import EntityId, MCEntities, MCItems, NotInVersion
from mcdex import Version


def _records() -> dict:
  """The data file, read directly, to compare the catalogue against."""
  text = files('mcdex.entities').joinpath('entities.json').read_text('utf-8')
  return json.loads(text)['entities']


#  The names a person would use beside the game's, each with the data of
#  the entity the game's name is.
HUMAN_NAMES = ('primed_tnt', 'thrown_egg', 'thrown_ender_pearl',
               'thrown_bottle_o_enchanting')


class TestMCEntities(BaseTest):
  """
  TestMCEntities tests the 'MCEntities' catalogue.
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.records = _records()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  LOOKUP   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_getitem(self) -> None:
    creeper = MCEntities.CREEPER
    self.assertIsInstance(creeper, MCEntities)
    self.assertEqual(creeper.uniqueName, 'creeper')

  def test_getitem_same_object(self) -> None:
    self.assertIs(MCEntities['creeper'], MCEntities['creeper'])

  def test_getitem_unknown(self) -> None:
    with self.assertRaises(KeyError) as context:
      _ = MCEntities['creper']
    self.assertIn("mcdex has no entity named 'creper'",
                  str(context.exception))

  def test_getitem_by_position(self) -> None:
    """An 'int' is a position, as in any enumeration."""
    self.assertIs(MCEntities[50], list(MCEntities)[50])

  def test_getitem_not_a_name(self) -> None:
    for name in (Version.V1_9, ('creeper',)):
      with self.subTest(name=name):
        with self.assertRaises(KeeResolveError):
          _ = MCEntities[name]

  def test_len(self) -> None:
    self.assertEqual(len(MCEntities), len(self.records))

  def test_iter(self) -> None:
    entities = list(MCEntities)
    self.assertEqual([e.uniqueName for e in entities], list(self.records))
    for entity in entities:
      self.assertIs(entity, MCEntities[entity.uniqueName])

  def test_iter_again(self) -> None:
    self.assertEqual(len(list(MCEntities)), len(list(MCEntities)))

  def test_contains(self) -> None:
    self.assertIn('creeper', MCEntities)
    self.assertIn(MCEntities['creeper'], MCEntities)
    self.assertNotIn('creper', MCEntities)
    self.assertNotIn(50, MCEntities)

  def test_items_are_not_entities(self) -> None:
    """The two catalogues are apart, though names may meet: an egg."""
    self.assertNotIn(MCItems['egg'], MCEntities)
    self.assertIsNot(MCEntities.EGG, MCItems.EGG)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  THE DATA   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_names_are_lowercase_words(self) -> None:
    for name in self.records:
      with self.subTest(name=name):
        self.assertRegex(name, r'^[a-z0-9]+(_[a-z0-9]+)*$')

  def test_records_begin_together(self) -> None:
    """Every record's ids begin at the first version the data covers."""
    for name, record in self.records.items():
      with self.subTest(name=name):
        self.assertEqual(list(record), ['ids'])
        self.assertEqual(next(iter(record['ids'])), '1.7.2')

  def test_ids_fit_their_era(self) -> None:
    """
    To 1.10.2 the old names, as 'Creeper'; from 1.11 'minecraft:creeper';
    the data that told split entities apart until 1.21.5 split the last.
    """
    old = re.compile(r'[A-Z][A-Za-z]+(\{.+\})?')
    named = re.compile(r'minecraft:[a-z0-9_]+(\{.+\})?')
    flat = re.compile(r'minecraft:[a-z0-9_]+')
    for name, record in self.records.items():
      for text, minecraftId in record['ids'].items():
        with self.subTest(name=name, version=text):
          if not minecraftId:
            continue
          if Version(text) < Version.V1_11:
            self.assertIsNotNone(old.fullmatch(minecraftId))
          elif Version(text) < Version.V1_21_5:
            self.assertIsNotNone(named.fullmatch(minecraftId))
          else:
            self.assertIsNotNone(flat.fullmatch(minecraftId))

  def test_latest_version(self) -> None:
    """26.3 has 161 entities, one id each, the name its own path."""
    latest = {}
    for name, record in self.records.items():
      id_ = list(record['ids'].values())[-1]
      if id_ and name not in HUMAN_NAMES:
        latest[id_] = name
    self.assertEqual(len(latest), 161)
    for id_, name in latest.items():
      with self.subTest(name=name):
        self.assertEqual(id_, 'minecraft:' + name)

  def test_one_id_one_entity(self) -> None:
    """No version gives two entities the same id."""
    for text in ('1.7.2', '1.10.2', '1.12.2', '1.20.4', '26.3'):
      with self.subTest(version=text):
        ids = [i.minecraftId for e in MCEntities if e.versionIds[Version(
          text)] and e.uniqueName not in HUMAN_NAMES for i in (e[text],)]
        self.assertEqual(len(ids), len(set(ids)))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  KNOWN ENTITIES   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def test_creeper(self) -> None:
    creeper = MCEntities.CREEPER
    self.assertEqual(creeper[Version.V1_7_2], EntityId('creeper', 'Creeper'))
    self.assertEqual(creeper[Version.V1_10_2].minecraftId, 'Creeper')
    self.assertEqual(creeper[Version.V1_11].minecraftId, 'minecraft:creeper')
    self.assertEqual(creeper[Version.V26_3].minecraftId, 'minecraft:creeper')

  def test_renamed(self) -> None:
    cases = {
      ('zombified_piglin', '1.10.2'): 'PigZombie',
      ('zombified_piglin', '1.15.2'): 'minecraft:zombie_pigman',
      ('zombified_piglin', '1.16'): 'minecraft:zombified_piglin',
      ('snow_golem', '1.12.2'): 'minecraft:snowman',
      ('snow_golem', '1.13'): 'minecraft:snow_golem',
      ('evoker', '1.11'): 'minecraft:evocation_illager',
      ('evoker', '1.13'): 'minecraft:evoker',
      ('minecart', '1.10.2'): 'MinecartRideable',
      ('experience_orb', '1.7.10'): 'XPOrb',
      ('tnt', '1.10.2'): 'PrimedTnt',
    }
    for (name, text), minecraftId in cases.items():
      with self.subTest(name=name, version=text):
        self.assertEqual(MCEntities[name][text].minecraftId, minecraftId)

  def test_skeleton_split(self) -> None:
    witherSkeleton = MCEntities.WITHER_SKELETON
    self.assertEqual(witherSkeleton[Version.V1_7_2].minecraftId,
                     'Skeleton{SkeletonType:1}')
    self.assertEqual(witherSkeleton[Version.V1_11].minecraftId,
                     'minecraft:wither_skeleton')
    stray = MCEntities.STRAY
    self.assertEqual(stray[Version.V1_10].minecraftId,
                     'Skeleton{SkeletonType:2}')
    with self.assertRaises(NotInVersion) as context:
      _ = stray[Version.V1_9_4]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.9.4 has no 'stray'; vanilla added it in 1.10!",
    )
    self.assertEqual(MCEntities.SKELETON[Version.V1_10_2].minecraftId,
                     'Skeleton')

  def test_zombie_split(self) -> None:
    zombieVillager = MCEntities.ZOMBIE_VILLAGER
    self.assertEqual(zombieVillager[Version.V1_8_9].minecraftId,
                     'Zombie{IsVillager:1b}')
    self.assertEqual(zombieVillager[Version.V1_9_4].minecraftId,
                     'Zombie{IsVillager:1b,VillagerProfession:1}')
    self.assertEqual(zombieVillager[Version.V1_10].minecraftId,
                     'Zombie{ZombieType:1}')
    self.assertEqual(MCEntities.HUSK[Version.V1_10_2].minecraftId,
                     'Zombie{ZombieType:6}')

  def test_horse_split(self) -> None:
    cases = {'horse': 'EntityHorse', 'donkey': 'EntityHorse{Type:1}',
             'mule': 'EntityHorse{Type:2}',
             'zombie_horse': 'EntityHorse{Type:3}',
             'skeleton_horse': 'EntityHorse{Type:4}'}
    for name, minecraftId in cases.items():
      with self.subTest(name=name):
        self.assertEqual(MCEntities[name][Version.V1_7_10].minecraftId,
                         minecraftId)
        self.assertEqual(MCEntities[name][Version.V1_11].minecraftId,
                         'minecraft:' + name)

  def test_cat(self) -> None:
    cat = MCEntities.CAT
    self.assertEqual(cat[Version.V1_7_10].minecraftId, 'Ozelot{CatType:1}')
    self.assertEqual(cat[Version.V1_13_2].minecraftId,
                     'minecraft:ocelot{CatType:1}')
    self.assertEqual(cat[Version.V1_14].minecraftId, 'minecraft:cat')

  def test_boats(self) -> None:
    self.assertEqual(MCEntities.OAK_BOAT[Version.V1_7_2].minecraftId, 'Boat')
    self.assertEqual(MCEntities.OAK_BOAT[Version.V1_21_1].minecraftId,
                     'minecraft:boat')
    spruceBoat = MCEntities.SPRUCE_BOAT
    self.assertEqual(spruceBoat[Version.V1_9].minecraftId,
                     'Boat{Type:"spruce"}')
    self.assertEqual(spruceBoat[Version.V1_21_1].minecraftId,
                     'minecraft:boat{Type:"spruce"}')
    self.assertEqual(spruceBoat[Version.V1_21_2].minecraftId,
                     'minecraft:spruce_boat')
    with self.assertRaises(NotInVersion):
      _ = spruceBoat[Version.V1_8_9]
    self.assertEqual(MCEntities.MANGROVE_BOAT[Version.V1_19].minecraftId,
                     'minecraft:boat{Type:"mangrove"}')

  def test_potions(self) -> None:
    self.assertEqual(MCEntities.SPLASH_POTION[Version.V1_8_9].minecraftId,
                     'ThrownPotion')
    self.assertEqual(MCEntities.SPLASH_POTION[Version.V1_21_5].minecraftId,
                     'minecraft:splash_potion')
    lingeringPotion = MCEntities.LINGERING_POTION
    self.assertEqual(
        lingeringPotion[Version.V1_20_4].minecraftId,
        'minecraft:potion{Item:{id:"minecraft:lingering_potion",Count:1b}}',
    )
    self.assertEqual(
        lingeringPotion[Version.V1_20_5].minecraftId,
        'minecraft:potion{Item:{id:"minecraft:lingering_potion"}}',
    )

  def test_names_the_list_adds(self) -> None:
    """The lightning bolt and the player, which no world saves."""
    for name, old in (('lightning_bolt', 'LightningBolt'),
                      ('player', 'Player')):
      with self.subTest(name=name):
        entity = MCEntities[name]
        self.assertEqual(entity[Version.V1_8].minecraftId, old)
        self.assertEqual(entity[Version.V1_11].minecraftId,
                         'minecraft:' + name)
        with self.assertRaises(NotInVersion):
          _ = entity[Version.V1_7_10]

  def test_removed(self) -> None:
    creakingTransient = MCEntities.CREAKING_TRANSIENT
    self.assertEqual(creakingTransient[Version.V1_21_3].minecraftId,
                     'minecraft:creaking_transient')
    with self.assertRaises(NotInVersion) as context:
      _ = creakingTransient[Version.V26_3]
    self.assertEqual(
        str(context.exception),
        "Vanilla 26.3 has no 'creaking_transient'; vanilla removed it in "
        "1.21.4!",
    )
