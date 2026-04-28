class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if visited[i]:
                continue
        
            provinces += 1
            stack = [i]
            visited[i] = True

            while stack:
                u = stack.pop()
                for v in range(n):
                    if isConnected[u][v] == 1 and not visited[v]:
                        visited[v] = True
                        stack.append(v)
        
        return provinces
        