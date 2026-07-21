class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            
            seen[num] =  i


        """
        Hash map
        storing the index : num in seen
        diff = target - num
        if the diff in seen
        return i: diff, i
        """    