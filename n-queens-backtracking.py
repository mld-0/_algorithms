import pprint


def n_queens_valid(queens_list, n):
    board = n_queens_attack_board(queens_list, n, False)
    for row, col in queens_list:
        if board[row][col] > 0:
            return False

    return True

def n_queens_attack_board(queens_list, n, attack_self=False):
    board = [ [ 0 for col in range(n) ] for row in range(n) ]

    for row, col in queens_list:
        #   Ongoing: 2021-09-03T16:41:34AEST how to treat square containing queen (which currently is 'attacked' 4 times, once by each of the loops below) 
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

    

def n_queens_backtracking(n, queens_list=None, col=0):
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
    

n = 8
queens_list = n_queens_backtracking(n)
valid = n_queens_valid(queens_list, n)
print("queens_list=(%s)" % str(queens_list))
print("valid=(%s)" % valid)
print()


