# 31 Jul

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        preq_map = {i: [] for i in range(numCourses)}
        for preq in prerequisites:
            preq_map[preq[0]].append(preq[1])
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if preq_map[crs] == []:
                return True
            visited.add(crs)
            for each in preq_map[crs]:
                if not dfs(each): return False
            
            visited.remove(crs)
            preq_map[crs] = []
            return True

        for each in prerequisites:
            if not dfs(each[0]): return False
        return True
    
print(Solution().canFinish(5, [[1,0],[2,3], [3,4]]))
            