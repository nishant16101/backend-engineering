processes = [
    ("P1", 8),
    ("P2", 4),
    ("P3", 2),
    ("P4", 6)
]
processes.sort(key=lambda x:x[1])
current_time = 0
total_waiting = 0
for name,burst in processes:
    waiting = current_time
    current_time += burst
    total_waiting += waiting

    print(name,"Waiting",waiting)
print("average waiting",total_waiting/len(processes))