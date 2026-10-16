class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for sub in strs:
            count = [0] * 26

            for c in sub:
                #{(1,0,2): []}
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(sub)
        return list(res.values())