from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """"""
        if not intervals: return [newInterval]
        inserted = False

        newInters = []
        if newInterval[0] <= intervals[0][0]:
            newInters = [newInterval, *intervals]
        else:
            for i in intervals:
                if not inserted and newInterval[0] <= i[0]:
                    newInters.append(newInterval)
                    newInters.append(i)
                    inserted = True
                else:
                    newInters.append(i)
            if not inserted:
                newInters.append(newInterval)
        
        intervals = newInters

        output = [intervals[0]]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            latest = output[-1]


            if latest[-1] >= curr[0]:
                latest[-1] = max(latest[-1], curr[-1])
            else:
                output.append(curr)
        return output


intervals = [[1,5]]
newInterval = [1,7]
print(Solution().insert(intervals, newInterval))