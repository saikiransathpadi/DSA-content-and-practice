# 21 July

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hash_para = {
            "}": "{",
            ")": "(",
            "]": "[",
        }
        for i in s:
            if i in "([{":
                stack.append(i)
            elif stack and stack[-1] == hash_para[i]:
                stack.pop()
            else:
                return False
        return True if not stack else False
        