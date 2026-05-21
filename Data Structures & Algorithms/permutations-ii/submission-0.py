class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = {key:0 for key in nums}
        curr_perm = []
        result = []

        for num in nums:
            count[num] += 1 

        def helper():
            if len(curr_perm) == len(nums):
                result.append(curr_perm[:])
                return 
            
            for num in count :
                if count[num] > 0 :
                    count[num] -= 1
                    curr_perm.append(num)
                    helper()
                    curr_perm.pop()
                    count[num] += 1
        helper()
        return result
                    