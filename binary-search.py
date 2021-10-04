#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
#   {{{2

def binary_search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums)-1

    while l <= r:
        mid = (r + l) // 2
        #   alternatively, less likely to overflow: 
        #   mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1

    return -1


def bsearch_find_left(nums: List[int], target: int) -> List[int]:
    """Get index of leftmost instance of 'target' in sorted list 'nums', or -1 if not found"""
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (r + l) // 2
        if nums[mid] == target:
            while mid-1 >= 0 and nums[mid-1] == target:
                mid = mid - 1
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    return -1


def bsearch_find_right(nums: List[int], target: int) -> List[int]:
    """Get index of rightmost instance of 'target' in sorted list 'nums', or -1 if not found"""
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (r + l) // 2
        if nums[mid] == target:
            while mid+1 < len(nums) and nums[mid+1] == target:
                mid = mid + 1
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    return -1


def test_binary_search():
    #   {{{
    input_values = [ ( [-1,0,3,5,9,12], 9 ), ( [-1,0,3,5,9,12], 2 ), ( [5], 5 ) ]
    input_checks = [ 4, -1, 0 ]
    for (nums, target), check in zip(input_values, input_checks):
        result = binary_search(nums, target)
        print("result=(%s)" % str(result))
        assert( result == check )
    #   }}}

def test_bsearch_find_ends():
    #   {{{
    input_values = [ ([5,7,7,8,8,10], 8), ([5,7,7,8,8,10], 6), ([], 0), ([1,2,3,3,3,4], 3), ([1], 1), ([1,1,2], 1), ]
    input_checks = [ [3,4], [-1,-1], [-1,-1], [2,4], [0,0], [0,1], ]
    for (nums, target), check in zip(input_values, input_checks):
        print("nums=(%s), target=(%s)" % (nums, target))
        #result = searchRange(nums, target)
        result = [ bsearch_find_left(nums, target), bsearch_find_right(nums, target) ]
        print("result=(%s)" % result)
        assert result == check, "Check failed"
    #   }}}


if __name__ == '__main__': 
    print("test_binary_search():")
    test_binary_search()
    print()
    print("test_bsearch_find_ends():")
    test_bsearch_find_ends()
    print()

