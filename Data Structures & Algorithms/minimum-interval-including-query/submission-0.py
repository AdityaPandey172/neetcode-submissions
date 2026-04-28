class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        queries_sorted = sorted(enumerate(queries), key=lambda x: x[1])

        min_heap = []
        ans = [-1] * len(queries)
        i = 0

        for query_index, query in queries_sorted:
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(min_heap, (end - start + 1, end))
                i += 1

            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            if min_heap:
                ans[query_index] = min_heap[0][0]
        
        return ans
        