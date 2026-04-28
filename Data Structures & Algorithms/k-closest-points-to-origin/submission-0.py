class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0] ** 2 + point[1] ** 2
        
        min_heap = [(distance(point), point) for point in points]
        heapq.heapify(min_heap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(min_heap)[1])
        
        return result
        