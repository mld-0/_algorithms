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
        #   alternatively: 
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
        #   alternatively: 
        #   mid = l + (r - l) // 2
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
        #   alternatively: 
        #   mid = l + (r - l) // 2
        if nums[mid] == target:
            while mid+1 < len(nums) and nums[mid+1] == target:
                mid = mid + 1
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    return -1


def bsearch_findMin(nums: List[int]) -> int:
    """Binary search for index about which sorted list 'nums' has been rotated (index of min element)"""
    l = 0
    r = len(nums) - 1
    if len(nums) == 1:
        return nums[0]
    if nums[l] < nums[r]:
        return nums[l]
    while l <= r:
        mid = l + (r - l) // 2
        #   alternatively: 
        #   mid = l + (r - l) // 2
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        if nums[mid-1] > nums[mid]:
            return nums[mid]
        if nums[l] < nums[mid]:
            l = mid + 1
        else:
            r = mid - 1

#   bsearch leftmost insertion point:
#   {{{
#         BinarySearch_Left(A[0..N-1], value) {
#             low = 0
#             high = N - 1
#             while (low <= high) {
#                 // invariants: value > A[i] for all i < low
#                                value <= A[i] for all i > high
#                 mid = (low + high) / 2
#                 if (A[mid] >= value)
#                     high = mid - 1
#                 else
#                     low = mid + 1
#             }
#             return low
#         }
#   }}}
#   bsearch rightmost insertion point:
#   {{{
#         BinarySearch_Right(A[0..N-1], value) {
#             low = 0
#             high = N - 1
#             while (low <= high) {
#                 // invariants: value >= A[i] for all i < low
#                                value < A[i] for all i > high
#                 mid = (low + high) / 2
#                 if (A[mid] > value)
#                     high = mid - 1
#                 else
#                     low = mid + 1
#             }
#             return low
#         }
#   }}}


def test_binary_search():
    #   {{{
    input_values = [ ( [-1,0,3,5,9,12], 9 ), ( [-1,0,3,5,9,12], 2 ), ( [5], 5 ) ]
    input_checks = [ 4, -1, 0 ]
    for (nums, target), check in zip(input_values, input_checks):
        result = binary_search(nums, target)
        print("result=(%s)" % str(result))
        assert result == check, "Check failed"
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

def test_bsearch_findMin():
    #   {{{
    input_values = [ [3,4,5,1,2], [4,5,6,7,0,1,2], [11,13,15,17], [1,2], [2,3,4,5,6,1], [284,287,289,293,295,298,0,3,8,9,10,11,12,15,17,19,20,22,26,29,30,31,35,36,37,38,42,43,45,50,51,54,56,58,59,60,62,63,68,70,73,74,81,83,84,87,92,95,99,101,102,105,108,109,112,114,115,116,122,125,126,127,129,132,134,136,137,138,139,147,149,152,153,154,155,159,160,161,163,164,165,166,168,169,171,172,174,176,177,180,187,188,190,191,192,198,200,203,204,206,207,209,210,212,214,216,221,224,227,228,229,230,233,235,237,241,242,243,244,246,248,252,253,255,257,259,260,261,262,265,266,268,269,270,271,272,273,277,279,281], [1], ]
    input_checks = [ min(x) for x in input_values ]
    for nums, check in zip(input_values, input_checks):
        print("nums=(%s)" % nums)
        result = bsearch_findMin(nums)
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
    print("test_bsearch_findMin():")
    test_bsearch_findMin()
    print()

