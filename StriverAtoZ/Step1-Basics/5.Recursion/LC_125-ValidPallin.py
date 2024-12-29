# https://leetcode.com/problems/valid-palindrome/description/
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()

        output = ""

        for i in s:
            if i.isalnum():
                output += i
        
        def isPalin(str, i, j):
            if i >= j:
                return True

            if str[i] != str[j]:
                return False
            
            return isPalin(str, i+1, j-1)
        return isPalin(output, 0, len(output)-1)