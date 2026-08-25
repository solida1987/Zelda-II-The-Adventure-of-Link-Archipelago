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
