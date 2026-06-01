class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[n] = longest increasing subsequence ending at n
        N = len(nums)
        dp = [1] * (N + 1)

        for i in range (1, len(nums)):
            for j in range (i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])


        return max(dp)