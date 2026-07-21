class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for curnum in nums:
            if curnum in seen:
                return True
            seen.add(curnum)
        return False