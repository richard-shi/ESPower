# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)

import gc
from netconnect import connect
from server import start

# Connect to network
station = connect()

# Start web server
start()


gc.collect()


