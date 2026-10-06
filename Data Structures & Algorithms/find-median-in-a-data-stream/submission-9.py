from heapq import heappush, heappop, heappush_max, heappop_max
class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        small = self.small
        large = self.large


        if small and num < small[0]:
            heappush_max(small, num) 
        else:
            heappush(large, num)
        
        while (len(small) - len(large)) > 1:
            val = heappop_max(small)
            heappush(large, val)
        
        while (len(large) - len(small)) > 1:
            val = heappop(large)
            heappush_max(small, val)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        
        if len(self.small) < len(self.large):
            return self.large[0]
        
        return (self.small[0] + self.large[0])/2
        