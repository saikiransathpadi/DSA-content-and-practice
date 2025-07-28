# 28 Jul

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        myhash = {}
        for i in s:
            if i not in myhash:
                myhash[i] = 0
            myhash[i] += 1
        
        for i in t:
            if i in myhash:
                myhash[i] -= 1
                if not myhash[i]:
                    myhash.pop(i)
            else:
                return False
        return True if not myhash else False
