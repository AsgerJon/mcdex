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
    stoneAge = MCAdvancements.StoneAge
    self.assertIsInstance(stoneAge, MCAdvancements)
    self.assertIsInstance(stoneAge, MCThing)
    self.assertEqual(stoneAge[Version.V1_12],
                     AdvancementId('stone_age', 'minecraft:story/mine_stone'))
    self.assertIsInstance(stoneAge[Version.V26_3], GameId)
    self.assertEqual(repr(stoneAge), "<MCAdvancements>.StoneAge")
    self.assertEqual(len(MCAdvancements), 1938)
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
        (MCAdvancements.StoneAge, 'minecraft:story/mine_stone'),
        (MCAdvancements.TwoByTwo, 'minecraft:husbandry/bred_all_animals'),
        (MCAdvancements.ThePowerOfBooks,
         'minecraft:adventure/read_power_of_chiseled_bookshelf'),
        (MCAdvancements.TheEnd, 'minecraft:story/enter_the_end'),
        (MCAdvancements.EndRoot, 'minecraft:end/root'),
        (MCAdvancements.StoryRoot, 'minecraft:story/root'),
        (MCAdvancements.AcaciaPlanksRecipe,
         'minecraft:recipes/building_blocks/acacia_planks')):
      with self.subTest(advancement=advancement):
        self.assertEqual(advancement[Version.V26_3].minecraftId, minecraftId)
    for advancement in MCAdvancements:
      with self.subTest(advancement=advancement):
        self.assertRegex(advancement.uniqueName, r'^[a-z0-9_]+$')

  def test_renamed(self) -> None:
    """Mojang's renames: the lodestone's moved from nether to adventure."""
    countryLodeTakeMeHome = MCAdvancements.CountryLodeTakeMeHome
    self.assertEqual(countryLodeTakeMeHome[Version.V1_16].minecraftId,
                     'minecraft:nether/use_lodestone')
    self.assertEqual(countryLodeTakeMeHome[Version.V1_21_5].minecraftId,
                     'minecraft:adventure/use_lodestone')
    glisteringMelonSliceRecipe = MCAdvancements.GlisteringMelonSliceRecipe
    self.assertEqual(glisteringMelonSliceRecipe[Version.V1_12].minecraftId,
                     'minecraft:recipes/brewing/speckled_melon')

  def test_game_names(self) -> None:
    """
    The game's names find an advancement too, as '/advancement' takes
    them, the old ones included.
    """
    self.assertIs(MCAdvancements['story/mine_stone'],
                  MCAdvancements.StoneAge)
    self.assertIs(MCAdvancements['minecraft:story/mine_stone'],
                  MCAdvancements.StoneAge)
    self.assertIs(MCAdvancements['nether/use_lodestone'],
                  MCAdvancements.CountryLodeTakeMeHome)
    self.assertIs(MCAdvancements['recipes/brewing/speckled_melon'],
                  MCAdvancements.GlisteringMelonSliceRecipe)
    #  1.12's name of the cobblestone stairs' recipe, the stone stairs'
    #  from 1.14: the name finds the one that held it last.
    self.assertIs(MCAdvancements['recipes/building_blocks/stone_stairs'],
                  MCAdvancements.StoneStairsRecipe)

  def test_same_title_other_goal(self) -> None:
    """
    An advancement whose title went to another goal is two: "Serious
    Dedication" wore out a diamond hoe to 1.15.2 and makes a netherite hoe
    from 1.16. The newer has the title, the older its own name.
    """
    seriousDedication = MCAdvancements.SeriousDedication
    breakDiamondHoe = MCAdvancements.BreakDiamondHoe
    self.assertEqual(seriousDedication[Version.V1_16].minecraftId,
                     'minecraft:husbandry/obtain_netherite_hoe')
    self.assertEqual(breakDiamondHoe[Version.V1_15_2].minecraftId,
                     'minecraft:husbandry/break_diamond_hoe')
    with self.assertRaises(NotInVersion):
      _ = seriousDedication[Version.V1_15_2]
    with self.assertRaises(NotInVersion):
      _ = breakDiamondHoe[Version.V1_16]

  def test_moved(self) -> None:
    """A recipe moved from one category to another in 1.21.6 is one."""
    dyeBlackBedRecipe = MCAdvancements.DyeBlackBedRecipe
    self.assertEqual(dyeBlackBedRecipe[Version.V1_21_5].minecraftId,
                     'minecraft:recipes/building_blocks/dye_black_bed')
    self.assertEqual(dyeBlackBedRecipe[Version.V1_21_6].minecraftId,
                     'minecraft:recipes/decorations/dye_black_bed')
