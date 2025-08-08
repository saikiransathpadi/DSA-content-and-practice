from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myhash = {}

        for i in strs:
            sortstr = "".join(sorted(i))
            if sortstr not in myhash:
                myhash[sortstr] = []
            myhash[sortstr].append(i)
        
        return [ i for i in myhash.values()]

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))