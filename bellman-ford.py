import sys
import math
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class Graph(object):
    def __init__(self, num_verticies):
        self.verticies = list(range(num_verticies))
        self.edges = []
    def addEdge(self, start, end, weight):
        edge = (start, end, weight)
        self.edges.append(edge)


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


def bellman_ford(graph, source):
    """Determine the shortest distance from vertex 'source' to all other verticies"""

    #   distances[i]:   distance from verticies 'source' to 'i'
    distances = [ math.inf for x in graph.verticies ]
    distances[source] = 0

    #   predecessors[i]: from where do we depart to arive at vertex 'i' when starting from 'source'
    predecessors = [ None for x in graph.verticies ]

    #   len(verticies)-1 times:
    for x in range(len(graph.verticies)-1):

        #   Determine shortest route to 'end' for each edge that has already been visited
        for start, end, weight in graph.edges:
            if distances[start] != math.inf and distances[start] + weight < distances[end]:
                distances[end] = distances[start] + weight
                predecessors[end] = start

    #   Check for negative weight cycles
    for start, end, weight in graph.edges:
        if distances[start] != math.inf and distances[start] + weight < distances[end]:
            logging.warning("Graph contains negative weight cycle")
            return None

    return distances, predecessors


#   Unlike Dijkstra, Bellman-Ford can handle negative edge weights
g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

source = 0
distances, predecessors = bellman_ford(g, source)
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
distances, predecessors = bellman_ford(g, source)
routes = [ trace_route(g, predecessors, source, end) for end in range(len(g.verticies)) ]
print("source=(%s), distances=(%s), predecessors=(%s)" % (source, distances, predecessors))
print("routes=(%s)" % str(routes))
print()

