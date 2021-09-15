
def two_sum_twoPointers(nums: list, target: int) -> tuple:
    #   sort nums as 'nums_sorted', with 'indexes' giving the indexes of unsorted values such that: nums_sorted[indexes[i]] = nums[i]
    temp = sorted(zip(nums, range(0,len(nums))), key=lambda x: x[0])
    nums_sorted = [x[0] for x in temp]
    indexes = [x[1] for x in temp]
    i = 0
    j = len(nums_sorted)-1
    while i < j:
        trial = nums_sorted[i] + nums_sorted[j]
        if trial == target:
            return (indexes[i], indexes[j])
        elif trial < target:
            i += 1
        elif trial > target:
            j -= 1


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
    assert( result == check )

    result = two_sum_map(nums, target)
    assert( result == check )

    print("result=(%s)" % str(result))
    print()

