class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            next_num = 0
            while num > 0:
                num, digit = divmod(num, 10)
                next_num += digit ** 2
            
            return next_num
        
        slow, fast = n, get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1