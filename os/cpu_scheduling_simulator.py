# CPU Scheduling Simulator
# Day 5 - Operating Systems Project
# Algorithms: FCFS and SJF (Non-Preemptive)

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

    choice = int(input("Enter choice: "))

    if choice == 1:
        calculate_fcfs(burst_times)
    elif choice == 2:
        calculate_sjf(burst_times)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
