class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
        
        adj = [[] for _ in range(n)]
        deg = [0] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            deg[u] += 1
            deg[v] += 1
        
        q = deque(i for i in range(n) if deg[i] == 1)
        remaining = n

        while remaining > 2:
            layer = len(q)
            remaining -= layer
            for _ in range(layer):
                leaf = q.popleft()
                for nei in adj[leaf]:
                    deg[nei] -= 1
                    if deg[nei] == 1:
                        q.append(nei)
        
        return list(q)