# 1 Aug


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count_map = {}
        for i in words:
            count_map[i] = 1 + count_map.get(i, 0)
        
        count_to_word = {}
        for i in count_map:
            if count_map[i] not in count_to_word:
                count_to_word[count_map[i]] = []
            count_to_word[count_map[i]].append(i)

        res = []
        c = 0


        for i in range(len(count_map), -1, -1):
            if i in count_to_word:
                count_to_word[i].sort()
                for j in count_to_word[i]:
                    res.append(j)
                    c += 1
                    if c == k:
                        return res