class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftAcc, rightAcc = [1] * len(nums), [1] * len(nums)

        for i in range (1, len(nums)):
            leftAcc[i] *= nums[i - 1] * leftAcc[i-1]

        for j in range (len(nums) - 2, -1, -1):
            rightAcc[j] *= nums[j + 1] * rightAcc[j + 1]
            
        res = [1] * len(nums)

        for i in range (len(nums)):
            res[i] = leftAcc[i] * rightAcc[i]
        
        return res


        
