class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen_s, seen_t = {}, {}

        for c in s:
            seen_s[c] = seen_s.get(c, 0) + 1
        
        for c in t:
            seen_t[c] = seen_t.get(c, 0) + 1
        
        if seen_s != seen_t:
            return False
        
        return True