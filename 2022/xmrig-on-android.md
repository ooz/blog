---
title: XMRig on Android
date: 2022-02-12T19:40:33Z
---

The Nobel Prize "for Economics" is fake, but money and blockchain are real? If your answer to this is "YES!", you may proceed at your own liability...

1. Install Termux
2. Install `proot-distro` package in Termux
3. Setup an Ubuntu environment
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
5. Start `xmrig` with minimal configuration
    ```bash
    modprobe msr # if supported by the system
	./xmrig -o ${POOL} -u ${WALLET} -k --tls
    ```

Bonus: [How to mine on p2pool (nice summary in one of the posts)](https://www.reddit.com/r/Monero/comments/sse4b1/stop_minexmr_p2pool_guide_how_to_mine_xmr_using/)

