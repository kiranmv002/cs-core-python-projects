# Trie Data Structure
# Day 29 - Data Structures Project


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # insert word
    def insert(self, word):

        node = self.root

        for ch in word:

            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.end_of_word = True

        print("Word inserted")

    # search word
    def search(self, word):

        node = self.root

        for ch in word:

            if ch not in node.children:
                print("Word not found")
                return

            node = node.children[ch]

        if node.end_of_word:
            print("Word found")
        else:
            print("Word not found")

    # display all words
    def display(self, node=None, word=""):

        if node is None:
            node = self.root

        if node.end_of_word:
            print(word)

        for ch in node.children:
            self.display(node.children[ch], word + ch)


# -------- MAIN --------

trie = Trie()

while True:

    print("\n--- Trie Menu ---")
    print("1. Insert Word")
    print("2. Search Word")
    print("3. Display Words")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        word = input("Enter word: ")
        trie.insert(word)

    elif choice == "2":

        word = input("Enter word to search: ")
        trie.search(word)

    elif choice == "3":

        print("\nStored Words:")
        trie.display()

    elif choice == "4":

        print("Exiting...")
        break

    else:
        print("Invalid choice!")
