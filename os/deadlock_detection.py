# Deadlock Detection Algorithm
# Operating Systems - Day 19


def deadlock_detection(processes, resources, allocation, request, available):
    
    finish = [False] * processes

    # mark processes with no allocation as finished
    for i in range(processes):
        if sum(allocation[i]) == 0:
            finish[i] = True

    work = available.copy()

    changed = True

    while changed:
        changed = False

        for i in range(processes):
            if not finish[i]:
                
                possible = True

                for j in range(resources):
                    if request[i][j] > work[j]:
                        possible = False
                        break

                if possible:
                    for j in range(resources):
                        work[j] += allocation[i][j]

                    finish[i] = True
                    changed = True

    deadlocked = []

    for i in range(processes):
        if not finish[i]:
            deadlocked.append(i)

    if len(deadlocked) == 0:
        print("\nNo Deadlock detected.")
    else:
        print("\nDeadlock detected in processes:", deadlocked)


# -------- MAIN --------

p = int(input("Enter number of processes: "))
r = int(input("Enter number of resource types: "))

print("\nEnter Allocation Matrix")
allocation = []
for i in range(p):
    row = list(map(int, input().split()))
    allocation.append(row)

print("\nEnter Request Matrix")
request = []
for i in range(p):
    row = list(map(int, input().split()))
    request.append(row)

print("\nEnter Available Resources")
available = list(map(int, input().split()))

deadlock_detection(p, r, allocation, request, available)
