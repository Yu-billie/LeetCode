class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        result = 0

        # Roman Rule Dictionary 
        roman_rule = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }        

        for i in range(n):
            if i < n-1 and roman_rule[s[i]] < roman_rule[s[i+1]]:  # call Dictionary values from s[i] key
                result -= roman_rule[s[i]]
            else:
                result += roman_rule[s[i]]

        return result 

s = Solution()
print(s.romanToInt('MCMXCIV'))