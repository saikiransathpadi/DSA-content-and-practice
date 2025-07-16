# 16 Jul 2025

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        starts = {}
        all = {}

        for i in nums:
            all[i] = i
        
        for i in all:
            if i-1 not in all:
                starts[i] = i
        
        res = 0
        for i in starts:
            tempc = 1
            temInd = i
            while True:
                if temInd + 1 in all:
                    tempc += 1
                else:
                    break
                temInd += 1
            res = max(res, tempc)
        return res


inp = [0,0]
print(Solution().longestConsecutive(inp))