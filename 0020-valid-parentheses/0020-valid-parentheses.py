class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in brackets.values():
                stack.append(c)
            elif c in brackets:
                if not stack or stack.pop() != brackets[c]:
                    return False

        return len(stack) == 0

s = Solution()
print(s.isValid("()"))
