"""
class Solution(object):
    def fib(self, n):
        a = 0
        b = 1
        for i in range(n):
            a,b = b, a + b
        return a
"""
class Solution(object):
    def fib(self, n):
        if n == 0 or n == 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)

  


            
    
        