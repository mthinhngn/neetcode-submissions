class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for current_num in nums:
            if current_num in seen:
                return True
            seen.add(current_num)
        return False