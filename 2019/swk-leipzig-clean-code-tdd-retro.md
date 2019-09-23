---
date: 2019-09-22T23:57:48Z
title: Softwerkskammmer Leipzig: Clean Code Session "TDD"
description: Lessons learned from the meetup and Uncle Bob's videos
tags: retro
---

A little recap of what I learned/refreshed at the [Softwerkskammer Leipzig meetup](https://www.meetup.com/de-DE/Softwerkskammer-Leipzig/events/264030290/). We watched [Robert "Uncle Bob" Martin's Clean Code Episode 6 Part 1](https://cleancoders.com/video-details/clean-code-episode-6-p1) and [part 2](https://cleancoders.com/video-details/clean-code-episode-6-p2). Quotes by R. Martin if not noted otherwise:

## Programming wisdom

> Classes protect us from new types, data structures protect us from new functions

> High debugging skill correlates with low productivity

> Another word for testable is decoupled

> TDD is a prerequisite for professionalism

> Legacy code is code without tests (by Michael Feathers)

## Refactoring techniques

* Inline local/private functions before refactoring
* Extract code into inner class (quite commonly used by Uncle Bob)
* Do not use `StringBuffer` in modern Java, the compiler is smart enough
* Multiply `if`-statements
* Parametric loops

## General education

* Theories how the moon came to be
* [Ignaz Semmelweis](https://de.wikipedia.org/wiki/Ignaz_Semmelweis) not profiting from his [radical novelty](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD10xx/EWD1036.html) of hand washing during his lifetime

> Discipline are pre-made decisions
