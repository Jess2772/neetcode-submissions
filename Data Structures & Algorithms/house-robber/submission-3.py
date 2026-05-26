class Solution:
    def rob(self, nums: List[int]) -> int:
        # cannot rob two adjacent houses
        # at every house: rob or dont rob:
            # need to keep track of previous if you robbed or not?
        #recursion or DP?
        # what would dp[i] represent?

        # answer would be max(of the dp array)


        #dp[n] represents how much money you can make if you rob house n
        N = len(nums)
        if N == 1:
            return nums[0]
        dp = [0] * N

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])


        for i in range (2, N):
            dp[i] = max(dp[i- 1], nums[i] + dp[i - 2])

        return max(dp)

