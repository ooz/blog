---
title: Towards Online Autonomy
description: Migrating away from Google, Twitter etc. towards my own online presence.
date: 2021-06-06T21:49:18Z
---

Smartphones have become the "personal computer":
a computer in your hand, solving most of your consumer computer use-cases (e.g. communication, (re-)search, navigation, shopping, photo, video, music, social and other media).

Ever since, I'm annoyed, that we don't (can't) really *own* smartphones like we can own other computing equipment.
Smartphones have hard- and software obsolescence built-in.
They are tailored towards consumption and guided interactions, most of the time they are inferior tools for creation.
Users may perceive value from interacting with a smartphone, but the majority of interactions generate more revenue/profit for other entities through [attention economy](https://oliz.io/blog/2020/dev-talk-binge-random-wisdom/#attention-economy)
(making platforms more attractive for other users, network effects, data classification, entry and generation etc.)
If you don't use your smartphone to make money (media creator, influencer?), you are paying -sometimes premium- for being used and distracted.

## Tech is Getting Consolidated...

This entire development didn't start and won't end with smartphones.
[RMS](https://stallman.org/) has been anticipating and warning about it for decades already (see his [definition of "Useds"](https://stallman.org/glossary.html#used)). It's common knowledge by now, some examples:

* Hardware backdoors ([Intel ME](https://en.wikipedia.org/wiki/Intel_Management_Engine), undocumented x86 instructions) in mainline processors
* [The internet becoming more centralized](https://staltz.com/the-web-began-dying-in-2014-heres-how.html) with [a dozen of mega corporations owning the majority of the traffic](https://www.visualcapitalist.com/wp-content/uploads/2019/08/top-100-websites-ranking.html)
* In the near future, [we'll get smartphone-level surveillance and "ownership" for our other computers, too](https://sneak.berlin/20201112/your-computer-isnt-yours/)
* [Pegasus anyone?](https://oliz.io/blog/2021/pegasus-android-check/)

Expiring computers may be fine for most companies leasing or cycling every 2-3 years and some users, who rotate in a similar fashion to "stay on the edge".
In my opinion, sustainable, exhaustive tech usage should be preferred, which is also dependent on *user-serviceable*, secure hard- and software.
State and malicious actors may like loopholes, but [insecure infrastructure ultimately harms everyone](https://www.wired.com/story/power-grid-cyberattack-facebook-phone-numbers-security-news/).

The general population (not just the nerds) is spending more screentime consuming social media, streaming content and games. Thus we are increasingly exposed to and determined by the above developments.

## ...and Boring

Starting in 2019, I noticed how I barely got any value out of Twitter anymore. Of course, there was the occasional interesting tech news, story or funny pastime, but interacting with it felt like a chore.
So I stopped using it, [social media isn't there to connect us anyway](https://sneak.berlin/20200211/instagram/).
I'm still in the process of migrating my content away from the platform.

Another wake-up call has been [Google Photos' changed storage policy](https://blog.google/products/photos/storage-changes/): Unlimited photo storage and sync has been so convenient. Google profited greatly from all the training data! Now that the noise is increasing and the value is diminishing, economics are back to remind us all: "Useds" of a free service don't own anything.

So, this sped up my migration away from my previously central `gmail.com` address towards my own `oliz.io` domain in 2020. I evaluated my exposure to and reliance on "big tech", too.

## Progress so Far (to Be Updated Over Time)

Autonomy gained:

* [x] Acquire `oliz.io` domain in 2020
* [x] Use https://mailbox.org with own domain for email
* [x] Build static website on `oliz.io` domain, using [`gg.py`](https://oliz.io/ggpy/)
* [x] [Find good, local solution for keeping track of birthdays and contacts](https://oliz.io/blog/2022/personal-crm.html), migrate contacts

Stopped/minimized using:

* [x] **XING**: Used its "one year pause" mode which recently expired, it spammed me again and I deleted it permanently.
                Preferring LinkedIn (and considering moving my data out there, too)
                Too much and not valuable recruiter spam made me lock down notification settings and network exposure, [but then again I'm probably not using it right](https://blog.calebjay.com/posts/how-to-use-linkedin-as-a-coding-bootcamp-grad/) nor [properly](https://twitter.com/j4n0/status/1125380024733925377). The CV tooling is neat, still I may just abandon it at some point and put the resume on here
* [ ] **Gmail**: Contacts are exported and [migrated](https://oliz.io/blog/2022/personal-crm.html). Haven't actively reached out to anyone regarding the email change, yet
* **Amazon**: In general, I prefer to buy in local or specialized (online) shops.
              Amazon still has the superior customer service and return/refund policy, so I may go with it for uncertain/risky purchases

Kept using:

* **GitHub**: Everything is static, in Git, under my domain and their fallback domain [https://ooz.github.io](https://ooz.github.io). *Migration* to any other service is *easy* if desired at all
* **circleci**: No problem with that, so far. Great free plan to offload some computing tasks like building this blog and observing the [Zeitgeist](https://oliz.io/zeitgeist/)!
* **Google / Android**: It's still unparalleled for advanced users. Smartphone usage is mostly work-related :)
* **Dropbox**: Still using due to convenience, [here is a guide to isolate the process](https://www.grepular.com/Protecting_Your_GNU_Linux_System_from_Dropbox) and [an alternative](https://privacyguides.org/software/file-sharing/#sync)
* [**VSCodium**](https://vscodium.com/): VSCode without tracking, plus [`vim`](https://github.com/ooz/olli/blob/master/.vimrc) of course

Educate others:

* Setup your own domain and [use it for email](https://sneak.berlin/20201029/stop-emailing-like-a-rube/)
* Look for alternatives, e.g. on ~~https://www.privacytools.io~~, https://privacyguides.org

**Twitter**:

* [x] Not using it anymore
* [x] Add RSS feed generation to ggpy to make it easier for others to subscribe to my content
* [ ] WIP: Migrating my content to this blog
* [ ] I still need a solution to follow some people I know or like

## Further Inspiration and Links

Certainly, I'm not the first to be alienated. [So here are a bunch of other nice, informative websites/blogs by people following the same idea of an independent internet](https://oliz.io/links.html). Even more resources and tools:

* https://victoria.dev/blog/make-your-own-independent-website/ (note to self: have a look at webmention)
* [Free messaging alternatives](https://sneak.berlin/20200220/discord-is-not-an-acceptable-choice-for-free-software-projects/) (haha, this entire post reeks of [sneak.berlin](https://sneak.berlin), great content!)
* https://riseup.net/ (various independent communication and collaboration services)
* [Website privacy checker](https://webbkoll.dataskydd.net/en), https://observatory.mozilla.org/
* [General security flaws with modern tech](https://madaidans-insecurities.github.io/) (nice, minimal website, too!)
* [Curated list of libre Android apps](https://gitlab.com/linuxcafefederation/awesome-android/-/blob/main/README.md)
* [Web browser privacy comparison](https://privacytests.org/)
* [Ruin My Search History](https://proprivacy.com/tools/ruinmysearchhistory) (a reader suggested this, I like the idea, but use at own risk™)

