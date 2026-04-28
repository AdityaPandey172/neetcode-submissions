class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo(edges: List[List[int]]) -> List[int]:
            adj = [[] for _ in range(k + 1)]
            indeg = [0] * (k + 1)

            for u, v in edges:
                adj[u].append(v)
                indeg[v] += 1
            
            q = deque([i for i in range(1, k + 1) if indeg[i] == 0])
            order = []

            while q:
                u = q.popleft()
                order.append(u)
                for v in adj[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)
            
            return order if len(order) == k else [] 
        
        rowOrder = topo(rowConditions)
        if not rowOrder:
            return []
        
        colOrder = topo(colConditions)
        if not colOrder: 
            return []
        
        rowPos = {val: i for i, val in enumerate(rowOrder)}
        colPos = {val: i for i, val in enumerate(colOrder)}

        ans = [[0] * k for _ in range(k)]
        for x in range(1, k + 1):
            ans[rowPos[x]][colPos[x]] = x
        
        return ans