from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordSet = set(wordDict)
        if not wordSet:
            return []

        lens = sorted({len(w) for w in wordSet})
        minL, maxL = lens[0], lens[-1]

        # 1) Feasibility DP: canBreak[i] = can segment suffix s[i:]
        canBreak = [False] * (n + 1)
        canBreak[n] = True
        for i in range(n - 1, -1, -1):
            # try only valid lengths
            for L in lens:
                j = i + L
                if j > n:
                    break
                if canBreak[j] and s[i:j] in wordSet:
                    canBreak[i] = True
                    break

        if not canBreak[0]:
            return []

        # 2) Build all sentences with memoization
        @lru_cache(None)
        def dfs(i: int) -> List[str]:
            if i == n:
                return [""]  # one "empty sentence" to help joining

            res = []
            for L in lens:
                j = i + L
                if j > n:
                    break
                if not canBreak[j]:
                    continue  # prune dead suffixes
                w = s[i:j]
                if w in wordSet:
                    tails = dfs(j)
                    for t in tails:
                        res.append(w if t == "" else w + " " + t)
            return res

        return dfs(0)