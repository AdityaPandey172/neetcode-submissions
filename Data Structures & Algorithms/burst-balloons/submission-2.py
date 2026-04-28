class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [x for x in nums if x != 0]
        arr = [1] + nums + [1]
        n = len(arr)

        dp = [[0] * n for _ in range(n)]

        for length in range(1, n - 1):
            for l in range(1, n - 1 - length + 1):
                r = l + length - 1
                best = 0
                for i in range(l, r + 1):
                    best = max(
                        best,
                        dp[l][i - 1] + arr[l - 1] * arr[i] * arr[r + 1] + dp[i + 1][r]
                    )
                dp[l][r] = best
            
        return dp[l][n - 2]

        