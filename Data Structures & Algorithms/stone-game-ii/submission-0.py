class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}


        def helper(alice_turn,i,m):
            if i >= len(piles):
                return 0
            if (alice_turn,i,m) in memo:
                return memo[(alice_turn,i,m)]


            max_score = 0 if alice_turn else float("inf")
            curr_sum =  0
            for j in range(i,min(len(piles), i + 2 * m )):
                
                curr_sum += piles[j] 
                if alice_turn:
                    max_score =  max(max_score, curr_sum + helper(False, j+1, max(m,j - i+1 )))
                else:
                    max_score =  min(max_score, helper(True, j+1, max(m,j - i+1)))


            memo[(alice_turn,i,m)] = max_score
            return max_score


        return helper(True,0,1)


