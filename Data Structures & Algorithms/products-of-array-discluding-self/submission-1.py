class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre_prod = 1
        for i in range(len(nums)):
            res[i] = pre_prod
            pre_prod *= nums[i]

        post_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post_prod
            post_prod *= nums[i]

        return res



