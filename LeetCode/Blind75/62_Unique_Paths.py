class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        def dfs(i, j):
            if i == m-1 and j == n-1:
                return 1
            if i >=m or j >= n:
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            right =  dfs(i, j+1)
            dp[(i, j+1)] = right
            down = dfs(i+1, j)
            dp[(i+1, j)] = down

            return right + down

        return dfs(0,0)


print(Solution().uniquePaths(3, 7))