class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        i = 0
        j = len(height) - 1
        max_h = 0
        while i < j:
            max_h = max(
                max_h,
                (
                    (j-i) * min (height[j], height[i])
                )
            )
            if height[i] < height[j]:
                i += 1
            else: 
                j-= 1
        return max_h

print(Solution().maxArea([1,2,3,4,5]))