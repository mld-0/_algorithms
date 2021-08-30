#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=100 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=1:
#   }}}1
import sys
import math
import logging
import re
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
#   {{{2

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

    def is_game_won(self):
        score = self.evaluate(0)
        logging.debug("score=(%s)" % str(score))
        #   Ongoing: 2021-08-30T14:50:44AEST Use 'score != 0' instead of == 100 or -100?
        if score == 100 or score == -100:
            return True
        return False

    def evaluate(self, depth):
        """Determine whether player or opponent have won, returning 100-depth or -100+depth if so respectively, or 0 if nobody has won"""
        #   {{{
        #   Check rows
        for loop_row in range(0, self.height):
            result = True
            for loop_col in range(1, self.width):
                if self.board[loop_row][loop_col-1] != self.board[loop_row][loop_col]:
                    result = False
            if result:
                if self.board[loop_row][0] == self.player:
                    return 100 - depth
                elif self.board[loop_row][0] == self.opponent:
                    return -100 + depth
        #   Check columns
        for loop_col in range(0, self.width):
            result = True
            for loop_row in range(1, self.height):
                if self.board[loop_row-1][loop_col] != self.board[loop_row][loop_col]:
                    result = False
            if result:
                if self.board[0][loop_col] == self.player:
                    return 100 - depth
                elif self.board[0][loop_col] == self.opponent:
                    return -100 + depth
        #   Only check diagonals if board is square
        if self.width != self.height:
            return 0

        #   Check diagonal 1
        result = True
        for loop_i in range(1, self.height):
            #logging.debug("compare %s, %s" % (self.board[loop_i-1][loop_i-1], self.board[loop_i][loop_i]))
            if self.board[loop_i-1][loop_i-1] != self.board[loop_i][loop_i]:
                result = False
        if result:
            if self.board[0][0] == self.player:
                return 100 - depth
            elif self.board[0][0] == self.opponent:
                return -100 + depth

        #   Check diagonal 2
        result = True
        for loop_i, loop_j in zip(range(0, self.height-1), range(self.width-1, 0, -1)):
            loop_delta_i = loop_i + 1
            loop_delta_j = loop_j - 1
            #logging.debug("loop_delta_i=(%s), loop_delta_j=(%s), loop_i=(%s), loop_j=(%s)" % (loop_delta_i, loop_delta_j, loop_i, loop_j))
            if self.board[loop_delta_i][loop_delta_j] != self.board[loop_i][loop_j]:
                result = False
        if result:
            if self.board[self.height-1][0] == self.player:
                return 100 - depth
            elif self.board[self.height-1][0] == self.opponent:
                return -100 + depth
        return 0
        #   }}}

    def minmax(self, depth, is_player_move):
        score = self.evaluate(depth)

        #   If player or opponent has won:
        if score != 0:
            return score

        #   If there are no moves remaining game is a tie:
        if not self.is_move_remaining():
            return 0

        #   Either maximise for player, or minimise for opponent
        if not is_player_move:
            best = math.inf
            for loop_row in range(self.height):
                for loop_col in range(self.width):
                    if self.board[loop_row][loop_col] == self.empty:
                        self.board[loop_row][loop_col] = self.opponent
                        trial_best = self.minmax(depth+1, not is_player_move)
                        if trial_best < best:
                            best = trial_best
                        self.board[loop_row][loop_col] = self.empty
        else:
            best = -math.inf
            for loop_row in range(self.height):
                for loop_col in range(self.width):
                    if self.board[loop_row][loop_col] == self.empty:
                        self.board[loop_row][loop_col] = self.player
                        trial_best = self.minmax(depth+1, not is_player_move)
                        if trial_best > best:
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
                    trial_best = self.minmax(0, False)
                    self.board[loop_row][loop_col] = self.empty
                    if trial_best > best:
                        best = trial_best
                        best_index = (loop_row, loop_col)
        return best_index, best


    def opponent_best_move(self):
        best = math.inf
        best_index = None
        for loop_row in range(self.height):
            for loop_col in range(self.width):
                if self.board[loop_row][loop_col] == self.empty:
                    self.board[loop_row][loop_col] = self.opponent
                    trial_best = self.minmax(0, True)
                    self.board[loop_row][loop_col] = self.empty
                    if trial_best < best:
                        best = trial_best
                        best_index = (loop_row, loop_col)
        logging.debug("best_index=(%s)" % str(best_index))
        return best_index, best


    #   TODO: 2021-08-28T21:35:20AEST validate that user hasn't selected square already containing move
    def prompt_player_move(self):
        #   {{{
        flag_first = True
        user_input = ""
        validate_input = r'^\d,\d$'
        while not re.match(validate_input, user_input):
            if not flag_first:
                print("invalid input, ", end="")
            print("enter move: 'row,col'")
            user_input = input()
            flag_first = False
        user_input_row, user_input_col = map(int, user_input.split(","))
        logging.debug("user_input_row=(%s), user_input_col=(%s)" % (user_input_row, user_input_col))
        self.board[user_input_row][user_input_col] = self.player
        self.board_print()
        #   }}}

    def make_ai_player_move(self):
        #   {{{
        best_index, best = self.player_best_move()
        logging.debug("ai player move=(%s), score=(%s)" % (best_index, best))
        self.board[best_index[0]][best_index[1]] = self.player
        self.board_print()
        #   }}}

    def make_opponent_move(self):
        #   {{{
        best_index, best = self.opponent_best_move()
        logging.debug("ai opponent move=(%s), score=(%s)" % (best_index, best))
        self.board[best_index[0]][best_index[1]] = self.opponent
        self.board_print()
        #   }}}
    
    def player_vs_machine(self, player_first=True):
        #   {{{
        self.board_init()
        self.board_print()
        print("rows: [0,%s), cols: [0,%s)" % (self.height, self.width))
        if (player_first):
            self.prompt_player_move()
        while self.is_move_remaining():
            self.make_opponent_move()
            if not self.is_move_remaining() or self.is_game_won():
                break
            self.prompt_player_move()
            if not self.is_move_remaining() or self.is_game_won():
                break
        #   }}}

    def machine_vs_machine(self, player_first=True):
        #   {{{
        self.board_init()
        self.board_print()
        if (player_first):
            self.make_ai_player_move()
        while self.is_move_remaining():
            self.make_opponent_move()
            if not self.is_move_remaining() or self.is_game_won():
                break
            self.make_ai_player_move()
            if not self.is_move_remaining() or self.is_game_won():
                break
        #   }}}
       

def test_evaluate():
    #   {{{
    game = MinMax_TickTackToe()

    game.board = [ ['o','-','-'], ['o','-','x'], ['x','-','-'] ]
    game.board_print()
    result = game.evaluate(0)
    print("result=(%s)" % result)
    assert( result == 0 )

    game.board = [ ['x','-','-'], ['o','o','o'], ['x','-','-'] ]
    game.board_print()
    result = game.evaluate(0)
    print("result=(%s)" % result)
    assert( result == -100 )

    game.board = [ ['x','-','o'], ['o','-','o'], ['x','-','o'] ]
    game.board_print()
    result = game.evaluate(0)
    print("result=(%s)" % result)
    assert( result == -100 )

    game.board = [ ['x','-','o'], ['o','x','o'], ['x','-','x'] ]
    game.board_print()
    result = game.evaluate(0)
    print("result=(%s)" % result)
    assert( result == 100 )

    game.board = [ ['x','-','o'], ['-','o','-'], ['o','-','o'] ]
    game.board_print()
    result = game.evaluate(0)
    print("result=(%s)" % result)
    assert( result == -100 )

    game.board = [ ['x','-','-'], ['-','-','-'], ['o','-','x'] ]
    game.board_print()
    result = game.evaluate(0)
    print("result=(%s)" % result)
    #assert( result == -100 )
    assert( result == 0 )

    game.board = [ ['-','-','-'], ['-','-','-'], ['x','-','-'] ]
    game.board_print()
    result = game.evaluate(0)
    print("result=(%s)" % result)
    assert( result == 0 )

    game.board = [ ['-','-','-'], ['-','-','-'], ['x','-','-'] ]
    game.board_print()
    result = game.evaluate(0)
    print("result=(%s)" % result)
    assert( result == 0 )

    game.board = [ ['x','-','-'], ['-','-','-'], ['-','-','x'] ]
    game.board_print()
    result = game.evaluate(0)
    print("result=(%s)" % result)
    assert( result == 0 )

    game.board = [ ['x','-','x'], ['-','-','-'], ['-','-','x'] ]
    game.board_print()
    result = game.evaluate(0)
    print("result=(%s)" % result)
    assert( result == 0 )

    game.board = [ ['-','-','-'], ['-','x','-'], ['x','-','x'] ]
    game.board_print()
    result = game.evaluate(0)
    print("result=(%s)" % result)
    assert( result == 0 )

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

#   TODO: 2021-08-30T15:54:43AEST test_minmax result is not being asserted against anything
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


def test_opponent_best_move():
    #   {{{
    game = MinMax_TickTackToe()

    game.board = [ ['o','-','-'], ['o','-','x'], ['x','-','-'] ]
    game.board_print()
    result, score = game.opponent_best_move()
    print("result=(%s), score=(%s)" % (result, score))

    game.board = [ ['o','x','-'], ['o','-','x'], ['x','-','-'] ]
    game.board_print()
    result, score = game.opponent_best_move()
    print("result=(%s), score=(%s)" % (result, score))

    game.board = [ ['o','-','x'], ['o','o','x'], ['x','-','-'] ]
    game.board_print()
    result, score = game.opponent_best_move()
    print("result=(%s), score=(%s)" % (result, score))

    game.board = [ ['x','-','-'], ['o','o','o'], ['x','-','-'] ]
    game.board_print()
    result, score = game.opponent_best_move()
    print("result=(%s), score=(%s)" % (result, score))

    game.board = [ ['x','-','o'], ['o','-','o'], ['x','-','o'] ]
    game.board_print()
    result, score = game.opponent_best_move()
    print("result=(%s), score=(%s)" % (result, score))

    game.board = [ ['x','-','o'], ['o','x','o'], ['x','-','x'] ]
    game.board_print()
    result, score = game.opponent_best_move()
    print("result=(%s), score=(%s)" % (result, score))

    game.board = [ ['x','-','o'], ['-','o','-'], ['o','-','o'] ]
    game.board_print()
    result, score = game.opponent_best_move()
    print("result=(%s), score=(%s)" % (result, score))

    game.board = [ ['x','o','x'], ['x','o','o'], ['o','o','x'] ]
    game.board_print()
    result, score = game.opponent_best_move()
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

    print("test_opponent_best_move:")
    test_opponent_best_move()
    print()

    game = MinMax_TickTackToe()
    #game.player_vs_machine(True)
    game.machine_vs_machine(False)
    game.machine_vs_machine(True)

