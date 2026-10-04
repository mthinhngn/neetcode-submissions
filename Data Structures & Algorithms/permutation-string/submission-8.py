class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1, window = {}, {}

        if len(s1) > len(s2):
            return False
        
        for c in s1:
            countS1[c] = countS1.get(c, 0) + 1

        l = 0
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r],0) + 1

            if (r-l+1) > len(s1):
                window[s2[l]] -= 1

                if window[s2[l]] == 0:
                    del window[s2[l]]
                l+=1
            if window == countS1:
                return True
        return False