---
date: 2017-02-05T10:26:46+01:00
title: How to assign the Logitech MX518 extra buttons under Ubuntu 16.04
tags: gaming
      mx518
      ubuntu
---

Once a while™ I like to play strategy or MMO games on my PC.

Back in 2006 I bought the fantastic Logitech MX518 gaming mouse and have been using it ever since.

![Logitech MX518 gaming mouse](https://images-na.ssl-images-amazon.com/images/I/91YmmYMH40L._SL1500_.jpg)

([Image source: Amazon](https://www.amazon.com/Logitech-910-000616-MX518-Optical-Gaming/dp/B0015R8M7U))

As you can see in the picture the mouse sports extra buttons that are handy when assigned properly in games.
This works just fine under Windows with the tools Logitech provides.
Before Ubuntu switched to `systemd` there was a tool named [`btnx`](https://launchpad.net/btnx) that enabled you to assign keyboard keys to mouse buttons.

It just worked!

With the adaption of `systemd` in Ubuntu (16.04 was my first version with systemd, since I only use LTS versions), `btnx` stopped working since it relied on `init.d`.

So here is how I got it to work with `systemd`:

1. Install lomoco:

    ```bash
    sudo apt install lomoco
    ```

2. Configure lomoco and set the mouse resolution to 1200, otherwise the button reassignment is not possible:

    ```bash
    sudo vim /etc/default/lomoco
    ```

    The resulting file should look like this:

    ```
    # Configuration file for lomoco
    # see `man lomoco` for details

    # Define which resolution should be used
    # Values:      800,400,1200,1600
    LOGITECH_MOUSE_RESOLUTION=1200

    # Whether to disable SmartScroll/Cruise Control. Defaults to yes if not set.
    # Values:      yes,no
    LOGITECH_MOUSE_DISABLE_CC=
    ```

3. Install the outdated packages [btnx-config](https://launchpad.net/btnx-config/) and [btnx](https://launchpad.net/btnx) (in this order).

4. Restart Ubuntu.

5. Create the btnx.service for systemd (I still think one of those files is redundant, I did not dive that deep into systemd yet):

    Content of the btnx.service file:

    ```
    [Unit]
    Description=Btnx
    Documentation=https://ooz.github.io
    After=graphical.target

    [Service]
    Type=simple
    ExecStart=/usr/sbin/btnx
    PIDFile=/var/run/btnx.pid
    Restart=on-abort
    ```

    Place it at the following locations:

    ```bash
    sudo cp btnx.service /etc/systemd/system/
    sudo cp btnx.service /etc/systemd/system/graphical.target.wants/
    ```

6. Start the btnx.service:

    ```bash
    sudo systemctl start btnx.service
    ```

    You can verify whether the service has launched with the following command:

    ```bash
    systemctl status btnx.service
    ```

7. Launch btnx-config and configure your mouse!

    ```bash
    sudo btnx-config
    ```

    * "Detect mouse & buttons"
    * Press every mouse button once
    * Switch tab, select mouse button, enable keyboard overwrite, assign keyboard key to mouse button

8. Restart Ubuntu and you are done!
