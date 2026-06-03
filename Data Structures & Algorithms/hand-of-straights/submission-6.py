class orderMap:
    def __init__(self):
        self.map = {}

    def add(self,idx,card):
        if card not in self.map:
            self.map[card] = [0,[]]
        self.map[card][1].append(idx)

    def pop(self,card):
        pop_idx = self.map[card][0]
        if pop_idx >= len(self.map[card][1]):
            del self.map[card]
            return  None
        self.map[card][0] += 1
        val = self.map[card][1][pop_idx]
        if self.map[card][0] == len(self.map[card][1]):
            del self.map[card]

        return val

    def __contains__(self,card):
        return card in self.map
    def copy(self):
        new_map = orderMap()
        new_map.map = {key:[idx,arr] for key,(idx,arr) in self.map.items()}
        return new_map

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0 :
            return False
        card_freq = orderMap()

        for idx,card in enumerate(hand):
            card_freq.add(idx,card)
        
        return try_hand(hand,groupSize,card_freq)





def try_hand(hand,groupSize,card_freq):
    used = set()

    for idx,card in enumerate(hand):
        if idx in used:
            continue 

        curr_used = set([idx])
        next_card= card - 1
        curr_freq = card_freq.copy()
        curr_freq.pop(card)

        while len(curr_used) < groupSize:
            if next_card not in curr_freq:
                break
            popped_idx = curr_freq.pop(next_card)
            curr_used.add(popped_idx)
            next_card -= 1 

        if len(curr_used) != groupSize:
            continue
        for i in curr_used:
            used.add(i)
        card_freq = curr_freq

    return len(used) == len(list(hand))
            
