class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        wordOne = {}
        wordTwo = {}

        for i in range(len(s)):
            if s[i] in wordOne.keys():
                wordOne[s[i]] += 1
            else:
                wordOne[s[i]] = 1
            if t[i] in wordTwo.keys():
                wordTwo[t[i]] += 1
            else:
                wordTwo[t[i]] = 1
        print(wordOne, wordTwo)
        return wordOne == wordTwo
            