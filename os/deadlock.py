import threading
lock = threading.Lock()

def outer():
    with lock:
        inner()

def inner():
    with lock:
        print("Hello")


outer()