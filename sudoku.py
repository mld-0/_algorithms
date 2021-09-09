#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=1:
#   }}}1
import sys
import pprint
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
#   {{{2

#   {{{
#def sudoko_backtracking(board):
#    if not is_board_invalid(board, False):
#        return board
#    for row in range(9):
#        for col in range(9):
#            options = get_square_options(board, row, col)
#            if board[row][col] == 0:
#                for i in options:
#                    print("row=(%s), col=(%s), i=(%s)" % (row, col, i))
#                    board[row][col] = i
#                    result = sudoko_backtracking(board)
#                    if result is not None:
#                        return result
#                    board[row][col] = 0
#    return None
#
#
#def sudoko_iterative(board):
#    while is_board_invalid(board, False):
#        found_move = False
#        for row in range(9):
#            for col in range(9):
#                options = get_square_options(board, row, col)
#                if board[row][col] == 0 and len(options) == 1:
#                    found_move = True
#                    board[row][col] = options[0]
#        if not found_move:
#            break
#    return board
#
#def get_square_options(board, row, col):
#    counts = get_square_counts(board, row, col)
#    options = []
#    for i in range(1, 10):
#        if counts[i] == 0:
#            options.append(i)
#    return options
#
#def is_board_invalid(board, allow_zeros=True):
#    for row in range(9):
#        for col in range(9):
#            if is_square_invalid(board, row, col, allow_zeros):
#                return True
#    return False
#
#def is_square_invalid(board, row, col, allow_zeros=True):
#    """Is the value in a given square invalid"""
#    counts = [ 0 for i in range(10) ]
#    #   Check row
#    for loop_col in range(9):
#        val = board[row][loop_col]
#        counts[val] += 1
#    if not allow_zeros:
#        if counts[0] > 0:
#            return True
#    for i in range(1, 9):
#        if counts[i] > 1:
#            return True
#    counts = [ 0 for i in range(10) ]
#    #   Check col
#    for loop_row in range(9):
#        val = board[loop_row][col]
#        counts[val] += 1
#    if not allow_zeros:
#        if counts[0] > 0:
#            return True
#    for i in range(1, 9):
#        if counts[i] > 1:
#            return True
#    counts = [ 0 for i in range(10) ]
#    #   Check 3x3 sector
#    sector_row = row // 3
#    sector_col = col // 3
#    #logging.debug("sector_row=(%s), sector_col=(%s)" % (sector_row, sector_col))
#    for loop_row in range(sector_row*3, (sector_row+1)*3):
#        for loop_col in range(sector_col*3, (sector_col+1)*3):
#            val = board[loop_row][loop_col]
#            counts[val] += 1
#    if not allow_zeros:
#        if counts[0] > 0:
#            return True
#    for i in range(1, 9):
#        if counts[i] > 1:
#            return True
#    return False
#
#def get_square_counts(board, row, col):
#    counts = [ 0 for i in range(10) ]
#    #   Check row
#    for loop_col in range(9):
#        val = board[row][loop_col]
#        counts[val] += 1
#    #   Check col
#    for loop_row in range(9):
#        val = board[loop_row][col]
#        counts[val] += 1
#    #   Check 3x3 sector
#    sector_row = row // 3
#    sector_col = col // 3
#    #logging.debug("sector_row=(%s), sector_col=(%s)" % (sector_row, sector_col))
#    for loop_row in range(sector_row*3, (sector_row+1)*3):
#        for loop_col in range(sector_col*3, (sector_col+1)*3):
#            val = board[loop_row][loop_col]
#            counts[val] += 1
#    return counts
#   }}}

class Solution:

    def solveSudoku(self, board):
        self.setBoard(board)
        self.solve_backtracking()

    def setBoard(self, board):
        self.board = board

    def solve_backtracking(self):
        """Backtracking solution, fill next empty square with each possible option and recurse"""
        #   for next unassigned square
        row, col = self.findUnassigned()
        if row == -1 and col == -1:
            return True
        #   try to fill that square for each possible value
        options = self.options(row, col)
        for i in options:
            #   attempt to place each possible value, backtracking if unsucessful
            self.board[row][col] = i
            result = self.solve_backtracking()
            if result == True:
                return True
            self.board[row][col] = '.'
        #   If we failed to place a value, problem must be unsolveable for current board
        return False


    def findUnassigned(self):
        """Find coordinates of next empty square"""
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return (row, col)
        return (-1, -1)

    def options(self, row, col):
        """Get available values for a given (empty) square"""
        options_row = self.options_checkrow(row)
        options_col = self.options_checkcol(col)
        options_sector = self.options_checksector(row, col)
        return options_row & options_col & options_sector

    def options_checkrow(self, row):
        """Get available values for a given row"""
        options = set( [str(i) for i in range(1, 10) ] )
        for loop_col in range(9):
            val = self.board[row][loop_col]
            if val != '.':
                options.remove(val)
        return options

    def options_checkcol(self, col):
        """Get available values for a given col"""
        options = set( [str(i) for i in range(1, 10) ] )
        for loop_row in range(9):
            val = self.board[loop_row][col]
            if val != '.':
                options.remove(val)
        return options

    def options_checksector(self, row, col):
        """Get available values for a given (3x3) sector"""
        sector_row = row - row % 3
        sector_col = col - col % 3 
        options = set( [str(i) for i in range(1, 10) ] )
        for loop_row in range(sector_row, sector_row+3):
            for loop_col in range(sector_col, sector_col+3):
                val = self.board[loop_row][loop_col]
                if val != '.':
                    options.remove(val)
        return options


s = Solution()

board = [ ['.','6','.','8','.','.','5','.','.'], ['.','.','5','.','.','.','3','6','7'], ['3','7','.','.','6','5','8','.','9'], ['6','.','9','.','.','2','1','.','.'], ['.','.','1','4','8','9','2','.','.'], ['.','.','.','3','.','6','9','.','.'], ['.','5','.','.','.','.','4','.','.'], ['.','1','.','5','4','7','.','.','3'], ['.','9','6','.','3','8','.','5','1'], ]
board = [ ['.','.','9','7','4','8','.','.','.'], ['7','.','.','.','.','.','.','.','.'], ['.','2','.','1','.','9','.','.','.'], ['.','.','7','.','.','.','2','4','.'], ['.','6','4','.','1','.','5','9','.'], ['.','9','8','.','.','.','3','.','.'], ['.','.','.','8','.','3','.','2','.'], ['.','.','.','.','.','.','.','.','6'], ['.','.','.','2','7','5','9','.','.'], ] 

pprint.pprint(board)
print()

s.setBoard(board)
row, col = s.findUnassigned()
print("findUnassigned(): row=(%s), col=(%s)" % (row, col))
print()
assert( (row, col) == (0, 0) )

options = s.options(row, col)
print("options=(%s)" % options)
print()
assert( all([ x == str(y) for x, y in zip(sorted(options), [1,3,5,6] ) ])  )

s.solveSudoku(board)
pprint.pprint(s.board)

