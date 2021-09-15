import sys
import logging
import functools
import itertools
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def two_sum_multiple_usingMap(nums: list, target: int) -> tuple:
    result = set()
    value_to_index = dict()
    for i, n in enumerate(nums):
        delta = target - n
        if delta in value_to_index.keys():
            a = nums[value_to_index[delta]]
            b = nums[i]
            result.add((a, b))
        value_to_index[n] = i
    return result


def three_sum_usingTwoSum(nums: list[int], target) -> list[tuple[int]]:
    result = set()
    for i in range(len(nums)):
        delta = target - nums[i]
        loop_nums = nums[:i] + nums[i+1:]
        loop_results = two_sum_multiple_usingMap(loop_nums, delta)
        for loop_result in loop_results:
            loop_combination = list(loop_result) + [ nums[i] ] 
            result.add(tuple(sorted(loop_combination)))
    return result


def three_sum_naive(nums: list[int], target) -> list[tuple[int]]:
    result = set()
    for loop_combination in itertools.combinations(nums, 3):
        if sum(loop_combination) == target:
            result.add(tuple(sorted(loop_combination)))
    return result


def three_sum_twoPointer(nums: list[int], target) -> list[tuple[int]]:
    nums = sorted(nums)
    result = set()

    for i in range(len(nums)-2):
        l = i + 1
        r = len(nums) - 1

        while l < r:
            trial = nums[i] + nums[l] + nums[r]
            if trial == target:
                loop_combination = (nums[i], nums[l], nums[r])
                result.add(tuple(sorted(loop_combination)))
                l += 1
                r -= 1
            elif trial < target:
                l += 1
            elif trial > target:
                r -= 1

    return result


def three_sum_twoPointer_optimised(nums: list[int], target) -> list[tuple[int]]:
    nums = sorted(nums)
    result = set()

    for i in range(len(nums)-2):
        l = i + 1
        r = len(nums) - 1

        if i > 0 and nums[i] == nums[i-1]:
            continue
        if nums[i] > target:
            break

        while l < r:
            trial = nums[i] + nums[l] + nums[r]
            if trial == target:
                loop_combination = (nums[i], nums[l], nums[r])
                result.add(tuple(sorted(loop_combination)))

                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1

                l += 1
                r -= 1
            elif trial < target:
                l += 1
            elif trial > target:
                r -= 1

    return result



input_values = [ ([-1,0,1,2,-1,-4], 0), ([], 0), ([0], 0), ([-1,0,1,2,-1,-4,-2,-3,3,0,4], 0) ]
input_checks = [ set([(-1,-1,2), (-1,0,1)]), set(), set(), set([(-4,0,4), (-4,1,3), (-3,-1,4), (-3,0,3), (-3,1,2), (-2,-1,3), (-2,0,2), (-1,-1,2), (-1,0,1)]) ]

for (nums, target), check in zip(input_values, input_checks):
    print("nums=(%s), target=(%s)" % (str(nums), str(target)))

    result = three_sum_naive(nums, target)
    #print("result=(%s)" % str(result))
    assert( result == check )

    result = three_sum_usingTwoSum(nums, target)
    #print("result=(%s)" % str(result))
    assert( result == check )

    result = three_sum_twoPointer(nums, target)
    #print("result=(%s)" % str(result))
    assert( result == check )

    result = three_sum_twoPointer_optimised(nums, target)
    print("result=(%s)" % str(result))
    assert( result == check )

    print()

