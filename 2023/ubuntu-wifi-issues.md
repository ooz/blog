---
title: Ubuntu 22.04 WiFi Issues
date: 2023-04-08T00:45:04Z
tags: __inline__
---

I was getting silent wifi disconnects, this fixed the issue:

```
sudo vim /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
```

Change from `3` (powersave enabled) to `2` (powersave disabled)

Source: https://askubuntu.com/questions/1403954/wifi-issues-in-ubuntu-22-04lts
