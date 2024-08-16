# https://leetcode.com/problems/find-the-duplicate-number/description/
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        """
        set_nums = set()
        for i in nums:
            if i in set:
                return i
            else :
                set_nums.add(i)

        



# Need to learn optimal solution sooner

from typing import List
def findDuplicate(nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


if __name__ == "__main__":
    arr = [1, 3, 4, 2, 3]
    print("The duplicate element is ", findDuplicate(arr))
