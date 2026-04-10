class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr_sum = 1
        should_be = factorial(len(nums))
        zero_exists = False
        for num in nums:
            if num == 0:
                zero_exists = True 
                continue
            curr_sum *= num

        
        if not zero_exists :
            return 0

        return should_be // curr_sum 
        

def factorial(n):
    s = 1 

    for i in range(n):
        s *= (i + 1 )

    return s 