class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        for i in range(n-1):
            for j in range(i+1, n):   # Start j from i+1 to avoid duplicate pairs   
                if target == nums[i] + nums[j]:
                    return [i, j]

s = Solution()
nums = [2,7,11,15]
target = 9
print(s.twoSum(nums, target))