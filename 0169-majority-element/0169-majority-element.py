class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        unique = set(nums)

        result = max(unique, key=nums.count)

        return result