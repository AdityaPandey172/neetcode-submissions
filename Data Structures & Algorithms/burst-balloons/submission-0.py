class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        nums = [1] + nums + [1]

        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for length in range(2, n + 2):
            for left in range(0, n + 2 - length):
                right = left + length
                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right],

                    )
        
        return dp[0][n + 1]

        