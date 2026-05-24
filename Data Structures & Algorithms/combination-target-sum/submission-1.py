class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, combo, acc):
            if acc == target:
                res.append(combo)
                return
            if i == len(nums) or acc > target:
                return

            dfs(i + 1, combo[:], acc)
            dfs(i, combo + [nums[i]], acc + nums[i])

        dfs(0, [], 0)

        return res 