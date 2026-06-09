# Disk Scheduling Simulator
# Day 33 - Operating Systems Project


def fcfs(requests, head):

    total_seek = 0
    current = head

    print("\nFCFS Order:")

    for request in requests:

        print(request, end=" ")

        total_seek += abs(current - request)

        current = request

    print("\nTotal Seek Time:", total_seek)


def sstf(requests, head):

    total_seek = 0
    current = head

    pending = requests.copy()

    print("\nSSTF Order:")

    while pending:

        nearest = min(pending, key=lambda x: abs(x - current))

        print(nearest, end=" ")

        total_seek += abs(current - nearest)

        current = nearest

        pending.remove(nearest)

    print("\nTotal Seek Time:", total_seek)


# -------- MAIN --------

requests = list(map(int, input("Enter disk requests: ").split()))

head = int(input("Enter initial head position: "))

while True:

    print("\n--- Disk Scheduling ---")
    print("1. FCFS")
    print("2. SSTF")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        fcfs(requests, head)

    elif choice == "2":

        sstf(requests, head)

    elif choice == "3":

        print("Exiting...")
        break

    else:

        print("Invalid choice!")
