# Priority Queue using Heap
# Day 28 - Data Structures Project

import heapq

# create empty heap
priority_queue = []


while True:

    print("\n--- Priority Queue Menu ---")
    print("1. Insert Element")
    print("2. Remove Highest Priority")
    print("3. Display Queue")
    print("4. Exit")

    choice = input("Enter choice: ")

    # insert
    if choice == "1":

        value = int(input("Enter number: "))

        heapq.heappush(priority_queue, value)

        print("Element inserted")

