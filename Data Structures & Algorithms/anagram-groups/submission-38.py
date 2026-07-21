class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''
        Hash map
        sorted, then group it
        return a list(values)
        '''
        # mp = {}                 # create dict
        # if ch not in mp:        # if ch not in dict, create a list
        #     mp[ch] = []         
        # mp[ch].append(ch)       # else, add ch to a dict
        mp = defaultdict(list)
       
        for ch in strs:
            key = "".join(sorted(ch))
            mp[key].append(ch)
        return list(mp.values())
