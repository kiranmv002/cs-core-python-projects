# Singly Linked List Implementation
# Day 13 - Data Structures Project


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Display list
    def display(self):
        if self.head is None:
            print("Linked List is empty!")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Search element
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                print("Element found!")
                return
            temp = temp.next
        print("Element not found!")

    # Delete element
    def delete(self, key):
        temp = self.head
        prev = None

        if temp and temp.data == key:
            self.head = temp.next
            print("Element deleted!")
            return

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Element not found!")
            return

        prev.next = temp.next
        print("Element deleted!")


def main():
    ll = LinkedList()

    while True:
        print("\n--- Singly Linked List ---")
        print("1. Insert")
        print("2. Display")
        print("3. Search")
        print("4. Delete")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            value = input("Enter value to insert: ")
            ll.insert(value)

        elif choice == "2":
            ll.display()

        elif choice == "3":
            value = input("Enter value to search: ")
            ll.search(value)

        elif choice == "4":
            value = input("Enter value to delete: ")
            ll.delete(value)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
