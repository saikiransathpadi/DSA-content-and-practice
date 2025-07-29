# 29 Jul


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        visited = set()
        islands = 0
        m = len(grid)
        n = len(grid[0])
        def fill_islands(i, j):
            visited.add((i,j))
            stack = [(i, j)]
            while stack:
                p1, p2 = stack.pop()
                if p1+1 < m and (p1 + 1, p2) not in visited and grid[p1+1][p2] == "1":
                    stack.append((p1 + 1, p2))
                    visited.add((p1 + 1, p2))
                if p2+1 < n and (p1, p2 + 1) not in visited and grid[p1][p2+1] == "1":
                    stack.append((p1, p2 + 1))
                    visited.add((p1, p2 + 1))
                if p1-1 >= 0 and (p1 - 1, p2) not in visited and grid[p1-1][p2] == "1":
                    stack.append((p1 - 1, p2))
                    visited.add((p1 - 1, p2))
                if p2-1 >=0 and (p1, p2 - 1) not in visited and grid[p1][p2-1] == "1":
                    stack.append((p1, p2 - 1))
                    visited.add((p1, p2 - 1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    print("initial", i, j)
                    islands += 1
                    fill_islands(i, j)
        
        return islands


input = [
    ["1","0","1","1","1"],
    ["1","0","1","0","1"],
    ["1","1","1","0","1"]
]

print(Solution().numIslands(input))