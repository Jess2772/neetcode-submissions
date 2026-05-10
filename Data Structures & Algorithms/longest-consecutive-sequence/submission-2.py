class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        for n in nums:
            cur = 1
            if n + 1 not in nums:
                while n - 1 in nums:
                    n -= 1
                    cur += 1
                longest = max(longest, cur)
        

        return longest
        