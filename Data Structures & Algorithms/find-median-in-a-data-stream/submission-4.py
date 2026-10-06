class MedianFinder:

    def __init__(self):
        self.small = []   # max heap
        self.large = []   # min heap

    def addNum(self, num: int) -> None:
        small = self.small
        large = self.large

        heapq.heappush(small, -num)

        # Make sure every number in small <= every number in large
        if small and large and -small[0] > large[0]:
            val = -heapq.heappop(small)
            heapq.heappush(large, val)

        # Balance sizes
        if len(small) > len(large) + 1:
            val = -heapq.heappop(small)
            heapq.heappush(large, val)

        if len(large) > len(small) + 1:
            val = heapq.heappop(large)
            heapq.heappush(small, -val)

    def findMedian(self) -> float:
        small = self.small
        large = self.large

        if len(small) > len(large):
            return -small[0]

        if len(large) > len(small):
            return large[0]

        return (-small[0] + large[0]) / 2