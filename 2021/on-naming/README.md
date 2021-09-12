---
date: 2021-09-07T19:02:53Z
title: On Naming
description: Why naming is hard, important and at the heart of the programming profession
tags: __draft__
---

> "There are only two hard things in Computer Science: cache invalidation and naming things." -- Phil Karlton ([history and alterations of the phrase](https://martinfowler.com/bliki/TwoHardThings.html))

While the statement is humorously exaggerated, it has certain merit and fellow programmers can certainly relate.
But why is naming hard, important and at the very heart of the programming profession?

## Natural language

We use language to communicate with fellow humans and describe the world around us.
There, information loss and distortion is inherent (comp. Shannon-Weaver model, K. Gödel's incompleteness theorems).
We try to mitigate this by using further communication channels (e.g. mimics), common language, defining words and grammar.
Further, we shun people not sharing our definitions or having a different perception as ill or mad.
Sometimes this "social reality" is false and contesting ["radical novelties"](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD10xx/EWD1036.html) are met with [harsh resistance](https://en.wikipedia.org/wiki/Galileo_affair).


Back to computers, ...

The graphic below illustrates how we reflect our reality in language and interact with the world around us.
Each dashed arrow means an interaction/information exchange at loss of information (by using natural language or due to human error).
Solid arrows represent transformations/communication without information loss (e.g. compiling a program written in a well-defined programming language to machine code).

Compilers are good at ...
Compilers and machines do not care about naming.

* Programming is abstract, metaphors and real-world analogies help. Thus they are used widely in entire computer science

## Examples

* Dead verbs
* Generic nouns
* `result`
* add, remove (git messages)

## Further reads

* R. Martin: Clean Code, entire chapter 2 on "Meaningful Names"
* Minified JavaScript is not human-readable, thus not understandable and non-free: https://www.gnu.org/philosophy/javascript-trap.html

