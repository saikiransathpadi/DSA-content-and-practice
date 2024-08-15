from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Max Subarray"""

        max_sum = 0
        current_sum = 0
        start = 0
        end = None

        for i in nums:
            current_sum += i
            if current_sum < 0:
                current_sum = 0
            max_sum = max(max_sum, current_sum)
        
        if max(nums) < 0:
            return max(nums)
        return max_sum


print(Solution().maxSubArray([-1]))