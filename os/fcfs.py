processes = [("p1",5),("p2",3),("p3",1),("p4",2)]

current_time = 0
total_waiting = 0

for name,burst in processes:
    waiting = current_time
    current_time += burst
    total_waiting += waiting

    print(name,"waiting=",waiting,"completion=",current_time)

print("average waiting",total_waiting/len(processes))