class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate product of all numbers
        q = 1
        zero_c = 0
        for n in nums:
            if n != 0:
                q *= n
            else: zero_c += 1

        res = [0] * len(nums)
        if zero_c > 1: return res

        for i, n in enumerate(nums):
            if zero_c: res[i] = 0 if n else q
            else: res[i] = int(q/n)
        
        return res





