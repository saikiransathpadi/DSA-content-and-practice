# 20 Jul

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        start = 0
        max_len = 0

        for i in range(len(s)):
            if s[i] in char_index and char_index[s[i]] >= start:
                # Move start right past the previous index of s[i]
                start = char_index[s[i]] + 1
            char_index[s[i]] = i
            max_len = max(max_len, i - start + 1)

        return max_len


# Test cases
for input_s in ["dvdf", "pwwkkew", "bbb", "gaabcdg", "tmmzuxt"]:
    print(f"{input_s} → {Solution().lengthOfLongestSubstring(input_s)}")


