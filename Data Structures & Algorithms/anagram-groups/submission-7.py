from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            res[sorted_word].append(word)
        
        anagram = []
        for k,v in res.items():
            anagram.append(v)
        return anagram



            


