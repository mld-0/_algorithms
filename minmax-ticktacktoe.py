#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=20 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=1:
#   }}}1
import sys
import math
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
#   {{{2

#   TODO: 2021-08-28T18:10:23AEST _algorithms, minmax-ticktacktoe, interactive game against computer
#   TODO: 2021-08-28T18:11:22AEST _algorithms, minmax-ticktacktoe, implement opponent_best_move() 

class MinMax_TickTackToe(object):
    player = 'x'
    opponent = 'o'
    empty = '-'

    def __init__(self):
        self.width = 3
        self.height = 3
        self.board_init()

    def board_init(self):
        self.board = [ [ self.empty ] * self.width for x in range(self.height) ]

    def board_print(self):
        for loop_row in range(self.height):
            print("   ", end="")
            for loop_col in range(self.width):
                print("%1s" % self.board[loop_row][loop_col], end="")
            print("")

    def is_move_remaining(self):
        for loop_row in range(self.height):
            for loop_col in range(self.width):
                if self.empty == self.board[loop_row][loop_col]:
                    return True
        return False

    def evaluate(self, depth):
        """Determine whether player or opponent have won, returning 20-depth or -20+depth if so respectively, or 0 if nobody has won"""
        #   {{{
        #   Check rows
        for loop_row in range(0, self.height):
            result = True
            for loop_col in range(1, self.width):
                if self.board[loop_row][loop_col-1] != self.board[loop_row][loop_col]:
                    result = False
            if result == True:
                if self.board[loop_row][0] == self.player:
                    return 20 - depth
                elif self.board[loop_row][0] == self.opponent:
                    return -20 + depth
        #   Check columns
        for loop_col in range(0, self.width):
            result = True
            for loop_row in range(1, self.height):
                if self.board[loop_row-1][loop_col] != self.board[loop_row][loop_col]:
                    result = False
            if result == True:
                if self.board[0][loop_col] == self.player:
                    return 20 - depth
                elif self.board[0][loop_col] == self.opponent:
                    return -20 + depth
        #   Only check diagonals if board is square
        if self.width != self.height:
            return 0
        #   Check diagonal 1
        result = True
        for loop_i in range(1, self.height):
            if self.board[loop_i-1][loop_i-1] != self.board[loop_i][loop_i]:
                result = False
        if result == True:
            if self.board[0][0] == self.player:
                return 20 - depth
            elif self.board[0][0] == self.opponent:
                return -20 + depth
        #   Check diagonal 2
        result = True
        for loop_i in range(1, self.height):
            if self.board[self.height-loop_i-1][loop_i-1] != self.board[self.height-loop_i][loop_i]:
                result = False
        if result == True:
            if self.board[self.height-1][0] == self.player:
                return 20 - depth
            elif self.board[self.height-1][0] == self.opponent:
                return -20 + depth
        return 0
        #   }}}

    def minmax(self, depth, is_player_move):
        score = self.evaluate(depth)

        #   If player or opponent has won:
        if score != 0:
            return score
        #   If there are no moves remaining game is a tie
        if not self.is_move_remaining():
            return 0

        if not is_player_move:
            best = -math.inf

            for loop_row in range(self.height):
                for loop_col in range(self.width):

                    if self.board[loop_row][loop_col] == self.empty:
                        self.board[loop_row][loop_col] = self.opponent
                        trial_best = self.minmax(depth+1, not is_player_move)

                        if trial_best > best:
                            best = trial_best
                        self.board[loop_row][loop_col] = self.empty

        else:
            best = math.inf

            for loop_row in range(self.height):
                for loop_col in range(self.width):

                    if self.board[loop_row][loop_col] == self.empty:
                        self.board[loop_row][loop_col] = self.player
                        trial_best = self.minmax(depth+1, not is_player_move)

                        if trial_best < best:
                            best = trial_best
                        self.board[loop_row][loop_col] = self.empty

        return best


    def player_best_move(self):
        best = -math.inf
        best_index = None

        for loop_row in range(self.height):
            for loop_col in range(self.width):
                if self.board[loop_row][loop_col] == self.empty:
                    
                    self.board[loop_row][loop_col] = self.player
                    trial_best = self.minmax(0, True)
                    self.board[loop_row][loop_col] = self.empty

                    if trial_best > best:
                        best = trial_best
                        best_index = (loop_row, loop_col)

        return best_index, best


    def opponent_best_move(self):
        pass


def test_evaluate():
    #   {{{
    game = MinMax_TickTackToe()

    game.board = [ ['o','-','-'], ['o','-','x'], ['x','-','-'] ]
    game.board_print()
    result = game.evaluate()
    print("result=(%s)" % result)
    assert( result == 0 )

    game.board = [ ['x','-','-'], ['o','o','o'], ['x','-','-'] ]
    game.board_print()
    result = game.evaluate()
    print("result=(%s)" % result)
    assert( result == -20 )

    game.board = [ ['x','-','o'], ['o','-','o'], ['x','-','o'] ]
    game.board_print()
    result = game.evaluate()
    print("result=(%s)" % result)
    assert( result == -20 )

    game.board = [ ['x','-','o'], ['o','x','o'], ['x','-','x'] ]
    game.board_print()
    result = game.evaluate()
    print("result=(%s)" % result)
    assert( result == 20 )

    game.board = [ ['x','-','o'], ['-','o','-'], ['o','-','o'] ]
    game.board_print()
    result = game.evaluate()
    print("result=(%s)" % result)
    assert( result == -20 )
    #   }}}

def test_is_move_remaining():
    #   {{{
    game = MinMax_TickTackToe()

    game.board = [ ['o','-','-'], ['o','-','x'], ['x','-','-'] ]
    game.board_print()
    result = game.is_move_remaining()
    print("result=(%s)" % result)
    assert( result == True )

    game.board = [ ['x','-','-'], ['o','o','o'], ['x','-','-'] ]
    game.board_print()
    result = game.is_move_remaining()
    print("result=(%s)" % result)
    assert( result == True )

    game.board = [ ['x','-','o'], ['o','-','o'], ['x','-','o'] ]
    game.board_print()
    result = game.is_move_remaining()
    print("result=(%s)" % result)
    assert( result == True )

    game.board = [ ['x','-','o'], ['o','x','o'], ['x','-','x'] ]
    game.board_print()
    result = game.is_move_remaining()
    print("result=(%s)" % result)
    assert( result == True )

    game.board = [ ['x','-','o'], ['-','o','-'], ['o','-','o'] ]
    game.board_print()
    result = game.is_move_remaining()
    print("result=(%s)" % result)
    assert( result == True )

    game.board = [ ['o','o','x'], ['x','x','o'], ['o','o','x'] ]
    game.board_print()
    result = game.is_move_remaining()
    print("result=(%s)" % result)
    assert( result == False )
    #   }}}

def test_minmax():
    #   {{{
    game = MinMax_TickTackToe()

    print("depth=0, is_player_move=True")
    game.board = [ ['o','-','-'], ['o','-','x'], ['x','-','-'] ]
    game.board_print()
    result = game.minmax(0, True)
    print("result=(%s)" % result)
    #assert( result == True )
    game.board = [ ['x','-','-'], ['o','o','o'], ['x','-','-'] ]
    game.board_print()
    result = game.minmax(0, True)
    print("result=(%s)" % result)
    #assert( result == True )
    game.board = [ ['x','-','o'], ['o','-','o'], ['x','-','o'] ]
    game.board_print()
    result = game.minmax(0, True)
    print("result=(%s)" % result)
    #assert( result == True )
    game.board = [ ['x','-','o'], ['o','x','o'], ['x','-','x'] ]
    game.board_print()
    result = game.minmax(0, True)
    print("result=(%s)" % result)
    #assert( result == True )
    game.board = [ ['x','-','o'], ['-','o','-'], ['o','-','o'] ]
    game.board_print()
    result = game.minmax(0, True)
    print("result=(%s)" % result)
    #assert( result == True )
    game.board = [ ['x','o','x'], ['x','o','o'], ['o','o','x'] ]
    game.board_print()
    result = game.minmax(0, True)
    print("result=(%s)" % result)
    #assert( result == False )

    print("depth=0, is_player_move=False")
    game.board = [ ['o','-','-'], ['o','-','x'], ['x','-','-'] ]
    game.board_print()
    result = game.minmax(0, False)
    print("result=(%s)" % result)
    #assert( result == True )
    game.board = [ ['x','-','-'], ['o','o','o'], ['x','-','-'] ]
    game.board_print()
    result = game.minmax(0, False)
    print("result=(%s)" % result)
    #assert( result == True )
    game.board = [ ['x','-','o'], ['o','-','o'], ['x','-','o'] ]
    game.board_print()
    result = game.minmax(0, False)
    print("result=(%s)" % result)
    #assert( result == True )
    game.board = [ ['x','-','o'], ['o','x','o'], ['x','-','x'] ]
    game.board_print()
    result = game.minmax(0, False)
    print("result=(%s)" % result)
    #assert( result == True )
    game.board = [ ['x','-','o'], ['-','o','-'], ['o','-','o'] ]
    game.board_print()
    result = game.minmax(0, False)
    print("result=(%s)" % result)
    #assert( result == True )
    game.board = [ ['o','o','x'], ['x','x','o'], ['o','o','x'] ]
    game.board_print()
    result = game.minmax(0, False)
    print("result=(%s)" % result)
    #assert( result == False )

    #   }}}

def test_player_best_move():
    #   {{{
    game = MinMax_TickTackToe()

    game.board = [ ['o','-','-'], ['o','-','x'], ['x','-','-'] ]
    game.board_print()
    result, score = game.player_best_move()
    print("result=(%s), score=(%s)" % (result, score))

    game.board = [ ['o','x','-'], ['o','-','x'], ['x','-','-'] ]
    game.board_print()
    result, score = game.player_best_move()
    print("result=(%s), score=(%s)" % (result, score))

    game.board = [ ['o','-','x'], ['o','o','x'], ['x','-','-'] ]
    game.board_print()
    result, score = game.player_best_move()
    print("result=(%s), score=(%s)" % (result, score))

    game.board = [ ['x','-','-'], ['o','o','o'], ['x','-','-'] ]
    game.board_print()
    result, score = game.player_best_move()
    print("result=(%s), score=(%s)" % (result, score))

    game.board = [ ['x','-','o'], ['o','-','o'], ['x','-','o'] ]
    game.board_print()
    result, score = game.player_best_move()
    print("result=(%s), score=(%s)" % (result, score))

    game.board = [ ['x','-','o'], ['o','x','o'], ['x','-','x'] ]
    game.board_print()
    result, score = game.player_best_move()
    print("result=(%s), score=(%s)" % (result, score))

    game.board = [ ['x','-','o'], ['-','o','-'], ['o','-','o'] ]
    game.board_print()
    result, score = game.player_best_move()
    print("result=(%s), score=(%s)" % (result, score))

    game.board = [ ['x','o','x'], ['x','o','o'], ['o','o','x'] ]
    game.board_print()
    result, score = game.player_best_move()
    print("result=(%s), score=(%s)" % (result, score))
    #   }}}
    

if __name__ == "__main__":
    print("test_evaluate:")
    test_evaluate()
    print()

    print("test_is_move_remaining:")
    test_is_move_remaining()
    print()

    print("test_minmax:")
    test_minmax()
    print()

    print("test_player_best_move:")
    test_player_best_move()
    print()

