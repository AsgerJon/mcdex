"""
TestMCAdvancements tests the advancements: the 'AdvancementId' and
'MCAdvancements' classes, and the 'MCAdvancements' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import AdvancementId, GameId, MCAdvancements, Version
from mcdex import MCThing, NotInVersion, StatisticId


class TestMCAdvancements(BaseTest):
  """
  TestMCAdvancements tests the advancements.
  """

  def test_advancements(self) -> None:
    stoneAge = MCAdvancements.STONE_AGE
    self.assertIsInstance(stoneAge, MCAdvancements)
    self.assertIsInstance(stoneAge, MCThing)
    self.assertEqual(stoneAge[Version.V1_12],
                     AdvancementId('stone_age', 'minecraft:story/mine_stone'))
    self.assertIsInstance(stoneAge[Version.V26_3], GameId)
    self.assertEqual(repr(stoneAge), "<MCAdvancements>.STONE_AGE")
    self.assertEqual(len(MCAdvancements), 1937)
    self.assertNotEqual(AdvancementId('x', 'minecraft:x'),
                        StatisticId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = stoneAge[Version.V1_11_2]
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.11.2 has no 'stone_age'; vanilla added it in 1.12!",
    )
    with self.assertRaises(KeyError):
      _ = MCAdvancements['mine_stone']

  def test_names(self) -> None:
    """
    An advancement is its title, the one its own file names; the root of
    a tab is the tab's root; a recipe advancement its recipe and 'recipe'.
    """
    for advancement, minecraftId in (
        (MCAdvancements.STONE_AGE, 'minecraft:story/mine_stone'),
        (MCAdvancements.TWO_BY_TWO, 'minecraft:husbandry/bred_all_animals'),
        (MCAdvancements.THE_POWER_OF_BOOKS,
         'minecraft:adventure/read_power_of_chiseled_bookshelf'),
        (MCAdvancements.THE_END, 'minecraft:story/enter_the_end'),
        (MCAdvancements.END_ROOT, 'minecraft:end/root'),
        (MCAdvancements.STORY_ROOT, 'minecraft:story/root'),
        (MCAdvancements.ACACIA_PLANKS_RECIPE,
         'minecraft:recipes/building_blocks/acacia_planks')):
      with self.subTest(advancement=advancement):
        self.assertEqual(advancement[Version.V26_3].minecraftId, minecraftId)
    for advancement in MCAdvancements:
      with self.subTest(advancement=advancement):
        self.assertRegex(advancement.uniqueName, r'^[a-z0-9_]+$')

  def test_renamed(self) -> None:
    """Mojang's renames: the lodestone's moved from nether to adventure."""
    countryLodeTakeMeHome = MCAdvancements.COUNTRY_LODE_TAKE_ME_HOME
    self.assertEqual(countryLodeTakeMeHome[Version.V1_16].minecraftId,
                     'minecraft:nether/use_lodestone')
    self.assertEqual(countryLodeTakeMeHome[Version.V1_21_5].minecraftId,
                     'minecraft:adventure/use_lodestone')
    glisteringMelonSliceRecipe = MCAdvancements.GLISTERING_MELON_SLICE_RECIPE
    self.assertEqual(glisteringMelonSliceRecipe[Version.V1_12].minecraftId,
                     'minecraft:recipes/brewing/speckled_melon')

  def test_moved(self) -> None:
    """
    An advancement the game moved with no fixer to say so is one: the
    title of the diamond hoe's went to the netherite hoe's in 1.16, and a
    recipe moved from one category to another in 1.21.6.
    """
    seriousDedication = MCAdvancements.SERIOUS_DEDICATION
    self.assertEqual(seriousDedication[Version.V1_15_2].minecraftId,
                     'minecraft:husbandry/break_diamond_hoe')
    self.assertEqual(seriousDedication[Version.V1_16].minecraftId,
                     'minecraft:husbandry/obtain_netherite_hoe')
    dyeBlackBedRecipe = MCAdvancements.DYE_BLACK_BED_RECIPE
    self.assertEqual(dyeBlackBedRecipe[Version.V1_21_5].minecraftId,
                     'minecraft:recipes/building_blocks/dye_black_bed')
    self.assertEqual(dyeBlackBedRecipe[Version.V1_21_6].minecraftId,
                     'minecraft:recipes/decorations/dye_black_bed')
