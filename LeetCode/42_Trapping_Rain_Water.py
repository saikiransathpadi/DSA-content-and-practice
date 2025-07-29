class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """ 
        if len(height) <= 2:
            return 0
        maxl = []
        maxr = []
        l = len(height)
        for i in range(l):
            if not maxl:
                maxl.append(height[i])
                maxr.append(height[l-i - 1])
            else:
                maxl.append(max(height[i], maxl[-1]))
                maxr.append(max(height[l-i - 1], maxr[-1]))
        
        maxr = maxr[-1::-1]
        water = 0
        for i in range(l):
            water += max(min(maxl[i], maxr[i]) - height[i], 0)
        return water

inps = [
    [0,1,0,2,1,0,1,3,2,1,2,1],
    [4,2,0,3,2,5],
    [3,2,1,2,1]
]
for inp in inps:
    print(Solution().trap(inp))