# Dijkstra’s shortest path algorithm using Greedy Algo
"""
https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

Given a graph and a source vertex in the graph, find 
the shortest paths from the source to all vertices in 
the given graph.

Dijkstra’s algorithm is very similar to Prim’s 
algorithm for minimum spanning tree.
"""
import sys


class Graph:
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)]
                      for _ in range(vertices)]

    def minimum_distance(self, dist, spt_set):
        min_ = sys.maxsize
        for node in range(self.vertices):
            if dist[node] < min_ and not spt_set[node]:
                min_ = dist[node]
                min_index = node
        return min_index

    def dijkstra(self, source):
        spt_set = [False] * self.vertices
        distances = [sys.maxsize] * self.vertices
        distances[source] = 0
        for count in range(self.vertices):
            x = self.minimum_distance(distances, spt_set)
            spt_set[x] = True
            # Update the distance of the adjacent
            # vertices (i.e. self.graph[x][y] > 0)of 
            # the picked vertex only if
            # the current distance is greater than 
            # new distance and the vertex is not in
            # shortest path tree
            for y in range(self.vertices):
                if self.graph[x][y] > 0 and not spt_set[y] and distances[y] > distances[x] + self.graph[x][y]:
                    distances[y] = distances[x] + self.graph[x][y]

        self.print_solution(distances)

    def print_solution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.vertices):
            print(node, "\t", dist[node])


# Driver program
g = Graph(9)
g.graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
];
 
g.dijkstra(0);