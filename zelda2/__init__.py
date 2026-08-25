import os
from typing import ClassVar

import settings
from BaseClasses import Item, ItemClassification, Location, Region, Tutorial
from worlds.AutoWorld import WebWorld, World

from .Items import FILLER_KEY, ITEM_BY_KEY, ITEM_BY_NAME, ITEMS
from .Locations import LOCATIONS, LOCATION_NAME_TO_ID, REGIONS
from .Options import Zelda2Options
from .Rom import Zelda2ProcedurePatch, Zelda2Settings, write_tokens
from .Regions import COMPLETION_ITEMS, CONNECTIONS, MENU

CLASSIFICATION = {
    "progression": ItemClassification.progression,
    "useful": ItemClassification.useful,
    "filler": ItemClassification.filler,
}


class Zelda2Item(Item):
    game = "Zelda II: The Adventure of Link"


class Zelda2Location(Location):
    game = "Zelda II: The Adventure of Link"


class Zelda2Web(WebWorld):
    theme = "grass"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Zelda II: The Adventure of Link in Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["solida1987"],
    )]


class Zelda2World(World):
    """Hyrule's second adventure, shuffled across a multiworld."""

    game = "Zelda II: The Adventure of Link"
    options_dataclass = Zelda2Options
    options: Zelda2Options
    settings: ClassVar[Zelda2Settings]
    settings_key = "zelda2_options"
    web = Zelda2Web()

    item_name_to_id = {i.name: i.id for i in ITEMS}
    location_name_to_id = dict(LOCATION_NAME_TO_ID)

    def create_item(self, name: str) -> Zelda2Item:
        item = ITEM_BY_NAME[name]
        return Zelda2Item(name, CLASSIFICATION[item.classification],
                          item.id, self.player)

    def get_filler_item_name(self) -> str:
        return ITEM_BY_KEY[FILLER_KEY].name

    def _included(self) -> list:
        """Locations this seed keeps after the pool options.

        A category that is turned off is removed rather than filled with junk.
        """
        opts = self.options
        out = []
        for loc in LOCATIONS:
            v = loc.vanilla_item
            if v.startswith("exp_") and not opts.experience_shuffle:
                continue
            if v.endswith("_container") and not opts.container_shuffle:
                continue
            if v in ("trophy", "child", "medicine") and not opts.quest_item_shuffle:
                continue
            if v == "key" and opts.key_shuffle == 0:
                continue
            out.append(loc)
        return out

    def create_regions(self) -> None:
        regions = {MENU: Region(MENU, self.player, self.multiworld)}
        for name in REGIONS:
            regions[name] = Region(name, self.player, self.multiworld)
        self.multiworld.regions.extend(regions.values())

        for loc in self._included():
            region = regions[loc.region]
            region.locations.append(
                Zelda2Location(self.player, loc.name, loc.id, region))

        for conn in CONNECTIONS:
            if conn.source not in regions or conn.target not in regions:
                continue
            needed = [ITEM_BY_KEY[k].name for k in conn.requires]
            regions[conn.source].connect(
                regions[conn.target],
                f"{conn.source} -> {conn.target}",
                (lambda state, n=tuple(needed):
                 state.has_all(n, self.player)) if needed else None,
            )

    def create_items(self) -> None:
        pool = []
        for loc in self._included():
            key = loc.vanilla_item if loc.vanilla_item in ITEM_BY_KEY else FILLER_KEY
            pool.append(self.create_item(ITEM_BY_KEY[key].name))

        for name, count in self.options.start_inventory_from_pool.value.items():
            for _ in range(count):
                match = next((i for i in pool if i.name == name), None)
                if match:
                    pool.remove(match)

        self.multiworld.itempool += pool

    def set_rules(self) -> None:
        needed = tuple(ITEM_BY_KEY[k].name for k in COMPLETION_ITEMS)
        self.multiworld.completion_condition[self.player] = (
            lambda state, n=needed: state.has_all(n, self.player))

    def generate_output(self, output_directory: str) -> None:
        placements = {
            loc.name: loc.item.name
            for loc in self.multiworld.get_locations(self.player) if loc.item
        }
        patch = Zelda2ProcedurePatch(player=self.player,
                                     player_name=self.player_name)
        write_tokens(patch, placements, self.options)
        base = self.multiworld.get_out_file_name_base(self.player)
        patch.write(os.path.join(output_directory,
                                 f"{base}{patch.patch_file_ending}"))

    def fill_slot_data(self) -> dict:
        return {
            "starting_lives": self.options.starting_lives.value,
            "starting_attack": self.options.starting_attack.value,
            "starting_magic": self.options.starting_magic.value,
            "starting_life": self.options.starting_life.value,
        }
