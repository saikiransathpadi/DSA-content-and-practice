from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        currMin = nums[0]

        i = 0
        j = len(nums) - 1
        while  i <= j:
            mid = (i + j) // 2

            if nums[i] <= nums[mid]:
                currMin = min(currMin, nums[i])
                i = mid + 1
            else:
                currMin = min(currMin, nums[mid])
                j = mid - 1
        return currMin


print(Solution().findMin([11,13,15,17]))