

def two_sum_twoPointers(nums: list, target: int) -> tuple:
    #   two-pointers approach requires 'nums' be sorted
    #   'nums_indexes' describes the map from 'nums' to 'nums_sorted': nums_sorted[nums_indexes[i]] = nums[i]
    nums_sorted, nums_indexes = zip( *sorted(zip(nums, range(0,len(nums))), key=lambda x: x[0]) )
    l = 0
    r = len(nums_sorted) - 1
    while l < r:
        trial = nums_sorted[l] + nums_sorted[r]
        if trial == target:
            return (nums_indexes[l], nums_indexes[r])
        elif trial < target:
            l += 1
        elif trial > target:
            r -= 1


def two_sum_map(nums: list, target: int) -> tuple:
    value_to_index = dict()
    for i, n in enumerate(nums):
        delta = target - n
        if delta in value_to_index.keys():
            return (value_to_index[delta], i)
        value_to_index[n] = i



input_values = [ ([2,7,11,15],9), ([3,2,4],6), ([3,3],6) ]
input_check = [ (0,1), (1,2), (0,1) ]

for (nums, target), check in zip(input_values, input_check):
    print("nums=(%s), target=(%s)" % (str(nums), str(target)))
    result = two_sum_twoPointers(nums, target)
    assert result == check, "Check failed i" 
    result = two_sum_map(nums, target)
    assert result == check, "Check failed ii"
    print("result=(%s)" % str(result))
    print()

