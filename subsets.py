#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
import itertools
from typing import List
#   {{{2
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subsets_Cascading_i(nums)
        #return self.subsets_Cascading_ii(nums)
        #return self.subsets_Bitmask(nums)
        #return self.subsets_Itertools(nums)


    def subsets_Cascading_i(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for n in nums:
            temp = [ c + [n] for c in result ]
            result.extend(temp)
        return result


    def subsets_Cascading_ii(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for n in nums:
            for i in range(len(result)):
                temp = result[i] + [n]
                result.append(temp)
        return result


    def subsets_Backtracking(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(k, first=0, curr=None):
            if curr is None: 
                curr = []
            if len(curr) == k:
                result.append(curr[:])
                return
            for i in range(first, len(nums)):
                curr.append(nums[i])
                backtrack(k, i+1, curr)
                curr.pop()
        for k in range(len(nums)+1):
            backtrack(k)
        return result


    def subsets_Bitmask(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(2**len(nums), 2**(len(nums)+1)):
            bitmask = bin(i)[3:]
            result.append( [ nums[j] for j in range(len(nums)) if bitmask[j] == '1' ] )
        return result
    

    def subsets_Itertools(self, nums: List[int]) -> List[List[int]]:
        result = [ list(x) for i in range(len(nums)+1) for x in itertools.combinations(nums, i) ]
        return result


s = Solution()

input_values = [ [1,2,3], [0], ]
input_checks = [ [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]], [[],[0]], ]

for nums, check in zip(input_values, input_checks):
    print("nums=(%s)" % nums)
    result = s.subsets(nums)
    print("result=(%s)" % result)
    assert sorted(result) == sorted(check), "Check failed"
    print()


