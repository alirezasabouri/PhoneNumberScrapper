from datetime import datetime
from threading import Thread
import time
import requests

x = {"test": 100, "test2": {"name":"haha"}}

print(x.get("test2").get("nameX"))

exit()

list = []
list.append(1)
list.append(2)
list.append(3)

print(len(list))

exit()


def process(hashId):
    for x in range(10):
        print(f"haha {hashId} at {datetime.now()}")
        time.sleep(1)


print("starting of threads")

runningThreads = []
for x in range(10):
    t = Thread(target=process, args=[x])
    t.start()
    runningThreads.append(t)

for t in runningThreads:
    t.join()
    
print("all threads ended")