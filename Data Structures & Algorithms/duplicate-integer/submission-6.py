class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Change {} to set()
        # use hashmap
        # after a loop, if no dup, True
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False