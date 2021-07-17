"""
1. Clarification
2. Possible solutions
    - Dynamic programming
3. Coding
4. Tests
"""


# T=O(n), S=O(n), dp[i]: # of decode ways of pre i char of s
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        n = len(s)
        dp = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[n]
