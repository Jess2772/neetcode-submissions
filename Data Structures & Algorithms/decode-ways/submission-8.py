class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        N = len(s)
        if N == 1:
            return 1

        dp = [0] * N
        dp[0] = 1

        # FIX 1: properly initialize dp[1]
        if s[1] != "0":
            dp[1] += dp[0]

        if 10 <= int(s[:2]) <= 26:
            dp[1] += 1

        for i in range(2, N):

            # FIX 2: remove invalid early-return logic
            # (you don't need this at all)

            # FIX 3: remove the "s[i-1] == '0' special case"
            # (this was breaking transitions)

            # single digit decode (valid if not '0')
            if s[i] != "0":
                dp[i] += dp[i - 1]

            # two digit decode
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]