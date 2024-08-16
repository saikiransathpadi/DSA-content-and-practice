from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge Intervals
        """
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        output = [intervals[0]]

        for i in range(1, len(intervals)):
            left = output[-1]
            right = intervals[i]

            if left[1] < right[0]:
                output.append(right)
            elif left[1] >= right[0]:
                output[-1] = [left[0], max(left[1], right[1])]
        return output

print(Solution().merge([[1,3]]))

# 1,4
# 1,3 2,4
# 1,4 2,3

# 1, 7

# 1,3 2,9
