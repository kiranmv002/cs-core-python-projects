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

