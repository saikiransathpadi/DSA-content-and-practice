class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myhash = {}
        for i in range(len(nums)):
            myhash[nums[i]] = i
        
        for i in range(len(nums)):
            if target- nums[i] in myhash and i != myhash[target- nums[i]]:
                return i, myhash[target- nums[i]]


nums = [3,3]
target = 6

print(Solution().twoSum(nums, target))