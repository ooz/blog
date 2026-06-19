---
title: Ubuntu 24.04 Fixes and Tweaks
date: 2026-02-17T00:05:04Z
---

I'm a little late to the party here, it's soon Ubuntu 26.04 LTS time marking my 20-year Ubuntu anniversary!

## 1. 32bit Wine

After installing Wine, 32bit Windows programs might fail with:

```
it looks like wine32 is missing, you should install it.
as root, please execute "apt-get install wine32:i386"
```

[The solution](https://www.cherryservers.com/blog/install-wine-ubuntu). After that run:

```
sudo apt install wine32
rm -rf ~/.wine
WINEARCH=win32 WINEPREFIX=~/.wine wine wineboot
```

## 2. Shift+3 shortcuts not working or keyboard repeating keys

```
ibus exit
```

Source: https://www.reddit.com/r/gnome/comments/18kl6fz/need_help_issue_with_shift_3_key_combination_in/

## 3. Increase timeout for "app is not responding" dialog

https://askubuntu.com/questions/1068921/how-to-disable-the-window-not-responding-dialog

## 4. Wifi issues

* https://www.linux.org/threads/problem-with-wifi-failing-to-reconnect-automatically-in-xubuntu-ubuntu-24-04-solved.49961/
* https://askubuntu.com/questions/95676/a-tool-to-measure-signal-strength-of-wireless

## Closing

Maybe, I'll give [Bluefin](https://projectbluefin.io/) a try instead of updating to the next Ubuntu LTS, since I moved on from tinkering with my OS a few years ago.
