class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3: return len(nums)
        for i in range(len(nums)):
            nums[i] = nums[i] % 2

        count0 = 0
        count1 = 0
        for i in nums:
            if i == 1:
                count1 += 1
            if i == 0:
                count0 += 1
        
        countalt = 1

        j = 0
        while j < len(nums):
            if nums[j] == 1:
                j += 1
                while j < len(nums) and nums[j] !=0:
                    j += 1
                if j < len(nums) and nums[j] == 0:
                    countalt += 1
            elif nums[j] == 0:
                j += 1
                while j < len(nums) and nums[j] !=1:
                    j += 1
                if j < len(nums) and nums[j] == 1:
                    countalt += 1
        print(count0, count1, countalt, nums)
        return max(count0, count1, countalt)


input = [4,2,6]
print(Solution().maximumLength(input))