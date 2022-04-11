---
title: Remove snap(d)
date: 2022-04-11T14:49:25Z
tags: __inline__
---

Sometimes it may be desired to get packages from `apt` instead of `snap`,
e.g. the Chromium snap doesn't have hardware acceleration for video conferences.

```
# Remove all snap packages
snap list
sudo snap remove --purge $SNAP_NAME

# Remove cache
sudo rm -rf /var/cache/snapd/
sudo apt autoremove --purge snapd gnome-software-plugin-snap
rm -rf ~/snap

# Block snap from auto-installing
sudo apt-mark hold snapd
sudo apt install gnome-software
```

