class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        distances = []

        for i in range(n):
            for j in range(i + 1, n):
                distances.append((distance(points[i], points[j]), i, j))
    
        distances.sort()
        parent = list(range(n))
        rank = [0] * n
        mst_cost = 0

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
    
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                if rank[root1] != rank[root2]:
                    parent[root2] = root1
                else:
                    parent[root1] = root2
                    if rank[root1] == rank[root2]:
                        rank[root2] += 1
    
        for distance, u, v in distances:
            if find(u) != find(v):
                union(u, v)
                mst_cost += distance
        return mst_cost
        