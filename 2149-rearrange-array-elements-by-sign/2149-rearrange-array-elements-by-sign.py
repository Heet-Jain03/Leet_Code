class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        posi, negi = 0, 1
        for i in range(len(nums)):
            if nums[i] >= 0:
                result[posi] = nums[i]
                posi+=2
            else:
                result[negi] = nums[i]
                negi+=2
        return result