class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights) -1 
        max_container = 0

        while l < r :
            curr_container = min(heights[r],heights[l]) * (r-l)
            max_container = max(max_container,curr_container)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1 

        return max_container
