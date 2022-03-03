---
title: Personal Contacts CRM INI File
date: 2022-02-27T23:33:38Z
---

Wow, even without a clickbait, SEO-optimized *"How-to ..."* or *"X Reasons ..."* prefix, the post title sounds like a heap of BS! 😅

So far, my biggest pain point [migrating away from "big tech"](https://oliz.io/blog/2021/towards-online-autonomy/) was my contacts list neatly synchronized by Google.
In the last year, I missed quite some birthdays, address updates and have generally been "minimal-social" due to lack of proper bookkeeping!

## History and Requirements

I already made it a habit to note key learnings after interactions with people I don't meet regularly.
When companies do this, it's called [Customer Relationship Management (CRM)](https://en.wikipedia.org/wiki/Customer_relationship_management), so the ever rotating clerks know of your correspondence.
This may sound [creepy](https://en.wikipedia.org/wiki/Stasi#Recovery_of_Stasi_files), but has the benefit of being more considerate and respectful with each other's time.
No more *"I thought, I already told you"* or *"What was the name of your child again?"*
That "database" was a set of local text files and I wanted to combine it with the contacts list exported from Google (`.csv`).

Requirements:

* Human- and machine-readable, plaintext, easy to edit and process
* Support structured master data like name, birthday, email, phone, address
* Support optional, arbitrary fields
* Support timestamped list of events, meaning what interaction happened with that person on a specific day, key insights gained
* All data in a single file
* Store master file/backups in KeePass, have a local copy for scripts to access

## Solution and Format

Eventually, I settled for an [INI file](https://en.wikipedia.org/wiki/INI_file).
[Python has built-in support](https://docs.python.org/3/library/configparser.html) and `grep`ing works, too.
Each person gets a section.
Master data are key-value pairs, notable events are date-note pairs.

Example:

```
[FirstName_LastName]
bday = 1990-09-29
email = foobar@example.com
address = Foo St. 23, 01234 City
2020-06-22 = Met for lunch, recently switched to ABCorp, children are well
2021-09-29 = Birthday telephone call, vegan for 6 months

[FirstName_?]
phone = +49 123456789
info = Met at festival

[unsorted]
Alice = XYZ user group meetup 2022-02-02, new to City and topic
John = XYZ user group meetup 2022-02-02, did Karate (6th Kyu) in school
```

Keys for unknown values may be omitted, unknown values in structured data may be masked with `?` characters (e.g. unknown birth year may become `????`).
This has the benefit of easy parsing/`grep`ing.
I made a little [script](https://github.com/ooz/olli/blob/master/.scripts/birthdays.py) which reads all birthdays (if present), sorts them by month and day, and prints the entire list with a "today" marker.
For me, this is a good-enough substitute for Google Calendar birthday notifications.

## Next Steps

Currently, I keep the INI file locally and back it up to KeePass.
More automated encryption and synchronization would be nice.

But first, I still need to migrate a good chunk of contacts data. 🙂

