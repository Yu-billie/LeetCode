class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

# Creating an instance of the ClimbStairs class
cs = Solution()

# Testing the provided constraints
print(cs.climbStairs(1))   # Output: 1
print(cs.climbStairs(2))   # Output: 2
print(cs.climbStairs(3))   # Output: 3
print(cs.climbStairs(45))  # Output: 1836311903
