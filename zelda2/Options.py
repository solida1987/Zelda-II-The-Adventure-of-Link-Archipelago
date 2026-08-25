from dataclasses import dataclass

from Options import (Choice, DefaultOnToggle, PerGameCommonOptions, Range,
                     StartInventoryPool)


class KeyShuffle(Choice):
    """Where palace keys live.

    Vanilla keeps every key in the palace it opens. Anywhere puts them in the
    multiworld, which can place a palace behind another player's progress.
    """
    display_name = "Key Shuffle"
    option_vanilla = 0
    option_anywhere = 1
    default = 0


class ContainerShuffle(DefaultOnToggle):
    """Shuffle the four Heart and four Magic Containers into the multiworld."""
    display_name = "Shuffle Containers"


class ExperienceShuffle(DefaultOnToggle):
    """Shuffle the experience bags. These are 26 of the 68 locations."""
    display_name = "Shuffle Experience"


class QuestItemShuffle(DefaultOnToggle):
    """Shuffle Trophy, Kidnapped Child and Water of Life.

    Each is traded to a townsperson for a spell.
    """
    display_name = "Shuffle Quest Items"


class StartingLives(Range):
    display_name = "Starting Lives"
    range_start = 1
    range_end = 8
    default = 3


class StartingAttack(Range):
    display_name = "Starting Attack Level"
    range_start = 1
    range_end = 8
    default = 1


class StartingMagic(Range):
    display_name = "Starting Magic Level"
    range_start = 1
    range_end = 8
    default = 1


class StartingLife(Range):
    display_name = "Starting Life Level"
    range_start = 1
    range_end = 8
    default = 1


@dataclass
class Zelda2Options(PerGameCommonOptions):
    key_shuffle: KeyShuffle
    container_shuffle: ContainerShuffle
    experience_shuffle: ExperienceShuffle
    quest_item_shuffle: QuestItemShuffle
    starting_lives: StartingLives
    starting_attack: StartingAttack
    starting_magic: StartingMagic
    starting_life: StartingLife
    start_inventory_from_pool: StartInventoryPool
