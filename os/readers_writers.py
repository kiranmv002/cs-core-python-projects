# Readers-Writers Problem
# Day 38 - Operating Systems Project

readers = 0
data = "No data"


def read_data():

    global readers

    readers += 1

    print("\nReader entered.")
    print("Data:", data)

    readers -= 1

    print("Reader left.")


def write_data():

    global data

    if readers > 0:
        print("\nWriter cannot write while readers are reading.")
        return

    new_data = input("Enter new data: ")

    data = new_data

    print("Data written successfully.")
