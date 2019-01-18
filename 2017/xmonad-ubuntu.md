---
date: 2017-04-02T21:20:32+02:00
title: How to configure Xmonad for Ubuntu 16.04
tags: xmonad
      ubuntu
---

In the last six months I must have set up my default Ubuntu 16.04 + Xmonad desktop environment on like four or more machines.
The goal looks like this (I like to have the top bar for status and widgets):

![Ubuntu and Xmonad](ubuntu_xmonad.png)

Here is a small guide for future reference:

## Step-by-step Guide

1. Install the Xmonad package:

    ```bash
    sudo apt install xmonad
    ```

    At this point you can already select an Xmonad session at the login screen.
    But this is not recommended.

2. So additionally you should install the [`gnome-session-xmonad` package](https://github.com/Gekkio/gnome-session-xmonad):

    ```bash
    sudo add-apt-repository ppa:gekkio/xmonad
    sudo apt-get update
    sudo apt-get install gnome-session-xmonad
    ```

3. Configure Xmonad. The Xmonad configuration is written in Haskell. If you are uncertain or need something working to start from, you are free to take [my configuration](https://github.com/ooz/olli/blob/master/.xmonad/xmonad.hs). Place it here: `~/.xmonad/xmonad.hs`

4. Relog and choose the **GNOME + XMonad** session at the login screen.

5. If you dislike the bottom panel (like I do, see above screenshot), you can disable it with:

    ```
    dconf write /org/gnome/gnome-panel/layout/toplevel-id-list "['top-panel']"

    ```

    To redisplay it, execute:

    ```
    dconf write /org/gnome/gnome-panel/layout/toplevel-id-list "['top-panel','bottom-panel']"
    ```

Have fun!

