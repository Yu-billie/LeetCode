class Solution:
    def isPalindrome(self, x: int) -> bool:
        # change int --> string
        # string: sequence of character 
        x_str = str(x) 

        return x_str == x_str[::-1]   # []::-1] : read reversly (from end to the start) 

s = Solution()
x=121
print(s.isPalindrome(x))
