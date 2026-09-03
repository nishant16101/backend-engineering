#producer consumer problem
import threading
import time

condition = threading.Condition()

items = []
def consumer():
    with condition:
        while not items:
            print("consumer waiting")
            condition.wait()
        item = items.pop()
        print("consumer got",item)

def producer():
    time.sleep(2)
    with condition:
        items.append('Apple')
        print("Producer produced")
        condition.notify()

t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)

t1.start()
t2.start()

t1.join()
t2.join()