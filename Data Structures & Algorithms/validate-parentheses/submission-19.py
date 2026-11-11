class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(", "]": "[", "}": "{"}

        stack = []

        for i in s:
            if i in brackets.values():
                stack.append(i)
            else:
                if not stack or brackets[i] != stack.pop():
                    return False
        return True if len(stack) == 0 else False

                