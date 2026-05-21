class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        last_max  = nums[0]
        idx = 0
        num_of_jumps = 1

        while last_max  < len(nums) -1 :
            curr_max = 0
            new_idx = idx
            
            for i ,num in enumerate(nums[idx + 1:last_max+1]):
                if num > curr_max or idx + curr_max <= new_idx:   
                    curr_max = num
                    new_idx = i + idx + 1

            idx = new_idx
            last_max +=  curr_max
            num_of_jumps += 1 

        return num_of_jumps


