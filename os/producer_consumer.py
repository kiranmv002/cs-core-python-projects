# Producer Consumer Problem
# Day 36 - Operating Systems Project

BUFFER_SIZE = 5
buffer = []


def produce():

    if len(buffer) == BUFFER_SIZE:
        print("Buffer is Full!")
        return

    item = input("Enter item to produce: ")

    buffer.append(item)

    print(item, "produced successfully.")


def consume():

    if len(buffer) == 0:
        print("Buffer is Empty!")
        return

    item = buffer.pop(0)

    print(item, "consumed successfully.")


def display():

    print("\nCurrent Buffer:")

    if len(buffer) == 0:
        print("Empty")

    else:
        for item in buffer:
            print(item)


while True:

    print("\n--- Producer Consumer Menu ---")
    print("1. Produce")
    print("2. Consume")
    print("3. Display Buffer")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        produce()

    elif choice == "2":

        consume()

    elif choice == "3":

        display()

    elif choice == "4":

        print("Exiting...")
        break

    else:

        print("Invalid choice!")
