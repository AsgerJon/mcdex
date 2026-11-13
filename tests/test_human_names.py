"""
TestHumanNames tests that a thing whose game name is not the one a
person would use has the human name as well, most often Mojang's own
English name for it, with the same data, while the game's name stays
valid too, as Grass beside the short grass.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import MCAttributes, MCBannerPatterns, MCBlocks, MCEffects
from mcdex import MCEnchantments, MCEntities, MCItems, MCStatistics, Version


class TestHumanNames(BaseTest):
  """
  Each human name holds the same data as the game's name beside it.
  """

  def assertSameThing(self, pairs: tuple) -> None:
    for human, game in pairs:
      with self.subTest(human=human, game=game):
        self.assertIsNot(human, game)
        self.assertEqual(human.versionIds, game.versionIds)

  def test_items(self) -> None:
    self.assertSameThing((
      (MCItems.GRASS, MCItems.SHORT_GRASS),
      (MCItems.EYE_OF_ENDER, MCItems.ENDER_EYE),
      (MCItems.BOTTLE_O_ENCHANTING, MCItems.EXPERIENCE_BOTTLE),
      (MCItems.RAW_BEEF, MCItems.BEEF),
      (MCItems.RAW_CHICKEN, MCItems.CHICKEN),
      (MCItems.RAW_COD, MCItems.COD),
      (MCItems.RAW_MUTTON, MCItems.MUTTON),
      (MCItems.RAW_PORKCHOP, MCItems.PORKCHOP),
      (MCItems.RAW_RABBIT, MCItems.RABBIT),
      (MCItems.RAW_SALMON, MCItems.SALMON),
      (MCItems.STEAK, MCItems.COOKED_BEEF),
      (MCItems.LEATHER_CAP, MCItems.LEATHER_HELMET),
      (MCItems.LEATHER_TUNIC, MCItems.LEATHER_CHESTPLATE),
      (MCItems.LEATHER_PANTS, MCItems.LEATHER_LEGGINGS),
      (MCItems.TURTLE_SHELL, MCItems.TURTLE_HELMET),
      (MCItems.BOOK_AND_QUILL, MCItems.WRITABLE_BOOK),
      (MCItems.SLIMEBALL, MCItems.SLIME_BALL),
      (MCItems.NETHER_QUARTZ, MCItems.QUARTZ),
      (MCItems.REDSTONE_DUST, MCItems.REDSTONE),
      (MCItems.RABBITS_FOOT, MCItems.RABBIT_FOOT),
      (MCItems.DRAGONS_BREATH, MCItems.DRAGON_BREATH),
      (MCItems.REDSTONE_COMPARATOR, MCItems.COMPARATOR),
      (MCItems.REDSTONE_REPEATER, MCItems.REPEATER),
      (MCItems.MONSTER_SPAWNER, MCItems.SPAWNER),
      (MCItems.HAY_BALE, MCItems.HAY_BLOCK),
      (MCItems.EMPTY_MAP, MCItems.MAP),
    ))
    self.assertEqual(MCItems.STEAK[Version.V26_3].minecraftId,
                     'minecraft:cooked_beef')

  def test_blocks(self) -> None:
    self.assertSameThing((
      (MCBlocks.GRASS, MCBlocks.SHORT_GRASS),
      (MCBlocks.REDSTONE_COMPARATOR, MCBlocks.COMPARATOR),
      (MCBlocks.REDSTONE_REPEATER, MCBlocks.REPEATER),
      (MCBlocks.MONSTER_SPAWNER, MCBlocks.SPAWNER),
      (MCBlocks.HAY_BALE, MCBlocks.HAY_BLOCK),
      (MCBlocks.BAMBOO_SHOOT, MCBlocks.BAMBOO_SAPLING),
      (MCBlocks.WHEAT_CROPS, MCBlocks.WHEAT),
      (MCBlocks.POTTED_AZALEA, MCBlocks.POTTED_AZALEA_BUSH),
      (MCBlocks.POTTED_FLOWERING_AZALEA,
       MCBlocks.POTTED_FLOWERING_AZALEA_BUSH),
    ))

  def test_entities(self) -> None:
    self.assertSameThing((
      (MCEntities.PRIMED_TNT, MCEntities.TNT),
      (MCEntities.THROWN_EGG, MCEntities.EGG),
      (MCEntities.THROWN_ENDER_PEARL, MCEntities.ENDER_PEARL),
      (MCEntities.THROWN_BOTTLE_O_ENCHANTING, MCEntities.EXPERIENCE_BOTTLE),
    ))

  def test_the_rest(self) -> None:
    self.assertSameThing((
      (MCEffects.BAD_LUCK, MCEffects.UNLUCK),
      (MCEnchantments.CURSE_OF_BINDING, MCEnchantments.BINDING_CURSE),
      (MCEnchantments.CURSE_OF_VANISHING, MCEnchantments.VANISHING_CURSE),
      (MCAttributes.ZOMBIE_REINFORCEMENTS, MCAttributes.SPAWN_REINFORCEMENTS),
      (MCBannerPatterns.STRIPE_DOWN_LEFT, MCBannerPatterns.STRIPE_DOWNLEFT),
      (MCBannerPatterns.STRIPE_DOWN_RIGHT, MCBannerPatterns.STRIPE_DOWNRIGHT),
    ))

  def test_statistics(self) -> None:
    """Every statistic has the name its screen shows, Mojang's English."""
    self.assertSameThing((
      (MCStatistics.DISTANCE_BY_BOAT, MCStatistics.BOAT_ONE_CM),
      (MCStatistics.DISTANCE_BY_ELYTRA, MCStatistics.AVIATE_ONE_CM),
      (MCStatistics.HOPPERS_SEARCHED, MCStatistics.INSPECT_HOPPER),
      (MCStatistics.INTERACTIONS_WITH_BREWING_STAND,
       MCStatistics.INTERACT_WITH_BREWINGSTAND),
      (MCStatistics.NUMBER_OF_DEATHS, MCStatistics.DEATHS),
      (MCStatistics.GAMES_QUIT, MCStatistics.LEAVE_GAME),
    ))
    self.assertEqual(len(MCStatistics), 80 + 66)
