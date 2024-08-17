from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """"""
        count1 = 0
        count2 = 0
        ele1 = None
        ele2 = None
        for i in range(0, len(nums)):
            if count1 == 0 and ele2 != nums[i]:
                ele1 = nums[i]
            elif count2 == 0 and ele1 != nums[i]:
                ele2 = nums[i]
            if nums[i] == ele1:
                count1 += 1
            elif nums[i] == ele2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        print(ele1, ele2, count1, count2)
        c1 = 0
        c2 = 0
        res = []
        for i in nums:
            if i == ele1:
                c1+= 1
            elif i == ele2:
                c2 += 1
        if c1 > len(nums)//3:
            res.append(ele1)
        if c2 > len(nums)//3:
            res.append(ele2)
        return res


print(Solution().majorityElement([1,1,1,2,3,7,8,1,6,9]))