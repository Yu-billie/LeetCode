from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        if not strs:
            return ""
        
        prefix = strs[0]  # starts with the first stringi as the initial prefix 

        for i in range(n):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1] # remove the last character from the prefix 

                if not prefix:       # keep removing --> if the prefix becomes empty, there is no common prefix 
                    return ""
        
        return prefix 

s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))