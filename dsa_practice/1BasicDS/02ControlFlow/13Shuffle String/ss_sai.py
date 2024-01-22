from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [0] * len(s)
        for s,i in zip(s,indices):
            result[i] = s
        return "".join(result)