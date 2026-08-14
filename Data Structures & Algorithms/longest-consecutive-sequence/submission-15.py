class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set
        # longest = 0
        numSet = set(nums)
        longest = 0

        # for each n in nums 
        # if n-1 is not in set - length = 1
        # while n + length in set - lenght +=1
        # longest is max of lenght and  longest
        for n in nums:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
