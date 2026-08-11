class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # idea: run thru every word in the strs. Then run thru every char in that word. And store it something like hat = {h:1, a:1, t:1}. If the next word have the same count and similar char, example aht = {a:1, h:1, t:1}, put it in the similar group with hat. Else, create a new group. The output as an array with subarray inside  
        groups = {}

        for word in strs:
            count = {}
            for char in word:
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1
            
            key = tuple(sorted(count.items()))
            if key not in groups:
                groups[key] = []
            
            groups[key].append(word)

        return list(groups.values())