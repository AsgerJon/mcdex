"""
mcdex is a typed, version-agnostic catalogue of Minecraft: every item,
block and entity with one identity across all versions of the game,
carrying what it is, what it does and when it arrived. The elytra is one
thing, whatever a given version calls it or numbers it.

- base: the versions of the game, and the classes every kind is built on
- items: the catalogue of items
- entities: the catalogue of entities
- blocks: the catalogue of blocks
- effects: the catalogue of effects
- enchantments: the catalogue of enchantments
- potions: the catalogue of potions
- biomes: the catalogue of biomes
- block_entities: the catalogue of block entities
- particles: the catalogue of particles
- sounds: the catalogue of sounds
- attributes: the catalogue of attributes
- statistics: the catalogue of statistics
- game_rules: the catalogue of game rules
- villager_professions: the catalogue of villager professions
- villager_types: the catalogue of villager types
- dimensions: the catalogue of dimensions
- damage_types: the catalogue of damage types
- music: the catalogue of the songs of music discs
- trim_patterns: the catalogue of trim patterns
- trim_materials: the catalogue of trim materials
- wolf_variants: the catalogue of wolf variants
- cat_variants: the catalogue of cat variants
- frog_variants: the catalogue of frog variants
- pig_variants: the catalogue of pig variants
- cow_variants: the catalogue of cow variants
- chicken_variants: the catalogue of chicken variants
- zombie_nautilus_variants: the catalogue of zombie nautilus variants
- wolf_sound_variants: the catalogue of wolf sound variants
- cat_sound_variants: the catalogue of cat sound variants
- pig_sound_variants: the catalogue of pig sound variants
- cow_sound_variants: the catalogue of cow sound variants
- chicken_sound_variants: the catalogue of chicken sound variants
- painting_variants: the catalogue of painting variants
- banner_patterns: the catalogue of banner patterns
- advancements: the catalogue of advancements
- structures: the catalogue of structures

mcdex is not affiliated with Mojang or Microsoft.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

__version__ = '0.1.0-dev0'

from . import base
from . import items
from . import entities
from . import blocks
from . import effects
from . import enchantments
from . import potions
from . import biomes
from . import block_entities
from . import particles
from . import sounds
from . import attributes
from . import statistics
from . import game_rules
from . import villager_professions
from . import villager_types
from . import dimensions
from . import damage_types
from . import music
from . import trim_patterns
from . import trim_materials
from . import wolf_variants
from . import cat_variants
from . import frog_variants
from . import pig_variants
from . import cow_variants
from . import chicken_variants
from . import zombie_nautilus_variants
from . import wolf_sound_variants
from . import cat_sound_variants
from . import pig_sound_variants
from . import cow_sound_variants
from . import chicken_sound_variants
from . import painting_variants
from . import banner_patterns
from . import advancements
from . import structures
from .base import MCVersion, Version, EquipmentSlot, ItemId, NotInVersion
from .base import GameId, MCThing
from .base import EntityId, BlockId
from .items import MCItems
from .entities import MCEntities
from .blocks import MCBlocks
from .base import EffectId
from .effects import MCEffects
from .base import EnchantmentId
from .enchantments import MCEnchantments
from .base import PotionId, PotionModifier
from .potions import MCPotions, ModifiedPotion
from .base import BiomeId
from .biomes import MCBiomes
from .base import BlockEntityId
from .block_entities import MCBlockEntities
from .base import ParticleId
from .particles import MCParticles
from .base import SoundId
from .sounds import MCSounds
from .base import AttributeId
from .attributes import MCAttributes
from .base import StatisticId
from .statistics import MCStatistics
from .base import GameRuleId
from .game_rules import MCGameRules
from .base import VillagerProfessionId
from .villager_professions import MCVillagerProfessions
from .base import VillagerTypeId
from .villager_types import MCVillagerTypes
from .base import DimensionId
from .dimensions import MCDimensions
from .base import DamageTypeId
from .damage_types import MCDamageTypes
from .base import MusicId
from .music import Music
from .base import TrimPatternId
from .trim_patterns import MCTrimPatterns
from .base import TrimMaterialId
from .trim_materials import MCTrimMaterials
from .base import WolfVariantId
from .wolf_variants import MCWolfVariants
from .base import CatVariantId
from .cat_variants import MCCatVariants
from .base import FrogVariantId
from .frog_variants import MCFrogVariants
from .base import PigVariantId
from .pig_variants import MCPigVariants
from .base import CowVariantId
from .cow_variants import MCCowVariants
from .base import ChickenVariantId
from .chicken_variants import MCChickenVariants
from .base import ZombieNautilusVariantId
from .zombie_nautilus_variants import MCZombieNautilusVariants
from .base import WolfSoundVariantId
from .wolf_sound_variants import MCWolfSoundVariants
from .base import CatSoundVariantId
from .cat_sound_variants import MCCatSoundVariants
from .base import PigSoundVariantId
from .pig_sound_variants import MCPigSoundVariants
from .base import CowSoundVariantId
from .cow_sound_variants import MCCowSoundVariants
from .base import ChickenSoundVariantId
from .chicken_sound_variants import MCChickenSoundVariants
from .base import PaintingVariantId
from .painting_variants import MCPaintingVariants
from .base import BannerPatternId
from .banner_patterns import MCBannerPatterns
from .base import AdvancementId
from .advancements import MCAdvancements
from .base import StructureId
from .structures import MCStructures

__all__ = (
  'base',
  'items',
  'entities',
  'blocks',
  'effects',
  'enchantments',
  'potions',
  'biomes',
  'block_entities',
  'particles',
  'sounds',
  'attributes',
  'statistics',
  'game_rules',
  'villager_professions',
  'villager_types',
  'dimensions',
  'damage_types',
  'music',
  'trim_patterns',
  'trim_materials',
  'wolf_variants',
  'cat_variants',
  'frog_variants',
  'pig_variants',
  'cow_variants',
  'chicken_variants',
  'zombie_nautilus_variants',
  'wolf_sound_variants',
  'cat_sound_variants',
  'pig_sound_variants',
  'cow_sound_variants',
  'chicken_sound_variants',
  'painting_variants',
  'banner_patterns',
  'advancements',
  'structures',
  'MCVersion',
  'Version',
  'EquipmentSlot',
  'ItemId',
  'NotInVersion',
  'MCItems',
  'EntityId',
  'MCEntities',
  'GameId',
  'MCThing',
  'BlockId',
  'MCBlocks',
  'EffectId',
  'MCEffects',
  'EnchantmentId',
  'MCEnchantments',
  'PotionId',
  'PotionModifier',
  'ModifiedPotion',
  'MCPotions',
  'BiomeId',
  'MCBiomes',
  'BlockEntityId',
  'MCBlockEntities',
  'ParticleId',
  'MCParticles',
  'SoundId',
  'MCSounds',
  'AttributeId',
  'MCAttributes',
  'StatisticId',
  'MCStatistics',
  'GameRuleId',
  'MCGameRules',
  'VillagerProfessionId',
  'MCVillagerProfessions',
  'VillagerTypeId',
  'MCVillagerTypes',
  'DimensionId',
  'MCDimensions',
  'DamageTypeId',
  'MCDamageTypes',
  'MusicId',
  'Music',
  'TrimPatternId',
  'MCTrimPatterns',
  'TrimMaterialId',
  'MCTrimMaterials',
  'WolfVariantId',
  'MCWolfVariants',
  'CatVariantId',
  'MCCatVariants',
  'FrogVariantId',
  'MCFrogVariants',
  'PigVariantId',
  'MCPigVariants',
  'CowVariantId',
  'MCCowVariants',
  'ChickenVariantId',
  'MCChickenVariants',
  'ZombieNautilusVariantId',
  'MCZombieNautilusVariants',
  'WolfSoundVariantId',
  'MCWolfSoundVariants',
  'CatSoundVariantId',
  'MCCatSoundVariants',
  'PigSoundVariantId',
  'MCPigSoundVariants',
  'CowSoundVariantId',
  'MCCowSoundVariants',
  'ChickenSoundVariantId',
  'MCChickenSoundVariants',
  'PaintingVariantId',
  'MCPaintingVariants',
  'BannerPatternId',
  'MCBannerPatterns',
  'AdvancementId',
  'MCAdvancements',
  'StructureId',
  'MCStructures',
)
