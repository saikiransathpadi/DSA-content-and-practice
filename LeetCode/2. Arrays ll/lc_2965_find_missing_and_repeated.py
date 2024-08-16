# https://leetcode.com/problems/find-missing-and-repeated-values/description/
# https://www.interviewbit.com/problems/repeat-and-missing-number-array/

from typing import List

class Solution:
    def sum_of_n(self, n):
        return n * (n + 1) // 2

    def sum_of_squares_of_n(self, n):
        return n * (n + 1) * (2 * n + 1) // 6
    
    def sum_of_array(self, arr):
        return sum(arr)

    def sum_of_squares_of_array(self, arr):
        return sum(x * x for x in arr)

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """"""
        final = []

        [final.extend(i) for i in grid]

        # [1, 3, 2, 2]

        n_sum = self.sum_of_n(len(final))
        n2_sum = self.sum_of_squares_of_n(len(final))

        arr_sum = self.sum_of_array(final)
        arr2_sum = self.sum_of_squares_of_array(final)

        minus = n_sum - arr_sum
        minus2 = n2_sum - arr2_sum

        plus = minus2 // minus

        a = (plus + minus) // 2

        b = a - minus

        return b, a


    
print(Solution().findMissingAndRepeatedValues([[1,3],[2,2]]))
print(Solution().findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))


# need to learn bit manipulation solution for this