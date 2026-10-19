from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Input: nums = [3,30,34,5,9] 
        Output: "9534330"

        Gready problem
        9, 34
        934 > 349
        Convert to a string, then compare


        Iterate i, n thru the nums
            Convert each n to a string
        Def compare(n1,n2)
            if n1 + n2 > n2 + n1
                return -1
            else:
                return 1
        Sort(num, key=cmp_to_key(compare))
        return str(int("".join(nums)))
        """
        for i, n in enumerate(nums):
            nums[i] = str(n)
        
        def compare(n1,n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int("".join(nums)))