from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]

        for ind in range(1, len(intervals)):
            interval = intervals[ind]
            latest = output[-1]
            if latest[-1] >= interval[0]:
                latest[-1] = max(latest[-1], interval[-1])
            else:
                output.append(interval)
        
        return output


inter = [[1,4],[2,3],[8,10],[15,18]]

print(Solution().merge(inter))