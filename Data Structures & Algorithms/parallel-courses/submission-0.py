class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        indeg = [0] * (n + 1)

        for u, v in relations:
            adj[u].append(v)
            indeg[v] += 1
        
        q = deque([i for i in range(1, n + 1) if indeg[i] == 0])
        taken = 0
        semesters = 0

        while q:
            semesters += 1
            for _ in range(len(q)):
                u = q.popleft()
                taken += 1
                for v in adj[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)

        return semesters if taken == n else -1
        