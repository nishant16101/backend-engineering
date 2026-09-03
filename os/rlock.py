# rlock - reentrant lock -- same thread can acquire multiple times
import threading
lock = threading.RLock()

def outer():
    with lock:
        print("print outer")
        inner()

def inner():
    with lock:
        print("inner")

outer()