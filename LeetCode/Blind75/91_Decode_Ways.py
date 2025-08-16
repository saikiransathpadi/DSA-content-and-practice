class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        dp = {}
        alpha_map = {str(i): chr(96 + i) for i in range(1, 27)}

        def dfs(cur):
            if cur >= l:
                return 1
            
            if cur in dp:
                return dp[cur]
            
            if s[cur] not in alpha_map and (cur + 1 < l and (s[cur] + s[cur+1]) not in alpha_map):
                return 0

            x = 0
            y = 0
            if s[cur] in alpha_map:
                x = dfs(cur+1)
            
            if (cur + 1 < l and (s[cur] + s[cur+1]) in alpha_map):
                y = dfs(cur + 2)

            dp[cur] = x+y

            return x+y
        return dfs(0)
    
print(Solution().numDecodings("226"))