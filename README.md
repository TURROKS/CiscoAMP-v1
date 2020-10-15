# CiscoAMP-v1
This Script retrieves events from the Cisco AMP for Endpoints API v1

### Requirements

In order to run this script you need Python3 and the following libraries

- requests
- json
- datetime

Fortunately jason and datetime come by default so you only need to install requests, but hey, what are Requirements file for.

**Run** pip install -r Requirements.txt

you will also need a valid client id and api key (you can get this from your admin).

### Options

You can run the script as it is and it will retrieve the events that occured within the last 20mins.

but you also have an option to change the offset by Hours or Minutes within the file.

- Hour_Offset = 0
- Minute_Offset = 20

### How to run it?

Simple

**Run** python amp_events.py

Enjoy the tool
