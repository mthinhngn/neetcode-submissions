class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = set()

        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)
        return False

        """
        hash map
        loop to check an array
        if num in seen -> True
        else, add num to seen
        return False end loop
        """