class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s) == sorted(t):
        #     return True
        # return False

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for ch in s:
            countS[ch] = countS.get(ch, 0) + 1
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1
        if countS == countT:
            return True
        return False