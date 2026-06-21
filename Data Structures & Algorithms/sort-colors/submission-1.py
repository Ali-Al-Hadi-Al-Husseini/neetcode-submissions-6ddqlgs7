class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0,0,0]

        for num in nums:
            colors[num] += 1 
        print(colors)
        color_idx = 0
        for idx in range(len(nums)):
            if color_idx >= 3: break
            while colors[color_idx] <= 0:
                color_idx += 1
            
            nums[idx] = color_idx
            colors[color_idx] -= 1


        return colors