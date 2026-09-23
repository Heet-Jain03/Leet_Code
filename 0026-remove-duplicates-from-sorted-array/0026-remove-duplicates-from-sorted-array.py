
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        seen = set()
        count = 0

        for num in nums:
            if num in seen:
                continue

            seen.add(num)
            nums[count] = num
            count += 1

        return count

        