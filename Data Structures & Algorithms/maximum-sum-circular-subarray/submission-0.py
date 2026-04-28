class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0

        curMax = 0
        maxSum = nums[0]

        curMin = 0
        minSum = nums[0]
        
        for x in nums:
            total += x

            curMax = max(x, curMax + x)
            maxSum = max(maxSum, curMax)

            curMin = min(x, curMin + x)
            minSum = min(minSum, curMin)
        

        if maxSum < 0:
            return maxSum
        

        return max(maxSum, total - minSum)