class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for char in s:
            countS[char] = countS.get(char, 0) + 1
        for char in t:
            countT[char] = countT.get(char, 0) + 1

        if countS == countT:
            return True
            
        return False

        '''
        Hash map for CountS, CountT
        add every char to hashmap, if it doesnt exist, add a char, if it is existed, +1
        sorted countS and CountT if == mean True

        '''