
def binary_search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums)-1

    while l <= r:
        mid = (r + l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1

    return -1


input_values = [ ( [-1,0,3,5,9,12], 9 ), ( [-1,0,3,5,9,12], 2 ), ( [5], 5 ) ]
input_checks = [ 4, -1, 0 ]

for (nums, target), check in zip(input_values, input_checks):
    result = binary_search(nums, target)
    print("result=(%s)" % str(result))
    assert( result == check )
    print()

