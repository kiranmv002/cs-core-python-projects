# Dijkstra Algorithm
# Day 26 - Data Structures Project

import sys


def dijkstra(graph, start):

    nodes = len(graph)

    visited = [False] * nodes
    distance = [sys.maxsize] * nodes

    distance[start] = 0

    for _ in range(nodes):

        min_distance = sys.maxsize
        min_index = -1

        # find minimum distance node
        for i in range(nodes):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                min_index = i

        visited[min_index] = True

        # update distances
        for j in range(nodes):

            if (graph[min_index][j] > 0 and
                not visited[j] and
                distance[j] > distance[min_index] + graph[min_index][j]):

                distance[j] = distance[min_index] + graph[min_index][j]
