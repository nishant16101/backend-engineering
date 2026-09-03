from collections import deque
processes = [
    ["P1", 5],
    ["P2", 3],
    ["P3", 1]
]
quantum =2
queue = deque(processes)
time = 0

while queue:
    name,remaining = queue.popleft()
    execution = min(quantum,remaining)
    print(f"{name}:{time}->{time+execution}")

    time += execution
    remaining -= execution

    if remaining >0:
        queue.append((name,remaining))

