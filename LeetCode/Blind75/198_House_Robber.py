from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        last1, last2 = 0, 0

        for i in nums:
            temp = last2
            last2 = max(i + last1, last2)
            last1 = temp
        
        return last2
