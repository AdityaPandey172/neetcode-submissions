class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        cooldown = 0
        while max_heap:
            temp = []
            for _ in range(n + 1):
                if max_heap:
                    temp.append(heapq.heappop(max_heap) + 1)
            
            for count  in temp:
                if count < 0:
                    heapq.heappush(max_heap, count)
            
            if max_heap:
                cooldown += n + 1
            else:
                cooldown += len(temp)
        
        return cooldown

        