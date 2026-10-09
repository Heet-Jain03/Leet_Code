class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        posi = []
        neg = []

        for i in range(len(nums)):
            if nums[i] > 0:
                posi.append(nums[i])
            else:
                neg.append(nums[i])

        for i in range(len(posi)):
            nums[2 * i] = posi[i]
            nums[2 * i + 1] = neg[i]

        return nums