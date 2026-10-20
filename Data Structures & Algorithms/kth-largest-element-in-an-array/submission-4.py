class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Input: nums = [2,3,1,5,4], k = 2
        Output: 4
                            5      <= max   
                           / \
                          3   4
                         / \
                        1   2 

        Everytime we pop from the heap, k -= 1
        k == 0, then stop

        #Create a min heap:
        heapq.heapify(nums)

        #Push an element
        minHeap = []
        heapq.heappush(minHeap, 5)

        #Pop an element
        heapq.heappop(minHeap)

        #Create a max heap:
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)
        print(-maxHeap[0])  

        #Push an element
        maxHeap = []
        heapq.heappush(maxHeap, -5)
        print(-maxHeap[0])  

        #Pop an element
        largest = -heapq.heappop(maxHeap)
        
        Pseudo:
        Create a new array convert all the num to negative
        Initiate a maxheap

        while k > 0:
            largest = -heapq.pop(maxHeap)
            decrease the k
        return the largest
        """

        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)

        while k > 0:
            largest = -heapq.heappop(maxHeap)
            k -= 1
        return largest
