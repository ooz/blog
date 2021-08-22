---
title: List gradle test execution order
date: 2018-08-17T02:53:42Z
tags: __inline__
---

```
tasks.matching {it instanceof Test}.all {
    testLogging.events = ["failed", "passed", "skipped"]
}
```

Useful for finding tests that do not clean up properly!
