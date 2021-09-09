import pprint

class Solution:

    #   Results:
    #       runtime: beats 25%
    def solveSudoku(self, board):
        """Solve by modifying the input board in-place"""
        self.board = board
        self.solve()

    def solve(self):
        """Backtracking solution, fill next empty square with each possible option and recurse"""
        #   find next unassigned square
        row, col = self.findUnassigned()
        if row == -1 and col == -1:
            return True
        #   try to fill that square for each of [1,9]
        for i in range(1, 10):
            num = str(i)
            #   attempt to place each possible value, backtracking if successful
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                result = self.solve()
                if result == True:
                    return True
                self.board[row][col] = "."
        #   If we failed to place a value, problem must be unsolveable for current board
        return False

    def findUnassigned(self):
        """Find coordinates of next empty square"""
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1

    def isSafe(self, row, col, check):
        """Check can a given value 'check' be placed at a given position"""
        if self.isSafe_checkrow(row,check) and self.isSafe_checkcol(col,check) and self.isSafe_checksector(row, col, check):
            return True
        return False

    def isSafe_checkrow(self, row, check):
        """Check whether given row contains given value"""
        for col in range(9):
            if self.board[row][col] == check:
                return False
        return True

    def isSafe_checkcol(self, col, check):
        """Check whether given column contains given value"""
        for row in range(9):
            if self.board[row][col] == check:
                return False
        return True

    def isSafe_checksector(self, row, col, check):
        """Check whether the given sector (3x3) contains given value"""
        sector_row = row - row%3
        sector_col = col - col%3
        for r in range(sector_row, sector_row+3):
            for c in range(sector_col, sector_col+3):
                if self.board[r][c] == check:
                    return False
        return True


#board = [ [".","6",".", "8",".",".", "5",".","."], [".",".","5", ".",".",".", "3","6","7"], ["3","7",".", ".","6","5", "8",".","9"], ["6",".","9", ".",".","2", "1",".","."], [".",".","1", "4","8","9", "2",".","."], [".",".",".", "3",".","6", "9",".","."], [".","5",".", ".",".",".", "4",".","."], [".","1",".", "5","4","7", ".",".","3"], [".","9","6", ".","3","8", ".","5","1"], ]
board = [ [".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."], ]
pprint.pprint(board)
print()

s = Solution()
s.solveSudoku(board)

pprint.pprint(board)
print()

