class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        count = 0
        smallest = float("-inf")
        n = len(nums)
        longest = 0
        for i in range(n):
            num = nums[i]
            if num - 1 == smallest:
                count += 1
                smallest = num
            elif num != smallest:
                count = 1
                smallest = num
            longest = max(longest, count)
        return longest
