# CPU Scheduling Simulator
# Day 6 Upgrade: Added Round Robin


def calculate_fcfs(burst_times):
    n = len(burst_times)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_times[i - 1]

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_times[i]

    print_results("FCFS", burst_times, waiting_time, turnaround_time)


def calculate_sjf(burst_times):
    sorted_bt = sorted(burst_times)
    n = len(sorted_bt)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + sorted_bt[i - 1]

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + sorted_bt[i]

    print_results("SJF", sorted_bt, waiting_time, turnaround_time)


def calculate_round_robin(burst_times, quantum):
    n = len(burst_times)
    remaining = burst_times[:]
    waiting_time = [0] * n
    time = 0

    while True:
        done = True
        for i in range(n):
            if remaining[i] > 0:
                done = False
                if remaining[i] > quantum:
                    time += quantum
                    remaining[i] -= quantum
                else:
                    time += remaining[i]
                    waiting_time[i] = time - burst_times[i]
                    remaining[i] = 0
        if done:
            break

    turnaround_time = [burst_times[i] + waiting_time[i] for i in range(n)]

    print_results("Round Robin", burst_times, waiting_time, turnaround_time)


def print_results(algo, burst_times, waiting_time, turnaround_time):
    print(f"\n--- {algo} Scheduling ---")
    print("Process\tBurst\tWaiting\tTurnaround")

    for i in range(len(burst_times)):
        print(f"P{i+1}\t{burst_times[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

    avg_wait = sum(waiting_time) / len(waiting_time)
    print(f"\nAverage Waiting Time: {avg_wait:.2f}")


def main():
    n = int(input("Enter number of processes: "))
    burst_times = []

    for i in range(n):
        bt = int(input(f"Enter burst time for P{i+1}: "))
        burst_times.append(bt)

    print("\nChoose Scheduling Algorithm:")
    print("1. FCFS")
    print("2. SJF")
    print("3. Round Robin")

    choice = int(input("Enter choice: "))

    if choice == 1:
        calculate_fcfs(burst_times)
    elif choice == 2:
        calculate_sjf(burst_times)
    elif choice == 3:
        quantum = int(input("Enter time quantum: "))
        calculate_round_robin(burst_times, quantum)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
