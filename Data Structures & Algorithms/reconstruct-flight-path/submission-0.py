class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for start, end in sorted(tickets, reverse=True):
            graph[start].append(end)
        
        route = []

        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            route.append(node)
        
        dfs("JFK")

        return route[::-1]
        