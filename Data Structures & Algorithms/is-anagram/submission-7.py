class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        seen_s = {}
        seen_t = {}

        if len(s) != len(t):
            return False
        
        for char in s:
            seen_s[char] = seen_s.get(char, 0) + 1
        for char in t:
            seen_t[char] = seen_t.get(char, 0) + 1
        if seen_s == seen_t:
            return True
        return False
        # making 2 dict s and t, we store every char as a : 1, b : 4, etc
        # then we compare each at the end