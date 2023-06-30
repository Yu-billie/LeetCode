class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # continud sequence --> [:] 
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1

s = Solution()
haystack = "sadbutsad"
needle = "sad"
print(s.strStr(haystack, needle))                
