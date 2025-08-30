from typing import List
from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        neighbours = {i: [] for i in range(n)}

        for i in edges:
            neighbours[i[0]].append(i[1])
            neighbours[i[1]].append(i[0])
        

        def dfs(i, prev):
            if i in visited: return False
            visited.add(i)

            for j in neighbours[i]:
                if j != prev:
                    if not dfs(j, i):
                        False
            return True
        if  dfs(0, -1) and len(visited) == n:
            return True
        return False


