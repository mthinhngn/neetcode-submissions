class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Bucket Sort
        freq   [0 1 2 3 4 5 6]]   <-
        val    [  1 2 3] 

        nums = [1,2,2,5,3,3], k = 2

        freq   [0   1      2    3   4   5   6]]   <-
        val    [  [1,5]  [2,3]] 

        Time: O(n)
        Space: O(n)

        Create bucket list 
        Create freq hashmap

        Iterate thru n in nums:
            update freq hashmap with num:count   #{1:1, 2:2, 5:1,...etc}

        Mapping n, f in the freq hashmap.items():   #get the pair    freq = {n:f}
            #we add f as the index key : [n] is the value
            bucket[f].append(n)

        Create an empty list res = []   
        Iterate backward thru the bucket[i] (start -1: stop 0, backward -1)
            Iterate the number values at the bucket[i]
                Append n to the res []

                if the len(res) == k:
                    return res
        """

        bucket = [[] for i in range(len(nums)+1)]
        freq = {}

        for n in nums:
            freq[n] = freq.get(n,0) + 1
        
        for n, f in freq.items():
            bucket[f].append(n)
        
        res = []
        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res



        
        






        