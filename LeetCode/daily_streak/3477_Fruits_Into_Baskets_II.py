class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        is_filled = [0] * len(baskets)
        
        for i in fruits:
            for j in range(len(baskets)):
                if not is_filled[j] and baskets[j] >= i:
                    is_filled[j] = 1
                    break
        
        return is_filled.count(0)
        


fruits = [4,2,5]
baskets = [3,5,4]

print(Solution().numOfUnplacedFruits(fruits, baskets))