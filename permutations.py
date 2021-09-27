import itertools
from typing import List

def is_sortable(obj):
    cls = obj.__class__
    return cls.__lt__ != object.__lt__ or cls.__gt__ != object.__gt__

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        #return self.permute_Itertools(nums)
        #return self.permute_ItertoolsEquivalent(nums)
        #return self.permute_Backtracking(nums)
        return self.permute_Recursive(nums)

    def permute_Backtracking(self, nums: List[int]) -> List[List[int]]:
        result = []

        def permute(first=0):
            if first == len(nums):
                result.append(nums[:])
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                permute(first+1)
                nums[first], nums[i] = nums[i], nums[first]

        permute()
        return result


    def permute_Recursive(self, nums: List[int]) -> List[List[int]]:
        result = []

        def permute(s, answer):
            if len(s) == 0:
                result.append(answer)
                return
            for i in range(len(s)):
                ch = [ s[i] ]
                left_substr = s[0:i]
                right_substr = s[i + 1:]
                rest = left_substr + right_substr
                permute(rest, answer + ch)

        permute(nums, [])
        return result
         

    def permute_Itertools(self, nums: List[int]) -> List[List[int]]:
        result = [ list(x) for x in itertools.permutations(nums) ]
        return result


    def permute_ItertoolsEquivalent(self, nums: List[int]) -> List[List[int]]:

        def permutations(iterable, r=None):
            """implement itertools.permutations()"""
            #   LINK: https://docs.python.org/3/library/itertools.html#itertools.permutations
            # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
            # permutations(range(3)) --> 012 021 102 120 201 210
            pool = tuple(iterable)
            n = len(pool)
            r = n if r is None else r
            if r > n:
                return
            indices = list(range(n))
            cycles = list(range(n, n-r, -1))
            yield tuple(pool[i] for i in indices[:r])
            while n:
                for i in reversed(range(r)):
                    cycles[i] -= 1
                    if cycles[i] == 0:
                        indices[i:] = indices[i+1:] + indices[i:i+1]
                        cycles[i] = n - i
                    else:
                        j = cycles[i]
                        indices[i], indices[-j] = indices[-j], indices[i]
                        yield tuple(pool[i] for i in indices[:r])
                        break
                else:
                    return

        result = [ list(x) for x in permutations(nums) ]
        return result

    

s = Solution()

input_values = [ [1,2,3], [0,1], [1], ]
input_checks = [ [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], [[0,1],[1,0]], [[1]], ]

for nums, check in zip(input_values, input_checks):
    print("nums=(%s)" % str(nums))
    result = s.permute(nums)
    print("result=(%s)" % str(result))
    assert is_sortable(result), "'is_sortable()' failed"
    assert sorted(result) == sorted(check), "Check failed"
    print()


