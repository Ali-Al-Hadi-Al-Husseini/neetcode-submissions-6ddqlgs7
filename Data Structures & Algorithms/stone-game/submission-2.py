class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        memo = {}

        def helper(left, right):
            if left > right:
                return 0
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            pick_left = piles[left] - helper(left + 1, right)
            pick_right = piles[right] - helper(left, right - 1)
            
            memo[(left, right)] = max(pick_left, pick_right)
            return memo[(left, right)]

        return helper(0, len(piles) - 1) > 0