# CPU Scheduling Simulator
# Algorithms: FCFS, SJF, Round Robin

def fcfs(processes):
    wt = [0] * len(processes)
    tat = [0] * len(processes)

    for i in range(1, len(processes)):
        wt[i] = wt[i - 1] + processes[i - 1]

    for i in range(len(processes)):
        tat[i] = wt[i] + processes[i]

    print_results("FCFS", wt, tat)


def sjf(processes):
    processes.sort()
    wt = [0] * len(processes)
    tat = [0] * len(processes)

    for i in range(1, len(processes)):
        wt[i] = wt[i - 1] + processes[i - 1]

    for i in range(len(processes)):
        tat[i] = wt[i] + processes[i]

    print_results("SJF", wt, tat)


def round_robin(processes, quantum):
    rem_bt = processes[:]
    wt = [0] * len(processes)
    t = 0

    while True:
        done = True
        for i in range(len(processes)):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - processes[i]
                    rem_bt[i] = 0
        if done:
            break

    tat = [processes[i] + wt[i] for i in range(len(processes))]
    print_results("Round Robin", wt, tat)


def print_results(algo, wt, tat):
    print(f"\n--- {algo} Scheduling ---")
    print("Process\tWaiting Time\tTurnaround Time")
    for i in range(len(wt)):
        print(f"P{i+1}\t\t{wt[i]}\t\t{tat[i]}")

    print("Average Waiting Time:", sum(wt) / len(wt))
    print("Average Turnaround Time:", sum(tat) / len(tat))


def main():
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        bt = int(input(f"Enter burst time for P{i+1}: "))
        processes.append(bt)

    print("\n1. FCFS\n2. SJF\n3. Round Robin")
    choice = int(input("Choose scheduling algorithm: "))

    if choice == 1:
        fcfs(processes)
    elif choice == 2:
        sjf(processes)
    elif choice == 3:
        quantum = int(input("Enter time quantum: "))
        round_robin(processes, quantum)
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
