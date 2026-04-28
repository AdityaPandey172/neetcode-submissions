class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        cache = [[0] * (m + 1) for _ in range(n + 1)]

        for j in range(m + 1):
            cache[n][j] = m - j
        for i in range(n + 1):
            cache[i][m] = n - i

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(
                        cache[i + 1][j],
                        cache[i][j + 1],
                        cache[i + 1][j + 1]
                    )
        return cache[0][0]


    def editScript(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        cache = [[0] * (m + 1) for _ in range(n + 1)]    

        for j in range(m + 1):
            cache[n][j] = m - j
        for i in range(n + 1):
            cache[m][i] = n - i 

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])

        i = j = 0
        ops = []
        while i < n or j < m:
            if i == n:
                ops.append(('INSERT', word2[j]))
                j += 1 
                continue

            if j == m:
                ops.append(('DELETE', word1[i]))
                i += 1        
                continue

            if word[i] == word[j]:
                ops.append(('MATCH', word1[i]))
                i += 1
                j += 1
            else:
                if cache[i][j] == 1 + cache[i + 1][j + 1]:
                    ops.append(("REPLACE", f"{word1[i]} -> {word2[j]}"))
                    i += 1
                    j += 1
                elif cache[i][j] == 1 + cache[i + 1][j]:
                    ops.append(("DELETE", word1[i]))
                    i += 1
                else:
                    ops.append(("INSERT", word2[j]))
                    j += 1

        return ops

