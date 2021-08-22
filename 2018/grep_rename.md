---
title: grep_rename.sh
date: 2018-02-02T03:23:19Z
tags: __inline__
---

```
grep -rl 'old' ./ | xargs sed -i 's/old/new/g'
```

