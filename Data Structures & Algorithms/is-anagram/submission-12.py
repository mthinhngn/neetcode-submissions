class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for char in s:
            countS[char] = countS.get(char, 0) + 1 
            countT[char] = countT.get(char, 0) + 1

            if sorted(s) == sorted(t):
                return True

        return False

     

            
        




 # check length
 # hashmap
 # check how may letter in s, like 2 r, 2a, 1c, 1e
 # count that letter on t
 # check if they match correct return True O(n + n)
 # using sorting