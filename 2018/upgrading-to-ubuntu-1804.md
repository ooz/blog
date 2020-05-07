---
date: 2018-11-05T23:08:49Z
title: Upgrading to Ubuntu 18.04
description: A little checklist when upgrading from Ubuntu (+ XMonad) 16.04 to 18.04
---

So far I upgraded three Ubuntu machines from 16.04 LTS to 18.04 LTS.
Just my work laptop is left. A little checklist for future upgrades:

## Before upgrading

* Cleanup unneeded packages to minimize the need to update

## Upgrade!

* Do the actual upgrade to Ubuntu 18.04:
    ```bash
    sudo apt update
    sudo do-release-upgrade
    ```
* Add PPA for [Gnome + XMonad](https://github.com/Gekkio/gnome-session-xmonad) again:
    ```bash
    sudo add-apt-repository ppa:gekkio/xmonad
    sudo apt-get update
    sudo apt-get install gnome-session-xmonad
    ```
* Select `GNOME + XMonad` session at login

## Polish

* Install Gnome tweak tool:
    ```bash
    sudo apt install gnome-tweak-tool
    ```
* Use `gnome-tweaks` to hide desktop icons (category by category, hiding all at once resets the wallpaper as well!)
* Backup wineprefix under `~/.wine`, let wine 3.0 initialize the default wineprefix again, e.g. by executing `winecfg`. Then copy relevant programs back into the wineprefix

