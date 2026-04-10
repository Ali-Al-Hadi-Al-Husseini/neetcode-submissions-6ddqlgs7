class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub_sets = [[]]

        
        for num in nums :
            curr_sub_sets = [] 
            for sub_set in sub_sets :
                new_sub_set = sub_set + [num]
                curr_sub_sets.append(new_sub_set)
            sub_sets.extend(curr_sub_sets)


        return sub_sets
        