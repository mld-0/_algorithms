import sys
import math
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

#   Dijkstra uses an adjacency matrix
class Graph(object):
    def __init__(self, num_verticies):
        self.verticies = list(range(num_verticies))
        self.adjacency = [ [0 for col in self.verticies] for row in self.verticies ]
    def addEdge(self, start, end, weight):
        self.adjacency[start][end] = weight


#   Same as used in bellman-ford
def trace_route(graph, predecessors, start, end):
    """Given 'predecessors' array, determine path found from 'end' to 'start'"""
    if start == end:
        return [start]
    if predecessors[end] is None:
        return None
    result = [end]
    while predecessors[end] != start:
        end = predecessors[end]
        result.append(end)
    result.append(start)
    return result[::-1]


def dijkstra(graph, source):
    """Determine the shortest distance from vertex 'source' to all other verticies"""

    #   distances[i]:   distance from verticies 'source' to 'i'
    distances = [ math.inf for x in graph.verticies ]
    distances[source] = 0

    #   predecessors[i]: from where do we depart to arive at vertex 'i' when starting from 'source'
    predecessors = [ None for x in graph.verticies ]

    #   At each stage, we search for vertex 'x' in 'Q' that gives mininum 'distances[x]'
    Q = [ x for x in graph.verticies ]
    while len(Q) > 0:
        _, start = min([ (distances[x], x) for x in Q ])
        Q.remove(start)

        #   Determine shortest route to each 'end' from 'start'
        for end in graph.verticies:
            if graph.adjacency[start][end] > 0 and distances[start] + graph.adjacency[start][end] < distances[end]:
                distances[end] = distances[start] + graph.adjacency[start][end]
                predecessors[end] = start

    return distances, predecessors


#   Dijkstra cannot handle negative index weights
g = Graph(9)
g.adjacency = [ [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0],
];

source = 0
distances, predecessors = dijkstra(g, source)
routes = [ trace_route(g, predecessors, source, end) for end in range(len(g.verticies)) ]
print("source=(%s), distances=(%s), predecessors=(%s)" % (source, distances, predecessors))
print("routes=(%s)" % str(routes))
print()


g = Graph(5)
g.addEdge(0, 1, 9)
g.addEdge(0, 2, 3)
g.addEdge(1, 4, 2)
g.addEdge(1, 2, 6)
g.addEdge(2, 1, 2)
g.addEdge(2, 3, 1)
g.addEdge(3, 2, 2)
g.addEdge(3, 4, 2)

source = 0
distances, predecessors = dijkstra(g, source)
routes = [ trace_route(g, predecessors, source, end) for end in range(len(g.verticies)) ]
print("source=(%s), distances=(%s), predecessors=(%s)" % (source, distances, predecessors))
print("routes=(%s)" % str(routes))
print()

