class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stop_to_routes = defaultdict(list)
        for i, stops in enumerate(routes):
            for s in stops:
                stop_to_routes[s].append(i)

        q = deque()
        visited_routes = set()

        for r in stop_to_routes[source]:
            q.append((r, 1))
            visited_routes.add(r)

        visited_stops = set([source])

        while q:
            r, buses = q.popleft()

            for stop in routes[r]:
                if stop == target:
                    return buses

                for nr in stop_to_routes[stop]:
                    if nr not in visited_routes:
                        visited_routes.add((nr))
                        q.append((nr, buses + 1))

            stop_to_routes[stop].clear()

        return -1       