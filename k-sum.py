from typing import List

def twoSum_Map(nums: List[int], target: int) -> List[List[int]]:
    result = set()
    seen = dict()
    for i, x in enumerate(nums):
        delta = target - x
        if delta in seen:
            result.add( ( delta, x ) )
        seen[x] = i
    return [ list(sorted(x)) for x in result ]


def twoSum_TwoPointers(nums: List[int], target: int) -> List[List[int]]:
    nums = sorted(nums)
    result = set()
    l = 0
    r = len(nums)-1
    while l < r:
        trial = nums[l] + nums[r]
        if trial == target:
            result.add( ( nums[l], nums[r] ) )
            l += 1
            r -= 1
        elif trial > target:
            r -= 1
        elif trial < target:
            l += 1
    return [ list(sorted(x)) for x in result ]


def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
    assert k >= 2
    if len(nums) == 0:
        return []
    #result = set()
    result = []
    if k == 2:
        return twoSum_Map(nums, target)
    for i in range(len(nums)):
        delta = target - nums[i]
        #   Ongoing: 2022-09-11T00:21:21AEST question of the exercise - why this works without first half of list [...] (we would be getting duplicate answers with it, except for the fact we sort each list and use sets to eliminate duplicates?) (without it, there are no duplicates even if we do not use sets), (x[0] has already been checked against x[1:] so x[1] does not need to be checked against x[0]?)
        #sublist = nums[:i] + nums[i+1:]
        sublist = nums[i+1:]
        for p in kSum(sublist, delta, k - 1):
            if len(p) > 0:
                #result.add( ( nums[i], *p ) )
                result.append( ( nums[i], *p ) )
    return [ list(sorted(x)) for x in result ]


def kSum_Optimised(nums: List[int], target: int, k: int) -> List[List[int]]:
    raise NotImplementedError()


def twoSumIndex(nums: List[int], target: int) -> List[List[int]]:
    raise NotImplementedError()


def kSumIndex(nums: List[int], target: int, k: int) -> List[List[int]]:
    raise NotImplementedError()


def test_twoSum():
    test_functions = [ twoSum_Map, twoSum_TwoPointers, ]
    input_values = [ ([2,7,11,15],9), ([3,2,4],6), ([3,3],6), ([1,2,3], 27), ([9,7,5,3,1,2], 5), ]
    result_validation = [ [[2,7]], [[2,4]], [[3,3]], [], [[2,3]], ]
    assert len(input_values) == len(result_validation)
    for f in test_functions:
        print(f.__name__)
        for (nums, target), check in zip(input_values, result_validation):
            print("nums=(%s), target=(%s)" % (nums, target))
            result = f(nums, target)
            print("result=(%s)" % result)
            assert all( [ x in check for x in result ] ), "Check comparison failed i"
            assert all( [ x in result for x in check ] ), "Check comparison failed ii"
        print()


def test_twoSumIndex():
    raise NotImplementedError()


def test_kSum_4():
    test_functions = [ kSum, kSum_Optimised, ]
    k = 4
    input_values = [ ([1,0,-1,0,-2,2], 0), ([2,2,2,2,2], 8), ([1,0,-1,0,-2,2], 0), ]
    result_validation = [ [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]], [[2,2,2,2]], [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]], ]
    assert len(input_values) == len(result_validation)
    for f in test_functions:
        print(f.__name__)
        for (nums, target), check in zip(input_values, result_validation):
            print("nums=(%s), target=(%s), k=(%s)" % (nums, target, k))
            result = f(nums, target, k)
            print("result=(%s)" % result)
            assert all( [ x in check for x in result ] ), "Check comparison failed i"
            assert all( [ x in result for x in check ] ), "Check comparison failed ii"
        print()


def test_kSumIndex():
    raise NotImplementedError()


if __name__ == '__main__':
    test_twoSum()
    test_kSum_4()

