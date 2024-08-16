# https://leetcode.com/problems/missing-number/description/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        return ((length * (length + 1)) / 2) - sum(nums)