class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set()
        result = set()
        for num in nums1:
            if num in seen:
                continue
            seen.add(num)
        
        for num in nums2:
            if num in seen:
                result.add(num)
        return list(result)


