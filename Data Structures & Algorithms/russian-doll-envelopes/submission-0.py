class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        envelopes.sort(key = lambda x : (x[0], -x[1]))
        tails = []

        for _, h in envelopes:
            i = bisect_left(tails, h)
            if i == len(tails):
                tails.append(h)
            else:
                tails[i] = h
        
        return len(tails)