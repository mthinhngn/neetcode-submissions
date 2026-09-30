class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                #update the key in the array with each char as a key 2a 3b
                count[ord(c)-ord("a")] += 1            
            #group every same sub together
            res[tuple(count)].append(s)
        return list(res.values())
