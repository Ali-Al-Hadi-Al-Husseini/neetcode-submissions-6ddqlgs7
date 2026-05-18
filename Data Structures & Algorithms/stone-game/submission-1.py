class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def helper(left,right,alice,bob,alice_turn):
            if right < left:
                return alice > bob
            if (left,right) in memo:
                return memo[(left,right)]
            alice_wins = False
            if alice_turn:

                alice_wins |=helper(left+1,right, alice + piles[left],bob,False)
                alice_wins |= helper(left,right-1, alice + piles[right],bob,False)
            else:
                alice_wins |=  helper(left+1,right, alice ,bob + piles[left],True)
                alice_wins |= helper(left,right-1, alice ,bob + piles[right],True)       
                  
            memo[(left,right)] = alice_wins
            return  alice_wins

        return helper(0,len(piles) -1 , 0,0, True)