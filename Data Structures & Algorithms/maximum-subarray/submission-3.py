class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        cur = nums[0]
        bestL = bestR = 0
        start = 0

        for i in range(1, len(nums)):
            x = nums[i]

            if x > cur + x:
                cur = x
                start = i
            
            else:
                cur = cur + x
            
            if cur > best:
                best = cur
                bestL, bestR = start, i
        
        return best

        