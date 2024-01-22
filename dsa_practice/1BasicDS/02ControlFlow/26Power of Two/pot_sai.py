class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        curr = 1
        while curr<=n:
            if n == curr:
                return True
            curr*=2
        return False