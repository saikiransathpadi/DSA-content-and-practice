class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l = len(fruits)
        if l <= 2: return l
        maxf= 0
        curr = 0
        myhash = {}

        i = 0

        while i < l:
            if fruits[i] in myhash:
                myhash[fruits[i]] += 1
            elif fruits[i] not in myhash and len(myhash) < 2:
                myhash[fruits[i]] = 1
            elif fruits[i] not in myhash and len(myhash) >= 2:
                curr = sum(list(myhash.values()))
                maxf = max(maxf, curr)
                myhash = {}
                myhash[fruits[i]] = 1
                p = i -1
                myhash[fruits[p]] = 0
                while fruits[p] in myhash and p >= 0:
                    myhash[fruits[p]] += 1
                    p-= 1
            i += 1
        curr = sum(list(myhash.values()))
        maxf = max(maxf, curr)
        return maxf

            


print(Solution().totalFruit([1,2,1]))
print(Solution().totalFruit([1,2,3,2,2]))