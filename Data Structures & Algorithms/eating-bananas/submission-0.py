class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """        
        piles = [1,4,3,2], h = 9
        k = 2
 
         0 1 2 3
        [1,2,3,4]   k = 2
         l     r 
         m     
        """
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l+r)//2
        
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/k)
            if totalTime <= h:
                res = k
                r = k-1
            else: 
                l = k+1
        return res





    