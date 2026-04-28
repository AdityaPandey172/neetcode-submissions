class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counter = Counter(hand)
        hand.sort()

        for card in hand:
            if counter[card] > 0:
                for i in range(groupSize):
                    if counter[card + i] <= 0:
                        return False
                    counter[card + i] -= 1
        
        return True