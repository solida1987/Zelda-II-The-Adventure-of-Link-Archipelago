# Zelda II: The Adventure of Link — Archipelago

An Archipelago world for **Zelda II: The Adventure of Link** (NES). Items across
Hyrule are shuffled, so what you find may belong to another player, and what you
need may be in their game.

You supply your own cartridge dump. Nothing from the game is distributed here.

## What gets randomised

**68 locations**, every one a fixed pickup somewhere in the world:

| Where | Locations |
|---|---|
| Palaces 3, 4 and 6 | 20 |
| Palaces 1, 2 and 5 | 19 |
| West Hyrule | 11 |
| East Hyrule | 11 |
| Death Mountain | 4 |
| Towns | 2 |
| Great Palace | 1 |

The game stores one item per area-data block, and several rooms share a block —
the same room reached from different places on the map. Those rooms cannot hold
different items, so each block is one location rather than several.

Between them they cover the eight key items (Candle, Handy Glove, Raft, Boots, Flute,
Cross, Hammer, Magical Key), all four Heart Containers and four Magic Containers, the palace keys, the experience bags, the jars and extra lives, and
the three quest items — Trophy, Kidnapped Child and Water of Life — that
townspeople trade for spells.

## How it works

The game records every collectable it has given you as a single bit in work
RAM. The client watches that block, so picking something up is what sends the
check — there is no separate tracker to keep in sync, and it survives a
reconnect because the record lives in your save.

Generating a seed produces an `.apz2` patch. Opening it writes your own items
into a copy of your ROM, so a single-player seed plays through with nothing
running alongside it. Your cartridge dump is never modified and never leaves
your machine.

Logic gates on the Hammer, Raft, Boots and Flute, which the game is universally
documented as requiring, and nothing finer. Some locations are therefore
reachable in logic slightly earlier than in practice; it will not produce a seed
that cannot be finished.

## Options

Key shuffle (vanilla or anywhere in the multiworld) · whether containers,
experience and quest items join the pool · starting Attack, Magic and Life
levels · starting lives.

## Installing

See **[docs/setup_en.md](zelda2/docs/setup_en.md)** for the full walkthrough.
In short: put `zelda2.apworld` in your Archipelago `custom_worlds` folder,
create a YAML, generate, then open the patch and connect the BizHawk client.

## Known issues

- **Items found for you by other players do not arrive in your game.** Checks
  you find are sent to the server correctly, and a single-player seed plays and
  finishes normally, but the client does not yet write an incoming item into the
  running game. Treat this as a single-player world until that is fixed.
- **Patching needs a dump with the 16-byte iNES header** (262,160 bytes). Every
  patch offset is counted from the start of a headered file. A headerless dump
  is recognised but refused with a message rather than patched wrongly.

## Legal

Zelda II: The Adventure of Link is © Nintendo. This project contains no game
code, no game data and no ROM — it reads and writes a copy you already own, and
the patch is useless without it. Supply your own legally obtained cartridge
dump.

This world was written from
[FiendsOfTheElements/z2disassembly](https://github.com/FiendsOfTheElements/z2disassembly),
a disassembly of the game released under **CC0-1.0** (public domain), with
addresses cross-checked against the
[Data Crystal](https://datacrystal.tcrf.net/wiki/Zelda_II:_The_Adventure_of_Link)
community ROM map.

## Credits

World and plugin by **solida1987**.

Thanks to the authors of the CC0 disassembly, without which none of the
addresses in this world could have been established, and to the Data Crystal
contributors who documented the game's data formats.

## Licence

MIT — see [LICENSE](LICENSE).

---

## Archipelago Discord Notice

I have been permanently banned from the official Archipelago Discord server.
Because of this, please do not post or share links to this project on the
official Archipelago Discord, as this project is not permitted there.

For clarity, the ban was not related to malware, viruses, malicious code, or
any security issue with this project.

The moderation issues were related to:

* Copyright/distribution concerns involving game files in earlier versions of
  my projects. Those files were removed, the affected repositories and
  releases were cleaned up, and the distribution process was changed
  accordingly.
* Violations of the Discord server's own content rules, including
  links/content involving games that were restricted or considered 18+ under
  their server rules.

These issues relate to the official Archipelago Discord's moderation and
content policies.

Development and support for this project will continue independently outside
of the official Archipelago Discord.

---

## AI Usage Disclosure

Everything in this project was made by AI.

The code is AI.
The documentation is AI.
The artwork is AI.
I am AI.
My mother and father are also AI.

At this point, just assume everything is AI unless proven otherwise.

