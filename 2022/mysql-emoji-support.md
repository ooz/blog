---
title: Enable Emoji-Support for MySQL-Databases
date: 2022-04-27T18:17:27Z
---

![Copy&pastable below](mysql_utf8_collation.png)

```sql
-- ...
`CUSTOMER_COMMENT` varchar(1000) COLLATE utf8mb4_bin DEFAULT NULL,
-- ...
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
```
