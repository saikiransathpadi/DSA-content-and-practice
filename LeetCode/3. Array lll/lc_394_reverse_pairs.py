from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """"""
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    count += 1
        
        return count


print(Solution().reversePairs([2,4,3,5,1]))



def merge_sort_algo(arr, l, h):
    pass


def merge_sort(arr: list):
    sorted_arr = []


