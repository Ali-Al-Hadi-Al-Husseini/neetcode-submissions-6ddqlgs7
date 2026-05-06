class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        negtive_numbers = 0

        for num in nums:
            if num < 0 :
                negtive_numbers += 1 


        curr_product = 1 
        rev_product = 1 
        rev_negtive_numbers = negtive_numbers
        max_product = nums[0]

        for idx in range(len(nums)):
            num= nums[idx]
            rev_num = nums[len(nums)- idx -1 ]

            if (curr_product == 0) or curr_product < 0 and negtive_numbers == 0:
                curr_product = 1
            if (rev_product == 0) or rev_product < 0 and rev_negtive_numbers == 0:
                rev_product = 1               
            if num <0 :
                negtive_numbers -= 1

            if rev_num <0 :
                rev_negtive_numbers -= 1

            curr_product *= num
            rev_product  *= rev_num
            max_product = max(max_product,curr_product)
            max_product = max(max_product,rev_product)
        return max_product