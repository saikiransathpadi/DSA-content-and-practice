from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        rob1, rob2 = 0, 0

        for n in nums[:-1]:
            tem =rob2
            rob2 = max(rob2, n + rob1)
            rob1 = tem
        
        n1, n2 = 0, 0

        for n in nums[1:]:
            tem =n2
            n2 = max(n2, n + n1)
            n1 = tem
        return max(rob2, n2)
