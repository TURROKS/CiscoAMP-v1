#!/usr/bin/env python3

__author__ = "Mario Rojas"
__version__ = "1.0.1"
__maintainer__ = "mariro_ch@hotmail.com"
__status__ = "Development"

import requests
import json
import datetime


# Select Offset range based on Hours or Minutes
Hour_Offset = 0
Minute_Offset = 20
lastEvents = []
newEvents = []

date = datetime.datetime.now()
start_date = (date - datetime.timedelta(hours=Hour_Offset, minutes=Minute_Offset)).strftime("%Y-%m-%d")
start_Hour = (date - datetime.timedelta(hours=Hour_Offset)).strftime("%H")
start_Min = (date - datetime.timedelta(minutes=Minute_Offset)).strftime("%M")


def get_amp_events(
    host="AMP HOST",
    client_id="",
    api_key="",
):
    # Open a new file for dumping the results
    with open('results.txt', 'w') as fp1:

        try:
            # Get Data from AMPs API
            url = f"https://{client_id}:{api_key}@{host}/v1/events?start_date={start_date}T{start_Hour}%3A{start_Min}%3A00%2B00%3A00"
            response = requests.get(url, verify=False)
            response.raise_for_status()
            # Get only JSON lines with "data"
            events_list = response.json()["data"]

            # Load list of previous events
            try:
                with open('lastevents.txt', 'r') as fp3:
                    for line in fp3:
                        current_place = line[:-1]
                        lastEvents.append(current_place)
            except FileNotFoundError:
                print('File Not Found')

            # Create new json object with new event only
            jsondata = [obj for obj in events_list if str(obj['id']) not in lastEvents]
            json.dump(jsondata, fp1)

            # Add current events to last events list
            for i in jsondata:
                if i["id"]:
                    newEvents.append(i["id"])

            # Update lastevents.txt file
            with open('lastevents.txt', 'w') as fp2:
                for event_id in newEvents:
                    fp2.write('%s\n' % event_id)

        except requests.exceptions.HTTPError as Error:
            print("Error: {}".format(Error))


if __name__ == '__main__':

    get_amp_events()
