import sys
import math

def print_table(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print("%4s" % str(a[i][j])[0:3], end="")
            if (j != len(a[0])-1):
                print(", ", end="")
        print("")


def chosen_items(B, value, weight):
    """Given results matrix 'B' from knapsack_dynamic, determine which items were selected"""
    i = len(B)-1
    j = len(B[0])-1
    chosen_items = []
    while (i > 1 and j > 1):
        print("i=(%d), j=(%d), B=(%d)" % (i, j, B[i][j]))
        if B[i][j] != B[i-1][j]:
            loop_item = { 'value': value[i-1], 'weight': weight[i-1], 'index': i }
            chosen_items.append(loop_item)
            j -= weight[i-1]
        i -= 1
    return chosen_items


#   Note that list value/weight are 1-indexed
def knapsack_dynamic(value, weight, capacity):
    """1/0 selection knapsack problem implemented with dynamic programming"""

    #   require value/weight to have same length
    assert(len(value) == len(weight))

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


#   TODO: 2021-08-26T18:17:11AEST algorithms, knapsack, Fractional selection
#   TODO: 2021-08-26T18:16:57AEST algorithms, knapsack, 1/0 selection (with replacement)


capacity = 10
value = [ 10, 40, 30, 50 ]
weight = [ 5, 4, 6, 3 ]

#capacity = 7
#value = [ 1, 4, 5, 7 ]
#weight = [ 1, 3, 4, 5 ] 

result = knapsack_dynamic(value, weight, capacity)
print("knapsack: value=(%s), weight=(%s)" % (str(value), str(weight)))
print_table(result)

chosen_items = chosen_items(result, value, weight)
print("chosen_items=(%s)" % str(chosen_items))

