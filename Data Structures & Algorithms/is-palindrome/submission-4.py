class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointer
        # 1 at the beginning and 1 at the end
        # check every point, if match, keep going until meet
        # if not, return False
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters on left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric characters on right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True

