class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ways = defaultdict(int)
        ways[0] = 1

        for x in nums:
            nxt = defaultdict(int)
            for s, cnt in ways.items():
                nxt[s + x] += cnt
                nxt[s - x] += cnt
            ways = nxt
        
        return ways[target]