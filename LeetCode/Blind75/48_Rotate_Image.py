from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def rev(arr):
            i = 0
            j = len(arr) - 1
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i+= 1
                j-= 1

        i = 0
        r = len(matrix)
        while i < r:
            for j in range(i, r):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            i += 1
        print(matrix)
        for arr in matrix:
            rev(arr)
        

m = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(m)
print(m)