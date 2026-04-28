class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)
        maxSide = 0
        
        for i in range(1, m + 1):
            prevDiag = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = 1 + min(dp[j], dp[j - 1], prevDiag)
                    maxSide = max(maxSide, dp[j])
                else:
                    dp[j] = 0
                prevDiag = temp

        return maxSide * maxSide        