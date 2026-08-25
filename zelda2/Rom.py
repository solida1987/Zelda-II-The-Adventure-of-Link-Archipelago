import hashlib

import settings
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes

from .Items import ITEM_BY_NAME
from .Locations import LOCATIONS

GAME = "Zelda II: The Adventure of Link"

# PRG+CHR of Zelda II (USA), header excluded, so both the iNES and NES 2.0
# forms of the same dump are accepted.
HEADERLESS_MD5 = "88c0493fb1146834836c0ff4f3e06e45"
# The same dump with the usual 16-byte iNES header, which is what AP records
# in the patch manifest. verify() is the real gate and ignores the header.
HEADERED_MD5 = "764d36fa8a2450834da5e8194281035a"
HEADER_LEN = 16

START_ATTACK_OFFSET = 0x17AF3
START_MAGIC_OFFSET = 0x17AF4
START_LIFE_OFFSET = 0x17AF5
START_LIVES_OFFSET = 0x1C369

FOREIGN_ITEM_CODE = 0x10


class PatchError(Exception):
    pass


class Zelda2Settings(settings.Group):
    class RomFile(settings.UserFilePath):
        """Your own Zelda II: The Adventure of Link (USA) cartridge dump."""
        description = "Zelda II: The Adventure of Link (USA) ROM"
        copy_to = "Zelda II - The Adventure of Link (USA).nes"

    rom_file: RomFile = RomFile(RomFile.copy_to)


def split_header(data: bytes) -> tuple[bytes, bytes]:
    if data[:4] == b"NES\x1a":
        return data[:HEADER_LEN], data[HEADER_LEN:]
    return b"", data


def verify(rom: bytes) -> None:
    header, body = split_header(rom)
    got = hashlib.md5(body).hexdigest()
    if got != HEADERLESS_MD5:
        raise PatchError(
            "That is not an unmodified Zelda II (USA) dump. Its fingerprint is "
            f"{got}, and this needs {HEADERLESS_MD5}. An already-patched or "
            "ROM-hacked file will land here; use your original dump.")
    if not header:
        raise PatchError(
            "That dump has no iNES header. Every patch offset is counted from "
            "the start of a headered file, so a headerless dump cannot be "
            "patched. Re-dump the cartridge or add the 16-byte header.")


def get_base_rom_bytes() -> bytes:
    rom = bytes(open(settings.get_settings().zelda2_options.rom_file, "rb").read())
    verify(rom)
    return rom


class Zelda2ProcedurePatch(APProcedurePatch, APTokenMixin):
    game = GAME
    hash = HEADERED_MD5
    patch_file_ending = ".apz2"
    result_file_ending = ".nes"
    procedure = [("apply_tokens", ["token_data.bin"])]

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()


def _clamp(v: int) -> int:
    return max(1, min(8, v))


def build_tokens(placements: dict[str, str], options) -> list[tuple[int, bytes]]:
    by_name = {l.name: l for l in LOCATIONS}
    tokens = []

    for loc_name, item_name in placements.items():
        loc = by_name.get(loc_name)
        if loc is None:
            continue
        item = ITEM_BY_NAME.get(item_name)
        # Another world's item has no code of its own; the pickup still fires
        # the check and the server sends what the player actually receives.
        code = item.game_code if item and item.game_code is not None else FOREIGN_ITEM_CODE
        tokens.append((loc.code_offset, bytes([code])))
        # Death Mountain and Maze Island read the same area data from two PRG
        # banks. Both copies must change or the item reverts.
        if loc.code_offset_mirror is not None:
            tokens.append((loc.code_offset_mirror, bytes([code])))

    tokens.append((START_ATTACK_OFFSET, bytes([_clamp(options.starting_attack.value)])))
    tokens.append((START_MAGIC_OFFSET, bytes([_clamp(options.starting_magic.value)])))
    tokens.append((START_LIFE_OFFSET, bytes([_clamp(options.starting_life.value)])))
    tokens.append((START_LIVES_OFFSET, bytes([_clamp(options.starting_lives.value)])))
    return tokens


def write_tokens(patch: Zelda2ProcedurePatch, placements: dict[str, str],
                 options) -> None:
    for offset, value in build_tokens(placements, options):
        patch.write_token(APTokenTypes.WRITE, offset, value)
    patch.write_file("token_data.bin", patch.get_token_binary())
