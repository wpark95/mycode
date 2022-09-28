#!/usr/bin/python3
""" Challenge - ISS Tracker | Will """

import requests
import datetime
import reverse_geocoder as rg

ISS_LOCATION = "http://api.open-notify.org/iss-now.json"

def main():
    iss_pos = requests.get(ISS_LOCATION).json()
    latitude = iss_pos["iss_position"]["latitude"]
    longitude = iss_pos["iss_position"]["longitude"]
    rg_res = rg.search((latitude, longitude))[0]

    print("CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {datetime.datetime.fromtimestamp(iss_pos['timestamp'])}")
    print(f"Lon: {latitude}")
    print(f"Lat: {longitude}")
    print(f"City/Country: {rg_res['name']}, {rg_res['cc']}")

if __name__ == "__main__":
    main()
