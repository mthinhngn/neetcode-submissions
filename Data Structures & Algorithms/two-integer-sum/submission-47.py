class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         
         seen = {}

         for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

         """
         hash map
         loop i : num in array
         diff = target - current value 
         if diff in seen
         return index of diff, i
         else add current to seen save as i
         """
