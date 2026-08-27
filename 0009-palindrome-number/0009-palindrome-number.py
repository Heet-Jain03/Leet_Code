class Solution:
    def isPalindrome(self, x: int) -> bool:
        ori = x
        rev = 0
        while x>0:
            digit = x % 10
            x = x // 10
            rev = (rev * 10) + digit
        return rev == ori
        