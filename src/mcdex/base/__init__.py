"""
The 'mcdex.base' package provides what every catalogue is built on: the
versions of the game, the equipment slots, the base of every catalogue
('MCThing'), and each kind's id class: the item's, the entity's, the
block's.

- MCVersion
- Version
- EquipmentSlot
- ItemId
- NotInVersion
- GameId
- CatalogueMeta
- MCThing
- EntityId
- BlockId
- EffectId
- EnchantmentId
- PotionId
- PotionModifier
- BiomeId
- BlockEntityId
- ParticleId
- SoundId
- AttributeId
- StatisticId
- GameRuleId
- VillagerProfessionId
- VillagerTypeId
- DimensionId
- DamageTypeId
- MusicId
- TrimPatternId
- TrimMaterialId
- WolfVariantId
- CatVariantId
- FrogVariantId
- PigVariantId
- CowVariantId
- ChickenVariantId
- ZombieNautilusVariantId
- WolfSoundVariantId
- CatSoundVariantId
- PigSoundVariantId
- CowSoundVariantId
- ChickenSoundVariantId
- PaintingVariantId
- BannerPatternId
- AdvancementId
- StructureId
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._mc_version import MCVersion
from ._version import Version
from ._equipment_slot import EquipmentSlot
from ._item_id import ItemId
from ._not_in_version import NotInVersion
from ._game_id import GameId
from ._catalogue_meta import CatalogueMeta
from ._mc_thing import MCThing
from ._entity_id import EntityId
from ._block_id import BlockId
from ._effect_id import EffectId
from ._enchantment_id import EnchantmentId
from ._potion_id import PotionId
from ._potion_modifier import PotionModifier
from ._biome_id import BiomeId
from ._block_entity_id import BlockEntityId
from ._particle_id import ParticleId
from ._sound_id import SoundId
from ._attribute_id import AttributeId
from ._statistic_id import StatisticId
from ._game_rule_id import GameRuleId
from ._villager_profession_id import VillagerProfessionId
from ._villager_type_id import VillagerTypeId
from ._dimension_id import DimensionId
from ._damage_type_id import DamageTypeId
from ._music_id import MusicId
from ._trim_pattern_id import TrimPatternId
from ._trim_material_id import TrimMaterialId
from ._wolf_variant_id import WolfVariantId
from ._cat_variant_id import CatVariantId
from ._frog_variant_id import FrogVariantId
from ._pig_variant_id import PigVariantId
from ._cow_variant_id import CowVariantId
from ._chicken_variant_id import ChickenVariantId
from ._zombie_nautilus_variant_id import ZombieNautilusVariantId
from ._wolf_sound_variant_id import WolfSoundVariantId
from ._cat_sound_variant_id import CatSoundVariantId
from ._pig_sound_variant_id import PigSoundVariantId
from ._cow_sound_variant_id import CowSoundVariantId
from ._chicken_sound_variant_id import ChickenSoundVariantId
from ._painting_variant_id import PaintingVariantId
from ._banner_pattern_id import BannerPatternId
from ._advancement_id import AdvancementId
from ._structure_id import StructureId

__all__ = (
  'MCVersion',
  'Version',
  'EquipmentSlot',
  'ItemId',
  'NotInVersion',
  'GameId',
  'CatalogueMeta',
  'MCThing',
  'EntityId',
  'BlockId',
  'EffectId',
  'EnchantmentId',
  'PotionId',
  'PotionModifier',
  'BiomeId',
  'BlockEntityId',
  'ParticleId',
  'SoundId',
  'AttributeId',
  'StatisticId',
  'GameRuleId',
  'VillagerProfessionId',
  'VillagerTypeId',
  'DimensionId',
  'DamageTypeId',
  'MusicId',
  'TrimPatternId',
  'TrimMaterialId',
  'WolfVariantId',
  'CatVariantId',
  'FrogVariantId',
  'PigVariantId',
  'CowVariantId',
  'ChickenVariantId',
  'ZombieNautilusVariantId',
  'WolfSoundVariantId',
  'CatSoundVariantId',
  'PigSoundVariantId',
  'CowSoundVariantId',
  'ChickenSoundVariantId',
  'PaintingVariantId',
  'BannerPatternId',
  'AdvancementId',
  'StructureId',
)
