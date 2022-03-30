---
title: Database Normalization
date: 2022-03-30T12:29:02Z
tags: __inline__
tags: database, sql, computerscience, interview
---

Discovered some old notes for software dev interview prep.: [Database normalization](https://en.wikipedia.org/wiki/Database_normalization)!

|Normal form|Criteria|
|---|---|
|1NF|only atomic attribute values|
|2NF|all non-key attributes are functionally dependent on a key|
|3NF|no transitive dependencies between non-key attributes|
|BCNF|no transitive dependencies between key attributes, every determinant is key|
|4NF|no pair-wise, independent, multi-value dependencies between attributes|
|5NF|no JOIN-dependency|

On the same prep. sheet:
Knuth-Morris-Pratt algorithm (KMP) for String/Substring-Problem is in `O(n + k)`

