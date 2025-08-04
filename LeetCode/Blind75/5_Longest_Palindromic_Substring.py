# 4 Aug


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindrome(ip, i, j):
            while i < j:
                if ip[i] != ip[j]:
                    return False
                i += 1
                j -= 1
            return True
        max = 0
        st,e = 0,0
        l = len(s)
        for i in range(len(s)):
            for j in range(len(s)-1, i, -1):
                # print("checkk",i,j,isPalindrome(s, i, j))
                if isPalindrome(s, i, j):
                    if j-i > max:
                        max = j-i
                        st,e = i,j
            if max >= len(s) // 2:
                return s[st:e+1]
        return s[st:e+1]

