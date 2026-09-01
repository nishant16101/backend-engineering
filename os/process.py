from multiprocessing import Process
import os

def worker():
    print("Worker PID",os.getpid())

if __name__ == "__main__":
    print("Main PIDs",os.getpid())
    p = Process(target=worker)
    p.start()
    p.join()