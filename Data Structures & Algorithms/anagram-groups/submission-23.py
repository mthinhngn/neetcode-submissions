class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for sub in strs:
            count = [0] * 26
            for c in sub:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(sub)
        return list(res.values())
                