class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        if sum(nums) % k != 0 :
            return False 

        expected_size = sum(nums) / k

        nums_dict = defaultdict(int)

        for num in nums :
            if num > expected_size :
                return False 
            nums_dict[num] += 1 

        
        def helper(curr_size,sets):
            if sets == k:
                return True 


            for num in nums_dict.keys():
                if nums_dict[num] <= 0 or num + curr_size > expected_size:
                    continue

                nums_dict[num] -= 1 
                new_size = curr_size + num
                if new_size == expected_size and helper(0,sets+1):
                    return True
                elif helper(new_size,sets):
                    return True

                nums_dict[num] += 1 
            
            return False


        return helper(0,0)








        

