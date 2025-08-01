class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        preq_map = {i: [] for i in range(numCourses)}
        for preq in prerequisites:
            preq_map[preq[0]].append(preq[1])
        visited = set()
        taken = []
        for i in preq_map:
            if preq_map[i] == []:
                taken.append(i)
        def dfs(crs):
            if crs in visited:
                return []
            if preq_map[crs] == []:
                if crs not in taken:
                    taken.append(crs)
                return True
            visited.add(crs)
            for each in preq_map[crs]:
                if not dfs(each): return []
            
            visited.remove(crs)
            preq_map[crs] = []
            if crs not in taken:
                taken.append(crs)
            return True

        for each in prerequisites:
            if not dfs(each[0]): return []
        
        return taken
        