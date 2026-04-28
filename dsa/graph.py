# Graph Implementation using Adjacency List
# Day 23 - Data Structures Project

from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    # Add edge
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)   # remove this if directed

    # Display graph
    def display(self):
        print("\nGraph:")
        for node in self.graph:
            print(node, "->", self.graph[node])

    # BFS
    def bfs(self, start):
        visited = set()
        queue = deque([start])

        print("\nBFS Traversal:")

        while queue:
            node = queue.popleft()

            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                for neighbour in self.graph[node]:
                    if neighbour not in visited:
                        queue.append(neighbour)

        print()

    # DFS
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        print(start, end=" ")
        visited.add(start)

        for neighbour in self.graph[start]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)


# -------- MAIN --------

g = Graph()

while True:
    print("\n--- Graph Menu ---")
    print("1. Add Edge")
    print("2. Display Graph")
    print("3. BFS")
    print("4. DFS")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        u = input("Enter node u: ")
        v = input("Enter node v: ")
        g.add_edge(u, v)

    elif ch == "2":
        g.display()

    elif ch == "3":
        start = input("Enter start node: ")
        g.bfs(start)

    elif ch == "4":
        start = input("Enter start node: ")
        print("\nDFS Traversal:")
        g.dfs(start)
        print()

    elif ch == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
