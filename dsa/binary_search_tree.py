# Binary Search Tree Implementation
# Day 15 - Data Structures Project


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert node
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    # Inorder Traversal
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    # Search node
    def search(self, node, key):
        if node is None:
            print("Value not found!")
            return

        if node.value == key:
            print("Value found!")
        elif key < node.value:
            self.search(node.left, key)
        else:
            self.search(node.right, key)


def main():
    bst = BinarySearchTree()

    while True:
        print("\n--- Binary Search Tree ---")
        print("1. Insert")
        print("2. Display (Inorder)")
        print("3. Search")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            value = int(input("Enter value to insert: "))
            bst.insert(value)

        elif choice == "2":
            print("Inorder Traversal:")
            bst.inorder(bst.root)
            print()

        elif choice == "3":
            value = int(input("Enter value to search: "))
            bst.search(bst.root, value)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
