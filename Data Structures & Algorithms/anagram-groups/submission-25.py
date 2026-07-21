class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)
        
        for word in strs:
            key = "".join(sorted(word))  # "cat" -> "act"
            hashmap[key].append(word)    # {"act": ["act", "cat"]}
        
        return list(hashmap.values())
        
        '''
        sorted to group the char
        return a list of sorted
        different list containt different style of sorted

        return the sorted array
        '''