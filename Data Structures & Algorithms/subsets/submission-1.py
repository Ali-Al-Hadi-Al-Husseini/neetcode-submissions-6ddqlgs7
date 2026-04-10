class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub_sets = [[]]

        
        for num in nums :
            sub_sets += [ sub_set + [num] for sub_set in sub_sets] 


        return sub_sets
        