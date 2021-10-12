#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
import itertools
from typing import List
#   {{{2

#   TODO: 2021-09-30T20:24:07AEST _algorithms, backtracking overview/compilation

#   Backtracking: (typically using call stack) building a solution incrementally, removing candidates from solution as they are deamed invalid

def generateParenthesis(n):
    result = []
    def backtrack(S=None, l=0, r=0):
        if S is None:
            S = []
        if len(S) == 2*n:
            result.append(''.join(S))
            return True
        if l < n:
            S.append("(")
            backtrack(S, l+1, r)
            S.pop()
        if r < l: 
            S.append(")")
            backtrack(S, l, r+1)
            S.pop()
    backtrack()
    return result


def n_queens_backtracking(n, queens_list=None, col=0):
    """Solve n-queens problem for a given sized board using backtracking"""
    if queens_list is None:
        queens_list = []

    if n <= col:
        return queens_list

    for row in range(n):
        loop_square = (row, col)
        queens_list.append(loop_square)
        if n_queens_valid(queens_list, n):
            if n_queens_backtracking(n, queens_list, col+1) != False:
                return queens_list
        queens_list.pop()

    return False


def n_queens_valid(queens_list, n):
    """Determine whether any of the given list of queens are under attack"""
    #   {{{
    board = n_queens_attack_board(queens_list, n, False)
    for row, col in queens_list:
        if board[row][col] > 0:
            return False
    return True
    #   }}}

def n_queens_attack_board(queens_list, n, attack_self=False):
    """Given list of queen positions, and dimensions of board, return grid with values indicating how many times each square is under attack. Square containing queen is excluded if 'attack_self' is False."""
    #   {{{
    board = [ [ 0 for col in range(n) ] for row in range(n) ]
    for row, col in queens_list:
        #   attack squares in row:
        for loop_col in range(n):
            board[row][loop_col] += 1
        #   attack squares in col:
        for loop_row in range(n):
            board[loop_row][col] += 1
        #   attack squares in diag:
        for delta_row, delta_col in zip(range(0-n+1,n,1), range(0-n+1,n,1)):
            if row+delta_row >= 0 and row+delta_row < n and col+delta_col >= 0 and col+delta_col < n:
                board[row+delta_row][col+delta_col] += 1
        for delta_row, delta_col in zip(range(n-1,0-n,-1), range(0-n+1,n,1)):
            if row+delta_row >= 0 and row+delta_row < n and col+delta_col >= 0 and col+delta_col < n:
                board[row+delta_row][col+delta_col] += 1
        #   We have attacked square containing queen once for each loop above, remove those attacks
        board[row][col] -= 4
        #   Optionally mark square containing queen as attacked
        if attack_self:
            board[row][col] += 1
    return board
    #   }}}


def combinations(values: List, k: int) -> List:
    result = []

    def backtrack(first=0, cur=None):
        if cur is None:
            cur = []
        #   if combination is done
        if len(cur) == k:
            result.append(cur[:])
            return
        for i in range(first, len(values)):
            cur.append(values[i])
            backtrack(i+1, cur)
            cur.pop()

    backtrack()
    return result


def permutations(values: List) -> List:
    result = []

    def permute(first=0):
        if first == len(values):
            result.append(values[:])
        for i in range(first, len(values)):
            values[first], values[i] = values[i], values[first]
            permute(first+1)
            values[first], values[i] = values[i], values[first]

    permute()
    return result


def test_generateParenthesis():
    #   {{{
    values_list = [ 3, 1 ]
    check_list = [ ["((()))","(()())","(())()","()(())","()()()"], [ "()" ] ]
    for value, check in zip(values_list, check_list):
        result = generateParenthesis(value)
        print("result=(%s)" % str(result))
        assert result == check, "Check failed"
    #   }}}
 
def test_n_queens_backtracking():
    #   {{{
    n = 8
    queens_list = n_queens_backtracking(n)
    valid = n_queens_valid(queens_list, n)
    print("queens_list=(%s)" % str(queens_list))
    assert valid == True, "Check failed"
    #   }}}

def test_combinations():
    #   {{{
    values = list(range(4))
    result = combinations(values, 3)
    check = [ list(x) for x in itertools.combinations(values, 3) ]
    print("result=(%s)" % str(result))
    assert sorted(result) == sorted(check), "Check failed"
    #   }}}

def test_permute():
    #   {{{
    values = list(range(3))
    result = permutations(values)
    check = [ list(x) for x in itertools.permutations(values) ]
    print("result=(%s)" % str(result))
    assert sorted(result) == sorted(check), "Check failed"
    #   }}}

def main():
    #   {{{
    print("test_generateParenthesis():")
    test_generateParenthesis()
    print()
    print("test_n_queens_backtracking():")
    test_n_queens_backtracking()
    print()
    print("test_combinations():")
    test_combinations()
    print()
    print("test_permute():")
    test_permute()
    print()
    #   }}}

if __name__ == '__main__':
    main()

