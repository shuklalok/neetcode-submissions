class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_c = 0
        for n in nums:
            if n == 0:
                zero_c += 1
                continue
            prod *= n

        res = [0] * len(nums)
        if zero_c > 1: return res

        for i, c in enumerate(nums):
            if zero_c: res[i] = 0 if c else prod
            else: res[i] = prod//c
        return res

