class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False   

        # check_start = 0
        # check_end = -1
        
        # for char in s, t:
        #     check_start += 1
        #     check_end -= 1
            
        #     if check_start == check_end:
        #         return True
        return sorted(s) == sorted(t)

            
        




 # check length
 # hashmap
 # check how may letter in s, like 2 r, 2a, 1c, 1e
 # count that letter on t
 # check if they match correct return True O(n^2)