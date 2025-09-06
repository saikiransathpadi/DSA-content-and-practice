from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Same TC but less optimal
        #  l,r = 0, 0
        # count_map = defaultdict(int)
        # res = 0
        # maxf = 0
        
        # while r < len(s):
        #     count_map[s[r]] += 1
        #     maxf = max(maxf, count_map[s[r]])
        #     while r!=l and ((r-l+1) - maxf) > k:
        #         count_map[s[l]] -= 1
        #         l += 1
        #     res = max(res, r-l+1)
        #     r += 1
                
        # return res

        l,r = 0, 0
        count_map = defaultdict(int)
        res = 0
        maxf = 0
        
        while r < len(s):
            count_map[s[r]] += 1
            maxf = max(maxf, count_map[s[r]])
            while r!=l and ((r-l+1) - maxf) > k:
                count_map[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
                
        return res


s = "AABABBA"
k = 1

s = "ABAB"
k = 2
print(Solution().characterReplacement(s, k))