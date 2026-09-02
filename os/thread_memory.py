import threading
counter = 0

def worker():
    global counter
    counter = 100
    print("Before",counter)

thread = threading.Thread(target=worker)
thread.start()
thread.join()

print("Main counter",counter)