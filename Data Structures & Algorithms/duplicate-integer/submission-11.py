class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Hash map
        every number in seen -> return True
        else, add the number to seen
        After a loop, no dup, return False
        '''

        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)
        return False

