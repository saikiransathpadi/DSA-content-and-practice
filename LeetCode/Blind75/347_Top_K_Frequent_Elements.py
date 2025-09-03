from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myheap = []

        my_hash = {}
        for i in nums:
            if i not in my_hash:
                my_hash[i] = 0
            my_hash[i] += 1
        
        for i in my_hash:
            heapq.heappush(myheap, (-my_hash[i], i))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(myheap)[1])
        
        return res


nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))