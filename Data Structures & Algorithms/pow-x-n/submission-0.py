class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(base, exp):
            if exp == 0:
                return 1.0
            temp = helper(base, exp // 2)
            if exp % 2 == 0:
                return temp * temp
            else:
                return base * temp * temp
        
        if n < 0:
            x = 1 / x
            n = - n
        
        return helper(x, n)