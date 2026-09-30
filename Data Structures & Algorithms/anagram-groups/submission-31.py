class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for sub in strs:
            count = [0] * 26

            for c in sub:
                #update the key in the array with each char as a key 2a 3b
                count[ord(c)-ord("a")] += 1            
            #group every same sub together
            res[tuple(count)].append(sub)
        return list(res.values())
