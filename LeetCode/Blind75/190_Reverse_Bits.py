# 26 July

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)[2:]
        print(binary)

        rem = 32-len(binary)
        binary = ("0" * rem) + binary
        print(binary[-1::-1])
        rev = int(binary[-1::-1], base=2)
        return rev

n = 2
print(Solution().reverseBits(n))

# Optimized solution
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):
            result <<= 1
            result |= (n & 1)
            n >>= 1
        return result

# divide and conquer solution
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = (n >> 16) | (
            (n & 0x0000FFFF) << 16)
        n = ((n >> 8) & 0x00FF00FF) | (
            (n & 0x00FF00FF) << 8)
        n = ((n >> 4) & 0x0F0F0F0F) | (
            (n & 0x0F0F0F0F) << 4)
        n = ((n >> 2) & 0x33333333) | (
            (n & 0x33333333) << 2)
        n = ((n >> 1) & 0x55555555) | (
            (n & 0x55555555) << 1)
        return n
n = 2
print(Solution().reverseBits(n))



    