class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # frequncy count dictionary 
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + num  # dictionary.get() : get values from the key 
                                                ## dict.get(x,`default value`): 
                                                ## find the value of key `x`, and if there're not any key named `x` then return `default value`

        max_num = max(nums)         # max(list): return max value from the list 

        # dp list: MAX money possible to earn 
        dp = [0] * (max_num + 1)   # + 1: list index is started from 0 ==> make index order & num order equal 
        dp[1] = freq.get(1, 0)     # dp[0] -> 0 (automatically)

        for num in range(2, max_num + 1):
            dp[num] = max(dp[num - 1],     # money up to `num-1`, without choosing current `num`
                      dp[num - 2] + freq.get(num, 0))  # money up to `num-2` step, with choosing current `num`

        return dp[max_num]

s = Solution() 
nums = [3,4,2]
print(s.deleteAndEarn(nums))   