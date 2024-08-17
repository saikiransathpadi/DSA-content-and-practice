from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_map = {}
        for i in nums:
            if i not in my_map:
                my_map[i] = 0
            my_map[i] += 1

            if my_map[i] >len(nums)//2:
                return i
            
    def majorityElementOptimal(self, nums):
        """"""
        count = 1
        ele = nums[0]
        for i in range(1, len(nums)):
            if count == 0:
                ele = nums[i]
            if nums[i] == ele:
                count += 1
            else:
                count -= 1
        return ele
    
print(Solution().majorityElementOptimal([3,2,3,2,2,3, 2]))
