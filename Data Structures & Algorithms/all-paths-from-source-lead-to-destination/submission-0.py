class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph  = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
        
        if graph[destination]:
            return False
        
        state = [0] * n

        def dfs(u: int) -> bool:
            if state[u] == 1:
                return False
            if state[u] == 2:
                return True
            
            if not graph[u]:
                return u == destination
            
            state[u] = 1
            for v in graph[u]:
                if not dfs(v):
                    return False
            state[u] = 2
            return True
        
        return dfs(source)

      