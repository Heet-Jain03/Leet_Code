class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        ori = 0
        exp = n * (n+1) / 2
        for num in nums:
            ori += num
        return int(exp - ori)
            

        