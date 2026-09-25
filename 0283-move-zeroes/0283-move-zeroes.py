class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp = []
        for i in range(n):
            if nums[i] != 0:
                temp.append(nums[i])
        nz = len(temp)
        for i in range(nz):
            nums[i] = temp[i]
        for i in range(nz,n):
            nums[i] = 0


        