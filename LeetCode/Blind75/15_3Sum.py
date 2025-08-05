class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        m = 0
        while m < len(nums):
            if m > 0 and nums[m-1] == nums[m]:
                m += 1
                continue

            i = m + 1
            j = len(nums) - 1

            while i < j:
                sum3 = nums[m] + nums[i] + nums[j]
                if sum3 == 0:
                    res.append([nums[m], nums[i], nums[j]])
                    i += 1
                    while nums[i] == nums[i-1] and i < len(nums):
                        i +=1
                elif sum3 > 0:
                    j -= 1
                elif sum3 < 0:
                    i += 1
            
            m += 1
        return res
        



        

print("==>",Solution().threeSum([-1,0,1,2,-1,-4]))
print("==>",Solution().threeSum([-2,0,1,1,2]))
# inp = [8,5,12,3,-2,-13,-8,-9,-8,10,-10,-10,-14,-5,-1,-8,-7,-12,4,4,10,-8,0,-3,4,11,-9,-2,-7,-2,3,-14,-12,1,-4,-6,3,3,0,2,-9,-2,7,-8,0,14,-1,8,-13,10,-11,4,-13,-4,-14,-1,-8,-7,12,-8,6,0,-15,2,8,-4,11,-4,-15,-12,5,-9,1,-2,-10,-14,-11,4,1,13,-1,-3,3,-7,9,-4,7,8,4,4,8,-12,12,8,5,5,12,-7,9,4,-12,-1,2,5,4,7,-2,8,-12,-15,-1,2,-11]
# print("==>",Solution().threeSum(inp))