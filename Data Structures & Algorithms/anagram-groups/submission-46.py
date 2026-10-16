class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        aact = {a: 2
                c: 1
                t: 1 }
                 a b c d    t
                 0 1 2 3
        count = [2|0|1|0.. |1] #26
        res = {count[]:[sub]}
        
        Create res = defaultdict(list)  #{}
        
        Iterate sub in strs:
            Create count array = [0] * 26

            Iterate c in sub:
                count[ord(c)-ord("a")] +=1

            Count as the key in res.append(sub)
        return the list(res.values())   # [[]]
        """
    
        res = defaultdict(list)

        for sub in strs:
            count = [0] * 26

            for c in sub: 
                count[ord(c)-ord("a")] += 1

            res[tuple(count)].append(sub)
        return list(res.values())        