from typing import List

# Revisit for Union Find algorithm

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        total = 0

        visited = set()

        nei_hash = {i: [] for i in range(n)}

        for i in edges:
            nei_hash[i[0]].append(i[1])
            nei_hash[i[1]].append(i[0])

        def dfs(cur, prev):
            if cur in visited:
                return

            visited.add(cur)
            for c in nei_hash[cur]:
                if c != prev:
                    dfs(c, cur)
        
        for i in range(n):
            if i not in visited:
                total +=1
                dfs(i, -1)
        return total
            


n=3
edges=[[0,1],[0,2],[1,2]]
print(Solution().countComponents(n, edges))
