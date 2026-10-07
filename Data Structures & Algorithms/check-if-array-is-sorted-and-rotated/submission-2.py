class Solution:
    def check(self, nums: List[int]) -> bool:
        
        infliction_point = 0

        for i in range(len(nums) - 1 ):
            if nums[i] > nums[i+1]:
                infliction_point += 1
        print(infliction_point)
        if nums[-1] > nums[0]:
            infliction_point +=1 
        print(infliction_point)

        return infliction_point <= 1 