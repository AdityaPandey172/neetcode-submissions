class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Hashset = set()

        for n in nums:
            if n in Hashset:
                return True
            Hashset.add(n)
        return False
        
            