---
title: S. Crater, K. Pepperdine: Java in the Cloud: Sensible JVM Configuration
date: 2022-10-17T22:17:24Z
---

https://www.youtube.com/watch?v=Ce_mEZP1XFk

TL;DW:

**Use defaults, usually there is no need to mess with JVM flags!**

If you insist changing things:

* Start with defaults
* Measure app behavior
* Change things one by one:
    - heap size
    - number of helper threads
    - garbage collector

## Know the defaults!

Heap size:

* Initial: 1/64 of real memory
* Max, <250MB available: 1/2 of real memory
* Max, >250MB available: 1/4 of real memory

Helper threads:

* <5 cores: threads = number of cores
* 5+ cores: threads = 5/8 * number of cores

Default Garbage Collector:

* JDK8: ParallelGC (shouldn't be used in the cloud anymore, from pre-container days!)
* JDK11+, 1 CPU and <1728MB memory: SerialGC
* JDK11+, 2+ CPU or >1728MB memory: G1GC

## Recommendations

* Set heap size based on allocation rate and live set size
* Ideally, number of active threads = number of cores
* Don't change the default GC ;)

