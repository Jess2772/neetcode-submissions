class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp[n] = max subarray product up to n

        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            tmp = curMax * n
            curMax = max(n, tmp, n * curMin)
            curMin = min(n, tmp, n * curMin)

            res = max(res, curMax)


        return res


        