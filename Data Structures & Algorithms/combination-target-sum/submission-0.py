class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, combo):
            if sum(combo) == target:
                res.append(combo)
                return
            if i == len(nums) or sum(combo) > target:
                return

            dfs(i + 1, combo[:])
            dfs(i, combo + [nums[i]])

        dfs(0, [])

        return res 