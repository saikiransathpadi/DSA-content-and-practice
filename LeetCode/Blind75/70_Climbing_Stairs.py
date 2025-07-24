# 24 July

class Solution(object):
    def climbStairs(self, n, mem={}):
        """
        :type n: int
        :rtype: int
        """
        if n in mem:
            return mem[n]
        if n == 0:
            return 1
        if n < 0:
            return 0
        step1 = self.climbStairs(n-1, mem)
        if n-1 not in mem:
            mem[n-1] = step1
        step2 = self.climbStairs(n-2, mem)
        if n-2 not in mem:
            mem[n-2] = step2
        return step1 + step2
        


print(Solution().climbStairs(45))