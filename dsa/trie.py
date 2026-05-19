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
