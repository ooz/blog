---
title: E. Wolff: Why Continuous Delivery Doesn't Work
date: 2022-04-04T07:08:35Z
---

On 2020-11-10 (yes, I'm slightly behind on blog schedule), E. Wolff replicated his [famous talk](https://www.youtube.com/watch?v=lNR92yO_9y8) for SWK Chemnitz.
At that time, I was also lecturing Software Engineering at university and recommended students to attend the meetup or watch the talk on YT.
This post should serve as another summary of the talk.

## Reasons to do Continuous Delivery (CD)

* Faster time to market
* Faster to restore service
* Lower failure rate
* Less unplanned work
* Less rework
* Less security issues
* Less user issues
* Less support
* 66% more productive
* Less burnout, more psychological safety

## Misunderstanding CD

CD isn't just about deploying multiple times a day (or on demand).
Instead:

* It's about feedback, not features
* It's treating working software as a series of experiments
* CD enables more experiments

Improving the software process is a positive side-effect!

## Why do some not like feedback?

Traditional business setting: People doing mistakes gets them fired.
As a consequence, people try to avoid doing mistakes and seek no feedback.
For some, feedback is only valuable if the plan is bad and it's hard for those people to admit, that their plan is bad.

Problem: **60-90% of ideas do not improve metrics** (and lots don't even have proper metrics/KPIs)

Typical statements of this crowd:

* "We need to train users"
* "Users don't want new features"

## How to get CD to work?

**Culture is key!** E. Wolff named some examples (HP developing and deploying printer firmware on emulators), even outside software development ([NUMMI](https://en.wikipedia.org/wiki/NUMMI)).

* Accept feedback
* Handle mistakes
* Make stakeholders appreciate and demand better tools

## Questions and feedback from the audience

*Q: How do Sprints and CD fit together?"*

A: Sprints are a frame for feedback loops. Sprints order input tasks, CD delivers outputs. Someone recommended https://www.youtube.com/watch?v=502ILHjX9EE

Also related: https://puppet.com/resources/report/2021-state-of-devops-report/

