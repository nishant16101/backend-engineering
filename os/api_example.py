import threading
import time

def api(name):
    print(name,"started")
    time.sleep(2)
    print(name,"finished")

threads = []
start = time.time()

for i in range(5):
    t = threading.Thread(
        target=api,args=(f"API{i+1}",)
    )
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Time:",time.time()-start)