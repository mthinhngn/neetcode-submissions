class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for ch in strs:
            key = "".join(sorted(ch))
            mp[key].append(ch)
        return list(mp.values())