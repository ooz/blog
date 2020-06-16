---
date: 2020-06-15T22:27:27Z
title: On Software Minimalism
description: Exploring how minimal software is a mean to an end searching for quality software.
---

Recently, I iterated on [`gg.py`](https://ooz.github.io/ggpy/) again, which ultimately led to the age-old question:

*Why (re-inventing the wheel)?*

## Minimal Software

I like the idea of minimal software, just the amount of software needed to solve a problem, to fulfill a need. Typical characteristics of minimal software are:

* [Simple, elegant, usable, focused, reasonable and attainable](https://suckless.org/philosophy/)
* Easier to understand
* Less prone to errors
* Less need for maintenance
* Less code (maybe)

I acknowledge that `gg.py` could have also been realized in shell using the [BusyBox set of UNIX utilities](https://busybox.net/).
Regardless, I enjoy working with Python and having a pet project keeps my language skills and tool chain sharp.
Software minimalism followed to the extreme would consider Python and anything written in it as "bloat" and not minimal. On a second look, the above traits of minimal software seem to be rather *means goals* than end goals. Extrapolated, I see one over-arching objective:

*To spend less time with software!*

## Standard Software and Innovation

Spending less time with software frees you up to spend more time outside, off the computer, with friends and family. Or to focus on the business side of things. Shell one-liners and clever single-file programs may be one approach, but for plenty of people the use of *standard software* is exactly that:

* The majority of people use it
* The majority of people has good-enough understanding of its benefits and constraints
* Someone else develops, maintains and supports it

Standard software is not necessarily user-facing software, but also common software libraries, frameworks, programming languages, open-source or industry standards.
One downside of using standard software is the loss of competitive advantage stemming from superior tools and craft. Then, [beating the averages](http://www.paulgraham.com/avg.html) and innovation are not a matter of technology, but of appropriate and repeated creative application valuing the zeitgeist.

## Conclusion

This cannot be an argument for minimal, custom-built software, nor standard software. Neither seems to grant an advantage inherently, so a healthy dose of pragmatism is required when developing or utilizing software in a competitive space.
Shifting the point of view, someone's minimal software might be someone else's standard software (e.g. UNIX utilities leveraged by an advanced user) and someone's standard software might be considered "overkill" by minimalists (e.g. WYSIWYG word processors for writing plain text).
At the end of the day, users minding their respective computer skills could still all agree that their preferred software tool enables them *to spend less time* with the computer.

This turns the question *"does this software enable me to spend more quality time off (or on) the machine?"* into a metric for gauging software value.

* Does this social network enrich my life or is it just artificially keeping me hooked to my phone for corporate profits?
* Does this computer game offer quality experience and immersion or is it just a paint over grind to grow [MAU](https://www.investopedia.com/terms/m/monthly-active-user-mau.asp)?
* Does this software tool enable me to get more things done and turn off the computer earlier?

As for `gg.py`, it covers my static site generator needs. Growing with it and having full creative expression are their own rewards. ☺