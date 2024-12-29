# https://leetcode.com/problems/fibonacci-number/
class Solution(object):
    def isPalindrome(self, s: str):
        """
        :type s: str
        :rtype: bool
        """
        s: str = s.lower()

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


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))