import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.myheap =[i for i in range(1, 1001)]
        heapq.heapify(self.myheap)


    def popSmallest(self):
        """
        :rtype: int
        """
        return heapq.heappop(self.myheap)
        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.myheap:
            heapq.heappush(self.myheap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
            

# Actual solution


class SmallestInfiniteSet(object):

    def __init__(self):
        self.smallest = 1
        self.removed = set()

    def popSmallest(self):
        """
        :rtype: int
        """
        res = self.smallest
        self.removed.add(self.smallest)
        self.smallest += 1
        while self.smallest in self.removed:
            self.smallest += 1
        return res
        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num in self.removed:
            self.removed.remove(num)
        self.smallest = min(self.smallest, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
