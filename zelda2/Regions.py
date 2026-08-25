from typing import NamedTuple

MENU = "Menu"


class Connection(NamedTuple):
    source: str
    target: str
    requires: tuple[str, ...]


REGION_ORDER = (
    "West Hyrule",
    "Towns",
    "Palaces 1, 2 and 5",
    "Death Mountain",
    "East Hyrule",
    "Maze Island",
    "Palaces 3, 4 and 6",
    "Great Palace",
)

CONNECTIONS = (
    Connection(MENU, "West Hyrule", ()),
    Connection("West Hyrule", "Towns", ()),
    Connection("West Hyrule", "Palaces 1, 2 and 5", ()),
    Connection("West Hyrule", "Death Mountain", ("hammer",)),
    Connection("West Hyrule", "East Hyrule", ("raft",)),
    Connection("East Hyrule", "Maze Island", ("raft",)),
    Connection("East Hyrule", "Palaces 3, 4 and 6", ()),
    Connection("East Hyrule", "Great Palace", ("boots", "flute")),
)

COMPLETION_ITEMS = ("candle", "glove", "raft", "boots", "flute", "cross",
                    "hammer", "magic_key")

# Where an item may physically sit. The game only has graphics and pickup
# handling for what it ever shows in a scene type: keys, experience bags, jars
# and extra lives appear (as drops or fixed objects) everywhere; the eight key
# items are drawn from one shared tile block wherever any of them appears;
# containers and the quest items exist only in overworld and town scenes. A
# Magic Container placed in a palace rendered as garbage and could not be
# picked up.
UNIVERSAL_KINDS = frozenset((
    "key", "exp_50", "exp_100", "exp_200", "exp_500",
    "blue_jar", "red_jar", "link_doll"))
MAJOR_KINDS = frozenset((
    "candle", "glove", "raft", "boots", "flute", "cross",
    "hammer", "magic_key"))
CONTAINER_KINDS = frozenset(("heart_container", "magic_container"))
QUEST_KINDS = frozenset(("child", "trophy", "medicine"))

_NO_MAJORS = frozenset(("great_palace",))
_OVERWORLD = frozenset(("west_hyrule", "east_hyrule", "death_mountain"))
_CONTAINER_OK = _OVERWORLD | frozenset(("towns",))


def kind_allowed_at(kind: str, region_key: str) -> bool:
    if kind in UNIVERSAL_KINDS:
        return True
    if kind in MAJOR_KINDS:
        return region_key not in _NO_MAJORS
    if kind in CONTAINER_KINDS:
        return region_key in _CONTAINER_OK
    if kind in QUEST_KINDS:
        return region_key in _OVERWORLD
    return False
