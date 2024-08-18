class Solution:

    def factorial(self, n):
        if n <= 1:
            return 1
        return n * self.factorial(n-1)
    def uniquePaths(self, m: int, n: int) -> int:
        nc = m+n-2
        r = min(m-1,n-1)

        return int(self.factorial(nc) /( self.factorial(nc-r) * self.factorial(r)))

print(Solution().uniquePaths(3,7))

