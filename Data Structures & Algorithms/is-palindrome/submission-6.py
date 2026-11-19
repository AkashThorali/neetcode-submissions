class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for ch in s:
            if ch.isalnum():
                res += ch.lower()
        print(res)
        l, r = 0, len(res) - 1

        while r > l:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1
        return True