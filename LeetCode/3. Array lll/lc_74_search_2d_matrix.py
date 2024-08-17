from typing import List

class Solution:
    def binary_search(self, arr, target):
        """"""
        l = 0
        h = len(arr) -1
        while l <= h:
            mid = (l+h) //2
            if arr[mid] == target:
                return True
            
            elif arr[mid] > target:
                h = mid-1
            else:
                l = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """"""

        l = 0
        h = len(matrix) -1

        needed = None

        while l <= h:
            mid_ind = (l+h)//2
            mid = matrix[mid_ind]

            if mid[0] <= target and mid[-1] >= target:
                needed = mid
                break

            elif target < mid[0]:
                h = mid_ind - 1
            elif target > mid[-1]:
                l = mid_ind + 1
        
        if not needed:
            print("Matrix not found")
            return False

        return self.binary_search(needed, target)


print(Solution().searchMatrix([[1]], 1))