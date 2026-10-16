class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:   
        """
        nums      = [0,3,2,5,4,6,1,1]  Output: 7, [0, 1, 2, 3, 4, 5, 6]
        set(nums) = [0,3,2,5,4,6,1]
        Because we iterate the array thru n not index so no need sorted
        Let sorted for visualization:
        set(nums) = [0,1,2,3,4,5,6]
                           7       

        nums  = [2,20,4,10,3,4,5]        Output: 4
        sorted= [2,3,4,4,5,10,20]
        set   = [2,3,4,5,10,20]
                    4     1  1 
        
        setN= set(nums)
        longest = 2
        res = 0
        Iterate n in setN
            if (n-1) not in setN:
                longest = 1
                while (n+longest) in sortN:
                    longest +=1 
            res = max(res, longest)
        return res
        """
        setN = set(nums)
        res = 0

        for n in nums:
            if (n-1) not in setN:
                longest = 1
                while (n + longest) in setN:
                    longest += 1
                res = max(res, longest)
        return res