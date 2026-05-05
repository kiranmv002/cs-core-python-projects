# Hash Table Implementation
# Day 25 - Data Structures Project

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function
    def hash_function(self, key):
        return key % self.size

    # Insert key-value
    def insert(self, key, value):
        index = self.hash_function(key)

        # check if key exists
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print("Key updated")
                return

        self.table[index].append([key, value])
        print("Key inserted")

    # Search
    def search(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                print(f"Value: {pair[1]}")
                return

        print("Key not found")

    # Delete
    def delete(self, key):
        index = self.hash_function(key)

        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                print("Key deleted")
                return

        print("Key not found")

    # Display
    def display(self):
        print("\nHash Table:")
        for i, bucket in enumerate(self.table):
            print(i, ":", bucket)


# -------- MAIN --------

size = int(input("Enter size of hash table: "))
ht = HashTable(size)

while True:
    print("\n--- Hash Table Menu ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        key = int(input("Enter key (number): "))
        value = input("Enter value: ")
        ht.insert(key, value)

    elif ch == "2":
        key = int(input("Enter key to search: "))
        ht.search(key)

    elif ch == "3":
        key = int(input("Enter key to delete: "))
        ht.delete(key)

    elif ch == "4":
        ht.display()

    elif ch == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
