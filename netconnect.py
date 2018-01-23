# For Micropython

import network
from sys import exit
from ujson import loads

def connect(cred_file="wifi.json"):
    with open(cred_file) as f:
        creds = loads(f.read())

        print(creds)

        station = network.WLAN(network.STA_IF)
        print("Wifi station is: ", station.active())

        print(creds["ssid"])
        print(creds["password"])

        station.connect(creds["ssid"], creds["password"])
        return station


