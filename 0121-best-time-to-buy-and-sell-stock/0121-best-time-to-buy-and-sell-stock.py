class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = float("inf")
        maxi = float("-inf")
        for nums in prices:
            mini = min(nums, mini)
            prof = nums - mini
            maxi = max(prof, maxi)
        return maxi
        