class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen_s = {}
        seen_t = {}
        
        for char in s:
            #here: if the it is the same char, +1 into seen
            #else: add the char to seen
            if char in seen_s:
                seen_s[char] += 1
            else:
                seen_s[char] = 1
        for char in t:
            #same logic
            if char in seen_t:
                seen_t[char] += 1
            else:
                seen_t[char] = 1
        if seen_s == seen_t:
            return True
        return False