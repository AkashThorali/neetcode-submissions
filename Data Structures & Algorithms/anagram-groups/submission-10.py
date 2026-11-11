from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                freq[index] += 1
            groups[tuple(freq)].append(word)
        return list(groups.values())
            


            



            


