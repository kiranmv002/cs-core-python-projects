# Stack and Queue Simulator
# Day 12 - Data Structures Project


# ---------------- STACK ----------------
def stack_operations():
    stack = []

    while True:
        print("\n--- Stack Operations ---")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            value = input("Enter value to push: ")
            stack.append(value)
            print("Value pushed successfully!")

        elif choice == "2":
            if stack:
                print("Popped value:", stack.pop())
            else:
                print("Stack is empty!")

        elif choice == "3":
            print("Stack:", stack)

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


# ---------------- QUEUE ----------------
def queue_operations():
    queue = []

    while True:
        print("\n--- Queue Operations ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            value = input("Enter value to enqueue: ")
            queue.append(value)
            print("Value added to queue!")

        elif choice == "2":
            if queue:
                print("Dequeued value:", queue.pop(0))
            else:
                print("Queue is empty!")

        elif choice == "3":
            print("Queue:", queue)

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n--- Stack & Queue Simulator ---")
        print("1. Stack")
        print("2. Queue")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            stack_operations()
        elif choice == "2":
            queue_operations()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")



if __name__ == "__main__":
    main()
