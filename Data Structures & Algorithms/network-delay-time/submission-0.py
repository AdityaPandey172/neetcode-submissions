class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        distances = [float("inf")] * (n + 1)
        distances[k] = 0

        pq = [(0, k)]

        while pq:
            distance, node = heapq.heappop(pq)
            if distance > distances[node]:
                continue
            for neighbor, weight in graph[node]:
                if distance + weight < distances[neighbor]:
                    distances[neighbor] = distance + weight
                    heapq.heappush(pq, (distances[neighbor], neighbor))
            
        max_distance = max(distances[1:])

        return max_distance if max_distance < float("inf") else -1

        