class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack(n, n, "", result)
        return result

    def backtrack(self, left: int, right: int, curr: str, result: List[str]):
        if left == 0 and right == 0:
            result.append(curr)
            return
        
        if left > 0:
            self.backtrack(left - 1, right, curr + "(", result)
        if right > left:
            self.backtrack(left, right - 1, curr + ")", result)

s = Solution()
n = 3
print(s.generateParenthesis(n))