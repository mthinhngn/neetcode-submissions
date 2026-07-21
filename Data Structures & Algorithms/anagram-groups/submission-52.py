class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        mp {}

        sorted words in str
        - sorted every word in a strs, use sorted as a key

        sorted ch in words
        - sorted every ch in words, glue it 
        '''

        mp = {}

        for word in strs:
            key = "".join(sorted(word))
        
            if key in mp:
                mp[key].append(word)
            else:
                mp[key] = [word]             
        

        return list(mp.values())
