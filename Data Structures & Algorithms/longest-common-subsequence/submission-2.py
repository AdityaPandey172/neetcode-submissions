class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        # If you only need length, return dp[0][0]
        return dp[0][0]

    def oneLCS(self, text1: str, text2: str) -> str:
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        # Reconstruct one LCS by walking dp
        i = j = 0
        out = []
        while i < n and j < m:
            if text1[i] == text2[j]:
                out.append(text1[i])
                i += 1
                j += 1
            else:
                # move in the direction that keeps LCS optimal
                if dp[i + 1][j] >= dp[i][j + 1]:
                    i += 1
                else:
                    j += 1

        return "".join(out)