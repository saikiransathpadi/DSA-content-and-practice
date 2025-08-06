class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        l = len(ratings)
        points = [1] * l

        for i in range(1, l):
            if ratings[i] > ratings[i - 1]:
                points[i] = points[i-1] + 1
        
        for i in range(l-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                points[i] = max(points[i], points[i+1] + 1)
        
        return sum(points)
