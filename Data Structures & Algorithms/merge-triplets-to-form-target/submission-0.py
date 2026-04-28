class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_values = [0, 0, 0]

        for triplet in triplets:
            if (
                triplet[0] <= target[0]
                and triplet[1] <= target[1]
                and triplet[2] <= target[2]
            ):
                max_values = [max(max_values[i], triplet[i]) for i in range(3)]
            
        return max_values == target
        