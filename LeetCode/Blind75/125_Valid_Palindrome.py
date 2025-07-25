# 25 Jul

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1

        while i < len(s) and j >= 0 and i < j:
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j >= 0  and not s[j].isalnum():
                j -= 1
            if i < len(s) and j >= 0 and i < j and s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1

        return True

inp = ".,"

print(Solution().isPalindrome(inp))