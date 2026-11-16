class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_yet = 0 
        res = []

        for i in range(len(heights)-1, -1, -1):
            if heights[i] > max_yet :
                res.append(i)
            max_yet = max(max_yet, heights[i])

        return res[::-1]