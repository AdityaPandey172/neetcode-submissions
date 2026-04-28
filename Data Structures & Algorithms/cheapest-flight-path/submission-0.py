class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        min_heap = [
            (0, src, k + 1)
        ]
        distances = [[math.inf] * (k + 2) for _ in range(n)]

        for u, v, w in flights:
            graph[u].append((v, w))
        
        while min_heap:
            total_cost, current_city, remaining_stops = heapq.heappop(min_heap)
            if current_city == dst:
                return total_cost
            if remaining_stops > 0:
                for neighbor, cost in graph[current_city]:
                    new_cost = total_cost + cost
                    if new_cost < distances[neighbor][remaining_stops - 1]:
                        distances[neighbor][remaining_stops - 1] = new_cost
                        heapq.heappush(
                            min_heap, (new_cost, neighbor, remaining_stops - 1)
                        )
        
        return -1