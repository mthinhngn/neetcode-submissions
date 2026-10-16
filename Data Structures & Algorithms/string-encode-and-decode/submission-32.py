class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        strs = ["Hello","World"]
        s = 5#Hello5#World    
        one string s += len + "#" + strs
        """
        res = ""
        for sub in strs:
            res += str(len(sub)) + "#" + sub
        return res
    def decode(self, s: str) -> List[str]:
        """
        Need a pointer i at "number" index 0 and j move to find "#"
        s = 5#Hello5#World    
            i      i
             j      j
        
        Create res = []
        Set i = 0

        Iterate while i moving not touch the end of s
            set j = i
            while j != "#"
                move j += 1
            The len of the sub is a number distance int(s[i:j])
            Append the word after "#" into res
            Move i to the next number i = j + 1 + len
        return res
        """
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i = j + 1 + length
        return res