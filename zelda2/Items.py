from typing import NamedTuple

BASE_ID = 0x5A320000
ITEM_ID_BLOCK = 0x1000


class ItemDef(NamedTuple):
    key: str
    name: str
    classification: str
    game_code: int | None

    @property
    def id(self) -> int:
        return BASE_ID + ITEM_ID_BLOCK + ITEM_ORDER[self.key]


# Order is fixed: an item's id is its index here, so entries may be appended
# but never reordered.
_ITEMS = (
    ("candle",          "Candle",          "progression", 0x00),
    ("glove",           "Handy Glove",     "progression", 0x01),
    ("raft",            "Raft",            "progression", 0x02),
    ("boots",           "Boots",           "progression", 0x03),
    ("flute",           "Flute",           "progression", 0x04),
    ("cross",           "Cross",           "progression", 0x05),
    ("hammer",          "Hammer",          "progression", 0x06),
    ("magic_key",       "Magical Key",     "progression", 0x07),
    ("key",             "Palace Key",      "progression", 0x08),
    ("exp_50",          "50 Experience",   "filler",      0x0A),
    ("exp_100",         "100 Experience",  "filler",      0x0B),
    ("exp_200",         "200 Experience",  "filler",      0x0C),
    ("exp_500",         "500 Experience",  "filler",      0x0D),
    ("magic_container", "Magic Container", "progression_skip_balancing", 0x0E),
    ("heart_container", "Heart Container", "progression_skip_balancing", 0x0F),
    ("blue_jar",        "Blue Jar",        "filler",      0x10),
    ("red_jar",         "Red Jar",         "filler",      0x11),
    ("link_doll",       "Extra Life",      "filler",      0x12),
    ("child",           "Kidnapped Child", "progression", 0x13),
    ("trophy",          "Trophy",          "progression", 0x14),
    ("medicine",        "Water of Life",   "progression", 0x15),
)

ITEM_ORDER = {key: i for i, (key, *_) in enumerate(_ITEMS)}
ITEMS = tuple(ItemDef(*row) for row in _ITEMS)
ITEM_BY_KEY = {i.key: i for i in ITEMS}
ITEM_BY_NAME = {i.name: i for i in ITEMS}

FILLER_KEY = "blue_jar"
