#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
import math
#   {{{2

#   TODO: 2021-09-30T20:22:47AEST _algorithms, dynamic-programming overview/compilation
#   (Also) See: (_leetcode)
#       198-house-robber
#       120-triangle
#       <...>

#   Dynamic Programming: storing the solutions to the subproblems of a problem to find the overall solution
#   Either top-down (recursive memoization) or bottom-up (iterative table filling)
#   <...>


def pascals_triangle(numRows: int) -> List[List[int]]:
    """Create Pascal's Triangle for a given height"""
    result = [ [ None for col in range(row+1) ] for row in range(numRows) ]
    result[0][0] = 1

    for row in range(1, numRows):
        result[row][0] = 1
        result[row][-1] = 1

    for row in range(1, numRows):
        for col in range(1, row):
            result[row][col] = result[row-1][col-1] + result[row-1][col]

    return result


def minFallingPathSum_TopDown(matrix: List[List[int]]) -> int:
    """Lowest cost path from top->bottom through a table of numbers"""
    memoized = {}

    def min_path(row, col):
        """Calculate the min-falling-path starting from a given cell in the first row, with a dict used to memoize results"""
        if (row,col) in memoized:
            return memoized[(row,col)]

        path = matrix[row][col]
        trials = [ math.inf ] * 3

        if row < len(matrix) - 1:
            if col-1 >= 0: trials[0] = min_path(row+1, col-1)
            trials[1] = min_path(row+1, col)
            if col+1 < len(matrix[row]): trials[2] = min_path(row+1, col+1)

            path += min(trials)

        memoized[(row,col)] = path
        return path

    #   solution is given by minimum of min_path() for each cell in first row
    results = []
    for col in range(len(matrix[0])):
        results.append( min_path(0, col) )
    return min(results)


def minFallingPathSum_BottomUp(matrix: List[List[int]]) -> int:
    """Lowest cost path from top->bottom through a table of numbers, Calculate the min-falling-path, iteratively with table, and rule defining cells in terms of previous row"""
    #   create 'grid' with values of 'matrix'
    grid = [ x[:] for x in matrix ]

    #   skipping first row, for each cell in subsiquent rows/columns, to which add whichever of the cells above and adjacent have the smallest value
    for row in range(1, len(matrix)):
        for col in range(len(matrix[row])):
            trials = [ math.inf ] * 3

            if col-1 >= 0: trials[0] = grid[row-1][col-1]
            trials[1] = grid[row-1][col]
            if col+1 < len(matrix[row]): trials[2] = grid[row-1][col+1]

            grid[row][col] += min(trials)

    #   solution given by:
    return min(grid[-1])


def coinChange_DP_TopDown(coins: List[int], amount: int) -> int:
    """Determine minimum number of values from 'coins' (with replacement) that sum to 'amount'"""
    memo = dict()

    def solve(remaining):
        if remaining in memo:
            return memo[remaining]

        if remaining < 0:
            memo[remaining] = -1
            return -1
        if remaining == 0:
            memo[remaining] = 0
            return 0

        minimum = math.inf
        for c in coins:
            result = solve(remaining-c)
            if result >= 0 and result < minimum:
                minimum = 1 + result

        if minimum == math.inf:
            memo[remaining] = -1
            return -1
        else:
            memo[remaining] = minimum
            return minimum

    return solve(amount)


#   runtime: beats 86%
def coinChange_DP_BottomUp(coins: List[int], amount: int) -> int:
    """Determine minimum number of values from 'coins' (with replacement) that sum to 'amount'"""
    #   table[i]: minimum number of coins that sum to amount
    table = [ math.inf for x in range(amount+1) ]
    table[0] = 0

    for c in coins:
        for x in range(c, amount+1):
            table[x] = min(table[x], table[x-c] + 1)

    if table[amount] == math.inf:
        return -1
    else:
        return table[amount]



def test_pascals_triangle():
    #   {{{
    input_values = [ 5, 1, ]
    input_checks = [ [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], [[1]], ]
    for numRows, check in zip(input_values, input_checks):
        print("numRows=(%s)" % numRows)
        result = pascals_triangle(numRows)
        print("result=(%s)" % str(result))
        assert result == check, "Check failed"
    #   }}}

def test_minFallingPathSum():
    #   {{{
    input_values = [ [[2,1,3],[6,5,4],[7,8,9]], [[-19,57],[-40,-5]], [[-48]], [[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]], [[17,82],[1,-44]], ]
    input_checks = [ 13, -59, -48, -36, -27 ]
    for matrix, check in zip(input_values, input_checks):
        print("matrix=(%s)" % str(matrix))
        result = minFallingPathSum_TopDown(matrix)
        print("result=(%s)" % str(result))
        assert result == check, "Check failed"
        result = minFallingPathSum_BottomUp(matrix)
        assert result == check, "Check failed"
    #   }}}

def test_coinChange():
    #   {{{
    test_functions = [ coinChange_DP_TopDown, coinChange_DP_BottomUp, ]
    input_values = [ ([1,2,5], 11), ([2], 3), ([1], 0), ([1], 1), ([1], 2), ]
    input_checks = [ 3, -1, 0, 1, 2, ]
    for test_func in test_functions:
        print(test_func.__name__)
        for (coins, amount), check in zip(input_values, input_checks):
            print("coins=(%s), amount=(%s)" % (coins, amount))
            result = test_func(coins, amount)
            print("result=(%s)" % result)
            assert result == check, "Check comparison failed"
        print()
    #   }}}

if __name__ == '__main__':
    #   {{{
    print("test_pascals_triangle():")
    test_pascals_triangle()
    print()
    print("test_minFallingPathSum():")
    test_minFallingPathSum()
    print()
    test_coinChange()
    #   }}}

