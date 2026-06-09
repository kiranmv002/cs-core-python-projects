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


        print("Invalid choice!")
