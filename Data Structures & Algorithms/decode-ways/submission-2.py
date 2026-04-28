class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        next1 = 1
        next2 = 0

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                cur = 0
            else:
                cur = next1
                if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
                    cur += next2
            next2, next1 = next1, cur

        return next1
        