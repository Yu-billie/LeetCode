class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
 
        # matrix length
        m = len(grid)
        n = len(grid[0]) 

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0] 

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        min_sum = dp[m-1][n-1]

        # Backtrack to find the path
        # path = [(m-1, n-1)]
        # i, j = m-1, n-1

        # while i>0 or j>0: 
        #     if i>0 and (j==0 or dp[i-1][j] < dp[i][j-1]):
        #         path.append((i-1, j))
        #         i -= 1
           
        #     else: 
        #         path.append((i, j-1))
        #         j -= 1
        
        # path.reverse()

        # return min_sum, path 
        return min_sum
        
s = Solution()
print(s.minPathSum([[1,2,3],[4,5,6]]))   