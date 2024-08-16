from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Transpose
        for i in range(len(matrix)):
            for j in range(i):
                # print(matrix)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        print(matrix)
        for i in matrix:
            self.reverse(i)
        
        print(matrix)

    def reverse(self, arr):
        i = 0
        j = len(arr)-1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1


Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])