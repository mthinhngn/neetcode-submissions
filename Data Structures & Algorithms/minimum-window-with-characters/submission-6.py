class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #handle edge case
        if t == "": return ""
        #create a hashmap and 2 pointer
        countT, window = {}, {}
        l = 0
        #adding every char in t as a key in hashmap
        for c in t:
            countT[c] = countT.get(c, 0) + 1 
        #set have and need
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        #move the right pointer foward 
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = (r-l+1)
                window[s[l]] -= 1

                #handle mult dup char
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l,r = res

        return s[l: r+1] if resLen != float("infinity") else ""

