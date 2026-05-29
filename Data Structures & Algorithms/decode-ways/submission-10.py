class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[n] is the number of ways to decode
        N = len(s)

        dp = [0] * N
        if s[0] == "0":
            return 0
        if N == 1:
            return 1

        dp[0] = 1
        if s[1] != "0":
            dp[1] += 1
        
        if int(s[:2]) >= 10 and int(s[:2]) <= 26:
            dp[1] += 1
        
        for i in range (2, N):
            if int(s[i-1: i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2]
            
            if s[i] != "0":
                dp[i] += dp[i-1]
            
        return dp[-1]
            

        