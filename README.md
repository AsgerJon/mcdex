[![Tokens](https://img.shields.io/badge/Tokens-1.2B-D97757)](https://claude.com/claude-code)
[![codecov](https://codecov.io/gh/AsgerJon/mcdex/graph/badge.svg)](https://codecov.io/gh/AsgerJon/mcdex)
[![PyPI version](https://img.shields.io/pypi/v/mcdex)](https://pypi.org/project/mcdex/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# mcdex v0.1.0-dev0 (development build)
A typed, version-agnostic catalogue of Minecraft for Python: every item, block and entity with one identity across all versions, carrying what it is, what it does and when it arrived. Name a thing once and it means the same on 1.7.10 and on 26.3. Not affiliated with Mojang or Microsoft.

Items, entities, blocks, mob effects, enchantments, potions, biomes, block entities, particles, sounds, attributes, statistics, game rules, villager professions and types, dimensions, damage types, armor trims, music, mob variants, paintings, banner patterns, advancements and structures are in. The data covers every release from 1.7.2 to 26.3.

```python
from mcdex import MCEntities, MCItems

pinkWool = MCItems['pink_wool']

pinkWool['1.7.10'].minecraftId    # 'minecraft:wool:6'
pinkWool['1.12.2'].minecraftId    # 'minecraft:wool:6'
pinkWool['1.13'].minecraftId      # 'minecraft:pink_wool'
pinkWool['26.3'].minecraftId      # 'minecraft:pink_wool'

witherSkeleton = MCEntities['wither_skeleton']

witherSkeleton['1.7.10'].minecraftId    # 'Skeleton{SkeletonType:1}'
witherSkeleton['1.10.2'].minecraftId    # 'Skeleton{SkeletonType:1}'
witherSkeleton['1.11'].minecraftId      # 'minecraft:wither_skeleton'
witherSkeleton['26.3'].minecraftId      # 'minecraft:wither_skeleton'
```

You write `pink_wool` once. mcdex knows that 1.12.2 calls it `minecraft:wool` with meta 6 and 1.13 calls it `minecraft:pink_wool`, and the same for every other item and version.

Entities work the same way, and their ids are what `/summon` takes. Until 1.11 the wither skeleton was a skeleton of type 1, so 1.10.2 summons it as `Skeleton{SkeletonType:1}`. Since 1.11 it is `minecraft:wither_skeleton`.

## Contents

- [Items](#items)
  - [Finding an item](#finding-an-item)
  - [What a version calls an item](#what-a-version-calls-an-item)
  - [When vanilla has no such item](#when-vanilla-has-no-such-item)
  - [The whole history of an item](#the-whole-history-of-an-item)
  - [One old id, two items](#one-old-id-two-items)
- [Entities](#entities)
  - [Finding an entity](#finding-an-entity)
  - [What a version calls an entity](#what-a-version-calls-an-entity)
  - [Entities told apart by their data](#entities-told-apart-by-their-data)
  - [When vanilla has no such entity](#when-vanilla-has-no-such-entity)
- [Blocks](#blocks)
- [Mob effects](#mob-effects)
- [Enchantments](#enchantments)
- [Potions](#potions)
- [Biomes](#biomes)
- [Block entities](#block-entities)
- [Particles](#particles)
- [Sounds](#sounds)
- [Attributes](#attributes)
- [Statistics](#statistics)
- [Game rules](#game-rules)
- [Villager professions and types](#villager-professions-and-types)
- [Dimensions](#dimensions)
- [Damage types](#damage-types)
- [Armor trims](#armor-trims)
- [Music](#music)
- [Mob variants](#mob-variants)
- [Paintings](#paintings)
- [Banner patterns](#banner-patterns)
- [Advancements](#advancements)
- [Structures](#structures)
- [Versions](#versions)
- [Equipment slots](#equipment-slots)
- [Item ids](#item-ids)
- [Entity ids](#entity-ids)
- [Block ids](#block-ids)
- [Recipes](#recipes)
- [Where the data comes from](#where-the-data-comes-from)
- [Development](#development)

## Items

### Finding an item

`MCItems` is the catalogue, and an enumeration: each item is one of its members, named by the item's unique name in capitals. A member is found by that name, in any case, or by indexing the catalogue with the unique name:

```python
from mcdex import MCItems

diamond = MCItems.DIAMOND
diamond                        # <MCItems>.DIAMOND
diamond.uniqueName             # 'diamond'
MCItems['diamond'] is diamond  # True
MCItems.Diamond is diamond     # True
```

Every catalogue of mcdex is such an enumeration, built on worktoy's `KeeNum`, so an editor can complete `MCItems.PINK_WOOL`. A unique name that is no member's name, as the sound `entity.creeper.primed`, is found by indexing: `MCSounds['entity.creeper.primed']` is `MCSounds.ENTITY_CREEPER_PRIMED`.

The data ships inside the package, in `mcdex/items/items.json`. Importing mcdex makes the members but reads none of the data: the first use of a catalogue reads its file, in a few milliseconds, and an item's record is read at the item's first use.

The class itself is the catalogue. It has a length, it can be searched, and it can be iterated, in the order of the names:

```python
len(MCItems)                   # 1672
'pink_wool' in MCItems         # True
'grss' in MCItems              # False

for item in MCItems:
    print(item.uniqueName)     # abandoned_camp_map, acacia_boat, acacia_button, ...
```

A name the catalogue lacks raises `KeyError`:

```python
MCItems['grss']                # KeyError: "mcdex has no item named 'grss'"
```

A unique name is mcdex's own name for the item, the same in every version, in lowercase words joined by underscores. It is the item's most modern name: the name it has in 26.3, or, for an item removed before 26.3, the last name it had. A name means one thing in every version: `grass` is the short grass growing on top of blocks, in every version, and `grass_block` is the block. A few items have two names. The short grass is both `grass` and `short_grass`, the name 26.3 gives it, and either name gives the same item's ids.

### What a version calls an item

Index an item with a version to get its `ItemId` in that version:

```python
from mcdex import MCItems, MCVersion, Version

pinkWool = MCItems['pink_wool']

pinkWool[Version.V1_12_2]      # ItemId('pink_wool', 'minecraft:wool:6')
pinkWool['1.12.2']             # the same: the version as the game reports it
pinkWool['V1_13']              # ItemId('pink_wool', 'minecraft:pink_wool'), by member name
pinkWool[MCVersion(26, 3)]     # ItemId('pink_wool', 'minecraft:pink_wool')
```

An `ItemId` holds two strings: `uniqueName`, mcdex's name, and `minecraftId`, everything that version of the game needs to identify the item. The `minecraftId` is written in the notation of its era:

| Versions | Notation | Pink wool | Creeper spawn egg |
|---|---|---|---|
| 1.7.2 to 1.8.9 | name, and the meta where it tells items apart | `minecraft:wool:6` | `minecraft:spawn_egg:50` |
| 1.9 to 1.10.2 | the same, with NBT where the game tells items apart by it | `minecraft:wool:6` | `minecraft:spawn_egg{EntityTag:{id:"Creeper"}}` |
| 1.11 to 1.12.2 | the same | `minecraft:wool:6` | `minecraft:spawn_egg{EntityTag:{id:"minecraft:creeper"}}` |
| 1.13 to 26.3 | the name alone | `minecraft:pink_wool` | `minecraft:creeper_spawn_egg` |

The meta is part of the id only where it tells items apart: `minecraft:diamond` has none, and neither do tools, whose meta is only their damage. Stone has none in 1.7.10, when there was only one kind, and has `:0` from 1.8, when granite, diorite and andesite joined it as `:1` to `:6`. Before 1.9, a splash potion was a potion with the splash bit set in its meta: `minecraft:potion:16384`.

Some items and what they were called over the years:

```python
MCItems['grass']['1.12.2'].minecraftId              # 'minecraft:tallgrass:1'
MCItems['grass']['1.13'].minecraftId                # 'minecraft:grass'
MCItems['grass']['26.3'].minecraftId                # 'minecraft:short_grass'

MCItems['grass_block']['1.12.2'].minecraftId        # 'minecraft:grass'
MCItems['grass_block']['1.13'].minecraftId          # 'minecraft:grass_block'

MCItems['red_bed']['1.11.2'].minecraftId            # 'minecraft:bed'
MCItems['red_bed']['1.12.2'].minecraftId            # 'minecraft:bed:14'
MCItems['red_bed']['1.13'].minecraftId              # 'minecraft:red_bed'

MCItems['cooked_cod']['1.7.10'].minecraftId         # 'minecraft:cooked_fished:0'
MCItems['cooked_cod']['1.8.9'].minecraftId          # 'minecraft:cooked_fish:0'
MCItems['cooked_cod']['1.13'].minecraftId           # 'minecraft:cooked_cod'

MCItems['oak_door']['1.12.2'].minecraftId           # 'minecraft:wooden_door'
MCItems['dragon_head']['1.12.2'].minecraftId        # 'minecraft:skull:5'
MCItems['iron_chain']['1.20.2'].minecraftId         # 'minecraft:chain'
MCItems['iron_chain']['1.21.9'].minecraftId         # 'minecraft:iron_chain'
MCItems['splash_potion']['1.8.9'].minecraftId       # 'minecraft:potion:16384'
```

### When vanilla has no such item

A version without the item raises `NotInVersion`, a `LookupError`. Its message says when vanilla added the item, or when it removed it:

```python
from mcdex import MCItems, NotInVersion

MCItems['elytra']['1.7.10']
# NotInVersion: Vanilla 1.7.10 has no 'elytra'; vanilla added it in 1.9!

MCItems['lit_furnace']['1.10']
# NotInVersion: Vanilla 1.10 has no 'lit_furnace'; vanilla removed it in 1.9!

try:
    MCItems['elytra']['1.7.10']
except NotInVersion as exception:
    exception.item             # <MCItems>.ELYTRA
    exception.version          # <Version>.V1_7_10
```

This speaks only of vanilla. A mod may bring the elytra to 1.7.10 under an id of its own, so `NotInVersion` cannot tell whether a given game has the item; it is what a test cites when the game lacks it.

Two other failures are not `NotInVersion`. A version before the data raises `ValueError`, and a version that is no release raises `KeeResolveError`:

```python
MCItems['diamond']['1.6.4']             # ValueError: mcdex has no data on 'diamond' before 1.7.2
MCItems['diamond']['26.4-snapshot-7']   # KeeResolveError
```

### The whole history of an item

Each item has three tables, built when first read and handed out as copies:

- `versionIds`: the id in every version from the first the data covers, `''` where vanilla has no such item.
- `maxStackSize`: the max stack size in every version that has the item.
- `equipmentSlot`: the `EquipmentSlot` an entity equips the item to, in every version that has it.

```python
from mcdex import EquipmentSlot, MCItems, Version

elytra = MCItems['elytra']
elytra.versionIds[Version.V1_8_9]       # ''
elytra.versionIds[Version.V1_9]         # 'minecraft:elytra'
len(elytra.versionIds)                  # 84, from 1.7.2 to 26.3
elytra.maxStackSize[Version.V1_9]       # 1
elytra.equipmentSlot[Version.V1_9]      # <EquipmentSlot>.CHEST
Version.V1_8_9 in elytra.equipmentSlot  # False: vanilla 1.8.9 has no elytra
```

Stack sizes and slots change between versions, and mcdex reads them per version:

```python
MCItems['oak_door'].maxStackSize[Version.V1_7_10]       # 1
MCItems['oak_door'].maxStackSize[Version.V1_8]          # 64

MCItems['shield'].equipmentSlot[Version.V1_9]           # <EquipmentSlot>.MAINHAND
MCItems['shield'].equipmentSlot[Version.V1_10]          # <EquipmentSlot>.OFFHAND

MCItems['carved_pumpkin'].equipmentSlot[Version.V1_12_2]  # <EquipmentSlot>.HEAD
MCItems['white_carpet'].equipmentSlot[Version.V1_20_5]    # <EquipmentSlot>.BODY, for llamas
MCItems['saddle'].equipmentSlot[Version.V1_21_4]          # <EquipmentSlot>.MAINHAND
MCItems['saddle'].equipmentSlot[Version.V1_21_5]          # <EquipmentSlot>.SADDLE
```

The 1.9 shield is no mistake. 1.9 added the offhand, but its code deciding an item's slot had no case for the shield yet; 1.10 added one.

### One old id, two items

A game id can belong to two items in one version, when the old item was both. In 1.12.2 there was no undyed shulker box, and the purple one was the shulker box; 1.13 added the undyed one. Before 1.13 every pumpkin had a face; 1.13 added the plain one. Until 1.14 the stone slab had the smooth look; 1.14 renamed it and added a plain one.

```python
MCItems['shulker_box']['1.12.2'].minecraftId          # 'minecraft:purple_shulker_box'
MCItems['purple_shulker_box']['1.12.2'].minecraftId   # 'minecraft:purple_shulker_box'
MCItems['shulker_box']['1.13'].minecraftId            # 'minecraft:shulker_box'

MCItems['pumpkin']['1.12.2'].minecraftId              # 'minecraft:pumpkin'
MCItems['carved_pumpkin']['1.12.2'].minecraftId       # 'minecraft:pumpkin'
MCItems['carved_pumpkin']['1.13'].minecraftId         # 'minecraft:carved_pumpkin'

MCItems['stone_slab']['1.13'].minecraftId             # 'minecraft:stone_slab'
MCItems['smooth_stone_slab']['1.13'].minecraftId      # 'minecraft:stone_slab'
MCItems['smooth_stone_slab']['1.14'].minecraftId      # 'minecraft:smooth_stone_slab'
```

Where a name was reused for a different thing, nothing is shared: 1.12.2's `minecraft:grass` is the grass block alone, and the old `minecraft:stone_stairs` were cobblestone stairs, so `stone_stairs` begins in 1.14.

## Entities

### Finding an entity

`MCEntities` is the catalogue of entities: everything a version of the game knows an entity by, which is what `/summon` takes and what `@e[type=...]` matches. It works like `MCItems`:

```python
from mcdex import MCEntities

creeper = MCEntities['creeper']
creeper.uniqueName                 # 'creeper'
MCEntities['creeper'] is creeper   # True
len(MCEntities)                    # 162
'stray' in MCEntities              # True
```

An entity's unique name is its name in 26.3. An entity removed before 26.3 keeps its last name, as `creaking_transient` does. The player and the fishing bobber are in the catalogue because the game names them, though `/summon` refuses both.

### What a version calls an entity

```python
creeper['1.10.2'].minecraftId      # 'Creeper'
creeper['1.11'].minecraftId        # 'minecraft:creeper'

zombifiedPiglin = MCEntities['zombified_piglin']
zombifiedPiglin['1.10.2'].minecraftId   # 'PigZombie'
zombifiedPiglin['1.15.2'].minecraftId   # 'minecraft:zombie_pigman'
zombifiedPiglin['1.16'].minecraftId     # 'minecraft:zombified_piglin'
```

Up to 1.10.2 the game named its entities in CamelCase: `Creeper`, `EntityHorse`, `MinecartRideable`. 1.11 gave them `minecraft:` names, and later versions renamed some.

### Entities told apart by their data

Some entities were once one entity, told apart by a value in its data. Before 1.11 the wither skeleton was a skeleton of type 1. Before 1.21.2 every boat was one entity with a wood type. An old id carries that data after the name, as `/summon` takes it:

```python
witherSkeleton = MCEntities['wither_skeleton']
witherSkeleton['1.10.2'].minecraftId    # 'Skeleton{SkeletonType:1}'
witherSkeleton['1.11'].minecraftId      # 'minecraft:wither_skeleton'

MCEntities['donkey']['1.10.2'].minecraftId            # 'EntityHorse{Type:1}'
MCEntities['zombie_villager']['1.8.9'].minecraftId    # 'Zombie{IsVillager:1b}'
MCEntities['zombie_villager']['1.10'].minecraftId     # 'Zombie{ZombieType:1}'
MCEntities['cat']['1.13.2'].minecraftId               # 'minecraft:ocelot{CatType:1}'
MCEntities['spruce_boat']['1.21.1'].minecraftId       # 'minecraft:boat{Type:"spruce"}'
MCEntities['lingering_potion']['1.20.4'].minecraftId
# 'minecraft:potion{Item:{id:"minecraft:lingering_potion",Count:1b}}'
```

The entity without that data is the first of them. A plain `EntityHorse` is the horse, a plain boat is the oak boat, and a plain thrown potion is the splash potion:

```python
MCEntities['horse']['1.10.2'].minecraftId             # 'EntityHorse'
MCEntities['oak_boat']['1.21.1'].minecraftId          # 'minecraft:boat'
MCEntities['splash_potion']['1.21.4'].minecraftId     # 'minecraft:potion'
```

Each id uses the data in the form that version's own entity code reads it. A zombie villager is `Zombie{IsVillager:1b}` in 1.8.9, adds the `VillagerProfession` that 1.9 began to read, and becomes `Zombie{ZombieType:1}` in 1.10.

### When vanilla has no such entity

```python
MCEntities['stray']['1.9.4']
# NotInVersion: Vanilla 1.9.4 has no 'stray'; vanilla added it in 1.10!

MCEntities['creaking_transient']['26.3']
# NotInVersion: Vanilla 26.3 has no 'creaking_transient'; vanilla removed it in 1.21.4!
```

A 1.9.4 skeleton of type 2 is no stray: 1.9.4's code tells only type 1 apart. In the same way a spruce boat begins in 1.9, the first version whose boat reads a wood type.

One gap is Mojang's own. Before 1.16 a thrown potion kept its item under `Potion`, and nothing in the game's upgrade code turns that into the `Item` that later versions read. So nothing links a lingering potion entity of 1.9 to 1.15.2 to `lingering_potion`, and the data begins it at 1.16.

## Blocks

`MCBlocks` is the catalogue of blocks: what `/setblock` takes. It works like the others:

```python
from mcdex import MCBlocks

pinkWool = MCBlocks['pink_wool']
pinkWool['1.12.2'].minecraftId     # 'minecraft:wool:6'
pinkWool['1.13'].minecraftId       # 'minecraft:pink_wool'
len(MCBlocks)                      # 1287
```

Before 1.13 a block was a name and a meta, a number from 0 to 15. The meta is part of the id only where it tells blocks apart: any oak stairs is `minecraft:oak_stairs`, but the pink wool is wool with meta 6. An id takes the smallest meta of its block:

```python
MCBlocks['oak_stairs']['1.12.2'].minecraftId   # 'minecraft:oak_stairs'
MCBlocks['oak_wood']['1.12.2'].minecraftId     # 'minecraft:log:12'
MCBlocks['wall_torch']['1.12.2'].minecraftId   # 'minecraft:torch:1'
MCBlocks['granite']['1.8'].minecraftId         # 'minecraft:stone:1'
MCBlocks['granite']['1.7.10']
# NotInVersion: Vanilla 1.7.10 has no 'granite'; vanilla added it in 1.8!
```

Some old blocks were told apart by their block entity, the data a block keeps besides its meta. Their ids carry that data:
- a skull's type,
- a bed's colour, from 1.12,
- a banner's base colour,
- a flower pot's plant.

The data is written as that version's own code reads it:

```python
MCBlocks['creeper_head']['1.12.2'].minecraftId   # 'minecraft:skull:1{SkullType:4b}'
MCBlocks['white_bed']['1.12'].minecraftId        # 'minecraft:bed{color:0}'
MCBlocks['red_bed']['1.11.2'].minecraftId        # 'minecraft:bed'
MCBlocks['potted_poppy']['1.7.10'].minecraftId   # 'minecraft:flower_pot{Item:38,Data:0}'
MCBlocks['potted_poppy']['1.8'].minecraftId      # 'minecraft:flower_pot{Item:"minecraft:red_flower",Data:0}'
```

A bed before 1.12 was always red, and 1.7's flower pot held its plant's number. Until 1.17 the water cauldron was a cauldron with water in it, and the old pumpkin is both the pumpkin and the carved pumpkin, as for the items:

```python
MCBlocks['water_cauldron']['1.16.5'].minecraftId   # 'minecraft:cauldron[level=1]'
MCBlocks['carved_pumpkin']['1.12.2'].minecraftId   # 'minecraft:pumpkin'
MCBlocks['grass_block']['1.12.2'].minecraftId      # 'minecraft:grass'
MCBlocks['grass']['1.12.2'].minecraftId            # 'minecraft:tallgrass:1'
```

Where two old blocks became one, the block takes the old id nearest its default state:
- the furnace is `minecraft:furnace`, not `minecraft:lit_furnace`;
- the water is `minecraft:water`, not `minecraft:flowing_water`.

## Mob effects

`MCEffects` is the catalogue of mob effects: what `/effect` takes. 1.7's command took only an effect's number; from 1.8 it looks the effect up by name:

```python
from mcdex import MCEffects

speed = MCEffects['speed']
speed['1.7.10'].minecraftId                      # '1'
speed['1.8'].minecraftId                         # 'minecraft:speed'
MCEffects['instant_health']['1.7.10'].minecraftId   # '6'
len(MCEffects)                                   # 40
MCEffects['glowing']['1.8.9']
# NotInVersion: Vanilla 1.8.9 has no 'glowing'; vanilla added it in 1.9!
```

Which effect an old number is comes from the game's own table of numbers for upgrading old worlds. Every name 1.8 to 1.13.2 gives agrees with it.

## Enchantments

`MCEnchantments` is the catalogue of enchantments: what `/enchant` takes. 1.7's command took only an enchantment's number; from 1.8 it looks the enchantment up by name:

```python
from mcdex import MCEnchantments

protection = MCEnchantments['protection']
protection['1.7.10'].minecraftId                    # '0'
protection['1.8'].minecraftId                       # 'minecraft:protection'
MCEnchantments['sweeping_edge']['1.12.2'].minecraftId   # 'minecraft:sweeping'
MCEnchantments['sweeping_edge']['1.20.5'].minecraftId   # 'minecraft:sweeping_edge'
len(MCEnchantments)                                 # 43
MCEnchantments['mending']['1.8.9']
# NotInVersion: Vanilla 1.8.9 has no 'mending'; vanilla added it in 1.9!
```

Since 1.21 the game defines its enchantments as data, in its own data pack. Its code still declares a key for each, and the two agree in every version.

## Potions

`MCPotions` is the catalogue of potions: the potion a potion item, a tipped arrow or a lingering cloud is made with. From 1.9 a potion is a name, which the item's data carries (`Potion:"minecraft:swiftness"`). Before 1.9 there were no potions apart from the item, and a potion was the potion item's damage value:

```python
from mcdex import MCPotions

regeneration = MCPotions.REGENERATION
regeneration['1.8.9'].minecraftId                       # '1'
regeneration['1.9'].minecraftId                         # 'minecraft:regeneration'
MCPotions['leaping']['1.7.10']
# NotInVersion: Vanilla 1.7.10 has no 'leaping'; vanilla added it in 1.8!
```

The catalogue holds the base potions only. A long or a strong potion is a base potion with a `PotionModifier`, as the game makes it: the long night vision is the night vision potion for 9600 ticks instead of 3600. Indexing the catalogue with both gives it, the same object every time:

```python
from mcdex import MCPotions, PotionModifier

longNightVision = MCPotions[MCPotions.NIGHT_VISION, PotionModifier.LONG]
longNightVision['1.12.2'].minecraftId                   # 'minecraft:long_night_vision'
longNightVision['1.8.9'].minecraftId                    # '70'
MCPotions['regeneration', 'strong']['1.8.9'].minecraftId   # '33'
longNightVision is MCPotions['night_vision', 'long']    # True
len(MCPotions), len(PotionModifier)                     # (25, 2)
```

Which base potion and modifier a potion is comes from the game's own code: each long or strong potion is registered with its base potion's name, and its effects last longer or are stronger than the base potion's. Before 1.9 the same shows in the damage value: 64 for long and 32 for strong, on top of the base potion's number. Night vision is 6, so the long night vision is 70.

Which potion an old damage value is comes from the game's own table for upgrading old worlds. The table reads only the low seven bits: the smallest value is the id, and the bits for splash (16384) and drinkable (8192) are left out. An old version has a potion only if its own brewing rules can make every effect of the potion. 1.7 could not brew jump boost, so it has no leaping. How it goes inside an item in each version, and the command that gives one: [Ids that go inside an item](#ids-that-go-inside-an-item).

## Biomes

`MCBiomes` is the catalogue of biomes. Up to 1.8.9 the game knew a biome only by its number; from 1.9 by its name:

```python
from mcdex import MCBiomes

windsweptHills = MCBiomes['windswept_hills']
windsweptHills['1.8.9'].minecraftId      # '3'
windsweptHills['1.12.2'].minecraftId     # 'minecraft:extreme_hills'
windsweptHills['1.17.1'].minecraftId     # 'minecraft:mountains'
windsweptHills['1.18'].minecraftId       # 'minecraft:windswept_hills'
MCBiomes['sunflower_plains']['1.7.10'].minecraftId   # '129'
len(MCBiomes)                            # 93
```

1.18 folded several biomes into one. Both the mountains and the mountain edge became windswept hills. One of them is the biome renamed:
- the one already named as the result, if there is one;
- otherwise the one with the smallest old number, the original biome, numbered before its variants.

The others were removed and keep their last names:

```python
MCBiomes['mountain_edge']['1.17.1'].minecraftId   # 'minecraft:mountain_edge'
MCBiomes['mountain_edge']['1.18']
# NotInVersion: Vanilla 1.18 has no 'mountain_edge'; vanilla removed it in 1.18!
```

## Block entities

`MCBlockEntities` is the catalogue of block entities. A block entity is the data some blocks keep besides their state, as a chest keeps its items. Its id is the name the game saves it under, the `id` in its data. Up to 1.10.2 the names were the game's old ones; from 1.11 they are `minecraft:` names:

```python
from mcdex import MCBlockEntities

MCBlockEntities['dispenser']['1.10.2'].minecraftId      # 'Trap'
MCBlockEntities['dispenser']['1.11'].minecraftId        # 'minecraft:dispenser'
MCBlockEntities['brewing_stand']['1.10.2'].minecraftId  # 'Cauldron'
MCBlockEntities['trapped_chest']['1.12.2'].minecraftId  # 'minecraft:chest'
MCBlockEntities['trapped_chest']['1.13'].minecraftId    # 'minecraft:trapped_chest'
len(MCBlockEntities)                                    # 52
```

Until 1.13 a trapped chest kept its items in a chest's block entity, so that old id belongs to both. The note block and the flower pot lost their block entities in 1.13, and the bed lost its own in 26.2.

## Particles

`MCParticles` is the catalogue of particles: what `/particle` takes, from 1.8, when the command came. Up to 1.12.2 a particle had an old name; from 1.13 a registry name:

```python
from mcdex import MCParticles

MCParticles['flame']['1.12.2'].minecraftId              # 'flame'
MCParticles['flame']['1.13'].minecraftId                # 'minecraft:flame'
MCParticles['poof']['1.12.2'].minecraftId               # 'explode'
MCParticles['poof']['1.13'].minecraftId                 # 'minecraft:poof'
MCParticles['entity_effect']['1.12.2'].minecraftId      # 'mobSpell'
MCParticles['witch']['1.12.2'].minecraftId              # 'witchMagic'
MCParticles['dust']['1.12.2'].minecraftId               # 'reddust'
MCParticles['item']['1.8'].minecraftId                  # 'iconcrack_'
MCParticles['item']['1.9'].minecraftId                  # 'iconcrack'
MCParticles['item']['1.13'].minecraftId                 # 'minecraft:item'
len(MCParticles)                                        # 141
```

No world saves a particle, so the game has no table for upgrading them. Which particle is which comes from the game's own code instead:
- **1.8 to 1.12.2:** each particle is a constant of one enum, whose name stays while the command's name changes. `iconcrack_` and `iconcrack` are both `ITEM_CRACK`.
- **Across 1.13, by name:** an old particle is a new one where Mojang's names are the same. `flame` is `minecraft:flame`, and `DAMAGE_INDICATOR` is `minecraft:damage_indicator`.
- **Across 1.13, by code:** an old particle is also a new one where the same code draws or spawns them. That code is in the server jars and in the client jars, which hold what runs only on a player's computer, where most particles are drawn. Three kinds of code count:
  - **Classes.** The classes of 1.12.2 and 1.13 are paired by the constants they hold, their text and their numbers. The class that spawns `explode` in 1.12.2 spawns `minecraft:poof` in 1.13.
  - **Blocks.** A block's classes are paired by mcdex's own block data. The mycelium block spawns `townaura` in 1.12.2 and `minecraft:mycelium` in 1.13.
  - **Drawing.** The client's particle manager says which code draws each particle. `wake` and `minecraft:fishing` are drawn by the same code.
- **The rest:** that links 44 of 1.12.2's 49 particles. The other 5 have no 1.13 particle in the code, so they are removed in 1.13: `depthsuspend`, `footstep`, `snowshovel`, `blockdust` and `take`. 1.13 draws its `minecraft:block` with `blockcrack`'s code, and its `minecraft:item_snowball` with `snowballpoof`'s.

## Sounds

`MCSounds` is the catalogue of sound events: what `/playsound` takes. The game first listed its sounds in 1.9; before, a sound was any name its code handed the client, and the game kept no list, so the data begins at 1.9. A sound's unique name is its name without the namespace, dots and all:

```python
from mcdex import MCSounds

primed = MCSounds['entity.creeper.primed']
primed['1.9'].minecraftId          # 'minecraft:entity.creeper.primed'
MCSounds['item.goat_horn.sound.7']['1.19'].minecraftId   # 'minecraft:item.goat_horn.sound.7'
len(MCSounds)                      # 2151
primed['1.8.9']
# NotInVersion: Vanilla 1.8.9 has no 'entity.creeper.primed'; vanilla added it in 1.9!
```

No world saves a sound, so the game has no table for upgrading them. A sound is the same sound while its name is the same; a renamed sound is one removed and one added.

## Attributes

`MCAttributes` is the catalogue of attributes: max health, movement speed and the others. Up to 1.15.2 an attribute was a name in an entity's data; from 1.16 it is a registry name, which `/attribute` takes. 1.21.2 dropped the `generic.` in front:

```python
from mcdex import MCAttributes

maxHealth = MCAttributes['max_health']
maxHealth['1.15.2'].minecraftId     # 'generic.maxHealth'
maxHealth['1.16'].minecraftId       # 'minecraft:generic.max_health'
maxHealth['1.21.2'].minecraftId     # 'minecraft:max_health'
MCAttributes['jump_strength']['1.7.10'].minecraftId   # 'horse.jumpStrength'
MCAttributes['jump_strength']['1.20.5'].minecraftId   # 'minecraft:generic.jump_strength'
len(MCAttributes)                   # 40
```

Which attribute an old name is comes from the game's own renames for upgrading old worlds, its code run for the prefix it dropped.

## Statistics

`MCStatistics` is the catalogue of custom statistics: the counts the game keeps that are no item's, block's or entity's, as the times a player left the game, which `/scoreboard` objectives count. To 1.12.2 a statistic had a `stat.` name; from 1.13 a registry name:

```python
from mcdex import MCStatistics

MCStatistics['leave_game']['1.12.2'].minecraftId    # 'stat.leaveGame'
MCStatistics['leave_game']['1.13'].minecraftId      # 'minecraft:leave_game'
MCStatistics['play_time']['1.16.5'].minecraftId     # 'minecraft:play_one_minute'
MCStatistics['play_time']['1.17'].minecraftId       # 'minecraft:play_time'
len(MCStatistics)                                   # 80
```

Which statistic an old name is comes from the game's own 1.13 table of statistics and its renames since. Two statistics 1.11.1 removed have no later name. Their unique names, mcdex's own, are their old names in lower case, as `junk_fished`; their ids stay the game's.

## Game rules

`MCGameRules` is the catalogue of game rules: what `/gamerule` takes. Until 1.21.11 a rule had a camelCase name; since, a registry name, and many were renamed then:

```python
from mcdex import MCGameRules

MCGameRules['keep_inventory']['1.21.10'].minecraftId   # 'keepInventory'
MCGameRules['keep_inventory']['1.21.11'].minecraftId   # 'minecraft:keep_inventory'
MCGameRules['advance_time']['1.21.10'].minecraftId     # 'doDaylightCycle'
MCGameRules['block_drops']['1.12.2'].minecraftId       # 'doTileDrops'
len(MCGameRules)                                       # 62
```

Which rule an old name is comes from the game's own code for upgrading a world's rules, run on each old rule. Where that code made two old rules one, the one registered first is the rule. `doFireTick` became the fire spread radius; the `allowFireTicksAwayFromPlayer` it was merged with was removed. Removed rules have unique names in lower case words, as `spawn_chunk_radius`.

## Villager professions and types

`MCVillagerProfessions` and `MCVillagerTypes` are the catalogues of a villager's profession and its type, the look of its home biome. An id is what `/summon` takes for a villager of that profession or type, the villager with its data, as an entity's id is. Both are registries from 1.14, saved in a villager's `VillagerData`. Before 1.14 a profession was its `Profession` number and, from 1.8, its `Career` within it. Every villager before 1.14 is of the plains type, so the villager itself is that type's id:

```python
from mcdex import MCVillagerProfessions, MCVillagerTypes

MCVillagerProfessions['farmer']['1.7.10'].minecraftId      # 'Villager{Profession:0}'
MCVillagerProfessions['fisherman']['1.13.2'].minecraftId   # 'minecraft:villager{Profession:0,Career:2}'
MCVillagerProfessions['fisherman']['1.14'].minecraftId
# 'minecraft:villager{VillagerData:{profession:"minecraft:fisherman"}}'
MCVillagerTypes['plains']['1.13.2'].minecraftId            # 'minecraft:villager'
MCVillagerTypes['desert']['1.14'].minecraftId
# 'minecraft:villager{VillagerData:{type:"minecraft:desert"}}'
len(MCVillagerProfessions), len(MCVillagerTypes)           # (15, 7)
```

Which profession an old pair is comes from the game's own code for upgrading old villagers, run on each pair. The pairs an old version has are the ones its own trade table lists. That code also gives every old villager its type: plains.

## Dimensions

`MCDimensions` is the catalogue of dimensions: what `/execute in` takes, from 1.13, when the command came. Before it, a dimension is the number the game saves it by, as in a player's `Dimension:-1`:

```python
from mcdex import MCDimensions

theNether = MCDimensions['the_nether']

theNether['1.12.2'].minecraftId                   # '-1'
theNether['1.13'].minecraftId                     # 'minecraft:the_nether'
MCDimensions['the_end']['1.7.10'].minecraftId     # '1'
len(MCDimensions)                                 # 3
```

Each version's dimensions come from its own code. 1.7 and 1.8 make a dimension's world from its number, and that code is run on every number. 1.9 to 1.13 list them in one enum, and later versions register them by name. Which old number is which dimension comes from the game's own code for upgrading old dimension numbers.

## Damage types

`MCDamageTypes` is the catalogue of damage types: what `/damage` takes. Damage types came in 1.19.4 with the command, defined in the game's data pack:

```python
from mcdex import MCDamageTypes

inFire = MCDamageTypes['in_fire']

inFire['1.19.4'].minecraftId                         # 'minecraft:in_fire'
MCDamageTypes['mace_smash']['1.21.2'].minecraftId    # 'minecraft:mace_smash'
len(MCDamageTypes)                                   # 51
```

Each version's damage types are the keys its code declares for them, each checked against the version's data pack. None has been renamed or removed yet.

## Armor trims

`MCTrimPatterns` and `MCTrimMaterials` are the catalogues of an armor trim's pattern and its material, as an armor piece's `trim` takes them. Trims came in 1.19.4 in the experimental 1.20 pack, and are in the game itself from 1.20:

```python
from mcdex import MCTrimMaterials, MCTrimPatterns

MCTrimPatterns['coast']['1.19.4'].minecraftId      # 'minecraft:coast'
MCTrimPatterns['bolt']['1.20.5'].minecraftId       # 'minecraft:bolt'
MCTrimMaterials['resin']['1.21.4'].minecraftId     # 'minecraft:resin'
len(MCTrimPatterns), len(MCTrimMaterials)          # (18, 11)
```

Each version's patterns and materials are the keys its code declares for them, each checked against the version's data pack or its experimental packs. How it goes inside an item in each version, and the command that gives one: [Ids that go inside an item](#ids-that-go-inside-an-item).

## Music

`Music` is the catalogue of the songs music discs play: what an item's `jukebox_playable` component takes. Songs came in 1.21, defined in the game's data pack; before, a song was only its music disc, an item. The songs named by a number have the number spelled out: `Music.Thirteen` is the song `13`.

```python
from mcdex import Music

pigstep = Music.Pigstep

pigstep['1.21'].minecraftId                        # 'minecraft:pigstep'
Music['13'] is Music.Thirteen                      # True
Music.Tears['1.21.6'].minecraftId                  # 'minecraft:tears'
len(Music)                                         # 22
```

Each version's songs are the keys its code declares for them, each checked against the version's data pack. How it goes inside an item in each version, and the command that gives one: [Ids that go inside an item](#ids-that-go-inside-an-item).

## Mob variants

The mobs that come in variants each have a catalogue of them: their looks, and from 1.21.5 their sounds. A variant's id is what `/summon` takes for a mob of that variant, the mob with its data, as an entity's id is: the variant goes under the key the mob's own code saves it under, `variant` or `sound_variant`. Each kind is defined in the game's data pack, except the cat's and the frog's before 1.21.5, which the code registered. Before a mob had variants of a kind, every one of it was the one variant its code makes it with, its default: every wolf was pale. That variant's id there is the mob itself:

```python
from mcdex import MCCatVariants, MCFrogVariants, MCWolfSoundVariants
from mcdex import MCWolfVariants

black = MCCatVariants['black']

black['1.12.2'].minecraftId                            # 'minecraft:ocelot{CatType:1}'
black['1.18.2'].minecraftId                            # 'minecraft:cat{CatType:1}'
black['1.19'].minecraftId                              # 'minecraft:cat{variant:"minecraft:black"}'
MCCatVariants['tabby']['1.14'].minecraftId             # 'minecraft:cat{CatType:0}'
MCFrogVariants['warm']['1.19'].minecraftId             # 'minecraft:frog{variant:"minecraft:warm"}'
MCWolfVariants['pale']['1.12.2'].minecraftId           # 'minecraft:wolf'
MCWolfVariants['ashen']['1.20.5'].minecraftId          # 'minecraft:wolf{variant:"minecraft:ashen"}'
MCWolfSoundVariants['classic']['1.20.4'].minecraftId   # 'minecraft:wolf'
MCWolfSoundVariants['puglin']['1.21.5'].minecraftId    # 'minecraft:wolf{sound_variant:"minecraft:puglin"}'
```

Before 1.19 a cat's variant was its number, its `CatType`. Before 1.14, when the cat was not yet an entity of its own, it was a tamed ocelot's number, so only the black, red and siamese cats go back that far. Which number is which variant comes from the game's own code for upgrading old cats: its split of the ocelot, its names for the numbers, and its rename of `british` to `british_shorthair`.

So a variant's id splits into a `/summon` command as an entity's does, as the recipe below shows: `minecraft:cat{variant:"minecraft:black"}` is `/summon minecraft:cat ~ ~ ~ {variant:"minecraft:black"}`.

| Catalogue | Names from | Default, the mob before | In 26.3 |
|---|---|---|---|
| `MCCatVariants` | 1.19 | none: numbers from 1.7.2 | 11 |
| `MCFrogVariants` | 1.19 | none | 3 |
| `MCWolfVariants` | 1.20.5 | `pale` | 9 |
| `MCPigVariants`, `MCCowVariants`, `MCChickenVariants` | 1.21.5 | `temperate` | 3 each |
| `MCWolfSoundVariants` | 1.21.5 | `classic` | 7 |
| `MCZombieNautilusVariants` | 1.21.11 | none | 2 |
| `MCCatSoundVariants`, `MCPigSoundVariants`, `MCCowSoundVariants`, `MCChickenSoundVariants` | 26.1 | `classic` | 2, 3, 2 and 2 |

## Paintings

`MCPaintingVariants` is the catalogue of paintings, the pictures a painting shows. An id is what `/summon` takes for a painting of that picture, the painting with its data, as the mobs' variants are: its `Motive`, and from 1.19 its `variant`, the key checked against each version's own painting code. Up to 1.12.2 a picture was its title; from 1.13 a registry name, and from 1.21 an entry of the game's data pack:

```python
from mcdex import MCPaintingVariants

donkeyKong = MCPaintingVariants['donkey_kong']

donkeyKong['1.7.10'].minecraftId                     # 'Painting{Motive:"DonkeyKong"}'
donkeyKong['1.12.2'].minecraftId                     # 'minecraft:painting{Motive:"DonkeyKong"}'
donkeyKong['1.13'].minecraftId                       # 'minecraft:painting{Motive:"minecraft:donkey_kong"}'
MCPaintingVariants['earth']['1.19'].minecraftId      # 'minecraft:painting{variant:"minecraft:earth"}'
len(MCPaintingVariants)                              # 51
```

Which old title is which painting comes from the game's own code for upgrading old paintings, run on each title. No painting has been removed.

## Banner patterns

`MCBannerPatterns` is the catalogue of banner patterns: what a banner's patterns take for each, from 1.8, when banners came. Up to 1.20.4 a pattern was its code, as in `Patterns:[{Pattern:"bl",Color:1}]`; from 1.20.5 it is a name, an entry of the game's data pack:

```python
from mcdex import MCBannerPatterns

squareBottomLeft = MCBannerPatterns['square_bottom_left']

squareBottomLeft['1.8'].minecraftId              # 'bl'
squareBottomLeft['1.20.5'].minecraftId           # 'minecraft:square_bottom_left'
MCBannerPatterns['globe']['1.14'].minecraftId    # 'glb'
len(MCBannerPatterns)                            # 43
```

Which code is which pattern comes from the game's own table for upgrading old banners. From 1.19 to 1.20.4 the game registered each pattern with its code, and each of those agrees with the table. How it goes inside an item in each version, and the command that gives one: [Ids that go inside an item](#ids-that-go-inside-an-item).

## Advancements

`MCAdvancements` is the catalogue of advancements: what `/advancement` takes, from 1.12, when advancements came. The advancements that unlock recipes, `recipes/...`, are in too. An advancement's unique name is its name without the namespace, slashes and all:

```python
from mcdex import MCAdvancements

mineStone = MCAdvancements['story/mine_stone']
useLodestone = MCAdvancements['adventure/use_lodestone']

mineStone['1.12'].minecraftId          # 'minecraft:story/mine_stone'
useLodestone['1.16'].minecraftId       # 'minecraft:nether/use_lodestone'
useLodestone['1.21.5'].minecraftId     # 'minecraft:adventure/use_lodestone'
len(MCAdvancements)                    # 1984
```

Each version's advancements are the files of its own data pack, which the game loads them from. Which old advancement is which comes from the game's own advancement renames. Where the game moved or renamed one without such a rename, as many recipe advancements, the old one is removed and the new one added.

## Structures

`MCStructures` is the catalogue of structures: what `/locate` takes, from 1.11, when the command came, and before it the name the game saves a structure by. Before 1.19 one structure of the game could be several of today's: the village was the village of every kind of biome. There the id is the old structure, with what makes it the one kind, in the game's own data:

```python
from mcdex import MCStructures

villagePlains = MCStructures['village_plains']

villagePlains['1.7.10'].minecraftId      # 'Village{Children:[{Desert:0b}]}'
villagePlains['1.12.2'].minecraftId      # 'Village{Children:[{Type:0b}]}'
villagePlains['1.14'].minecraftId        # 'Village{start_pool:"village/plains/town_centers"}'
villagePlains['1.19'].minecraftId        # 'minecraft:village_plains'
MCStructures['desert_pyramid']['1.12.2'].minecraftId
# 'Temple{Children:[{id:"TeDP"}]}'
MCStructures['mineshaft_mesa']['1.18.2'].minecraftId
# 'minecraft:mineshaft{Children:[{MST:1}]}'
len(MCStructures)                        # 52
```

What makes the kind is the data the structure's pieces are saved with where they carry it: a temple's first piece, a village piece's `Desert` or `Type`, a mineshaft's `MST`, a shipwreck's `isBeached`, an ocean ruin's `BiomeType`. Otherwise it is what the structure is configured with: a village's start pool from 1.14, a ruined portal's type. A kind a version's code does not make is not in that version, as the snowy village before 1.14.

Which old structure is which comes from the game's own code: its upgrade of old temples by their first piece, its lower-casing of the old names in 1.16, its renames for 1.19, and the names 1.16.2 to 1.18.2 already give each configured kind, as `village_plains` for the village with the plains start pool. An old village's `Type` is the type 1.13 builds the villages of a biome with, and the game's upgrade code names the village of that biome.

## Versions

`Version` enumerates every release from 1.0 to 26.3, 103 of them, in the order Mojang released them. Each member holds its `MCVersion`. A member resolves from its name, from its `MCVersion`, or from the text the game reports, and members compare as versions:

```python
from mcdex import MCVersion, Version

Version('1.7.10')              # <Version>.V1_7_10
Version('v1_7_10')             # <Version>.V1_7_10
Version(MCVersion(26, 3))      # <Version>.V26_3
Version.V1_7_10.value          # MCVersion(1, 7, 10)
str(Version.V26_3.value)       # '26.3'
Version.V1_9 < Version.V1_10   # True, as numbers, not text
len(Version)                   # 103
```

Only real releases are members: there was never a 1.2 (the first was 1.2.1) nor a 1.5 (1.5.1), and `Version('1.2')` raises `KeeResolveError`. Since 26.1, Mojang numbers its releases by year.

`MCVersion` is the version itself, for the ones `Version` leaves out, such as a snapshot's release number:

```python
MCVersion('1.21.11')                     # MCVersion(1, 21, 11)
MCVersion(26, 4) > Version.V26_3.value   # True
str(MCVersion(1, 8, 0))                  # '1.8'
```

## Equipment slots

`EquipmentSlot` enumerates the slots an entity equips an item to, in the order of the game's own enumeration, each holding the name the game serializes it by:

```python
from mcdex import EquipmentSlot

list(EquipmentSlot)
# [<EquipmentSlot>.MAINHAND, <EquipmentSlot>.OFFHAND, <EquipmentSlot>.FEET,
#  <EquipmentSlot>.LEGS, <EquipmentSlot>.CHEST, <EquipmentSlot>.HEAD,
#  <EquipmentSlot>.BODY, <EquipmentSlot>.SADDLE]

EquipmentSlot('chest')         # <EquipmentSlot>.CHEST
EquipmentSlot.CHEST.value      # 'chest'
```

The offhand arrived in 1.9, the body in 1.20.5 and the saddle in 1.21.5. Before each, an item that would go there went to the main hand.

## Item ids

`ItemId` is what indexing an item by a version gives: the item's `uniqueName` and its `minecraftId` in that version. Its text is the `minecraftId`, and it compares and hashes by both strings:

```python
from mcdex import ItemId

id_ = ItemId('pink_wool', 'minecraft:wool:6')
id_.uniqueName                 # 'pink_wool'
id_.minecraftId                # 'minecraft:wool:6'
str(id_)                       # 'minecraft:wool:6'
id_ == ItemId('pink_wool', 'minecraft:wool:6')   # True
```

## Entity ids

`EntityId` is what indexing an entity by a version gives: the entity's `uniqueName` and its `minecraftId` in that version. It works like `ItemId`, but an entity's id is never an item's, even with the same text:

```python
from mcdex import EntityId, ItemId

id_ = EntityId('wither_skeleton', 'Skeleton{SkeletonType:1}')
id_.uniqueName                 # 'wither_skeleton'
id_.minecraftId                # 'Skeleton{SkeletonType:1}'
str(id_)                       # 'Skeleton{SkeletonType:1}'
EntityId('pig', 'minecraft:pig') == ItemId('pig', 'minecraft:pig')   # False
```

## Block ids

`BlockId` is what indexing a block by a version gives, as `ItemId` and `EntityId` are for items and entities. An id of one kind is never equal to an id of another, even with the same text:

```python
from mcdex import BlockId, EntityId

BlockId('tnt', 'minecraft:tnt') == EntityId('tnt', 'minecraft:tnt')   # False
```

## Recipes

### A /summon command for any version

`/summon` takes the entity, then the place, then the data:

```python
from mcdex import MCEntities


def summonCommand(name: str, version: str, where: str = '~ ~ ~') -> str:
    minecraftId = MCEntities[name][version].minecraftId
    base, brace, nbt = minecraftId.partition('{')
    return ' '.join(['/summon', base, where] + ([brace + nbt] if nbt else []))


summonCommand('wither_skeleton', '1.10.2')
# '/summon Skeleton ~ ~ ~ {SkeletonType:1}'
summonCommand('wither_skeleton', '26.3')
# '/summon minecraft:wither_skeleton ~ ~ ~'
summonCommand('spruce_boat', '1.12.2')
# '/summon minecraft:boat ~ ~ ~ {Type:"spruce"}'
```

### A /give command for any version

The command changed shape at 1.13: before it, the meta and the NBT came after the count; since, the NBT follows the name.

```python
from mcdex import MCItems, Version


def giveCommand(name: str, version: str, count: int = 1) -> str:
    version_ = Version(version)
    minecraftId = MCItems[name][version_].minecraftId
    base, brace, nbt = minecraftId.partition('{')
    nbt = brace + nbt
    if version_ < Version.V1_13:
        namespace, path, *meta = base.split(':')
        words = ['/give', '@p', '%s:%s' % (namespace, path), str(count),
                 meta[0] if meta else '0']
        return ' '.join(words + ([nbt] if nbt else []))
    return '/give @p %s%s %d' % (base, nbt, count)


giveCommand('pink_wool', '1.7.10')
# '/give @p minecraft:wool 1 6'
giveCommand('pink_wool', '26.3')
# '/give @p minecraft:pink_wool 1'
giveCommand('creeper_spawn_egg', '1.8.9')
# '/give @p minecraft:spawn_egg 1 50'
giveCommand('creeper_spawn_egg', '1.12.2')
# '/give @p minecraft:spawn_egg 1 0 {EntityTag:{id:"minecraft:creeper"}}'
giveCommand('splash_potion', '1.8.9')
# '/give @p minecraft:potion 1 16384'
```

### Ids that go inside an item

A potion, a banner pattern, an armor trim and a jukebox song are each right on their own, but a command takes them only inside an item's data: `MCPotions['swiftness']['1.20.4'].minecraftId` is what a potion item's `Potion` holds. Where that data is, and its shape, changed over the versions. Each version's own code was read for it; the colours of a banner's layers come from the game's own upgrade code for banners.

| What | Inside the item | Versions |
|---|---|---|
| Potion | the damage value: the potion's number, plus 16384 for a splash potion | 1.7.2 to 1.8.9 |
| | `{Potion:"minecraft:swiftness"}` | 1.9 to 1.20.4 |
| | `[potion_contents={potion:"minecraft:swiftness"}]` | from 1.20.5 |
| Banner pattern | `{BlockEntityTag:{Patterns:[{Pattern:"bl",Color:1}]}}`, the colour's number counted from black | 1.8 to 1.12.2 |
| | `{BlockEntityTag:{Patterns:[{Pattern:"bl",Color:14}]}}`, counted from white | 1.13 to 1.20.4 |
| | `[banner_patterns=[{pattern:"minecraft:square_bottom_left",color:"red"}]]` | from 1.20.5 |
| Armor trim | `{Trim:{pattern:"minecraft:coast",material:"minecraft:amethyst"}}` | 1.19.4 to 1.20.4 |
| | `[trim={pattern:"minecraft:coast",material:"minecraft:amethyst"}]` | from 1.20.5 |
| Jukebox song | `[jukebox_playable={song:"minecraft:pigstep"}]` | 1.21 to 1.21.4 |
| | `[jukebox_playable="minecraft:pigstep"]` | from 1.21.5 |

The commands, built from mcdex's ids:

```python
from mcdex import MCBannerPatterns, MCItems, MCPotions, Music
from mcdex import MCTrimMaterials, MCTrimPatterns, Version

#  The colours as 1.13 to 1.20.4 number them, and 1.20.5 names them.
DYES = ['white', 'orange', 'magenta', 'light_blue', 'yellow', 'lime', 'pink',
        'gray', 'light_gray', 'cyan', 'purple', 'blue', 'brown', 'green',
        'red', 'black']


def give(item: str, version: str, inside: str = '', meta: int = -1) -> str:
    """'/give' for an item of a version, with what goes inside it."""
    version_ = Version(version)
    namespace, path, *old = MCItems[item][version_].minecraftId.split(':')
    if version_ < Version.V1_13:
        if meta < 0:
            meta = int(old[0]) if old else 0
        words = ['/give @p %s:%s 1 %d' % (namespace, path, meta)]
        return ' '.join(words + ([inside] if inside else []))
    return '/give @p %s:%s%s 1' % (namespace, path, inside)


def potionCommand(item: str, potion: str | tuple, version: str) -> str:
    """A potion item of a potion, or of a base potion and a modifier."""
    version_ = Version(version)
    potionId = MCPotions[potion][version_].minecraftId
    if version_ < Version.V1_9:
        old = MCItems[item][version_].minecraftId.split(':')[2:] or ['0']
        return give(item, version, meta=int(old[0]) | int(potionId))
    if version_ < Version.V1_20_5:
        return give(item, version, '{Potion:"%s"}' % potionId)
    return give(item, version, '[potion_contents={potion:"%s"}]' % potionId)


def bannerCommand(banner: str, pattern: str, color: str, version: str) -> str:
    version_ = Version(version)
    patternId = MCBannerPatterns[pattern][version_].minecraftId
    if version_ < Version.V1_20_5:
        number = DYES.index(color)
        if version_ < Version.V1_13:
            number = 15 - number
        return give(banner, version, '{BlockEntityTag:{Patterns:[{Pattern:"%s",'
                                     'Color:%d}]}}' % (patternId, number))
    return give(banner, version, '[banner_patterns=[{pattern:"%s",color:"%s"}]]'
                % (patternId, color))


def trimCommand(armor: str, pattern: str, material: str, version: str) -> str:
    version_ = Version(version)
    trim = 'pattern:"%s",material:"%s"' % (
        MCTrimPatterns[pattern][version_].minecraftId,
        MCTrimMaterials[material][version_].minecraftId)
    if version_ < Version.V1_20_5:
        return give(armor, version, '{Trim:{%s}}' % trim)
    return give(armor, version, '[trim={%s}]' % trim)


def songCommand(item: str, song: str, version: str) -> str:
    version_ = Version(version)
    songId = Music[song][version_].minecraftId
    if version_ < Version.V1_21_5:
        return give(item, version, '[jukebox_playable={song:"%s"}]' % songId)
    return give(item, version, '[jukebox_playable="%s"]' % songId)


potionCommand('splash_potion', 'swiftness', '1.8.9')
# '/give @p minecraft:potion 1 16386'
potionCommand('splash_potion', 'swiftness', '1.12.2')
# '/give @p minecraft:splash_potion 1 0 {Potion:"minecraft:swiftness"}'
potionCommand('splash_potion', ('night_vision', 'long'), '1.12.2')
# '/give @p minecraft:splash_potion 1 0 {Potion:"minecraft:long_night_vision"}'
potionCommand('splash_potion', ('night_vision', 'long'), '1.8.9')
# '/give @p minecraft:potion 1 16454'
potionCommand('potion', 'swiftness', '26.3')
# '/give @p minecraft:potion[potion_contents={potion:"minecraft:swiftness"}] 1'
bannerCommand('white_banner', 'square_bottom_left', 'red', '1.12.2')
# '/give @p minecraft:banner 1 15 {BlockEntityTag:{Patterns:[{Pattern:"bl",Color:1}]}}'
bannerCommand('white_banner', 'square_bottom_left', 'red', '1.20.4')
# '/give @p minecraft:white_banner{BlockEntityTag:{Patterns:[{Pattern:"bl",Color:14}]}} 1'
bannerCommand('white_banner', 'square_bottom_left', 'red', '1.20.5')
# '/give @p minecraft:white_banner[banner_patterns=[{pattern:"minecraft:square_bottom_left",color:"red"}]] 1'
trimCommand('iron_chestplate', 'coast', 'amethyst', '1.20')
# '/give @p minecraft:iron_chestplate{Trim:{pattern:"minecraft:coast",material:"minecraft:amethyst"}} 1'
songCommand('diamond', 'pigstep', '1.21.4')
# '/give @p minecraft:diamond[jukebox_playable={song:"minecraft:pigstep"}] 1'
songCommand('diamond', 'pigstep', '26.3')
# '/give @p minecraft:diamond[jukebox_playable="minecraft:pigstep"] 1'
```

A structure's id before 1.19 is the same kind of thing: `/locate` takes the part before the braces, and the braces say which of today's structures it is in that version's data. `Village{Children:[{Type:0b}]}` is found with `/locate Village`.

### A test that does not know its version

mcdex exists for tests that run unchanged against any version. This is a test's pre-check, written once for the elytra, which fails with the reason when a version cannot have the elytra glide:

```python
from mcdex import EquipmentSlot, MCItems, NotInVersion, Version


def elytraPreTest(version: str) -> str:
    elytra = MCItems['elytra']
    try:
        id_ = elytra[version]
    except NotInVersion as exception:
        return 'FAIL: %s' % exception
    slot = elytra.equipmentSlot[Version(version)]
    if slot is not EquipmentSlot.CHEST:
        return 'FAIL: the elytra goes to %s, not the chest' % slot.value
    return 'ok: equip %s to the chest' % id_.minecraftId


elytraPreTest('1.7.10')   # "FAIL: Vanilla 1.7.10 has no 'elytra'; vanilla added it in 1.9!"
elytraPreTest('1.9')      # 'ok: equip minecraft:elytra to the chest'
elytraPreTest('26.3')     # 'ok: equip minecraft:elytra to the chest'
```

### What a version renamed

```python
from mcdex import MCItems, NotInVersion, Version


def renamed(old: str, new: str) -> list[tuple[str, str, str]]:
    old, new = Version(old), Version(new)
    found = []
    for item in MCItems:
        try:
            before, after = item[old].minecraftId, item[new].minecraftId
        except NotInVersion:
            continue
        if before != after:
            found.append((item.uniqueName, before, after))
    return found


renamed('1.21.8', '1.21.9')
# [('iron_chain', 'minecraft:chain', 'minecraft:iron_chain')]
renamed('1.20.2', '1.20.3')
# [('grass', 'minecraft:grass', 'minecraft:short_grass'),
#  ('short_grass', 'minecraft:grass', 'minecraft:short_grass')]
len(renamed('1.12.2', '1.13'))
# 369, the flattening
```

### What a version added

```python
from mcdex import MCItems, NotInVersion, Version


def added(version: str) -> list[str]:
    versions = list(Version)
    new = Version(version)
    old = versions[versions.index(new) - 1]
    found = []
    for item in MCItems:
        try:
            item[new]
        except NotInVersion:
            continue
        try:
            item[old]
        except NotInVersion:
            found.append(item.uniqueName)
    return found


added('1.21.5')
# ['blue_egg', 'brown_egg', 'bush', 'cactus_flower', 'firefly_bush', 'leaf_litter',
#  'short_dry_grass', 'tall_dry_grass', 'test_block', 'test_instance_block', 'wildflowers']
```

### Which items a game id is

The reverse lookup, for reading what a version reports. It gives a list, since an old id can be two items:

```python
from mcdex import MCItems, NotInVersion, Version


def itemsOf(minecraftId: str, version: str) -> list[str]:
    version_ = Version(version)
    found = []
    for item in MCItems:
        try:
            if item[version_].minecraftId == minecraftId:
                found.append(item.uniqueName)
        except NotInVersion:
            pass
    return found


itemsOf('minecraft:wool:6', '1.12.2')              # ['pink_wool']
itemsOf('minecraft:grass', '1.12.2')               # ['grass_block']
itemsOf('minecraft:grass', '1.13')                 # ['grass', 'short_grass']
itemsOf('minecraft:purple_shulker_box', '1.12.2')  # ['purple_shulker_box', 'shulker_box']
```

### An item's history, change by change

```python
from mcdex import MCItems


def history(name: str) -> list[tuple[str, str]]:
    changes, last = [], None
    for version_, id_ in MCItems[name].versionIds.items():
        if id_ != last:
            changes.append((str(version_.value), id_))
            last = id_
    return changes


history('grass')
# [('1.7.2', 'minecraft:tallgrass:1'), ('1.13', 'minecraft:grass'),
#  ('1.20.3', 'minecraft:short_grass')]
history('red_bed')
# [('1.7.2', 'minecraft:bed'), ('1.12', 'minecraft:bed:14'), ('1.13', 'minecraft:red_bed')]
```

### Items by slot, items no longer in the game

```python
from mcdex import EquipmentSlot, MCItems, Version

[item.uniqueName for item in MCItems
 if item.equipmentSlot.get(Version.V26_3) is EquipmentSlot.HEAD]
# ['carved_pumpkin', 'chainmail_helmet', 'copper_helmet', 'creeper_head',
#  'diamond_helmet', 'dragon_head', 'golden_helmet', 'iron_helmet', 'leather_helmet',
#  'netherite_helmet', 'piglin_head', 'player_head', 'skeleton_skull', 'turtle_helmet',
#  'wither_skeleton_skull', 'zombie_head']

[item.uniqueName for item in MCItems if not item.versionIds[Version.V26_3]]
# ['carrots', 'cocoa', 'double_stone_slab', 'double_wooden_slab', 'end_portal', 'fire',
#  'flowing_lava', 'flowing_water', 'lava', 'lit_furnace', 'portal', 'potatoes', 'water']
```

The ones gone by 26.3 are the block items 1.7 had for every block, which 1.8 and 1.9 dropped.

## Where the data comes from

All of it comes from Mojang's own files: the server jar of every release, the version manifest that lists them, and, for the particles, the client jars of 1.12.2 and 1.13. No third-party dataset is used.

- **Ids.** Each version's items are read from its server jar by following the game's own code that registers them, as the game would run it, so that names the game builds while starting up are found too. Jars whose names Mojang obfuscated are read through Mojang's own mappings, or, where Mojang published none, by the structure of the code.
- **Stack sizes and slots.** They are read off the objects that same registration makes, and off the game's own code deciding an item's slot.
- **Which old id is which item.** This comes from the game's own code for upgrading old worlds, in the 26.3 jar: its renames, the 1.13 flattening, and its fixes for beds, spawn eggs and potions, each applied from the data version of the version an id comes from.
- **Blocks.**
  - Up to 1.12.2, the blocks come from each server jar's numeric block registration. From 1.13 they come from the block registry.
  - Which old block and meta is which block comes from the game's own 1.13 flattening table, then its later renames and the cauldron split.
  - A block told apart by its block entity takes its data from the tables of the game's chunk upgrade code. That code is run to build them, and each table is checked against the old version's block entity classes.
- **Mob effects.** Up to 1.13.2 they come from each jar's numbered effects, and from 1.14 from the mob effect registry. Which old number is which effect comes from the game's own table of effect numbers.
- **Enchantments.** Up to 1.12.2 they come from each jar's numbered enchantments. From 1.13 to 1.20.6 they come from the enchantment registry. From 1.21 they come from the keys the code declares, checked against the jar's data pack. Which old number is which comes from the game's own table, then its rename of sweeping to sweeping_edge.
- **Potions.** From 1.9 they come from each jar's potion registration, and from 1.14 from the potion registry. Before 1.9 they are the potion item's damage values, named by the game's own upgrade table, and kept where the version's own brewing rules make every effect.
- **Biomes.**
  - Up to 1.8.9 they come from each jar's numbered biomes and the mutations its code makes of them. To 1.16.1 they come from its numbered registration. From 1.16.2 they come from the keys the code declares, checked against the jar's data packs.
  - Which old biome is which comes from the game's own table of old biome numbers, then its biome renames. Where a rename folds biomes together, the rule above decides which one was renamed.
- **Block entities.**
  - Up to 1.12.2 they come from the names each jar maps its block entity classes to. From 1.13 they come from the block entity type registry.
  - Which old name is which comes from the game's own table of old names and its renames. The trapped chest shares the chest's old id, as its upgrade fix shows.
- **Particles.** From 1.8 to 1.12.2 they come from each jar's particle enum, and from 1.13 from the particle type registry. They are linked across 1.13 by Mojang's own names and by the code of the server and client jars, as the section above says.
- **Sounds.** From 1.9 to 1.13.2 they come from each jar's sound registration method, and from 1.14 from the sound event registry. Sounds the game registers in loops, as the goat horns, come from running those methods on their own.
- **Attributes.** To 1.15.2 they come from every attribute any class of each jar makes. From 1.16 they come from the attribute registry. Which old name is which comes from the game's own attribute renames.
- **Statistics.** To 1.12.2 they come from each jar's list of statistics, and from 1.13 from the custom stat registry. Which old name is which comes from the game's own table of statistics and its renames.
- **Game rules.** Until 1.21.11 they come from every call of the helper each jar adds its rules with, and since from the game rule registry. Which old rule is which comes from running the game's own rule upgrade code on each.
- **Villager professions and types.**
  - From 1.14 they come from the registries, read by structure, through the mappings, or from the keys the code declares.
  - Before 1.14 a profession is the pairs of profession and career in each jar's own trade table. 1.7 has no careers, only the professions its villagers are given. Which old pair is which comes from running the game's own villager upgrade code, which also gives every old villager the plains type.
- **Dimensions.** In 1.7 and 1.8 they come from running each jar's code that makes a dimension's world from its number, on every number. From 1.9 to 1.13 they come from each jar's dimension enum, to 1.15.2 from its registration, and from 1.16 from the keys of its levels. Which old number is which comes from the game's own dimension upgrade code.
- **Damage types.** From 1.19.4 they come from the keys each jar's code declares for them, found through Mojang's mappings, each checked against the jar's own data pack.
- **Armor trims.** From 1.19.4 the patterns and materials come from the keys each jar's code declares for them, each checked against the jar's own data pack or its experimental packs.
- **Music.** From 1.21 the songs come from the keys each jar's code declares for them, each checked against the jar's own data pack.
- **Mob variants.** From the version each came in, they come from the keys each jar's code declares for them, or the entries it registers, each checked against the jar's own data pack. From 1.14 to 1.18.2 the cats are the numbers of each jar's own table of cat textures, and before 1.14 the ocelot numbers the game's own upgrade code makes cats. A default variant is the one the mob's code defines its data with, as the wolf's `PALE`. Each id's key is checked against the mob's own code in each version.
- **Paintings.** Each id is the painting with its picture, under the key each jar's painting code saves it under. To 1.12.2 they come from each jar's enum of paintings, to 1.14.3 from its registration, and from 1.14.4 from running the code that registers them or declares their keys, found through Mojang's mappings and checked against the jar's own data pack from 1.21. Which old title is which painting comes from running the game's own painting upgrade code.
- **Banner patterns.** To 1.18.2 they come from each jar's enum of patterns, to 1.20.4 from the code that registers each with its code, and from 1.20.5 from the keys each jar's code declares, checked against its data pack. Which old code is which pattern comes from the game's own table for upgrading banners.
- **Advancements.** From 1.12 they come from the files of each jar's own data pack, which the game loads them from. Which old advancement is which comes from the game's own advancement renames.
- **Structures.** To 1.15.2 they come from the names each jar registers its structures' starts with, to 1.18.2 from its structure features, and from 1.19 from the keys its code declares, checked against its data pack. The kinds of an old structure come from the data its pieces are saved with, or what it is configured with. Which old structure is which comes from the game's own upgrade code, and from the names 1.16.2 to 1.18.2 give each configured kind.
- **Entities.**
  - Up to 1.12.2, the names come from each server jar's entity list: every class it registers that is not abstract, and the names its code adds itself, `LightningBolt` and `Player`. From 1.13 they come from the entity type registry, read the same way as the items.
  - Which old entity is which comes from the game's own entity upgrade code in the 26.3 jar: its renames and its splits. That code is run, instruction by instruction, on each old entity and on the data it reads.
  - A split entity's old id is then checked against the old version's own entity code. That code must read the key, and must allow the value: a number by the enum it is looked up in or the values it is compared with, a word by naming it.

Checks made while building the data:
- 26.3's items, stack sizes and slots equal the game's own generator report for 26.3, item for item.
- 1.7.10's items and numeric ids equal the table of old numeric ids in the 26.3 jar.
- 1.14.4 read without its mappings equals 1.14.4 read with them.
- Every item that disappears between two versions is a rename in the game's own upgrade code.
- 26.3's entities equal the game's own generator report for 26.3, in the same order.
- 26.3's blocks equal the generator report, in the same order. 1.14 read without its mappings equals 1.14.4 read with them.
- Every block of every version is one block's id there, or merges into one, as the lit furnace does.
- 26.3's mob effects equal the generator report, in the same order. 1.14 read without its mappings equals 1.14.4.
- 26.3's structures are the 52 its code declares, each with its data-pack file. Every kind of an old structure is named by 1.16.2's configured kinds or by the game's upgrade code.
- 26.3's advancements are its 1,866 data-pack files.
- 26.3's banner patterns are the 43 its code declares, each with its data-pack file. Every code from 1.8 to 1.20.4 is in the game's own upgrade table.
- 26.3's paintings are the 51 its code declares, each with its data-pack file. Every version from 1.7.2 to 1.18.2 has its 26 paintings.
- 26.3's mob variants and sound variants are the ones its code declares, each with its data-pack file. Every version from 1.7.2 to 1.13.2 has the black, red and siamese cats, as a tamed ocelot's number.
- 26.3's songs are the 22 its code declares, each with its data-pack file.
- 26.3's trim patterns and materials are the 18 and 11 its code declares, each with its data-pack file.
- 26.3's damage types are the 51 its code declares, each with its data-pack file.
- Every version from 1.7.2 to 26.3 has the same three dimensions. The game's own upgrade code makes the old numbers -1, 0 and 1 the nether, the overworld and the end.
- 26.3's villager professions and types equal the generator report.
- 26.3's game rules equal the generator report, in the same order.
- 26.3's statistics equal the generator report, in the same order. 1.14 read without its mappings equals 1.14.4.
- 26.3's attributes equal the generator report, in the same order.
- 26.3's sounds are the generator report's 1,991. Those not made in loops come in the report's order. 1.14 read without its mappings equals 1.14.4.
- 26.3's particles equal the generator report, in the same order. 1.14 read without its mappings equals 1.14.4.
- 26.3's block entities equal the generator report, in the same order.
- 26.3's biomes are the 67 the code declares, each with its data-pack file. Every version from 1.7.2 to 1.8.9 has its 60 numbered biomes.
- 26.3's potions equal the generator report, in the same order. 1.14 read without its mappings equals 1.14.4.
- 26.3's enchantments are the 43 the code declares, each with its data-pack file. 1.14 read without its mappings equals 1.14.4.
- Every name of every version, 1.7.2 to 26.3, is exactly one entity's id in that version.

Versions before 1.7.2, when the game had only numbers, are not covered yet.

## Development

```
pip install -e ".[test]"
pytest --cov                     # 100% branch coverage is required
```

Mutation testing with cosmic-ray rewrites the sources while it runs, so run it on a copy of the repository; `cosmic-ray.toml` lists the commands.
