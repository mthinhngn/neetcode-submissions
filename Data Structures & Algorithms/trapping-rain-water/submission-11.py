class Solution:
    def trap(self, height: List[int]) -> int:
        
        """"""""""""""""""""
        # [3,2,1,5,0,4]
        #            x      
        #            x   o   x 
        # x   o   o  x   o   x             
        # x   x   o  x   o   x     
        # x   x   x  x   o   x 
        #   3-2 3-1     4-0
        """"""""""""""""""""
    
        l, r = 0, len(height) -1
        lmax, rmax = height[l], height[r]
        res = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                lmax = max(lmax,height[l])
                res += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]
        return res
    