class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        """
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
        """
        
        n = len(nums)
        result = [0] *  n
        posiI, negiI = 0, 1

        for i in range(n):
            if nums[i] >= 0:
                result[posiI] = nums[i]
                posiI+=2    
            else:
                result[negiI] = nums[i]
                negiI += 2
                
        return result
        