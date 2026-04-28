class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        reversed_num = 0
        sign = 1 if x > 0 else -1
        x = abs(x)

        while x != 0:
            pop = x % 10
            x //= 10

            if reversed_num > (INT_MAX - pop) // 10:
                return 0

            reversed_num = reversed_num * 10 + pop

        return reversed_num * sign