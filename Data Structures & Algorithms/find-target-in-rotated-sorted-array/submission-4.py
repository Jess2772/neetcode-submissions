class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l

        def binary_search(nums, target, l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            return -1
        
        res = binary_search(nums, target, 0, pivot)
        if res != -1:
            return res
        
        return binary_search(nums, target, pivot, len(nums) - 1)
