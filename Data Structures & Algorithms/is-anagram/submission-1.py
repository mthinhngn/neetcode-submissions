class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

# use hash map to check
# if anagram, return True
# if not add to seen
        return sorted(s) == sorted(t)