class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            parent[find(x)] = find(y)
        
        for edge in edges:
            u, v, = edge
            if find(u) == find(v):
                return edge
            union(u, v)
        
        return []
        