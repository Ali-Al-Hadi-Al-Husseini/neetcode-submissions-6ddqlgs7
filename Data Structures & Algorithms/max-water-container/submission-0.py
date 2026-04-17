class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        l,r = 0, len(heights) - 1

        while l <= r :
            curr_water = ( r- l) * min(heights[r], heights[l])
            max_water = max(max_water, curr_water)

            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1

        return max_water 
