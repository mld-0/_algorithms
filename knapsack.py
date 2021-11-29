import sys
import math
import pprint


#   Note that list value/weight are 1-indexed
def knapsack_dynamic(value, weight, capacity):
    """1/0 selection knapsack problem implemented with dynamic programming"""

    #   require value/weight to have same length
    assert len(value) == len(weight)

    #   n:  number of items
    n = len(value)

    #   B[i][j]:    maximum possible value selecting from items [1,2,...,i]  with weight limit j
    B = [ [ None ] * (capacity+1) for x in range(0, n+1) ]

    #   i=0, no items to select from
    for j in range(0, capacity+1):
        B[0][j] = 0

    #   j=0, no weight capacity
    for i in range(0, n+1):
        B[i][0] = 0

    for i in range(1, n+1):
        for j in range(1, capacity+1):
            trial_a = -math.inf
            trial_b = B[i-1][j]

            # if the current item i fits in capacity j
            if weight[i-1] <= j:  
                trial_a = value[i-1] + B[i-1][j-weight[i-1]]

            B[i][j] = max(trial_a, trial_b)

    return B


def unbound_knapsack_dynamic_i(value, weight, capacity):
    """1/0 selection knapsack problem with replacement"""
    assert len(value) == len(weight)

    n = len(value)

    table = [ 0 for i in range(capacity+1) ]

    for i in range(capacity+1):
        for j in range(n):
            if weight[j] <= i:
                table[i] = max(table[i], table[i-weight[j]] + value[j])

    return table


def unbound_knapsack_dynamic_ii(value, weight, capacity):
    """1/0 selection knapsack problem with replacement"""
    assert len(value) == len(weight)
    n = len(value)
    if capacity <= 0 or n == 0:
        return 0

    table = [ [ None for _ in range(capacity+1) ] for _ in range(n) ]

    for i in range(n):
        table[i][0] = 0

    for i in range(n):
        for c in range(1, capacity+1):
            trial1, trial2 = 0, 0
            if weight[i] <= c:
                trial1 = value[i] + table[i][c-weight[i]]
            if i > 0:
                trial2 = table[i-1][c]
            table[i][c] = max(trial1, trial2)

    return table


def get_chosen_items_knapsack_dynamic(B, value, weight):
    """Given results matrix 'B' from knapsack_dynamic, determine which items were selected"""
    i = len(B)-1
    j = len(B[0])-1
    chosen_items = []
    while (i > 1 and j > 1):
        #print("i=(%d), j=(%d), B=(%d)" % (i, j, B[i][j]))
        if B[i][j] != B[i-1][j]:
            loop_item = { 'value': value[i-1], 'weight': weight[i-1], 'index': i }
            chosen_items.append(loop_item)
            j -= weight[i-1]
        i -= 1
    return chosen_items


def get_chosen_items_unbound_knapsack_ii(table, values, weights, capacity):
    """Given results matrix 'table' from unbound_knapsack_dynamic_ii, determine which items were selected"""
    chosen_items = []
    n = len(weights)
    i = n - 1
    while i >= 0 and capacity >= 0:
        if i > 0 and table[i][capacity] != table[i - 1][capacity]:
            # include this item
            loop_item = { 'value': value[i], 'weight': weight[i], 'index': i }
            chosen_items.append(loop_item)
            capacity -= weights[i]
        elif i == 0 and capacity >= weights[i]:
            # include this item
            loop_item = { 'value': value[i], 'weight': weight[i], 'index': i }
            chosen_items.append(loop_item)
            capacity -= weights[i]
        else:
            i -= 1
    return chosen_items



#   TODO: 2021-08-26T18:17:11AEST algorithms, knapsack, Fractional selection (greedy?)

input_values = [ ([10,40,30,50], [5,4,6,3], 10), ([1,4,5,7], [1,3,4,5], 7), ]

print("1/0 selection, no replacement")
input_checks = [ 90, 9, ]
for (value, weight, capacity), check in zip(input_values, input_checks):
    print("knapsack: value=(%s), weight=(%s)" % (str(value), str(weight)))
    result = knapsack_dynamic(value, weight, capacity)
    print("table:")
    pprint.pprint(result)
    assert result[-1][-1] == check, "Check comparison failed"
    chosen_items = get_chosen_items_knapsack_dynamic(result, value, weight)
    print("chosen_items=(%s)" % str(chosen_items))
    print()
print()


print("1/0 selection with replacement")
input_checks = [ None, None, ]
for (value, weight, capacity), check in zip(input_values, input_checks):
    print("knapsack: value=(%s), weight=(%s), capacity=(%s)" % (str(value), str(weight), str(capacity)))
    result = unbound_knapsack_dynamic_ii(value, weight, capacity)
    print("table:")
    pprint.pprint(result)
    chosen_items = get_chosen_items_unbound_knapsack_ii(result, value, weight, capacity)
    print("chosen_items=(%s)" % str(chosen_items))
    print()
print()

