class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        curr_num = nums[0]
        length = 0
        longest = 0
        i = 0

        while i in range(len(nums)):
            if curr_num != nums[i]:
                length = 0 
                curr_num = nums[i]
            while i < len(nums) and nums[i] == curr_num:
                i += 1
            length += 1
            curr_num += 1

            longest = max(longest, length)

        return longest        
