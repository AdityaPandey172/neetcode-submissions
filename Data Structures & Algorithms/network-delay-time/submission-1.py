class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        INF = 10**18
        dist = [INF] * (n + 1)
        dist[k] = 0

        pq = [(0, k)]

        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        
        ans = max(dist[1:])
        return -1 if ans == INF else ans
        