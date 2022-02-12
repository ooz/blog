---
title: XMRig on Android
date: 2022-02-12T19:40:33Z
---

1. Install Termux
2. Install `proot-distro` package in Termux
3. Setup an Ubuntu environment:
    ```bash
    proot-distro install ubuntu
    proot-distro login ubuntu
    ```
4. Follow https://xmrig.com/docs/miner/build/ubuntu
    ```bash
    apt update && apt upgrade
    apt-get install git build-essential cmake automake libtool autoconf
    git clone https://github.com/xmrig/xmrig.git
    # Change donation rate if desired
    mkdir xmrig/build && cd xmrig/scripts
    ./build_deps.sh && cd ../build
    cmake .. -DXMRIG_DEPS=scripts/deps
    make -j$(nproc)
    ```
