import json
import pkgutil
from typing import NamedTuple

DATA_RESOURCE = "data/apworld_data.json"


class LocationDef(NamedTuple):
    id: int
    name: str
    region: str
    region_key: str
    area: int
    screen: int
    vanilla_item: str
    code_offset: int
    code_offset_mirror: int | None
    check_address: int
    check_bit: int
    presence_ambiguous: bool

    @property
    def check_mask(self) -> int:
        return 1 << self.check_bit


def _load() -> tuple[LocationDef, ...]:
    # pkgutil, not pathlib: an installed apworld is a zip.
    blob = pkgutil.get_data(__name__, DATA_RESOURCE)
    if blob is None:
        raise FileNotFoundError(f"{DATA_RESOURCE} is missing from the package")
    return tuple(
        LocationDef(
            id=e["id"], name=e["name"], region=e["region"],
            region_key=e["region_key"], area=e["area"], screen=e["screen"],
            vanilla_item=e["vanilla_item"], code_offset=e["code_offset"],
            code_offset_mirror=e.get("code_offset_mirror"),
            check_address=e["check_address"], check_bit=e["check_bit"],
            presence_ambiguous=e.get("presence_ambiguous", False),
        )
        for e in json.loads(blob.decode("utf-8"))["locations"]
    )


LOCATIONS = _load()
LOCATION_BY_NAME = {l.name: l for l in LOCATIONS}
LOCATION_NAME_TO_ID = {l.name: l.id for l in LOCATIONS}
REGIONS = tuple(dict.fromkeys(l.region for l in LOCATIONS))


def in_region(region: str) -> tuple[LocationDef, ...]:
    return tuple(l for l in LOCATIONS if l.region == region)


assert len(LOCATION_NAME_TO_ID) == len(LOCATIONS), "duplicate location name"
assert len({l.id for l in LOCATIONS}) == len(LOCATIONS), "duplicate location id"
