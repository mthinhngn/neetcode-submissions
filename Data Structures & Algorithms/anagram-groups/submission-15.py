class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for sub in strs:
            count = [0] * 26
            
            for char in sub:
                count[ord(char)- ord("a")] += 1
            result[tuple(count)].append(sub)
        return list(result.values())