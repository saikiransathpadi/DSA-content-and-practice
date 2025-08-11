from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Max Subarray"""

        curr = 0
        maxi = curr
        
        if max(nums) < 0: return max(nums)
        
        for i in nums:
            curr += i
            if curr < 0:
                curr = 0
            maxi = max(maxi, curr)
        return maxi


print(Solution().maxSubArray(nums = [-1,-2,-3,-4]))
