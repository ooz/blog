---
title: Checking an Android Phone for NSO Group's Pegasus Malware
date: 2021-07-22T22:40:11Z
---

After [Amnesty International’s Methodology Report](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/) from last Sunday, I early-adopted the [Mobile Verification Toolkit](https://github.com/mvt-project/mvt) on Monday evening.
At that time, parts of the documentation and cross-referencing were pretty basic, so I'm documenting my process and concentrating links to all resources here.

Less tech-savvy users may want to wait for the [announced GUI](https://github.com/mvt-project/mvt/issues/38).

Preconditions:

* Have `adb` installed or use the [Docker image](https://github.com/mvt-project/mvt/pull/16) (this saves some MVT installation steps, too)
* [Enable developer mode on the Android device, enable USB debugging in developer options](https://developer.android.com/studio/debug/dev-options#enable)

Further read:

* [Lookout's Analysis of Pegasus Spyware (2016 version)](https://info.lookout.com/rs/051-ESQ-475/images/lookout-pegasus-technical-analysis.pdf)

## Installing MVT in a pipenv

I installed the project's dependencies in a [`pipenv`](https://pipenv.pypa.io/en/latest/) to not pollute the system's python packages:

```bash
# Clone repository
git clone https://github.com/mvt-project/mvt.git
cd mvt/

# Install dependencies in pipenv
pipenv --python 3
pipenv run pip3 install .
```

## [Check APKs](https://mvt-docs.readthedocs.io/en/latest/android/download_apks.html)

Since you can't use the tool to download the APKs and check for malware signatures later,
it's best to do this right away.
Otherwise you'd need to download the packages twice:

```bash
mkdir android-apks
pipenv run mvt-android download-apks -o android-apks/ --virustotal
```

Sometimes the Android device is busy and MVT recommends to reset the adb server. This works just fine:

```bash
adb kill-server
```

On the phone, when downloading the APKs, you will be asked (multiple times, even if you check the 'allow future access' box) to allow `adb` access, this dialog needs to be accepted within 5 seconds, otherwise MVT times out. It's best to be attentive and watch the phone screen. ;)

## Check SMS backup for malicious links

This process is [well-documented](https://mvt-docs.readthedocs.io/en/latest/android/backup.html):

* A malware definition file in [STIX v2 format (pegasus.stix2)](https://github.com/AmnestyTech/investigations/tree/master/2021-07-18_nso) is needed. MVT is not compatible with STIX v1.
* Also, [Android Backup Extractor](https://github.com/nelenkov/android-backup-extractor/releases) is needed. Download `abe.jar` from the releases page.

```bash
# Backup SMS from Android device
adb backup com.android.providers.telephony

# Extract SMS backup
java -jar abe.jar unpack backup.ab backup.tar
tar xvf backup.tar

# Check backup against STIX v2 file
pipenv run mvt-android check-backup . --iocs pegasus.stix2
```
