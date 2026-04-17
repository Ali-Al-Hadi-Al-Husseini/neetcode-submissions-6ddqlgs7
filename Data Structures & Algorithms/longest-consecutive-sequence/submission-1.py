class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hash = {num:False for num in nums }
        max_length = 0

        for num in nums:
            if nums_hash[num]:
                continue
            curr_length = 1 
            curr_num = num
            while curr_num + 1 in nums_hash:
                curr_length += 1 
                curr_num += 1
                nums_hash[curr_num] = True 

            max_length = max(curr_length, max_length)
            nums_hash[num] = True 

        return max_length 