from typing import List

class Solution:
    def reverse(self, nums, start, end):
        """Reverse in place Based on index"""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start +=1
            end -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dipIndex = None
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                dipIndex = i-1
                break
        print(dipIndex)

        if dipIndex is None:
            self.reverse(nums, 0, len(nums)-1)
            return nums

        nextBig = None

        for i in range(len(nums)-1, dipIndex, -1):
            print("inside dipp", i, dipIndex)
            if nums[i] > nums[dipIndex]:
                nextBig = i
                break
        print(nextBig)

        nums[nextBig], nums[dipIndex] = nums[dipIndex], nums[nextBig]

        self.reverse(nums, dipIndex+1, len(nums)-1)
        print(nums)
        


print(Solution().nextPermutation([1,3,2]))
