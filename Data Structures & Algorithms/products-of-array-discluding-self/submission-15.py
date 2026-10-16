class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums = [1,2,4,6]
        out: [48,24,12,8]

        [6*4*2,1*4*6,1*2*6,1*2*4]

        nums =   [1, 2, 4, 6]     
        -> pre = [1, 1, 2, 8]
        <- post= [48,24,6, 1]
        out:     [48,24,12,8]

        Out = pre[i] * post[i]

        Initiate pre, post = [1] * len(nums), [1] * len(nums)
        res = [1] * len(nums)
        Assign pre = 1 #delete, we start at index 1
        Iterate i in range(1, len(nums))
            pre[i] = mult before index i

        Assign post = 1  #delete, we start at index 1 backward
        Iterate i in range(len(nums)-2,-1,-1)
            post[i] = mult after the index i

        res[i] = pre[i] * post[i]
        return res
        """

        pre, post, res = [1] * len(nums), [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            post[i] = post[i+1] * nums[i+1]
        for i in range(len(nums)):
            res[i] = pre[i] * post[i]
        return res 