class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]

        for i in range(1, n+1):
            bit = i & 1
            ans.append(ans[i >> 1] + bit)
        return ans

inps = [2, 5, 100]
for inp in inps:
    print(Solution().countBits(inp))