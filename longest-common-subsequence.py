#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
#   TODO: 2021-10-28T20:28:50AEDT _algorithms, longest-common-subsequence, determine LCS from resulting DP table
#   {{{2
class Solution:

    def longestCommonSubsequence_DP_TopDown_RecursiveMemorize(self, text1: str, text2: str) -> int:
        memo = dict()

        def solve(p1: int, p2: int) -> int:
            if (p1, p2) in memo:
                return memo[(p1, p2)]

            #   base case, empty string -> can't match any more characters
            if p1 == len(text1) or p2 == len(text2):
                memo[(p1,p2)] = 0
                return 0

            #   Case 1: Letters match
            if text1[p1] == text2[p2]:
                result = 1 + solve(p1+1, p2+1)
                memo[(p1, p2)] = result
                return result

            #   Case 2: Letters do not match
            else:
                result = max(solve(p1+1, p2), solve(p1, p2+1))
                memo[(p1, p2)] = result
                return result

        return solve(0, 0)


    def longestCommonSubsequence_DP_BottomUp_Iterative_i(self, text1: str, text2: str) -> int:
        #   table[i][j]: longest common subsequence of 'text1[i:]' and 'text2[j:]'
        table = [ [ 0 for col in range(len(text2)+1) ] for row in range(len(text1)+1) ]

        for col in range(len(text2)-1, -1, -1):
            for row in range(len(text1)-1, -1, -1):

                #   Case 1: Letters match
                if text1[row] == text2[col]:
                    table[row][col] = 1 + table[row+1][col+1]

                #   Case 2: Letters do not match
                else:
                    table[row][col] = max(table[row+1][col], table[row][col+1])

        return table[0][0]


s = Solution()
test_functions = [ s.longestCommonSubsequence_DP_TopDown_RecursiveMemorize, s.longestCommonSubsequence_DP_BottomUp_Iterative_i, s.longestCommonSubsequence_DP_BottomUp_Iterative_ii, ]

input_values = [ ("abcde", "ace"), ("abc", "abc"), ("abc", "def"), ]
input_checks = [ 3, 3, 0, ]

for test_func in test_functions:
    print(test_func.__name__)
    for (text1, text2), check in zip(input_values, input_checks):
        print("text1=(%s), text2=(%s)" % (text1, text2))
        result = test_func(text1, text2)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print()


