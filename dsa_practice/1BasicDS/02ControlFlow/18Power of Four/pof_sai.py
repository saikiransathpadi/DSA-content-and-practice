class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        curr = 1
        while curr<=n:
            if n == curr:
                return True
            curr*=4
        return False