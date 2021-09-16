
class Solution:

    def rotate(self, nums: list[int], k: int):
        """Rotate 'nums' right 'k' steps, in-place"""
        if k < 0: raise Exception("invalid negative k=(%s)" % str(k))
        #self.rotate_A(nums, k)
        #self.rotate_B(nums, k)
        #self.rotate_C(nums, k)
        #self.rotate_D(nums, k)
        #self.rotate_E(nums, k)
        #self.rotate_F(nums, k)
        #self.rotate_G(nums, k)
        #self.rotate_H(nums, k)
        self.rotate_I(nums, k)

    def rotate_A(self, nums: list[int], k: int):
        for i in range(k):
            temp = nums.pop()
            nums[:] = [ temp ] + nums[:]

    def rotate_B(self, nums: list[int], k: int):
        result = [ None for i in range(len(nums)) ]
        for i in range(len(nums)):
            j = i - k
            while j < 0: 
                j += len(nums)
            result[i] = nums[j]
        nums[:] = result[:]

    def rotate_C(self, nums: list[int], k: int):
        while k > len(nums):
            k -= len(nums)
        A = nums[::-1]
        B = A[k:] + A[:k]
        nums[:] = B[::-1]

    def rotate_D(self, nums: list[int], k: int):
        nums[:] = [ nums[(i-k)%len(nums)] for i, x in enumerate(nums) ]

    def rotate_E(self, nums: list[int], k: int):
        from collections import deque
        temp = deque(nums)
        temp.rotate(k)
        nums[:] = list(temp)

    def rotate_F(self, nums: list[int], k: int):
        n = len(nums)
        k = k % len(nums)
        j = 0
        while n > 0 and k % n != 0:
            for i in range(k):
                nums[j+i], nums[len(nums)-k+i] = nums[len(nums)-k+i], nums[j+i]
            n = n - k
            j = j + k
            k = k % n

    def rotate_G(self, nums: list[int], k: int):
        k = k % len(nums)
        for i in range(k):
            temp = nums[-1]
            for j in range(len(nums)-1):
                nums[len(nums)-1-j] = nums[len(nums)-2-j]
            nums[0] = temp

    def rotate_H(self, nums: list[int], k: int):
        k = k % len(nums)
        if k == 0: 
            return
        #nums.reverse()
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]

    def rotate_I(self, nums: list[int], k: int):
        n = len(nums)
        if n == 0: 
            return
        while k % n > 0 and n > 1:
            k = k % n
            z = n - k
            for i in range(1, z+1):
                val = nums[n-i]
                nums[n-i] = nums[n-i-k]
                nums[n-i-k] = val
            n = k
            k = n - (z % k)


s = Solution()

input_values = [ ( [1,2,3,4,5,6,7], 3 ), ( [-1,-100,3,99], 2 ), ([1,2], 5) ]
input_checks = [ [5,6,7,1,2,3,4], [3,99,-1,-100], [2,1] ]

for (nums, k), check in zip(input_values, input_checks):
    s.rotate(nums, k)
    print("nums=(%s)" % str(nums))
    assert( nums == check )
    print()


