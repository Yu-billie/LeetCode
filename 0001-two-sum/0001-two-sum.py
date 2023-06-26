class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        for i in range(n-1):  # loop for (n-1) times
            for j in range(i+1, n):   # Start j from i+1 to avoid duplicate pairs
                                      ## for j in range(i+1, n): from i+1 to n-1 (include just before n)    
                if target == nums[i] + nums[j]:  # DON'T USE sum() 
                                                 ## sum(): expects using iterable (ex: List)
                                                 ## BUT i, j are individual integer indices 
                    return [i, j]

s = Solution()
nums = [2,7,11,15]
target = 9
print(s.twoSum(nums, target))