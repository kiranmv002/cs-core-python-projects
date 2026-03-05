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
