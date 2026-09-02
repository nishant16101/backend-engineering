from multiprocessing import Process
counter = 0

def worker():
    global counter
    counter = 100
    print("Child counter:",counter)

if __name__ == "__main__":
    print("Before:",counter)
    p = Process(target=worker)
    p.start()
    p.join()

    print("Parent counter",counter)

