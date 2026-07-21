class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
# Using hashmap
# 1 way is running thru the array to find the 
# combination to match the target -> O(n^2)
# 2 way is Do calculate the first index with
# diff = target - i, then go array to find the j -> O(n^2)
# 3 way is cal diff every thing, then run array to check
# the diff in seen or not . 1 time run -> O(n)

        seen = {} # val & index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen: 
                return [seen[diff], i]
            seen[n] = i
        return