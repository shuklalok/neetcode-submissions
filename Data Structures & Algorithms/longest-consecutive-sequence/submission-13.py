class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 0
        nums.sort()

        current, streak = nums[0], 0
        i = 0
        while i < len(nums):
            #-------------------
            # if current is not nums[i]
            # nums[i] becomes current
            # streak ends becomes 0
            if current != nums[i]:
                current = nums[i]
                streak = 0
            #-------------------
            # remove repeated
            while i < len(nums) and nums[i] == current:
                i += 1
            #-------------------
            streak += 1
            current += 1
            res = max(res, streak)
        return res


        