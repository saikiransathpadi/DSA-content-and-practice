class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""

        for char in s:
            if len(output) <2:
                output += char
            elif output[-1] == char and output[-2] == char:
                pass
            else:
                output += char
        return output


inputs = ["leeetcode", "aaabaaaa", "aab"]
for s in inputs:
    print(Solution().makeFancyString(s))

        