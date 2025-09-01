from typing import List 

# Note: when revisit learn DP n^2 solution

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]
        res_len = 1

        for i in range(1, len(nums)):
            if nums[i] > res[-1]:
                res.append(nums[i])
                res_len += 1
            else:
                print(res)
                res[self.bs_position(res, nums[i], res_len)] = nums[i]
                print(res)
        return res_len

    def bs_position(self, arr, ele, n):
        l = 0
        h = n - 1
        while l < h:
            m = (l+h) // 2
            if arr[m] == ele:
                return m
            elif arr[m] < ele:
                l = m + 1
            else:
                h = m - 1
        if arr[l] < ele and l < n-1:
            return l+1
        return l
    



nums = [3,5,6,2,5,4,19,5,6,7,12]
print(Solution().lengthOfLIS(nums))

# 2 4 5 6 7 12