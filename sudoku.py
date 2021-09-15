#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=1:
#   }}}1
import sys
import math
import pprint
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
#   {{{2

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
        #   try to fill that square for each possible option
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
        """Find coordinates of the first empty square with the least possible options"""
        best = (-1, -1)
        best_options_len = math.inf
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    options = self.options(row, col)
                    if len(options) < best_options_len:
                        best_options_len = len(options)
                        best = (row, col)
        return best

    def options(self, row, col):
        """Get possible values for a given (empty) square"""
        options_row = self.options_checkrow(row)
        options_col = self.options_checkcol(col)
        options_sector = self.options_checksector(row, col)
        return options_row & options_col & options_sector

    def options_checkrow(self, row):
        """Get possible values for a given row"""
        options = set( [str(i) for i in range(1, 10) ] )
        for loop_col in range(9):
            val = self.board[row][loop_col]
            if val != '.':
                options.remove(val)
        return options

    def options_checkcol(self, col):
        """Get possible values for a given col"""
        options = set( [str(i) for i in range(1, 10) ] )
        for loop_row in range(9):
            val = self.board[loop_row][col]
            if val != '.':
                options.remove(val)
        return options

    def options_checksector(self, row, col):
        """Get possible values for a given (3x3) sector"""
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

#board = [ ['.','6','.','8','.','.','5','.','.'], ['.','.','5','.','.','.','3','6','7'], ['3','7','.','.','6','5','8','.','9'], ['6','.','9','.','.','2','1','.','.'], ['.','.','1','4','8','9','2','.','.'], ['.','.','.','3','.','6','9','.','.'], ['.','5','.','.','.','.','4','.','.'], ['.','1','.','5','4','7','.','.','3'], ['.','9','6','.','3','8','.','5','1'], ]
board = [ ['.','.','9','7','4','8','.','.','.'], ['7','.','.','.','.','.','.','.','.'], ['.','2','.','1','.','9','.','.','.'], ['.','.','7','.','.','.','2','4','.'], ['.','6','4','.','1','.','5','9','.'], ['.','9','8','.','.','.','3','.','.'], ['.','.','.','8','.','3','.','2','.'], ['.','.','.','.','.','.','.','.','6'], ['.','.','.','2','7','5','9','.','.'], ] 

pprint.pprint(board)
print()

s.solveSudoku(board)
pprint.pprint(s.board)

