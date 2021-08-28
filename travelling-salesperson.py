#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=1:
#   }}}1
import sys
import math
import itertools
import time
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
#   {{{2

#   TODO: 2021-08-27T17:39:54AEST _algorithms, traveling-salesperson, genetic, greedy, integerLinearProgram, and simulatedAnnealing implementations
def traveling_salesperson_genetic(graph_adjacencies):
    pass
def traveling_salesperson_greedy(graph_adjacencies):
    pass
def traveling_salesperson_integerLinearProgram(graph_adjacencies):
    pass
def traveling_salesperson_simulatedAnnealing(graph_adjacencies):
    pass

def array_print(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print("%10s" % str(a[i][j])[0:9], end="")
            if j != len(a[0])-1:
                print(",", end="")
        print("")

def node_distance(coords, i, j):
    result = math.sqrt( (coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2 )
    return result

def coords_to_distances(coords):
    distances = [ [ node_distance(coords, i, j) for j in range(len(coords)) ] for i in range(len(coords)) ]
    return distances

def graph_route_cost(graph_adjacencies, route):
    assert( len(graph_adjacencies) == len(graph_adjacencies[0]) )
    result = 0
    for i in range(1, len(route)):
        cost = graph_adjacencies[route[i]][route[i-1]]
        result += cost
    return result


def traveling_salesperson_bruteforce(graph_adjacencies):
    """Traveling salesperson solution - trying every possible combination of routes beginning/ending at node 0"""
    assert( len(graph_adjacencies) == len(graph_adjacencies[0]) )

    result_cost = math.inf
    result = None

    start = 0
    permutations = itertools.permutations(range(1,len(graph_adjacencies)))

    for loop_permutation in permutations:
        loop_route = [ start ] + list(loop_permutation) + [ start ]
        loop_cost = graph_route_cost(graph_adjacencies, loop_route)
        if loop_cost < result_cost:
            result = loop_route
            result_cost = loop_cost

    return result, result_cost


def traveling_salesperson_backtracking(graph_adjacencies, route=None, position=0, cost=0):
    """Traveling salesperson problem - backtracking breadth-first search of routes beginning/ending at node 0"""
    assert( len(graph_adjacencies) == len(graph_adjacencies[0]) )

    if route is None:
        route = [0]

    result_cost = math.inf
    result = None

    #   If every node has been visited, and start node '0' is accessible, return (route, cost) of returning as possible solution
    if (len(route) == len(graph_adjacencies) and graph_adjacencies[position][0]):
        return route+[0], cost+graph_adjacencies[position][0]

    #   Perform backtracking for each node accessible from the current node
    for i in range(len(graph_adjacencies)):
        if not i in route and graph_adjacencies[position][i] > 0:
            trial_route, trial_cost = traveling_salesperson_backtracking(graph_adjacencies, route+[i], i, cost+graph_adjacencies[position][i])
            if trial_cost < result_cost:
                result_cost = trial_cost
                result = trial_route

    return result, result_cost


def traveling_salesperson_dynamic(graph_adjacencies):
    """Traveling salesperson problem - dynamic programming search of routes beginning/ending at node 0"""
    assert( len(graph_adjacencies) == len(graph_adjacencies[0]) )

    #   C[k][j]:    shortest path beginning at 0, visiting all nodes in S for k(S), and ending at j
    C = [ [math.inf for y in range(len(graph_adjacencies))] for x in range(2**len(graph_adjacencies)) ]
    C[1][0] = 0

    #   P[k][j]:    previous node from j <after visiting all nodes in S for k(S)?>
    P = [ [None for y in range(len(graph_adjacencies))] for x in range(2**len(graph_adjacencies)) ]

    #   k describes nodes included in S, k(S) = sum([ 2**i for i in S ])

    #   Fill arrays 'C', 'P'
    for size in range(1, len(graph_adjacencies)):
        for S in itertools.combinations(range(1, len(graph_adjacencies)), size):
            S = (0,) + S
            k = sum([ 2**i for i in S ])
            for i in S:
                if i == 0:
                    continue
                for j in S:
                    if i == j:
                        continue
                    trial_C = C[k^(2**i)][j] + graph_adjacencies[j][i]
                    if trial_C < C[k][i]:
                        C[k][i] = trial_C
                        #result.append(j)
                        P[k][i] = j

    #   determine optimal route cost, and last point in route before returning to 0
    result_cost, result_index = min( [ ( C[-1][i] + graph_adjacencies[0][i], i ) for i in range(len(graph_adjacencies)) ] )

    #   trace optimal path as 'result'
    result = [0]
    #   Ongoing: 2021-08-28T14:10:27AEST note that 'k' is 1 greater than initial 'bits' as used in ans
    k = (2**len(graph_adjacencies) - 1)
    #   iterate for number of nodes visited, minus start/end
    for i in range(len(graph_adjacencies)-1):
        result.append(result_index)
        #   update k(S) to remove 'result_index' from S
        new_k = k & ~(2**result_index)
        result_index = P[k][result_index]
        k = new_k
    result.append(0)
    result = result[::-1]

    #   Check route 'result' has cost 'result_cost'
    assert( graph_route_cost(graph_adjacencies, result) == result_cost )

    return result, result_cost


#   LINK: https://github.com/hiteshsapkota/Optimal-Path-Detection/blob/master/travelling_salesman.py
def ans_traveling_salesperson_dynamic(dists):
#   {{{
    """
    Implementation of Held-Karp, an algorithm that solves the Traveling
    Salesman Problem using dynamic programming with memorization.
    Parameters:
        dists: distance matrix
    Returns:
        A tuple, (cost, path).
    """
    n = len(dists)
    # Maps each subset of the nodes to the cost to reach that subset, as well
    # as what node it passed before reaching this subset.
    # Node subsets are represented as set bits.
    C = {}
    # Set transition cost from initial state
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)
    # Iterate subsets of increasing length and store intermediate results
    # in classic dynamic programming manner
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            # Set bits for all nodes in this subset
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            # Find the lowest cost to get to this subset
            for k in subset:
                prev = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)
    #print(C)
    # We're interested in all bits but the least significant (the start state)
    bits = (2**n - 1) - 1
    # Calculate optimal cost
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)
    # Backtrack to find full path
    path = [0]
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits
    # Add implicit start state
    path.append(0)
    path = list(reversed(path))
    return path, opt
#   }}}


coords = [(1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 3)]
#coords = [(1, 1), (4, 2), (5, 2), (6, 4), (4, 4), (3, 6), (1, 5), (2, 9)]
distances = coords_to_distances(coords)

time_start = time.time()
result, result_cost  = traveling_salesperson_bruteforce(distances)
time_end = time.time()
time_elapsed = time_end - time_start
print("traveling_salesperson_bruteforce:")
print("result=(%s)" % str(result))
print("result_cost=(%s)" % str(result_cost))
print("time_elapsed=(%s)" % str(time_elapsed))
print()

time_start = time.time()
result, result_cost  = traveling_salesperson_backtracking(distances)
time_end = time.time()
time_elapsed = time_end - time_start
print("traveling_salesperson_backtracking:")
print("result=(%s)" % str(result))
print("result_cost=(%s)" % str(result_cost))
print("time_elapsed=(%s)" % str(time_elapsed))
print()


time_start = time.time()
result, result_cost  = traveling_salesperson_dynamic(distances)
time_end = time.time()
time_elapsed = time_end - time_start
print("traveling_salesperson_dynamic:")
print("result=(%s)" % str(result))
print("result_cost=(%s)" % str(result_cost))
print("time_elapsed=(%s)" % str(time_elapsed))
print()


