#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
import pprint
import math
#   {{{2
#   Ongoing: 2021-10-29T20:28:37AEDT Use of 0/1 indexing in recursive(/iterative) solutions for string position (vs position in table)?
class Solution:

    #   LINK: https://medium.com/@ethannam/understanding-the-levenshtein-distance-equation-for-beginners-c4285a5604f0
    def minDistance_Iterative(self, word1: str, word2: str, returnTable: bool=False) -> int:
        #   empty word, edit distance is length of other word
        if len(word1) == 0 or len(word2) == 0:
            return len(word1) + len(word2)

        #   table[i][j]: edit distance between word1[:i] and word2[:j]
        table = [ [ 0 for col in range(len(word2)+1) ] for row in range(len(word1)+1) ]

        #   initial conditions: 
        for row in range(len(table)):
            table[row][0] = row
        for col in range(len(table[0])):
            table[0][col] = col

        #   iteratively fill table
        for row in range(1, len(table)):
            for col in range(1, len(table[0])):
                diag = table[row-1][col-1]      #   Equal
                if word1[row-1] != word2[col-1]:
                    diag = diag + 1             #   Replace
                left = table[row-1][col] + 1    #   Remove
                down = table[row][col-1] + 1    #   Insert
                table[row][col] = min(left, down, diag)

        #   return either able, or last value, as per 'returnTable'
        if returnTable:
            return table
        return table[-1][-1]


    def minDistance_Recursive(self, word1: str, word2: str) -> int:

        def solve(m: int, n: int):
            if m == 0 or n == 0:
                return m + n
            if word1[m-1] == word2[n-1]:
                return solve(m-1, n-1)
            left = solve(m-1, n)    #   Remove
            down = solve(m, n-1)    #   Insert
            diag = solve(m-1, n-1)  #   Replace
            return 1 + min(left, down, diag)

        return solve(len(word1), len(word2))

    
    #   LINK: https://www.geeksforgeeks.org/edit-distance-dp-5/
    def minDistance_RecursiveMemorize(self, word1: str, word2: str) -> int:
        memo = dict()

        def solve(m: int, n: int):
            if (m,n) in memo:
                return memo[(m,n)]

            #   empty word, edit distance is length of other word
            if m == 0 or n == 0:
                result = m + n
                memo[(m,n)] = result
                return result

            if word1[m-1] == word2[n-1]:
                result = solve(m-1, n-1)    #   Equal
                memo[(m,n)] = result
                return result

            left = solve(m-1, n)            #   Remove
            down = solve(m, n-1)            #   Insert
            diag = solve(m-1, n-1)          #   Replace

            result = 1 + min(left, down, diag)
            memo[(m,n)] = result
            return result

        return solve(len(word1), len(word2))


    def minDistance_PythonLevenshtein(self, word1: str, word2: str) -> int:
        import Levenshtein
        return Levenshtein.distance(word1, word2)


    #   LINK: https://stackoverflow.com/questions/10638597/minimum-edit-distance-reconstruction
    def trace_minDistance_Table(self, table, w1, w2):
        result = []

        row = len(table)-1
        col = len(table[0])-1

        while row > 0 and col > 0:
            current = table[row][col]
            up = math.inf
            right = math.inf
            diag = math.inf

            if row-1 > 0 and col-1 > 0:
                diag = table[row-1][col-1]
            if row-1 > 0:
                up = table[row-1][col]
            if col-1 > 0:
                right = table[row][col-1]

            if diag <= up and diag <= right:
                if current == diag:
                    result.append( ("Equal", w1[row-1], w2[col-1]) )
                else:
                    result.append( ("Substitute", w1[row-1], w2[col-1]) )
                row -= 1
                col -= 1
            elif up <= diag and up <= right:
                result.append( ("Delete", w1[row-1]) )
                row -= 1
            elif right <= diag and right <= up:
                result.append( ("Insert", w2[col-1]) )
                col -= 1

        result = result[::-1]
        return result



s = Solution()
test_functions = [ s.minDistance_Iterative, s.minDistance_RecursiveMemorize, s.minDistance_PythonLevenshtein, ]

input_values = [ ("horse", "ros"), ("intention", "execution"), ("sitting", "kitten"), ("dinitrophenylhydrazine", "benzalphenylhydrazone"), ]
input_checks = [ 3, 5, 3, 7, ]

for test_func in test_functions:
    print(test_func.__name__)
    for (word1, word2), check in zip(input_values, input_checks):
        print("word1=(%s), word2=(%s)" % (word1, word2))
        result = test_func(word1, word2)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print()

print("Trace:")
for (word1, word2), check in zip(input_values, input_checks):
    print("word1=(%s), word2=(%s)" % (word1, word2))
    result = s.minDistance_Iterative(word1, word2, True)
    assert result[-1][-1] == check, "Check comparison failed"
    result_trace = s.trace_minDistance_Table(result, word1, word2)
    pprint.pprint(result_trace)
print()

