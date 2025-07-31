import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

        myheap = []
        left = right = nums[0][0]
        for i in range(len(nums)):
            left = min(left, nums[i][0])
            right = max(right, nums[i][0])
            heapq.heappush(myheap, (nums[i][0], i, 0))
        
        res = [left, right]
        while True:
            num, arr, idx = heapq.heappop(myheap)

            idx += 1
            if idx == len(nums[arr]):
                break

            heapq.heappush(myheap, (nums[arr][idx], arr, idx))

            right = max(right, nums[arr][idx])
            left = myheap[0][0]
            if right - left < res[1] - res[0]:
                res = [left, right]
        return res


inp = [[1,2,3],[1,2,3],[1,2,3]]
print(Solution().smallestRange(inp))

        