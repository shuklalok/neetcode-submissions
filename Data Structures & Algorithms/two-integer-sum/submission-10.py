class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map and map[diff] != i:
                return [map[diff], i]
            map[nums[i]] = i