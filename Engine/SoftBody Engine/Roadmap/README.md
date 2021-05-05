
***

# Roadmap for the softbody engine

The softbody engine is a key feature in this game, and will require the most work. The 0.5-2 minute demos of people rendering softbody graphics for Tetris are reported to take around ~36 hours to render. I will need to figure out how to do this in real time.

## Development platform

I will be focusing development solely on Linux to better promote Linux, although a Windows port, a BSD port, and a MacOS port will be available, but won't be as actively developed (if the developers can agree on this)

The current platform goal is designed to give people 3 choices for Linux as a starter

* Ubuntu 20.04 LTS Focal Fossa - Highest level of development

> * Debian 10 - Equal highest level of development

* Fedora 33 - Second highest level of development

* Arch Linux 2021.05.01 and up - Third highest level of development

Other Linux ports will be unavailable for now and will only be unofficial and unstable (unless a 4th distribution is highly requested)

If a Windows port is desired, I will only support the following releases (for now)

* Windows 7 Service Pack 1 (all x64 editions)

* Windows 10 Build 1803 and up (all x64 editions)

If the game can even be ran on a Mac in the beginning, I will support the following releases (for now)

* MacOS Big Sur 11.3 and up

An Android or iOS port will be in the works if the hardware becomes capable/the game becomes light enough

## CPU cycle goal

The softbody engine is the most complex engine in this distribution. The first goal is to get it to function with a 16 Gigahertz processor. Once this is done, the engine should be continously optimized to take less and less CPU cycles and be able to work on less and less CPU.

**Index:** `get the game to run with` **refers to:** _getting the game to run with the softbody engine in softbody mode at 4K 120 FPS or 8K 60 FPS with real time graphics_

- [x] Tier failing - Get the game to not run at all (successful, as of May 5th 2021)

- [ ] Tier 0 - Get the game to run with 16 Gigahertz of CPu

- [ ] Tier 1 - Get the game to run with 14 Gigahertz of CPU

- [ ] Tier 2 - Get the game to run with 12 Gigahertz of CPU

- [ ] Tier 3 - Get the game to run with 10 Gigahertz of CPU

- [ ] Tier 4 - Get the game to run with 8 Gigahertz of CPU

- [ ] Tier 5 - Get the game to run with 6 Gigahertz of CPU

- [ ] Tier 6 - Get the game to run with 5 Gigahertz of CPU

- [ ] Tier 7 - Get the game to run with 4 Gigahertz of CPU

- [ ] Tier 8 - Get the game to run with 3.5 Gigahertz of CPU

**The may not be possible tiers**

- [ ] Tier 9 - Get the game to run with 3 Gigahertz of CPU

- [ ] Tier 10 - Get the game to run with 2 Gigahertz of CPU

- [ ] Tier 11 - Get the game to run with 1 Gigahertz of CPU

- [ ] Tier 12 - Get the game to run with 800 Megahertz or less CPU

***

## File info

**File type:** `Markdown (*.md)`

**File version:** `1 (Wednesday, May 5th 2021 at 4:56 pm)`

**Line count (including blank lines and compiler line):** `131`

***

## File history

<details><summary><H3>View file history (click/tap here)</H3></summary>

***

**Version 1 (Wednesday, May 5th 2021 at 4:56 pm)**

> Changes:

> * Started the file

> * Added the title section, with general info

> * Added the development platforms section

> * Added the CPU goal chart, with 14 tiers

> * Added the file info section

> * Added the file history section

> * Added the footer section

> * No other changes in version 1

**Version 2 (Coming soon)**

> Changes:

> * Coming soon

> * No other changes in version 2

***

</details>

***

## Footer

You have reached the end of this file.

### EOF

***
