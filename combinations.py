from typing import List
import itertools

def is_sortable(obj):
    cls = obj.__class__
    return cls.__lt__ != object.__lt__ or cls.__gt__ != object.__gt__

class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.combine_Itertools(n, k)
        #return self.combine_Recursive(n, k)
        #return self.combine_Backtracking(n, k)
        #return self.combine_Lexicographic(n, k)


    #   runtime: beats 49%
    def combine_Backtracking(self, n: int, k: int):
        result = []
        values = list(range(1, n+1))

        def backtrack(first=0, cur=None):
            if cur is None:
                cur = []
            #   if combination is done
            if len(cur) == k:
                result.append(cur[:])
                return
            for i in range(first, n):
                cur.append(values[i])
                backtrack(i+1, cur)
                cur.pop()

        backtrack()
        return result


    #   runtime: beats 34%
    def combine_Recursive(self, n: int, k: int): 
        result = []
        values = list(range(1, n+1))

        def combinations(sofar, rest, n):
            if n == 0:
                result.append(sofar)
                return
            for i in range(len(rest)):
                combinations(sofar + [ rest[i] ], rest[i+1:], n-1)

        combinations([], values, k)
        return result


    #   runtime: beats 95%
    def combine_Lexicographic(self, n: int, k: int):
        #   first combination
        nums = list(range(1, k+1)) + [n+1]
        
        result = []
        j = 0

        while j < k:
            #   add current combination
            result.append(nums[:k])
            j = 0
            while j < k and nums[j+1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1

        return result

    

    #   runtime: beats 99%
    def combine_Itertools(self, n: int, k: int) -> List[List[int]]:
        values = list(range(1, n+1))
        result = [ list(x) for x in itertools.combinations(values, k) ]
        return result


    #   runtime: beats 90%
    def combine_ItertoolsEquivalent(self, n: int, k: int) -> List[List[int]]:

        def combinations(iterable, r):
            # combinations('ABCD', 2) --> AB AC AD BC BD CD
            # combinations(range(4), 3) --> 012 013 023 123
            pool = tuple(iterable)
            n = len(pool)
            if r > n:
                return
            indices = list(range(r))
            yield tuple(pool[i] for i in indices)
            while True:
                for i in reversed(range(r)):
                    if indices[i] != i + n - r:
                        break
                else:
                    return
                indices[i] += 1
                for j in range(i+1, r):
                    indices[j] = indices[j-1] + 1
                yield tuple(pool[i] for i in indices)

        values = list(range(1, n+1))
        result = [ list(x) for x in combinations(values, k) ]
        return result


s = Solution()

input_values = [ (4,2), (1,1), ]
input_checks = [ [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]], [[1]], ]

for (n, k), check in zip(input_values, input_checks):
    result = s.combine(n, k)
    print("result=(%s)" % str(result))
    assert sorted(result) == sorted(check), "Check failed"
    print()


