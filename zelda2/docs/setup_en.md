# Zelda II: The Adventure of Link Setup Guide

## Required Software

- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases) 0.6.0 or
  newer.
- The latest `zelda2.apworld` from
  [this project's releases](https://github.com/solida1987/Zelda-II-The-Adventure-of-Link-Archipelago/releases).
- [BizHawk](https://tasvideos.org/BizHawk/ReleaseHistory) 2.9.1 or newer.
- A legally obtained Zelda II: The Adventure of Link (USA) cartridge dump,
  with the usual 16-byte iNES header — 262,160 bytes.

## Installing the world

1. Double-click `zelda2.apworld`, or place it in your Archipelago install under
   `custom_worlds`.
2. Start `ArchipelagoLauncher.exe` once so the world is registered.

## Configuring BizHawk

- Under `Config > Customize`, tick **Run in background**, so the client does
  not disconnect while you are in another window.
- Under `Config > Hotkeys`, clear any keybinds you do not intend to use.

## Creating your YAML

In the Archipelago Launcher, choose **Generate Template Options**, or use the
Options Creator for a visual editor. A minimal file looks like this:

```yaml
name: YourName
game: "Zelda II: The Adventure of Link"
"Zelda II: The Adventure of Link":
  key_shuffle: vanilla
  container_shuffle: true
  experience_shuffle: true
```

Leaving `experience_shuffle` off drops 50 of the 116 locations, for a much
shorter seed.

Put the file in your `Players` folder.

## Generating and hosting

1. Choose **Generate** in the Launcher. The result lands in `output`.
2. Upload the zip to [the Archipelago website](https://archipelago.gg/uploads),
   or host it locally with **Host** in the Launcher.

## Starting the game

1. In the Launcher, choose **Open Patch** and select your `.apz2` file. You
   will be asked for your Zelda II ROM the first time.
2. The patched ROM opens in BizHawk.
3. Open the **BizHawk Client** from the Launcher and connect it to your room's
   address and your slot name.
4. Start a new file and play. Items you pick up are sent as you collect them.

## Playing through the Multiworld Launcher

If you use the Multiworld Launcher, install the Zelda II plugin from its
library instead. It handles the ROM, the patch and the connection itself, and
you do not need the BizHawk Client.

## Troubleshooting

**The client says the ROM is wrong.** The check is on the game data, not on the
file header, so a ROM that has already been patched or hacked is refused. Use
your original dump. A headerless dump is refused separately: the patch offsets
are counted from the start of a headered file.

**An item another player found for me never arrived.** Incoming items are not
written into the running game yet. Single-player seeds are unaffected, because
your own items are patched into the ROM.

**A check did not register.** Please open an issue with the location name and
your slot name, and attach the client log if you have it.

**Nothing happens at all.** Make sure BizHawk has the game running and a save
file loaded. The client waits until you are actually in the game before it
reads anything, so nothing is reported from the title screen.
