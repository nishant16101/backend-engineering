import threading
import time

semaphore = threading.Semaphore(3)

def worker(number):
    with semaphore:
        print(f"Woker {number} entered")
        time.sleep(2)
        print(f"Worker {number} leaving")

threads = []
for i in range(6):
    t = threading.Thread(
        target=worker,
        args=(i,)
    )
    threads.append(t)
    t.start()

for t in threads:
    t.join()