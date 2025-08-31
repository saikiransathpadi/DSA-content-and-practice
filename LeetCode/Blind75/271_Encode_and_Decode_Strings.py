from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        l = len(s)

        while i < l:
            num = ""
            while i < l and s[i].isnumeric():
                num += s[i]
                i += 1
            num = int(num)
            i += 1
            word = ""
            for _ in range(num):
                word += s[i]
                i +=1
            res.append(word)
        return res


Input = []

Output = [""]

en = Solution().encode(Input)
print(en)

print(Solution().decode(en))
