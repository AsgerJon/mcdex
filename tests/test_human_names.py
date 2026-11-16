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
from mcdex import MCEnchantments, MCEntities, MCItems, MCStatistics
from mcdex import MCVillagerProfessions, Version


class TestHumanNames(BaseTest):
  """
  Each human name holds the same data as the game's name beside it.
  """

  def assertSameThing(self, pairs: tuple) -> None:
    """Each pair two members with the same tables: ids, and an item's."""
    for human, game in pairs:
      with self.subTest(human=human, game=game):
        self.assertIsNot(human, game)
        self.assertEqual(human.versionIds, game.versionIds)
        if isinstance(game, MCItems):
          self.assertEqual(human.maxStackSize, game.maxStackSize)
          self.assertEqual(human.equipmentSlot, game.equipmentSlot)

  def test_items(self) -> None:
    self.assertSameThing((
      (MCItems.Grass, MCItems.ShortGrass),
      (MCItems.EyeOfEnder, MCItems.EnderEye),
      (MCItems.BottleOEnchanting, MCItems.ExperienceBottle),
      (MCItems.RawBeef, MCItems.Beef),
      (MCItems.RawChicken, MCItems.Chicken),
      (MCItems.RawCod, MCItems.Cod),
      (MCItems.RawMutton, MCItems.Mutton),
      (MCItems.RawPorkchop, MCItems.Porkchop),
      (MCItems.RawRabbit, MCItems.Rabbit),
      (MCItems.RawSalmon, MCItems.Salmon),
      (MCItems.Steak, MCItems.CookedBeef),
      (MCItems.LeatherCap, MCItems.LeatherHelmet),
      (MCItems.LeatherTunic, MCItems.LeatherChestplate),
      (MCItems.LeatherPants, MCItems.LeatherLeggings),
      (MCItems.TurtleShell, MCItems.TurtleHelmet),
      (MCItems.BookAndQuill, MCItems.WritableBook),
      (MCItems.NetherQuartz, MCItems.Quartz),
      (MCItems.RedstoneDust, MCItems.Redstone),
      (MCItems.RabbitsFoot, MCItems.RabbitFoot),
      (MCItems.DragonsBreath, MCItems.DragonBreath),
      (MCItems.RedstoneComparator, MCItems.Comparator),
      (MCItems.RedstoneRepeater, MCItems.Repeater),
      (MCItems.MonsterSpawner, MCItems.Spawner),
      (MCItems.HayBale, MCItems.HayBlock),
      (MCItems.EmptyMap, MCItems.Map),
    ))
    self.assertEqual(MCItems.Steak[Version.V26_3].minecraftId,
                     'minecraft:cooked_beef')

  def test_blocks(self) -> None:
    self.assertSameThing((
      (MCBlocks.Grass, MCBlocks.ShortGrass),
      (MCBlocks.RedstoneComparator, MCBlocks.Comparator),
      (MCBlocks.RedstoneRepeater, MCBlocks.Repeater),
      (MCBlocks.MonsterSpawner, MCBlocks.Spawner),
      (MCBlocks.HayBale, MCBlocks.HayBlock),
      (MCBlocks.BambooShoot, MCBlocks.BambooSapling),
      (MCBlocks.WheatCrops, MCBlocks.Wheat),
      (MCBlocks.PottedAzalea, MCBlocks.PottedAzaleaBush),
      (MCBlocks.PottedFloweringAzalea,
       MCBlocks.PottedFloweringAzaleaBush),
    ))

  def test_entities(self) -> None:
    self.assertSameThing((
      (MCEntities.PrimedTnt, MCEntities.Tnt),
      (MCEntities.ThrownEgg, MCEntities.Egg),
      (MCEntities.ThrownEnderPearl, MCEntities.EnderPearl),
      (MCEntities.ThrownBottleOEnchanting, MCEntities.ExperienceBottle),
    ))

  def test_the_rest(self) -> None:
    self.assertSameThing((
      (MCEffects.BadLuck, MCEffects.Unluck),
      (MCEnchantments.CurseOfBinding, MCEnchantments.BindingCurse),
      (MCEnchantments.CurseOfVanishing, MCEnchantments.VanishingCurse),
      (MCAttributes.ZombieReinforcements, MCAttributes.SpawnReinforcements),
    ))

  def test_game_names_no_member_takes(self) -> None:
    """
    A game's name that is the human name but for an underscore is the
    same name in PascalCase, and 'none' is the keyword 'None': the one
    member, the human name's, is found by both.
    """
    self.assertIs(MCItems['slime_ball'], MCItems.Slimeball)
    self.assertEqual(MCItems.Slimeball[Version.V26_3].minecraftId,
                     'minecraft:slime_ball')
    stripes = MCBannerPatterns.StripeDownLeft, MCBannerPatterns.StripeDownRight
    self.assertIs(MCBannerPatterns['stripe_downleft'], stripes[0])
    self.assertIs(MCBannerPatterns['stripe_downright'], stripes[1])
    self.assertEqual(stripes[0][Version.V26_3].minecraftId,
                     'minecraft:stripe_downleft')
    unemployed = MCVillagerProfessions.Unemployed
    self.assertIs(MCVillagerProfessions['none'], unemployed)
    self.assertEqual(unemployed[Version.V26_3].minecraftId,
                     'minecraft:villager{VillagerData:{profession:'
                     '"minecraft:none"}}')

  def test_statistics(self) -> None:
    """Every statistic has the name its screen shows, Mojang's English."""
    self.assertSameThing((
      (MCStatistics.DistanceByBoat, MCStatistics.BoatOneCm),
      (MCStatistics.DistanceByElytra, MCStatistics.AviateOneCm),
      (MCStatistics.HoppersSearched, MCStatistics.InspectHopper),
      (MCStatistics.InteractionsWithBrewingStand,
       MCStatistics.InteractWithBrewingstand),
      (MCStatistics.NumberOfDeaths, MCStatistics.Deaths),
      (MCStatistics.GamesQuit, MCStatistics.LeaveGame),
    ))
    self.assertEqual(len(MCStatistics), 80 + 66)
