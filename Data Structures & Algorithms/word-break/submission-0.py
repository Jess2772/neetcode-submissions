class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        # well you want to get to the end of the string
        # do we care what word was actaully used?
        # probably not. i think we want to know up to what index can we encode(split)
        # the string

        dp = [False] * (N + 1)
        dp[0] = True

        for i in range (1, len(s) + 1):
            for word in wordDict:
                if len(word) <= i:
                    if dp[i - len(word)] and word == s[i - len(word): i]:
                        dp[i] = True
        

        return dp[N]