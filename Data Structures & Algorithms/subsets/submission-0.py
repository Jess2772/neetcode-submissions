class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []

        def dfs(i, subset):
            if i == N:
                res.append(subset)
                return

            subset.append(nums[i])
            
            dfs(i + 1, subset[:])
            subset.pop()
            dfs(i + 1, subset[:])      
            
            
        dfs(0, [])
        return res