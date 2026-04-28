class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        maxL = max(map(len, wordDict))
        minL = min(map(len, wordDict))

        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for j in range(i + minL, min(n, i + maxL) + 1):
                if dp[j] and s[i:j] in wordSet:
                    dp[i] = True
                    break

        return dp[0]
        