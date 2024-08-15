from pprint import pprint

class Solution:
    def recur_permute(self, ds, nums, ans, freq):
        if len(ds) == len(nums):
            ans.append(ds[:])  # append a copy of ds
            return
        
        for i in range(len(nums)):
            if not freq[i]:
                ds.append(nums[i])
                freq[i] = 1
                self.recur_permute(ds, nums, ans, freq)
                freq[i] = 0
                ds.pop()

    def permute(self, nums):
        ans = []
        ds = []
        freq = [0] * len(nums)
        self.recur_permute(ds, nums, ans, freq)
        return ans
    
    def recur2(self, index, nums, ans):
        if index >= len(nums):
            ans.append(nums[:])
            return
        
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.recur2(index+1, nums, ans)
            # nums[i], nums[index] = nums[index], nums[i]
    
    def permute2(self, nums):
        ans = []
        self.recur2(0, nums, ans)
        pprint(ans)

# Example usage:
solution = Solution()
pprint(solution.permute([1, 2, 3, 4 ]))
