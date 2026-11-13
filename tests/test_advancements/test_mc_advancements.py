"""
TestMCAdvancements tests the advancements: the 'AdvancementId' and
'MCAdvancements' classes, and the 'MCAdvancements' catalogue.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from worktoy.work_test import BaseTest

from mcdex import AdvancementId, GameId, MCAdvancements
from mcdex import MCThing, NotInVersion, StatisticId


class TestMCAdvancements(BaseTest):
  """
  TestMCAdvancements tests the advancements.
  """

  def test_advancements(self) -> None:
    mineStone = MCAdvancements['story/mine_stone']
    self.assertIsInstance(mineStone, MCAdvancements)
    self.assertIsInstance(mineStone, MCThing)
    self.assertEqual(mineStone['1.12'],
                     AdvancementId('story/mine_stone',
                                   'minecraft:story/mine_stone'))
    self.assertIsInstance(mineStone['26.3'], GameId)
    self.assertEqual(repr(mineStone), "<MCAdvancements>.STORY_MINE_STONE")
    self.assertEqual(len(MCAdvancements), 1984)
    self.assertNotEqual(AdvancementId('x', 'minecraft:x'),
                        StatisticId('x', 'minecraft:x'))
    with self.assertRaises(NotInVersion) as context:
      _ = mineStone['1.11.2']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.11.2 has no 'story/mine_stone'; vanilla added it in 1.12!",
    )
    with self.assertRaises(KeyError):
      _ = MCAdvancements['mine_stone']

  def test_renamed(self) -> None:
    """Mojang's renames: the lodestone's moved from nether to adventure."""
    useLodestone = MCAdvancements['adventure/use_lodestone']
    self.assertEqual(useLodestone['1.16'].minecraftId,
                     'minecraft:nether/use_lodestone')
    self.assertEqual(useLodestone['1.21.5'].minecraftId,
                     'minecraft:adventure/use_lodestone')
    melon = MCAdvancements['recipes/brewing/glistering_melon_slice']
    self.assertEqual(melon['1.12'].minecraftId,
                     'minecraft:recipes/brewing/speckled_melon')
    breakDiamondHoe = MCAdvancements['husbandry/break_diamond_hoe']
    with self.assertRaises(NotInVersion) as context:
      _ = breakDiamondHoe['1.16']
    self.assertEqual(
        str(context.exception),
        "Vanilla 1.16 has no 'husbandry/break_diamond_hoe'; "
        "vanilla removed it in 1.16!",
    )
