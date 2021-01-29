class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        value={"(": ")", "{": "}", "[": "]"}
        for i in s:
            if i in value:
                stack.append(i)
            elif len(stack) == 0 or value[stack.pop()] != i:
                return False
        return len(stack) == 0