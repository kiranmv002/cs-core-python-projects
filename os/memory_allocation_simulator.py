# Memory Allocation Simulator
# Day 17 - Operating Systems Project

def first_fit(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break

    return allocation


def best_fit(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        best_index = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if best_index == -1 or blocks[j] < blocks[best_index]:
                    best_index = j

        if best_index != -1:
            allocation[i] = best_index
            blocks[best_index] -= processes[i]

    return allocation


def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        worst_index = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if worst_index == -1 or blocks[j] > blocks[worst_index]:
                    worst_index = j

        if worst_index != -1:
            allocation[i] = worst_index
            blocks[worst_index] -= processes[i]

    return allocation


def print_result(processes, allocation):
    print("\nProcess No.\tProcess Size\tBlock No.")
    for i in range(len(processes)):
        if allocation[i] != -1:
            print(f"{i+1}\t\t{processes[i]}\t\t{allocation[i]+1}")
        else:
            print(f"{i+1}\t\t{processes[i]}\t\tNot Allocated")


def main():
    blocks = list(map(int, input("Enter memory block sizes (space separated): ").split()))
    processes = list(map(int, input("Enter process sizes (space separated): ").split()))

    print("\nChoose Allocation Strategy:")
    print("1. First Fit")
    print("2. Best Fit")
    print("3. Worst Fit")

    choice = input("Enter choice: ")

    if choice == "1":
        allocation = first_fit(blocks.copy(), processes)
        print_result(processes, allocation)

    elif choice == "2":
        allocation = best_fit(blocks.copy(), processes)
        print_result(processes, allocation)

    elif choice == "3":
        allocation = worst_fit(blocks.copy(), processes)
        print_result(processes, allocation)

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
