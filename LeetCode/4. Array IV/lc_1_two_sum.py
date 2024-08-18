from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = []
            hash[nums[i]].append(i)
        
        for i in nums:
            if target-i in hash and hash[i]:
                a,b = ( hash[i][0], hash[target-i][-1])
                if a != b:
                    return [a, b]
    

print(Solution().twoSum([3,3], 6))

# sorting and two pointer and one more optimal

