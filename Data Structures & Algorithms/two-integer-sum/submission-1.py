class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keys = {num:idx for idx,num in enumerate(nums)}

        for idx ,num in enumerate(nums) :
            differnce = target - num
            if differnce in keys :
                if keys[differnce] == idx:
                    continue 
                return [idx,keys[differnce]]

        
        return [null.null]