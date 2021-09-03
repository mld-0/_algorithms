import pprint


def square_is_safe(n, row, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
    if (slashCodeLookup[slashCode[row][col]] or backslashCodeLookup[backslashCode[row][col]] or rowLookup[row]):
        return False
    return True


def n_queens(n, board=None, col=0, slashCode=None, backslashCode=None, rowLookup=None, slashCodeLookup=None, backslashCodeLookup=None):
    #   which squares contain queens
    if board is None:
        board = [ [0 for col in range(n)] for row in range(n) ]
    #   which rows are occupied
    if rowLookup is None:
        rowLookup = [ False for row in range(n) ]
    #   which diagonals are occupied
    x = 2 * n - 1
    if slashCodeLookup is None:
        slashCodeLookup = [ False for d in range(x) ]
    if backslashCodeLookup is None:
        backslashCodeLookup = [ False for d in range(x) ]
    #   helpers
    if slashCode is None:
        slashCode = [ [ row+col for col in range(n) ] for row in range(n) ]
    if backslashCode is None:
        backslashCode = [ [ row-col+7 for col in range(n) ] for row in range(n) ]

    if col >= n:
        return board

    #   place queen in col
    for row in range(n):

        #   if (row, col) is not attacked:
        if square_is_safe(n, row, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):

            #   place queen at (i, col)
            board[row][col] = 1
            rowLookup[row] = True
            slashCodeLookup[slashCode[row][col]] = True
            backslashCodeLookup[backslashCode[row][col]] = True

            #   recurse and return solution 'board' if successful
            if n_queens(n, board, col+1, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup) != False:
                    return board

            #   if unsuccessful, remove queen at (i, col)
            board[row][col] = 0
            rowLookup[row] = False
            slashCodeLookup[slashCode[row][col]] = False
            backslashCodeLookup[backslashCode[row][col]] = False

    return False

n = 8
result = n_queens(n)
pprint.pprint(result)

